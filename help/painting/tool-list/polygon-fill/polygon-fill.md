---
title: "Polygon fill"
description: "Use the Polygon Fill tool in Substance 3D Painter to fill selected polygons with paint for efficient texture painting."
helpx_description: Painter > Painting > Tool list > Polygon fill
helpx_url: "https://helpx.adobe.com/substance-3d-painter/painting/tool-list/polygon-fill.html"
helpx_creative_field:
  - graphic-design
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - polygon
  - fill-and-sign
  - content-aware-fill
---




# Polygon fill

The **Polygon Fill** tool (![](image2018-6-12-18-15-12.png)) allows you to draw masks quickly by turning selected polygons into a pixel mask. It might seem like a 3D selection tool from other 3DCC applications, but is actually a painting fill tool that results in pixel data. That means selecting and unselecting works by using it to paint white or black.

Polygon fill tool functions on [Paint Layers,](../../../help/interface/layer-stack/layer-stack.md) but is limited to basecolor only and not intended for this purpose. [Use it for masks only](../../../help/interface/layer-stack/masking-and-effects/masking-and-effects.md).

It has 4 selection modes:

* ![](image2020-9-30-11-31-53.png) **Triangle Fill** - fills individual mesh tri's.
* ![](image2020-9-30-11-32-12.png) **Polygon Fill** - fills entire polygons. Doesn't do anything different from Triangle Fill if your mesh is already triangulated upon export.
* **![](image2020-9-30-11-32-42.png) Mesh Fill** - fills entire connected sub-meshes. Like "sub-object" mode in 3D applications, will fill every polygon connected to the one clicked.
* **![](image2020-9-30-11-32-54.png) UV chunk Fill** - fills entire UV chunk or "island". Works like Mesh fill, but by looking at polygons connected in UV space. Filling stops at UV borders.

![](polygon-fill.gif)

These 4 Modes can be combined and switched, meaning some smart usage lets you quickly mark and unmark sections in a mask using Mesh and UV chunk mode.

The (default) hotkeys associated to Polygon Fill tool are:

* *Numeric key 4* - selects the Polygon Fill tool.
* *X* - Inverts current color when painting masks. Will quickly swap black for white. In material painting mode this hotkey has no effect.
