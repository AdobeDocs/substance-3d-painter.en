---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/workflow-issues/tools-issues/normal-map-looks-incorrect-when-loaded-in-layer-or-tool-properties.html"
breadcrumb-title: ""
description: Learn how to fix normal map display issues in Substance 3D Painter layer and tool properties for accurate surface detail.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Workflow Issues > Tools Issues > Normal map looks incorrect when loaded in layer or tool properties
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Normal map looks incorrect when loaded in layer or tool properties
user-guide-description: ""
user-guide-title: ""
---

# Normal map looks incorrect when loaded in layer or tool properties

When loading a normal into the current tool of fill layer, this one can appear incorrect if it's an OpenGL normal map.   
The reason is quite simple : the engine of Substance 3D Painter assume that loaded normal map are DirectX by default.

This behavior can easily be edited by clicking on the little arrow next to the substance material or the dedicated channel:

![](../../../../assets/channel-format-override.png)
