---
title: "Crash or freeze during startup | Substance 3D Painter"
description: "Painter > Technical support > Technical Issues > Startup Issues > Crash or freeze during startup"
---

# Crash or freeze during startup

This page list known issues and their solutions related to the application not starting up properly.

## Software conflicts

Take a look at the following page for a list of all the known software that may create conflicts: [Software conflicts](../software-conflicts/software-conflicts.md).

## Running on the wrong GPU

If the application doesn't start on the right GPU it might lead to stability issues. See this page for more: [Painter doesn't start on the right GPU](../../gpu-issues/painter-doesn-start-the/painter-doesn-t-start-on-the-right-gpu.md).

## Outdated GPU Drivers

Using old GPU drivers can lead to freezes and/or crashes. We recommend to use the latest GPU drivers when available. See: [GPU has outdated drivers](../../gpu-issues/gpu-has-outdated-drivers/gpu-has-outdated-drivers.md).

## White screen and unresponsive

If the application freeze right when starting up on Windows (leading to a white screen) it can be of a few reasons:

* An external application is creating a conflict, see [Software conflicts](../software-conflicts/software-conflicts.md) to know which ones.
* Some windows of the application were opened on another monitor. Restoring the interface to its default layout allow to start the application normally:
  1. Open the registry editor (**regedit** from the start menu)
  1. Navigate to the application preferences (see: [Preferences and application data location](https://helpx.adobe.com/substance-3d/unlisted/documentation/spdoc/application-preferences-location-147095594.html))
  1. Expand the **Adobe Substance 3D Painter** key
  1. Select the **Main window 2018** key and delete it
  1. Restart the application

## Crash because of incorrect system Path/Python Path

The application checks the system Path to load Python modules and environment settings. If the system has an incorrect setup it can lead to a crash during the startup.

On Windows:

1. Open the  **Start**  menu
1. Search for and select the  **System (Control Panel)**
1. Click on  **Advanced system settings**
1. Click on  **Environment Variables**
1. Under  **System Variables**  find the  **PATH**  variable

You can then edit the variable to verify its content. For example if the variable contains this kind of following characters it will lead to a crash

```

ï–›éŒ à €è¸€ì‡ì‡ç¿¹
```


## Windows 10 Updates

Some update of Windows 10 may sometimes create instabilities. Use the diagnostic tools provided with Windows to detect any potential errors in the system.

We recommend running the  **Deployment Image Servicing and Management**  (DISM) and the  **System File Checker**  (SFC) tool. DISM is useful to recover the replacement files needed by SFC in order to fix corrupted or missing system files.

Running  **DISM**  :

1. Open the Start menu
1. Search for Command Prompt
1. Right click on the result and choose "Run as Administrator"
1. Type the following command :  **DISM /Online /Cleanup-Image /RestoreHealth**
1. Press Enter

Running  **SFC**  :

1. Open the Start menu
1. Search for Command Prompt
1. Right click on the result and choose "Run as Administrator"
1. Type the following command :  **sfc /scannow**
1. Press Enter

Restart your computer after both commands to apply updates.

For more information on this subject see:  [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/en-us/help/929833/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system).

## Crash when starting up on older versions

On Windows, version 2018 (4.x) or older may not start because one of the dll file provided with the installation folder is too old for the operating system. This crash can be fixed by manually replacing the file with a more recent version.

To do so:

1. Navigate to Substance Painter installation folder.
1. Rename the file <b>libeay32.dll</b> in <b>backup\_libeay32.dll</b>.
1. Download the following file: [updated\_libeay32.zip](https://helpx.adobe.com/content/dam/help/en/substance-3d/documentation/spdoc/files/182266673/225968681/1/1644000679697/updated-libeay32.zip).
1. Extract the dll file from the zip file into the installation folder (next to Substance Painter.exe file).
1. Start the application.
