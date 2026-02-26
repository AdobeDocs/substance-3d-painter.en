---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/gpu-issues/gpu-is-not-recognized.html"
breadcrumb-title: ""
description: Learn how to fix GPU recognition issues in Substance 3D Painter to enable proper hardware acceleration and performance.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Technical Issues > GPU Issues > GPU is not recognized
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: GPU is not recognized
user-guide-description: ""
user-guide-title: ""
---

# GPU is not recognized

![](../../../../assets/not-recognized-gpu.png){width="500px"}

Some  **NVIDIA Optimus**  users can have troubles getting Substance 3D Painter to run on the right GPU. A workaround is to set the following keys in the Registry of Windows to 0:

* HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows\RequireSignedAppInit
* HKEY\_LOCAL\_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Windows\RequireSignedAppInit
