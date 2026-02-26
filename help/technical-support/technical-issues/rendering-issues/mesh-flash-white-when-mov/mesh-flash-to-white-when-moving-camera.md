---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/rendering-issues/mesh-flash-to-white-when-moving-camera.html"
breadcrumb-title: ""
description: Learn how to fix mesh flashing to white when moving the camera in Substance 3D Painter viewport for stable rendering.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Technical Issues > Rendering Issues > Mesh flash to white when moving camera
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Mesh flash to white when moving camera
user-guide-description: ""
user-guide-title: ""
---

# Mesh flash to white when moving camera

![](../../../../assets/white-flash-svt-optim.gif){width="300px"}

With old projects moving around the camera in the viewport may briefly show white flashes created by white/empty textures. This is because the  [Sparse Virtual Textures](https://substance3d.adobe.com/display/DRAFTPAINTER/Sparse+Virtual+Textures)  (SVT) system relies on specific shader configurations which older shaders don't use.

To get rid of the white flash simply  **update**  the  **project shader**:

* For **default shaders**: follow the step by step procedure from the [Updating a shader](../../../../interface/shader-settings/updating-a-shader/updating-a-shader.md) page.
* For **custom shaders**: take a look at the error message(s) in the log as well as the [Shader API](https://helpx.adobe.com/substance-3d/unlisted/documentation/spdoc/custom-shader-api-89686018.html) page.
