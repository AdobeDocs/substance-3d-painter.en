"""
fetch_known_issues.py

Fetches all issues from Jira epic SBSFOUR-6267 (Known Issues),
extracts Affects Version/s and Fix Version/s, and outputs a
formatted markdown file matching the Substance 3D Painter known
issues documentation pattern.

Usage:
    1. Set JIRA_PAT and TARGET_VERSION in a .env file (see .env.example).
    2. Run: python fetch_known_issues.py

.env file format:
    JIRA_PAT=your-personal-access-token
    TARGET_VERSION=12.0.3          # version you are generating docs for
    OUTPUT_FILE=known-issues.md    # optional, defaults to known-issues.md
"""

import os
import re
import json
import requests
import urllib3
from collections import defaultdict
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

JIRA_BASE_URL = "https://jira.corp.adobe.com"
EPIC_KEY = "SBSFOUR-6267"

# Load session cookie from environment (or .env file)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv optional; can set env vars manually

JIRA_PAT = os.environ.get("JIRA_PAT", "")
TARGET_VERSION = os.environ.get("TARGET_VERSION", "")
OUTPUT_FILE = os.environ.get("OUTPUT_FILE", "known-issues.md")

# ---------------------------------------------------------------------------
# Jira API helpers
# ---------------------------------------------------------------------------

