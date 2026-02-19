---
title: "Depth of Field"
description: "Learn how to use depth of field post-processing in Substance 3D Painter to create realistic camera focus blur effects."
helpx_description: Painter > Features > Post Processing > Depth of Field
helpx_url: "https://helpx.adobe.com/substance-3d-painter/features/post-processing/depth-of-field.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - camera
  - effects
  - perspective
---




# Depth of Field

![](dof-example.jpg)![](dof.png)

The **Depth of Field** (DOF) has no direct parameter. If enabled, it will **override** the DOF from **Iray**.

For controlling the look of the DOF in the viewport, two settings are available via the Camera :

| *Setting* | *Description* |
| --- | --- |
| **Focus Distance** | Defines the distance at which the focus point is located.  This point is used by the Depth of Field effect. <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table_row-r1-column-c1_dynamic_grid_items_grid-cell_position-par_image" src="focus-distance-optim.gif"/></div> **Note:**  The Focus Distance can be set automatically by clicking on a point of the mesh with the shortcut **CTRL + Middle Mouse Button.** |
| **Aperture** | Defines how wide the Depth of Field will be. <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table_row-r2-column-c1_dynamic_grid_items_grid-cell_position-par_image" src="dof-aperture-optim.gif"/></div> **Note:**  If Iray is controlling this parameter, changing it will re-trigger a computation. |
