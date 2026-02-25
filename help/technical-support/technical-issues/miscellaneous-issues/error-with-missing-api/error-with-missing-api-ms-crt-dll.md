---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/miscellaneous-issues/error-with-missing-api-ms-crt-dll.html"
breadcrumb-title: ""
description: Learn how to fix missing api-ms-crt DLL errors in Substance 3D Painter for proper Windows runtime library support.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Technical Issues > Miscellaneous Issues > Error with missing api-ms-crt dll
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Error with missing api-ms-crt dll
user-guide-description: ""
user-guide-title: ""
---


# Error with missing api-ms-crt dll

Substance 3D Painter cannot start because  **api-ms-win-crt-runtime-l1-1-0.dll**  is missing from your computer.   
 This is most likely because the update KB2999226 which is part of the  **Visual C++ Redistributable**  for Visual Studio 2015 failed to install.

## How to fix the issue ?

### 1 - Verify that Windows is up to date

1. Open the Start menu
1. Select Control Panel
1. Click on  **Windows Update**
1. Click on  **Check for updates**
1. **Install**  all available updates.
1. After the updates are installed,  **restart**  your computer.

After the restart repeat the steps above again until no more updates are available.

### 2 - Install Visual C++ Redistributable

1. Download the Visual C++ Redistributable :
   1. For  [Windows 64-bit](http://download.microsoft.com/download/9/3/F/93FCF1E7-E6A4-478B-96E7-D4B285925B00/vc_redist.x64.exe)
   1. For  [Windows 32-bit](http://download.microsoft.com/download/9/3/F/93FCF1E7-E6A4-478B-96E7-D4B285925B00/vc_redist.x86.exe)
1. Run the  **vcredist\_x64.exe**  (64-bit) or  **vcredist\_x86.exe**  (32-bit)
1. Select Uninstall and follow the procedure
1. Run the executable again
1. Select Install
