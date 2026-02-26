---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/gpu-issues/crash-when-working-with-overclocked-gpu.html"
breadcrumb-title: ""
description: Learn how to fix Substance 3D Painter crashes when working with overclocked GPUs for stable application performance.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Technical Issues > GPU Issues > Crash when working with overclocked GPU
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Crash when working with overclocked GPU
user-guide-description: ""
user-guide-title: ""
---

# Crash when working with overclocked GPU

Overclocked GPUs can often be more unstable because they run of frequencies that weren't initially designed by the GPU constructor. If your GPU is overclocked and you have stability issues we recommend going back to the factory default frequencies for a while.

## Nvidia GPU

On Nvidia GPUs, starting with drivers 355.82, it is possible to temporarily disable the GPU overclocking by enabling a debug mode in the drivers settings. This allows to check and determine problems related to the graphic cards.

To enable the debug mode:

1. Open the **Nvidia Control Panel** (right click on your desktop).
1. Click on the **Help** menu.
1. Click on **Debug Mode**.

>[!NOTE]
>
> The Debug Mode may not be available if your GPU is a reference card. It will be available only if the GPU runs on non-standard clocks or with a modified BIOS. In this case we recommend to manually disable the overclocking.
