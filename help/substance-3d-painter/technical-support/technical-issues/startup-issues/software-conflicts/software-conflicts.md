---
title: "Software conflicts | Substance 3D Painter"
description: "Painter > Technical support > Technical Issues > Startup Issues > Software conflicts"
---

# Software conflicts

This page contains a list of known issues with other software that may crash or stop Substance 3D Painter from running correctly.

| *Potential source of conflict* | *Issue* |
| --- | --- |
| **Anti-Virus / Anti-Spyware** | Anti-virus or anti-spyware software can create some of the following issues:<ul data-preserve-html="true"> <li data-preserve-html="true"><b> False positive</b>: Painter is incorrectly flagged as a virus or malware.</li> <li data-preserve-html="true"><b> Blocked files</b>: Painter cannot read or write files (export, preset creation, etc).</li> <li data-preserve-html="true"><b> File deletion</b>: Painter cannot start or work normally because necessary files have been removed.</li> </ul>If one of these situations arises, we recommend temporarily disabling the anti-virus to see if it helps or manually adding exceptions for Painter. |
| **AMD CrossFire &amp; NVIDIA SLI** | Multiple GPU configurations are unsupported by Painter, leading to crashes. We recommend disabling this feature. |
| <b> Autodesk assistant </b> | The Autodesk assistant application can create conflicts and make the application crash at startup or when opening a project file. Update the Autodesk application to resolve the problem. |
| <b> Alienware / Dell computers</b> | See this page for more information: [Crash when opening or saving a file](../../stability-issues/crash-when-opening-saving/crash-when-opening-or-saving-a-file.md). |
| **APFS by Paragon Software** | This software may register a location in the Windows Path environment variable that can crash the application at startup. Uninstalling the software may not be enough and the environment variable may need to removed manually. Example of problematic location:  ``` C:Program Files (x86)Paragon SoftwareAPFS for Windowsï–›éŒ à €è¸€ì‡ì‡ç¿¹ ``` |
| **Avecto** | Having an older version of Avecto running can cause slowdowns and crashes. Make sure you update it to the latest version. |
| **Asus GPU Tweak** | This software can cause issues during the compilation of shaders within Substance 3D Painter or even prevent shader compilation from starting. If this issue is encountered, we recommended uninstalling the software to see if it fixes the problem. |
| **Asus RAMCache** | This software may prevent Substance 3D Painter from launching properly or make it unstable while running. We recommend disabling or installing Asus RAMCache if you are experiencing stability issues. |
| **Asus Sonic Suite** | On computers with an ASUS Motherboard, <b>Asus Sonic Suite</b> may be installed by default. Uninstalling this software can fix some display/interface issues in Substance 3D Painter. |
| **Cloud Backup Software**    **(  **OneDrive,**  GDrive,**   **Dropbox,**   **Filestream, etc)** | Cloud backup software can be the source of numerous crashes while saving a project. If this happens, it is recommended to work on and save the project file to a non-synced folder and instead copy the project files back into the cloud drive once changes are no longer being made. |
| **Chitubox** | This software can create a conflict and crash the application when opening a file dialog (like opening or saving a project). You can disable the setting <b>Enable thumbnail preview of desktop model</b> in the Chitubox preferences to avoid this issue. |
| **Duet Display** | <b>Duet Display</b> is known to create GPU drivers issues that can impact the behavior of Substance 3D Painter. It is recommended to uninstall it. |
| **Google Chrome** | Google Chrome can cause some crashes when running alongside Substance 3D Painter. To improve the stability of Substance 3D Painter, it is recommended that you update Google Chrome and the GPU drivers. If crashes still occur, disable Hardware Acceleration in Google Chrome (which will stop Chrome from using the GPU). |
| **Nahimic audio software** | <b>Nahimic</b> can freeze or crash the Painter. Stopping it can help, and updating it can also avoid issues. Nahimic also runs background services that can interfere with the application and may need to be stopped or disabled. |
| **Openshot Video Software** | <b>Openshot Video Software</b> can create a conflict with Substance 3D Painter with the previews of the shelf. Updating Openshot should fix the issue. |
| **Pyinstaller** | This application can produce an incorrect environment setup leading to an error at startup. For more information see [Application failed to start because of Qt](../application-failed-start/application-failed-to-start-because-of-qt.md). |
| **Rptr / Plays.tv** | <b>Rptr</b> (or <b>&#91;Plays.tv&#93;(http://plays.tv/) </b>) is installed by default with some GPU drivers. This software can create instabilities and crash the application. Uninstalling the application is recommended. |
| **RGBFusion** | This software can create conflicts with Graphic Tablet drivers, stopping the process can temporarily fix the problem, or uninstall RGBFusion for a permanent fix. |
