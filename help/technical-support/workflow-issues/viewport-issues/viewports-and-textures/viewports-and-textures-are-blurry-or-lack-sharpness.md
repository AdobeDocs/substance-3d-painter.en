---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/workflow-issues/viewport-issues/viewports-and-textures-are-blurry-or-lack-sharpness.html"
breadcrumb-title: ""
description: Learn how to fix blurry viewports and textures in Substance 3D Painter to ensure sharp, clear visual quality.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Workflow Issues > Viewport Issues > Viewports and textures are blurry or lack sharpness
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Viewports and textures are blurry or lack sharpness
user-guide-description: ""
user-guide-title: ""
---

# Viewports and textures are blurry or lack sharpness

The viewports may appear blurry for different reasons.

## High-DPI screens (Retina) settings

By default Substance 3D Painter downscale the viewport resolution on High-DPI/Retina screen to improve performances.

This behavior can be changed in the  [main settings](https://helpx.adobe.com/substance-3d/unlisted/documentation/spdoc/general-71008262.html) by changing the  **Viewport Scaling**  parameter.

## Texture filtering

The viewports use mipmaps and texture filtering to be able to stream in and out [ Sparse Virtual Textures ](../../../../features/sparse-virtual-textures/sparse-virtual-textures.md) to improve performances. This can lead to blurry textures in some cases.

The texture filtering can be adjusted via the Display Settings window under the [ Viewport Settings](../../../../interface/display-settings/viewport-settings/viewport-settings.md) parameters.
