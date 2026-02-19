---
title: "Blocky artifacts appear on textures in the viewport"
description: "Learn how to fix blocky artifacts appearing on textures in Substance 3D Painter viewport for clean visual quality."
helpx_description: Painter > Technical support > Technical Issues > Rendering Issues > Blocky artifacts appear on textures in the viewport
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/rendering-issues/blocky-artifacts-appear-on-textures-in-the-viewport.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - texture
  - channels
  - troubleshooting
---




# Blocky artifacts appear on textures in the viewport

Starting with version 2018.3.0 the following kind of artifacts can appear in the viewport:

![](viewport-artifacts.jpg){width="400px"}

These artifacts are related to issues with Nvidia GPU Drivers.   
To avoid the artifacts the Sparse Virtual Textures hardware support needs to be deactivated.

The GeForce  **Drivers 440.97**  have now  **fixed this issue**  . We recommended to update to these drivers and to keep the SVT enabled to get good performances.

New drivers are available on Nvidia website: <https://www.nvidia.com/Download/index.aspx>

## Disabling the Sparse Virtual Textures Hardware acceleration

### 1 - Start Substance 3D Painter and open the Settings

![](settings-34.png)

Open the main Settings via Edit &gt; Settings.

### 2 - Find the section named "Sparse Virtual Textures"

![](svt-subsection.png)

Inside the "General" section, scroll down and find the sub-section named "Sparse Virtual Textures"

### 3 - Uncheck the setting

![](uncheck-hardware.png)

Disable the "Hardware support acceleration" setting by unchecking it.

### 4 - Validate and restart Substance 3D Painter

![](validate-1.png)

Validate the change by clicking on the "OK" button.

![](restart-3.png)

Restart Substance 3D Painter by clicking on the "Yes" button to apply the change.
