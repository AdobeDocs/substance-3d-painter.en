---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/miscellaneous-issues/assets-or-shelf-previews-are-empty.html"
breadcrumb-title: ""
description: Learn how to fix empty asset and shelf previews in Substance 3D Painter to restore thumbnail display functionality.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Technical Issues > Miscellaneous Issues > Assets (or shelf) previews are empty
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Assets (or shelf) previews are empty
user-guide-description: ""
user-guide-title: ""
---


# Assets (or shelf) previews are empty

This issue can be caused by other software, see: [Software conflicts](../../../../technical-support/technical-issues/startup-issues/software-conflicts/software-conflicts.md).

If it is impossible to determine which software updating/uninstalling, look for an environment variable named "QT\_PLUGIN\_PATH" and remove it.

**On Windows:**

1. Open **System** in Control Panel.
1. On the Advanced tab, click **Environment Variables**
1. Look for the variable named **"QT\_PLUGIN\_PATH"**
1. **Remove** it
1. **Restart** your computer
