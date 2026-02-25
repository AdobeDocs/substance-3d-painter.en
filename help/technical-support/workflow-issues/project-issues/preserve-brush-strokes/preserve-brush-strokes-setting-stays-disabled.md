---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/workflow-issues/project-issues/preserve-brush-strokes-setting-stays-disabled.html"
breadcrumb-title: ""
description: Learn how to fix the preserve brush strokes setting staying disabled in Substance 3D Painter for proper brush stroke preservation.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Workflow Issues > Project Issues > Preserve brush strokes setting stays disabled
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Preserve brush strokes setting stays disabled
user-guide-description: ""
user-guide-title: ""
---


# Preserve brush strokes setting stays disabled

Because of an unfortunate bug introduced in Substance 3D Painter 1.5 (partially fixed in 1.7) some projects have lost metadata related to the mesh. This bug makes therefore the "Preserve strokes positions on mesh" setting in the [ Project Configuration ](../../../../interface/project-configuration/project-configuration.md) window to stay disabled.

To solve the issue some specific steps need to be followed :

* Open the project with the issue in Substance 3D Painter 1.7 or superior
* Go to Edit &gt; Project Configuration
* Select and re-import the original mesh that you used in the current project (not the updated version)
* Validate and let Substance 3D Painter compute the layers, nothing should change if it's the same mesh
* Go again to Edit &gt; Project Configuration
* "Preserve strokes positions on mesh" should now be enabled again, allowing you to import the new mesh
