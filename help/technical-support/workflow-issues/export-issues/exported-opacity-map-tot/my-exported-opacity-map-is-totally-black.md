---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/workflow-issues/export-issues/my-exported-opacity-map-is-totally-black.html"
breadcrumb-title: ""
description: Learn how to fix exported opacity maps appearing totally black in Substance 3D Painter for proper transparency export.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Workflow Issues > Export Issues > My exported opacity map is totally black
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: My exported opacity map is totally black
user-guide-description: ""
user-guide-title: ""
---


# My exported opacity map is totally black

When you create a new project, the default color comes from the shader and not the textures. Therefore, when you export all the parts that you didn't paint they will be black with an alpha value set at 0 (because no data exist on these parts).

The easiest way to fix this is to put a fill layer at the bottom of your layer stack : it will fill all the UVs with a default color, which is identical to the default color of the shader.
