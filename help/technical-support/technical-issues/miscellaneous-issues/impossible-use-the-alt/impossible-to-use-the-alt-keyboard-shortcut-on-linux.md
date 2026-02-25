---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/miscellaneous-issues/impossible-to-use-the-alt-keyboard-shortcut-on-linux.html"
breadcrumb-title: ""
description: Learn how to fix ALT keyboard shortcut issues on Linux in Substance 3D Painter for proper keyboard navigation.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Technical Issues > Miscellaneous Issues > Impossible to use the ALT keyboard shortcut on Linux
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Impossible to use the ALT keyboard shortcut on Linux
user-guide-description: ""
user-guide-title: ""
---


# Impossible to use the ALT keyboard shortcut on Linux

If you are running a Linux distribution (**Ubuntu**  or  **CentOS**) which use  **Gnome**  as user interface, you might want to disable the default behavior of the  **ALT**  key to be able to navigate in the viewport.

## CentOS

1 - Go to  **System &gt; Windows**

![](centos-window.png){width="250px"}

2 - Change the "movement key" setting to something else than "  **Alt**  ". For example use "  **Super**  " (to choose the "Windows" key of your keyboard).

![](centos-setting.png){width="350px"}

## Ubuntu

1 - Open a terminal and run the following command:

```

sudo apt-get install dconf-tools
```


This will install an advanced configuration tool, you might have to allow additional dependencies to be installed to be able to run it.

2 - Open the start menu and look for "  **Dconf-tools**  ". Launch it.

3 - Expand the tree menu on the left by going to the following route :  **org &gt; gnome &gt; desktop &gt; wm &gt; preferences**

4 - Edit the "mouse-button-modifier" and change it value. Set it  or  instead, but  *don't leave it empty*  . Super is an equivalent to the "Windows" key.

![](ubuntu-setting.png){width="500px"}
