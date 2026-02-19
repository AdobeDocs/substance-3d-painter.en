---
title: "Running on integrated GPU"
description: "Learn how to configure Substance 3D Painter to use dedicated GPU instead of integrated graphics for better performance."
helpx_description: Painter > Technical support > Technical Issues > GPU Issues > Running on integrated GPU
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/gpu-issues/running-on-integrated-gpu.html"
helpx_creative_field:
  - painting-illustration
  - video
  - graphic-design
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - known-issues
  - system-requirements
  - rendering
---




# Running on integrated GPU

![](integrated-gpu.png){width="500px"}

It can happens that some computers are set by default to run on an integrated chipset rather than on a dedicated GPU.   
Since performances on integrated chipset are very low, we recommend to use a dedicated GPU instead. A pop-up can appears and warns you about it.

With an NVIDIA GPU, the switch to the NVIDIA GPU depends on application profiles. If an application does not have such profile, you can assign the graphics card manually:

1. Right-click on the Desktop and select NVIDIA Control Panel  **or**  Navigate to the Control Panel and search for NVIDIA Control Panel
1. Under  **3D Settings**  , go to  **Manage 3D Settings**
1. Under the tab  **Program settings**  add a new profile for  **Substance 3D Painter**
1. Change the preferred graphics processor setting to High-performance NVIDIA processor
