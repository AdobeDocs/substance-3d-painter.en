---
title: "Assets (or shelf) previews are empty"
description: ""
helpx_description: "Painter > Technical support > Technical Issues > Miscellaneous Issues > Assets (or shelf) previews are empty"
---

# Assets (or shelf) previews are empty

This issue can be caused by other software, see: [Software conflicts](../../startup-issues/software-conflicts/software-conflicts.md).

If it is impossible to determine which software updating/uninstalling, look for an environment variable named "QT\_PLUGIN\_PATH" and remove it.

**On Windows:**

1. Open **System** in Control Panel.
1. On the Advanced tab, click **Environment Variables**
1. Look for the variable named **"QT\_PLUGIN\_PATH"**
1. **Remove** it
1. **Restart** your computer
