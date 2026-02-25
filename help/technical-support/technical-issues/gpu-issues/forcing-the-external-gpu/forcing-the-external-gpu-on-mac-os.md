---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/gpu-issues/forcing-the-external-gpu-on-mac-os.html"
breadcrumb-title: ""
description: Learn how to force Substance 3D Painter to use external GPU on macOS for improved rendering performance.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Technical Issues > GPU Issues > Forcing the external GPU on Mac OS
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Forcing the external GPU on Mac OS
user-guide-description: ""
user-guide-title: ""
---


# Forcing the external GPU on Mac OS

On Mac OS Mojave, it is possible to specify per application to use the external GPU. Substance 3D Painter performances and stability may improve with this setting enabled.

For more information refer to [Apple documentation](https://support.apple.com/en-us/HT208544).

To enable it:

1. Close Substance 3D Painter if it is already running.
1. Select Substance 3D Painter in the Finder, it can be found in the **Applications** folder**.**
1. Presse **Command-I** or Right-Click on the **Substance 3D Painter** application and choose **Get Info**.
1. In the new window, enable the setting **Prefer External GPU**.
1. Restart Substance 3D Painter.

>[!NOTE]
>
> This setting won't be visible if an eGPU is not connected or if the current version of MacOS is too old.
