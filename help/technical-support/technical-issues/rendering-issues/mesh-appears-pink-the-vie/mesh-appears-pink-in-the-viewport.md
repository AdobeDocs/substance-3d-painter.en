---
title: "Mesh appears pink in the viewport"
description: "Learn how to fix pink mesh appearance in Substance 3D Painter viewport to restore proper material rendering."
helpx_description: Painter > Technical support > Technical Issues > Rendering Issues > Mesh appears pink in the viewport
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/rendering-issues/mesh-appears-pink-in-the-viewport.html"
helpx_creative_field:
  - video
  - painting-illustration
  - social-media
  - 3d-immersive
  - publishing
helpx_experience_level:
  - any
helpx_learn_topic:
  - polygon
  - creating-color-palettes
  - color
---




# Mesh appears pink in the viewport

![](pink-mesh.jpg){width="400px"}

The mesh can appear  **pink**  inside the viewport because the  **shader**  used to draw it  **doesn't compile anymore**  (as mentioned by the  **log window**  ). This can be caused by an outdated shader which doesn't support the latest version of the shader API.

Here is how to fix it:

* For  **default shaders**: follow the step by step procedure from the [Updating a shader](../../../../help/interface/shader-settings/updating-a-shader/updating-a-shader.md) page.
* For **custom shader**: take a look at the error message in the log window as well as the [Shader API](https://helpx.adobe.com/substance-3d/unlisted/documentation/spdoc/custom-shader-api-89686018.html) page.
