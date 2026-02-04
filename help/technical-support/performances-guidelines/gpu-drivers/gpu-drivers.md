---
title: "GPU VRAM and Drivers"
description: ""
helpx_description: "Painter > Technical support > Performances guidelines > GPU Drivers"
---

# GPU Drivers

We cannot guarantee performance without the use of recommended drivers. Non-WHQL drivers must be avoided.  
GPU drivers are like any software, each new release can introduce performance issues. If issues occur after updating to a more recent driver version, we recommend downgrading your drivers to a previous version.

## NVIDIA Drivers Settings

Some default NVIDIA settings can have an impact on performance, we recommend creating a profile and disabling the following parameters (set them to off) :

* Threaded Optimization
* Vertical Synchronization

## How other applications can utilize the GPU

Substance 3D Painter is not alone in working with the GPU, other applications do the same. Almost any 3D application will use the GPU and VRAM to run, including those commonly used alongside Painter, like Blender, Maya, Unreal Engine, Unity, C4D, and others. A solution to ensure good performance while keeping these applications open is to be sure Substance 3D Painter is launched first in order to request its own VRAM allocation. Still, some software can acquire some parts of the VRAM dynamically and can still be in conflict with Substance 3D Painter even if they are launched after Painter.

In general, the more VRAM Painter has access to, the faster it will run, so try to minimize the amount of VRAM used by other applications running concurrently with Painter.

## GPU VRAM amount and bandwidth

Substance 3D Painter relies a lot on the GPU to perform most of its computations. This is why it is important to have a GPU that follows the [System requirements](../../../getting-started/system-requirements/system-requirements.md).

Painter works by transferring textures into the GPU memory (VRAM) in order to do the computations (like blending operations to create the final textures). However, if the VRAM is starting to get full, the unused textures will be transferred back to the RAM of the computer to free VRAM space. Substance 3D Painter writes and reads GBs of data when working. This means that both the capacity of the VRAM (amount) and the bandwidth speed when doing transfers are important. You can use tools such as [MSI AfterBurner](https://www.msi.com/page/afterburner) to monitor this behavior.

>[!NOTE]
>
> The <b>Nvidia GTX 970</b> is known to have a problematic design regarding its GPU memory that affects Substance 3D Painter. The last 500MB of the whole 4GB work at a slower pace than the remaining 3.5GB. If Substance 3D Painter works on those last 500MB, the performance can be reduced by as much as 10 times (from what we measured). For more technical details, see : <https://www.pcper.com/news/Graphics-Cards/NVIDIA-Responds-GTX-970-35GB-Memory-Issue>
