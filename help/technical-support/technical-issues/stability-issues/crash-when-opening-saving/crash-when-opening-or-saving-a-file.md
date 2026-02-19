---
title: "Crash when opening or saving a file"
description: "Learn how to fix Substance 3D Painter crashes when opening or saving files for reliable project management."
helpx_description: Painter > Technical support > Technical Issues > Stability Issues > Crash when opening or saving a file
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/stability-issues/crash-when-opening-or-saving-a-file.html"
helpx_creative_field:
  - painting-illustration
  - web
  - 3d-immersive
  - graphic-design
helpx_experience_level:
  - any
helpx_learn_topic:
  - troubleshooting
  - gradient-mesh
  - system-requirements
---




# Crash when opening or saving a file

There are a few reasons why Substance 3D Painter would crash on Windows when opening a file dialog. This page regroups reasons and solutions to this issue.

## Software Conflicts

Some program can add custom shell extensions which can lead to instabilities or crashes. Take a look at the [Software conflicts](../../../../help/technical-support/technical-issues/startup-issues/software-conflicts/software-conflicts.md) list for more information.

## Shell extensions/Custom themes

Custom themes are not supported by our GUI framework, therefore it is highly recommended to uninstall the current theme before using Substance 3D Painter.

**Alienware**  /  **Dell**  computers integrate by default some shell extensions that are known to be incompatible with Substance 3D Painter. We recommend to uninstall them. While we do not know exactly all the extensions that are incompatible, most of the time they correspond to:

* DBROverlayIconBackuped.DBROverlayIconBackuped Class
* DBROverlayIconNotBackuped.DBROverlayIconNotBackuped Class

You can see which extensions are installed on your computer by using the following tool. Here is a rough procedure on how to proceed:

1. Download and install ShellExView from NirSoft: <http://www.nirsoft.net/utils/shexview.html>
1. Run the program
1. Click on  **Option**  and choose  **Filter By Extension Type**
1. Select  **Icon Overlay handler**
1. You should see the two entries for  **Alien Respawn**  .
1. Select  **both**  and click the red button to disable them.
