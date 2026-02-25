---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/stability-issues/crash-while-baking.html"
breadcrumb-title: ""
description: Learn how to fix Substance 3D Painter crashes during baking operations for reliable texture baking workflows.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Technical Issues > Stability Issues > Crash while baking
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Crash while baking
user-guide-description: ""
user-guide-title: ""
---


# Crash while baking

Substance 3D Painter may crash during the baking process on some configurations. This page regroups a list of know issues and how to mitigate them.

## Crash with Baking preview

By default Substance 3D Painter display in the viewport the in-progress state of the baking of a texture. On some computer this feature may lead to instabilities.

To disable it:

1. Use  **Edit &gt; Settings**  to open the main settings
1. Under  **General**  scrolls down to the section named  **Baking Options**  .
1. Uncheck/Disable the option  **Enable live preview baking process**  .

## Crash with GPU Raytracing

On some GPU with unstable drivers, the baking process may lead to crashes because of the GPU raytracing feature.

To disable it:

1. Use  **Edit &gt; Settings**  to open the main settings
1. Under  **General**  scrolls down to the section named  **Baking Options**  .
1. Uncheck/Disable the option  **Enable GPU raytracing**  .

## Crash with Ryzen CPUs

The application may crash during the baking process on some computer configuration running with a Ryzen CPU. An update of the BIOS usually fix the problem.

This is related to multi-threaded computations. Many Motherboard constructors have issued new BIOS updates to fix this issue, so we recommend applying the update. Refer to the Motherboard manual and constructor website for more information.

## Incompatible Assbin files

By default when baking, high-poly meshes are pre-processed into  **\*.assbin**  files to speed-up rebaking later. In some rare cases, these files may crash the application if they have been generated with a different version. Simply deleting them should solve the problem, as they will be regenerated.
