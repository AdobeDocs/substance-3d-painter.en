---
title: "Retrieving the installation path | Substance 3D Painter"
description: "Painter > Pipeline and integration > Installation and preferences > Retrieving the installation path"
---

# Retrieving the installation path

This page regroups information on ways to retrieve the installation path of the application depending on the version and platform.

## Windows

### Creative Cloud Desktop

1. Open Windows registry editor (**regedit**).
1. Navigate to the registry key: **HKEY\_LOCAL\_MACHINE\Software\Microsoft\Windows\CurrentVersion\App Paths\**
1. Open the sub-key named **Adobe Substance 3D Painter.exe**
1. The value of the key contains the path to the application executable where it is installed

>[!NOTE]
>
> This registry key is only available since version 7.2.  
>  For older versions, the installation path can be retrieved from the file associations in **HKEY\_CURRENT\_USER\Software\Microsoft\Windows\CurrentVersion\ Explorer\FileExts**.

### Substance 3D Standalone

1. Open Windows registry editor (**regedit**).
1. Navigate to the registry key: **HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall**
1. Find the sub-key matching the AppID of your application version (see the table below)
1. The value of the key contains the path to the application installation location

| Version | AppId |
| --- | --- |
| **Version 1.x** | ``` {410F5B6E-A29C-4F43-9DE3-44A1357D6AF5} ``` |
| **Version 2.x** | ``` {f42b7a996fa1d13a1d0a2e33eea2c0800bb5d1b8} ``` |
| **3.x (2017.x) to 7.1** | ``` {33C3E9E2-0675-4196-9019-28AB9C5E9BB0} ``` |
| **7.2 or newer** | ``` {2a8bbb68-725b-477c-9194-60efc5ece348} ``` |

### Steam

The application is installed in the **steamapps/common/** sub-folder of the Steam installation folder.

## Mac

On Mac the application is installed in the following:

| Version | Path |
| --- | --- |
| **7.2 or newer** | **/Applications/Adobe Substance 3D Painter.app** |
| **Legacy** | **/Applications/Substance Painter.app** |

## Linux

On Linux the rpm package is installed in the following path:

| Version | Path |
| --- | --- |
| **7.2 or newer** | **/opt/Adobe/Adobe\_Substance\_3D\_Painter** |
| **Legacy** | **/opt/Allegorithmic/Substance\_Painter** |
