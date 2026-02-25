---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/workflow-issues/viewport-issues/mesh-faces-disappear-when-looking-at-them-from-behind.html"
breadcrumb-title: ""
description: Learn how to fix mesh faces disappearing when viewed from behind in Substance 3D Painter viewport for proper mesh visibility.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Workflow Issues > Viewport Issues > Mesh faces disappear when looking at them from behind
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Mesh faces disappear when looking at them from behind
user-guide-description: ""
user-guide-title: ""
---


# Mesh faces disappear when looking at them from behind

By default, meshes in the viewport may not display the back of the mesh polygons (backface). This is because they are culled by the current shader.

To display the back of the faces, simply change the current shader to **pbr-metal-rough-alpha-test** in the [Shader settings](../../../../interface/shader-settings/shader-settings.md).
