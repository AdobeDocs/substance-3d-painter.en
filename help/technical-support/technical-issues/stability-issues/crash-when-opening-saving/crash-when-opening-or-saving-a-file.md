---
title: "Crash when opening or saving a file"
description: ""
helpx_description: "Painter > Technical support > Technical Issues > Stability Issues > Crash when opening or saving a file"
---

# Crash when opening or saving a file

There are a few reasons why Substance 3D Painter would crash on Windows when opening a file dialog. This page regroups reasons and solutions to this issue.

## Software Conflicts

Some program can add custom shell extensions which can lead to instabilities or crashes. Take a look at the [Software conflicts](../../startup-issues/software-conflicts/software-conflicts.md) list for more information.

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
