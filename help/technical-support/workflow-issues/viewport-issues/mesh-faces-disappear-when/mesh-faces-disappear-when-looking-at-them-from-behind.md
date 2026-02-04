---
title: "Mesh faces disappear when looking at them from behind"
description: ""
helpx_description: "Painter > Technical support > Workflow Issues > Viewport Issues > Mesh faces disappear when looking at them from behind"
---

# Mesh faces disappear when looking at them from behind

By default, meshes in the viewport may not display the back of the mesh polygons (backface). This is because they are culled by the current shader.

To display the back of the faces, simply change the current shader to **pbr-metal-rough-alpha-test** in the [Shader settings](../../../../interface/shader-settings/shader-settings.md).
