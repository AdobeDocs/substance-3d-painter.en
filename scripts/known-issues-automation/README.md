# Known Issues Generator — Substance 3D Painter

Automates generation of the known issues markdown document for Substance 3D Painter, published at:
`https://helpx.adobe.com/substance-3d-painter/release-notes/know-issues.html`

Issues are sourced from the Jira epic `SBSFOUR-6267`. The script fetches all issues, filters out anything already fixed in the target version, and outputs a formatted markdown file ready to commit.

---

## Quick Start

These steps assume you have already completed the one-time setup below.

1. Connect to **GlobalProtect VPN**
2. Set `TARGET_VERSION` in your `.env` file to the version you are generating docs for (e.g. `12.0.3`)
3. Run the script from the `scripts/known-issues-automation/` directory:
   ```
   python fetch_known_issues.py
   ```
4. Check the output summary — it will report how many issues were fetched and how many were excluded
5. Copy the generated `known-issues.md` to `help/release-notes/known-issues.md`

> If any issues are missing or unexpected, inspect `raw_issues.json` to see exactly what Jira returned before filtering was applied.

---

## One-Time Setup

### 1. Install dependencies

```bash
pip install requests python-dotenv
```

### 2. Create your `.env` file

```bash
cp .env.example .env
```

### 3. Get a Jira Personal Access Token

1. Log into `https://jira.corp.adobe.com`
2. Go to your profile → **Personal Access Tokens** in the left sidebar
3. Click **Create token**, give it a name, and copy the generated value

> PATs do not expire when your browser session ends, making them more reliable than session cookies for scripted API access.

### 4. Fill in your `.env` file

```
JIRA_PAT=your-personal-access-token
TARGET_VERSION=12.0.3
OUTPUT_FILE=known-issues.md
```

`TARGET_VERSION` is the version of Substance 3D Painter you are generating the known issues page for. It controls which fixed issues are excluded — see [Filtering Logic](#filtering-logic) below.

---

## Repository Structure

```
.
├── README.md                  # This file
├── fetch_known_issues.py      # Main script
├── .env.example               # Environment variable template (safe to commit)
├── .env                       # Your local credentials — never commit this
├── raw_issues.json            # Raw Jira dump from last run — gitignored
└── known-issues.md            # Generated output from last run — gitignored
```

---

## Jira Reference

| Field | Value |
|---|---|
| Jira instance | `https://jira.corp.adobe.com` |
| Project key | `SBSFOUR` |
| Known issues epic | `SBSFOUR-6267` |

All known issues must be linked to this epic to appear in the generated document. If an issue needs to be added to or removed from the page, update the epic in Jira rather than editing the markdown manually.

---

## How the Script Works

### Step 1 — Fetch

The script queries the Jira REST API using JQL:

```
"Epic Link" = SBSFOUR-6267 ORDER BY created ASC
```

Results are paginated at 50 issues per page. The following fields are retrieved for each issue: `summary`, `issuetype`, `status`, `affectedVersions`, `fixVersions`, `labels`.

Authentication uses a Bearer token from `JIRA_PAT`. The corporate Jira instance uses an internal SSL certificate, so certificate verification is disabled for these requests — this is expected behaviour on the Adobe network.

### Step 2 — Raw dump

Before any filtering or formatting, the script writes `raw_issues.json`. This is a simplified snapshot of every issue Jira returned, and is always generated regardless of what happens next. If the output looks wrong, inspect this file first — it shows exactly what data Jira provided.

### Step 3 — Filter

Issues are filtered using two rules applied together:

1. **Status filter** — only `Backlog` and `Dev In Progress` issues are active known issues. Issues with status `Fixed` are candidates for exclusion, subject to the version check below.

2. **Version filter** — a `Fixed` issue is excluded only if one of its fix versions is less than or equal to `TARGET_VERSION`. If the fix version is higher than `TARGET_VERSION`, the issue is still included because the fix has not shipped for the version being documented.

This handles the case where two versions are in development simultaneously: an issue fixed in `12.1.0` remains a known issue for `12.0.3`.

See [Filtering Logic](#filtering-logic) for the full decision table.

### Step 4 — Parse categories

Each issue summary is parsed for category tags at the start of the string:

- `[Shader] Some description` → categories: `["Shader"]`, description: `"Some description"`
- `[Crash][Engine] Some description` → categories: `["Crash", "Engine"]`, description: `"Some description"`
- `No brackets here` → no categories, treated as uncategorised

The **primary category** is always the first tag. It determines grouping and section placement.

### Step 5 — Group and sort

Issues are organised as follows:

- Issues are grouped by primary category
- Groups are sorted by issue count, descending (largest groups first)
- Groups with more than one issue appear at the top of the document
- Groups with only one issue, plus any uncategorised issues, appear after the multi-issue groups with no section header
- Issues with `[Crash]` as their primary category are always placed last, under a `## Stability` section

### Step 6 — Format and write

The script outputs `known-issues.md` with:

- YAML frontmatter (helpx metadata)
- A `# Known issues` heading with an intro paragraph that names the target version
- Issues formatted as: `` * `[Category]` Description ``
- Multi-category issues: `` * `[Category1]` `[Category2]` Description ``
- Blank lines between category groups
- A `## Stability` section at the end for crash issues

---

## Filtering Logic

| Status | Fix version set? | Fix version vs target | Included? |
|---|---|---|---|
| `Backlog` | — | — | Yes |
| `Dev In Progress` | — | — | Yes |
| `Fixed` | No | — | No (conservatively excluded) |
| `Fixed` | Yes | Fix version ≤ target | No (already shipped) |
| `Fixed` | Yes | Fix version > target | Yes (fix is in a future version) |

---

## Output Format

```markdown
---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/release-notes/know-issues.html"
...
---

# Known issues

This page lists all the active known issues present in v12.0.3 of Substance 3D Painter:

* `[Engine]` Error when using Smart Materials if Texture Set has no tile 1001
* `[Engine]` Geometry mask shows artifacts at UV borders with instanced layers

* `[Shader]` user0 channel always can not be read as sRGB with specific shader

* `[Export]` GLTF exports at the wrong size
* `[Import]` Cannot import obj file with "nan" values

## Stability

* `[Crash]` Select "Export mesh" when mesh failed to load

```

**Formatting note:** Category tags use single backtick wrapping — `` `[Category]` `` — not double backticks. The legacy manually-maintained document contained double-backtick errors; the script always produces the correct format.

---

## Troubleshooting

**401 Unauthorized**
- Confirm you are connected to **GlobalProtect VPN**
- Your PAT may have expired or been revoked — generate a new one at `https://jira.corp.adobe.com/secure/ViewProfile.jspa` and update your `.env`

**`JIRA_PAT is not set` error**
- Make sure you have created a `.env` file from `.env.example` and filled in your token
- Confirm you are running the script from within the `scripts/known-issues-automation/` directory so that `python-dotenv` can find the `.env` file

**Issues missing from the output**
- Check `raw_issues.json` — if the issue is not there, it is not linked to epic `SBSFOUR-6267` in Jira
- If the issue is in `raw_issues.json` but not in the output, it was excluded by the filter — check its status and fix version against your `TARGET_VERSION`

**`TARGET_VERSION` warning at runtime**
- The script will run but will conservatively exclude all `Fixed` issues if `TARGET_VERSION` is not set. Always set it before generating the final document.
