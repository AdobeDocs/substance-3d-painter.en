---
title: "Crash during export"
description: ""
helpx_description: "Painter > Technical support > Technical Issues > Stability Issues > Crash during export"
---

# Crash during export

Some specific cases can lead to Substance 3D Painter crashing while exporting, especially at very high resolution (such as 4K or 8K). Below is a list of the most common sources of this issue.

## TDR (Timeout Detection and Recovery)

The Timeout Detection and Recovery (TDR) is a safety mechanism of Microsoft Windows to prevent a GPU from locking up the system with a never ending computation. This mechanism is unfortunately too restrictive for Substance 3D Painter by default.

For more information see: [GPU drivers crash with long computations (TDR crash)](https://helpx.adobe.com/substance-3d/unlisted/documentation/spdoc/gpu-drivers-crash-with-long-computations-128745489.html).

## Low Virtual Memory

Exporting can consume a large amount of RAM (Computer Memory), in which case the system will try to fallback on the virtual memory if the system runs out of RAM. The virtual memory is usually additional memory stored on hard disk drives. If the virtual memory size is too small, Substance 3D Painter will crash because it ran out of total memory.

For more information, see: [Crash with low virtual memory](../crash-with-low-virtual/crash-with-low-virtual-memory.md).

## Lack of Disk Space

Since the introduction of the Sparse Virtual Textures (SVT) Substance 3D Painter can stream out on the disk some cache to balance performances. If there is not enough free space on your disk, it may lead to a crash because the application wasn't able to transfer and write the cache.

The cache location can be moved from the default system temporary files folder. For more information see: [Sparse Virtual Textures](../../../../features/sparse-virtual-textures/sparse-virtual-textures.md).

## Overclocked GPU frequency

Overclocked GPUs can often be more unstable because they run of frequencies that weren't initially designed by the GPU constructor. It may helps to disable the overclocking for a while.

For more information, see: [Crash when working with overclocked GPU](../../gpu-issues/crash-when-working-with/crash-when-working-with-overclocked-gpu.md).
