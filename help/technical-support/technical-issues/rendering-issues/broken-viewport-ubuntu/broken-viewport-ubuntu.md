---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/rendering-issues/broken-viewport-ubuntu.html"
breadcrumb-title: ""
description: Learn how to fix broken or unresponsive viewport issues on Ubuntu in Substance 3D Painter for proper 3D rendering.
helpx_creative_field: ""
helpx_description: Viewport appears broken or unresponsive on Ubuntu
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Viewport appears broken or unresponsive on Ubuntu
user-guide-description: ""
user-guide-title: ""
---


# Viewport appears broken or unresponsive on Ubuntu

When running Painter from Steam on Ubuntu starting with version 11.1, the viewport can appear broken or unresponsive.

This is is related to Painter not starting with the right GPU assigned to it. On Ubuntu the integrated GPU instead of the discreet one can end-up being selected. Painter inherits this configuration via Steam which can create issues.

A few solutions exists:

1. Run Steam from a Terminal. This will force a different context and should make Steam and Painter run on the right GPU.
1. Edit the Steam shortcut to disable the <b>Run using dedicated graphics card</b> setting. Then run Steam as normal.

For more information, see [this github issue](https://github.com/ValveSoftware/steam-for-linux/issues/9940).
