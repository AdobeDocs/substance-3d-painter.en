---
title: "Painter doesnt start on the right GPU | Substance 3D Painter"
description: "Painter > Technical support > Technical Issues > GPU Issues > Painter doesnt start on the right GPU"
---

# Painter doesn't start on the right GPU

On Windows, the application may not use the right GPU when starting up which can lead to performance and stability issues. Below is a list of of common issues and their solutions to make sure the software works with the right GPU.

To know which GPU is used, you can check the [log file](../../../exporting-the-log-file/exporting-the-log-file.md).

## Monitor Cables Configuration

On Windows the GPU assigned to an application depends of the monitor on which the application is running. This is because the monitor cables are linked directly to the output of the GPU itself. The application may start on the wrong GPU therefore if the monitor on which it starts is linked to the graphics output of the motherboard instead of the one from the graphic card itself. In that case, Windows is likely to use the integrated GPU rather than the dedicated GPU.

**To solve this issue** : simply fix the cable configuration by un-plugin the monitor linked to the motherboard and then linking it to the GPU outputs instead.

## Incorrect GPU Driver Installation

If the GPU drivers are not properly installed the application will be unable to reach the dedicated GPU and it will have to fallback on the integrated GPU instead.

**To solve this issue** : uninstall the current GPU drivers, perform a cleanup and then reinstall the GPU drivers after a reboot of the computer.

## Nvidia GPU driver profile setting

On some computers, such as Laptops, the application may run on the integrated GPU instead of the dedicated Nvidia GPU by default. With an NVIDIA GPU, the switch to the right GPU depends on application profiles. If an application does not have such profile, you can assign one manually.

**To solve this issue** :

1. Right-click on the Desktop and select NVIDIA Control Panel **or** Navigate to the Control Panel and search for NVIDIA Control Panel
1. Under **3D Settings**, go to **Manage 3D Settings**
1. Under the tab **Program settings** add a new profile for **Substance 3D Painter**
1. Change the preferred graphics processor setting to High-performance NVIDIA processor

## Windows Performance Setting

Windows may have set the wrong GPU setting for the application because of the default performance and power consumption settings.

**To solve this issue :** follow the step by step below to override the default GPU configuration.

1. Open the display settings by right-clicking on your desktop :

   ![](settings-33.png)
1. Navigate to the bottom of the window on the home and click on "Graphics Settings" :

   ![](graphics-settings.png)
1. Click on the "Browse" button and locate the Substance 3D Painter executable :

   ![](browse-16.png)
1. Once the application has been added, click on the button "Options" :

   ![](options-19.png)
1. Choose the setting "High performance" and click on the "Save" button

   ![](specs.png)
