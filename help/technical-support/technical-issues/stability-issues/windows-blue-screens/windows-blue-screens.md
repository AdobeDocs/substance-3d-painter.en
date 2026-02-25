---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/stability-issues/windows-blue-screens.html"
breadcrumb-title: ""
description: Learn how to prevent Windows blue screen errors when using Substance 3D Painter for stable system operation.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Technical Issues > Stability Issues > Windows Blue Screens
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Windows Blue Screens
user-guide-description: ""
user-guide-title: ""
---


# Windows Blue Screens

On Windows  [Blue Screens Of Death (BSOD)](https://en.wikipedia.org/wiki/Blue_screen_of_death)  are usually related to drivers or hardware malfunctions. Substance 3D Painter itself is not responsible of those BSODs, but it can put some light on an issue with the computer itself because of how intensive the application is. In the case of Substance 3D Painter, a BSOD can be caused because of the following issues.

## Unstable GPU drivers

Substance 3D Painter relies a lot on the GPU to perform its various computation. GPU drivers can sometimes be unstable or have regressions. We recommend to keep the GPU up to date to get the latest fixes and performance improvements. See: [GPU has outdated drivers](../../../../technical-support/technical-issues/gpu-issues/gpu-has-outdated-drivers/gpu-has-outdated-drivers.md).

### Unstable Windows installation

Windows itself can be unstable after some updates. Use the diagnostic tools provided with Windows to detect any potential errors in the system.

We recommend running the  **Deployment Image Servicing and Management**  (DISM) and the  **System File Checker**  (SFC) tool. DISM is useful to recover the replacement files needed by SFC in order to fix corrupted or missing system files.

Running  **DISM**  :

1. Open the  **Start menu**
1. Search for  **Command Prompt**
1. **Right click**  on the result and choose "  **Run as Administrator**  "
1. Type the following command :  **DISM /Online /Cleanup-Image /RestoreHealth**
1. Press  **Enter**

Running  **SFC**  :

1. Open the  **Start menu**
1. Search for  **Command Prompt**
1. **Right click**  on the result and choose "  **Run as Administrator**  "
1. Type the following command :  **sfc /scannow**
1. Press  **Enter**

Restart your computer after both commands to apply updates.

For more information on this subject see :  [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/en-us/help/929833/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system)

### Lack of Disk Space

Since the introduction of the [Sparse Virtual Textures](../../../../features/sparse-virtual-textures/sparse-virtual-textures.md) in Substance 3D Painter, the application now use the disk to cache textures while working. If the system run out of space, this can lead to instabilities.

There are two easy solution to this problem:

* Free some space of your disk to make more room to the cache system.
* Move the cache directory to another drive with more space. This location can be changed by going into the main settings of the application, see the  ["Temporary Files" setting](https://docs.substance3d.com/display/SPDOC/General)  .

### Faulty Disk (HDD or SSD)

As mentioned with the previous point, the cache system relies heavily on the disk. If the disk drive is faulty, this can make the system unstable when trying to write or read data.

To detect if a disk is faulty, you can run CHKDSK on Windows:

1. Open the  **Star Menu**
1. Select  **Computer / This PC**
1. **Right-click**  on your Hard Drive and choose  **Properties.**
1. Switch to the  **Tools**  tab.
1. Click on  **Check / Check now**  under  **Error Checking**  .

### Faulty Memory

Faulty memory (RAM) can lead to system instabilities if a program can't read or write to the memory safely. To check the memory integrity we recommend running  **MemTest**.

See  [this guide](https://www.memtest86.com/technical.htm)  on how to install and use MemTest.
