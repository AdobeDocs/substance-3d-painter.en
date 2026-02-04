---
title: "Remote Desktop"
description: ""
helpx_description: "Painter > Pipeline and integration > Configuration > Remote Desktop"
---

# Remote Desktop

This pages describes solutions and alternatives to make Substance 3D Painter able to run via Remote Desktop (RDP) on Windows.

By default RDP on Windows runs in an OpenGL context that is non-existent or too low, which makes the application unable to work properly or crash. Substance 3D Painter requires an OpenGL 3.3 context. Below are solutions to mitigate the problem, but there is no garanties they will work as the initial problem is dependent of Windows and some GPU drivers.

>[!NOTE]
>
> Nvidia Quadro GPUs can run the application in RDP mode by default while Nvidia GeForce GPUs only provide an OpenGL 1.4 context (which is too low for Substance 3D Painter). It is possible to install an executable to remedy to that, see: <https://developer.nvidia.com/designworks>

## Windows Policy Configuration

On Windows 10 it may be necessary to change the  **Group Policy**  to allow the GPU to be run while in RDP mode.

To do so:

1. Press  **Win + R**  to open the execute window
1. Type "  **gpedit.msc**  " then Enter
1. Navigate to  **Local Computer Policy\Computer Configuration\Administrative Templates\Windows Components\Remote Desktop Services\Remote Desktop Session Host\Remote Session Environment**
1. Enable the option  **Use the hardware default graphics adapter for all Remote Desktop Services sessions**  .

## Windows TSCON command

If the previous Policy change doesn't work, you may try to use the  **tscon**  command line. This command disconnect the remote computer and connect a new one to the physical hardware (mouse, keyboard, etc). Then simply running the application and reconnecting remotely should allow to work with the application on the GPU.

1. Press the key  **Windows+R**  to open the  **execute**  window.
1. Type  **cmd**  and press  **Enter**  .
1. In the command line type and the following command:  **tscon 1 /dest:console**
1. Press Enter
1. In the command line type the next command:  **start "Path/To/Substance/Painter/Folder/Substance 3D Painter.exe"**  (make sure to change the path to match your computer)
1. Press Enter

After these steps, wait a few seconds to let the application startup and then reconnect to your session.

You may have to run the Windows command line in administrator mode in case this procedure doesn't work.

## Alternatives

If previous suggestions still don't work we recommend using alternative solutions such as VNC or Teamviewer which support the GPU via remote connections.