def get_headers():
    return {
        "Authorization": f"Bearer {JIRA_PAT}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def fetch_issues_in_epic(epic_key):
    """
    Fetches all issues linked to the given epic using JQL.
    Handles pagination automatically.
    """
    issues = []
    start = 0
    page_size = 50

    # Fields we care about
    fields = "summary,issuetype,status,affectedVersions,fixVersions,labels,customfield_10008"

    while True:
        jql = f'"Epic Link" = {epic_key} ORDER BY created ASC'
        url = f"{JIRA_BASE_URL}/rest/api/2/search"
        params = {
            "jql": jql,
            "startAt": start,
            "maxResults": page_size,
            "fields": fields,
        }

        resp = requests.get(url, headers=get_headers(), params=params, verify=False)

        if resp.status_code != 200:
            print(f"[ERROR] Jira API returned {resp.status_code}: {resp.text}")
            resp.raise_for_status()

        data = resp.json()
        batch = data.get("issues", [])
        issues.extend(batch)

        total = data.get("total", 0)
        start += len(batch)

        print(f"  Fetched {start}/{total} issues...")

        if start >= total:
            break

    return issues


def fetch_epic_info(epic_key):
    """Fetches the epic issue itself to get its summary/name."""
    url = f"{JIRA_BASE_URL}/rest/api/2/issue/{epic_key}"
    resp = requests.get(url, headers=get_headers(), verify=False)
    if resp.status_code == 200:
        return resp.json()
    return None

# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

CATEGORY_PATTERN = re.compile(r'\[([^\]]+)\]')


def parse_categories(summary):
    """
    Extracts categories from square brackets at the start of the summary.
    e.g. "[Shader] Some issue"  ->  categories=["Shader"], desc="Some issue"
         "[Crash][Engine] Foo"  ->  categories=["Crash","Engine"], desc="Foo"
    Returns (categories: list, description: str)
    """
    categories = []
    remaining = summary.strip()

    while remaining.startswith("["):
        match = CATEGORY_PATTERN.match(remaining)
        if not match:
            break
        categories.append(match.group(1))
        remaining = remaining[match.end():].strip()

    return categories, remaining


def format_issue_line(categories, description):
    """
    Formats a single issue line in the correct markdown format.
    e.g. `[Shader]` Some description
         `[Instancing]` `[Projection]` Some description
    """
    tags = " ".join(f"`[{c}]`" for c in categories)
    if tags:
        return f"* {tags} {description}"
    else:
        return f"* {description}"


def extract_version_names(version_list):
    """Extracts version name strings from Jira version objects."""
    return [v.get("name", "") for v in version_list if v.get("name")]


def parse_version(version_str):
    """
    Parses a version string into a comparable tuple of ints, ignoring
    any pre-release suffix (e.g. "12.1.0 - beta2" -> (12, 1, 0)).
    """
    numeric = re.split(r'[\s\-]', version_str.strip())[0]
    try:
        return tuple(int(x) for x in numeric.split('.'))
    except ValueError:
        return (0,)


def is_active_issue(status, fix_versions):
    """
    Returns True if the issue should appear in the known issues list.

    Inclusion rules:
    - Non-Fixed issues (Backlog, Dev In Progress, etc.) are always included.
    - Fixed issues are included only if every fix version is strictly greater
      than TARGET_VERSION, meaning the fix has not yet shipped for the version
      we are generating docs for.
    - Fixed issues with no fix version, or where any fix version is <= TARGET_VERSION,
      are excluded.
    """
    if status != "Fixed":
        return True

    if not TARGET_VERSION:
        # No target specified: conservatively exclude all Fixed issues.
        return False

    if not fix_versions:
        # Fixed but no version recorded: assume already shipped, exclude.
        return False

    target = parse_version(TARGET_VERSION)
    return all(parse_version(fv) > target for fv in fix_versions)

# ---------------------------------------------------------------------------
# Markdown generation
# ---------------------------------------------------------------------------

FRONTMATTER = """\
---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/release-notes/know-issues.html"
breadcrumb-title: ""
description: Review known issues for Substance 3D Painter to stay informed about current limitations and workarounds in the latest version.
helpx_creative_field: ""
helpx_description: Substance 3D Painter
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Known issues
user-guide-description: ""
user-guide-title: ""
---"""

def build_intro():
    if TARGET_VERSION:
        version_str = f"v{TARGET_VERSION}"
    else:
        version_str = "the latest version"
    return f"# Known issues\n\nThis page lists all the active known issues present in {version_str} of Substance 3D Painter:"


def build_markdown(issues):
    """
    Groups issues by category, sorts by count (descending),
    moves single-issue categories to Miscellaneous,
    and moves Crash issues to the very end.
    """

    # Separate issues with and without categories
    categorised = []   # (categories, description, affects, fixes)
    uncategorised = [] # (description, affects, fixes)

    for issue in issues:
        fields = issue.get("fields", {})
        summary = fields.get("summary", "").strip()
        affects = extract_version_names(fields.get("affectedVersions") or [])
        fixes = extract_version_names(fields.get("fixVersions") or [])

        categories, description = parse_categories(summary)

        if categories:
            categorised.append((categories, description, affects, fixes))
        else:
            uncategorised.append((description, affects, fixes))

    # Build a map: primary_category -> list of (categories, description, affects, fixes)
    # Primary category = first bracket tag (used for grouping)
    category_map = defaultdict(list)
    crash_issues = []

    for item in categorised:
        categories, description, affects, fixes = item
        primary = categories[0]

        if primary.lower() == "crash":
            crash_issues.append(item)
        else:
            category_map[primary].append(item)

    # Sort categories by number of issues, descending
    sorted_categories = sorted(category_map.items(), key=lambda x: len(x[1]), reverse=True)

    # Split into multi-issue categories and single-issue (-> Miscellaneous)
    multi_issue = [(cat, items) for cat, items in sorted_categories if len(items) > 1]
    single_issue = [(cat, items) for cat, items in sorted_categories if len(items) == 1]

    # Build output lines
    lines = []
    lines.append(FRONTMATTER)
    lines.append("")
    lines.append(build_intro())
    lines.append("")

    def append_issue(item):
        categories, description, affects, fixes = item
        lines.append(format_issue_line(categories, description))

    # Multi-issue categories
    for i, (cat, items) in enumerate(multi_issue):
        for item in items:
            append_issue(item)
        lines.append("")

    # Single-issue categories and uncategorised (no header)
    if single_issue or uncategorised:
        for cat, items in single_issue:
            for item in items:
                append_issue(item)
        for desc, affects, fixes in uncategorised:
            lines.append(f"* {desc}")
        lines.append("")

    # Crash issues at the very end
    if crash_issues:
        lines.append("## Stability")
        lines.append("")
        for item in crash_issues:
            append_issue(item)
        lines.append("")

    return "\n".join(lines)

# ---------------------------------------------------------------------------
# Raw data dump (for inspection)
# ---------------------------------------------------------------------------

def dump_raw(issues, path="raw_issues.json"):
    """Dumps raw issue data to JSON for inspection."""
    output = []
    for issue in issues:
        fields = issue.get("fields", {})
        output.append({
            "key": issue.get("key"),
            "summary": fields.get("summary"),
            "status": fields.get("status", {}).get("name"),
            "affectedVersions": extract_version_names(fields.get("affectedVersions") or []),
            "fixVersions": extract_version_names(fields.get("fixVersions") or []),
            "labels": fields.get("labels", []),
        })
    with open(path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    print(f"[INFO] Raw data written to {path}")

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if not JIRA_PAT:
        print("[ERROR] JIRA_PAT environment variable is not set.")
        print("  Add it to your .env file:")
        print("  JIRA_PAT=your_personal_access_token")
        return

    if not TARGET_VERSION:
        print("[WARN] TARGET_VERSION is not set. All Fixed issues will be excluded.")
        print("  Set it in your .env file: TARGET_VERSION=12.0.3")

    print(f"[INFO] Fetching issues from epic {EPIC_KEY}...")
    issues = fetch_issues_in_epic(EPIC_KEY)
    print(f"[INFO] Total issues fetched: {len(issues)}")

    if not issues:
        print("[WARN] No issues returned. Check your JIRA_PAT or epic key.")
        return

    # Always dump raw JSON first so you can inspect the data
    dump_raw(issues, path="raw_issues.json")

    # Filter to active issues only
    active_issues = [
        issue for issue in issues
        if is_active_issue(
            issue.get("fields", {}).get("status", {}).get("name", ""),
            extract_version_names(issue.get("fields", {}).get("fixVersions") or [])
        )
    ]
    print(f"[INFO] Active issues after filtering: {len(active_issues)} (excluded {len(issues) - len(active_issues)})")

    # Build and write markdown
    markdown = build_markdown(active_issues)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"[INFO] Markdown written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
