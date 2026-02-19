---
title: "GPU drivers compatibility"
description: "Learn about GPU driver compatibility requirements for Substance 3D Painter to ensure stable rendering and performance."
helpx_description: Painter > Technical support > Technical Issues > GPU Issues > GPU drivers compatibility
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/gpu-issues/gpu-drivers-compatibility.html"
helpx_creative_field:
  - video
  - 3d-immersive
  - painting-illustration
helpx_experience_level:
  - any
helpx_learn_topic:
  - known-issues
  - system-requirements
  - troubleshooting
---




# GPU drivers compatibility

This page regroups information about GPU drivers that may lead to issues with Substance 3D Painter.

## Nvidia

The table below list all the driver versions know to create issues for Nvidia GPU (GeForce or Quadro models):

| *Driver version* | *Issue description* |
| --- | --- |
| <b> 425.xx </b> | GPU raytracing artifacts. |
| <b> 429.xx or older </b> | Black texture block artifacts. |
| <b> 435.xx or older </b> | sRGB color issues when computing textures. |
| <b> 439.xx </b> | Textures corruption. |
| <b> 441.08 </b> | Crash or stability issues. |
| <b> 442.19 </b> | Crash or stability issues. |
| <b>528.09</b> | Operating system freeze. |
| <b>572.16 to 572.42</b> | Artifacts or crash when baking textures. |

### AMD

| *Driver version* | *Issue description* |
| --- | --- |
| **20.7.x**  to  **20.11.2** | Textures glitch or corruption. |
| **20.11.3**  to  **21.2.1** | Textures glitch or corruption plus crash or stability issues. |
| **21.2.3**  to **21.6.1** | Crash or stability issues. |
