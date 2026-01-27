---
title: "Spherical projection | Substance 3D Painter"
description: "Painter > Painting > Fill projections > Spherical projection"
---

# Spherical projection

![](spherical-proj.jpg)

The fill Spherical projection allows to project images and patterns around an object. It can be useful to project on round objects or distort texture into circular patterns.

## Properties

| Setting | Description |
| --- | --- |
| **Filtering** | Controls how the texture or material will be filtered. This setting can impact how the texture looks when repeated multiple times. With high scaling values using a different filtering than the default may produce better looking result. Current settings available:<ul data-preserve-html="true"><li data-preserve-html="true"><strong>Bilinear &#124; HQ</strong> (default): Advanced bilinear filtering that tries to improve the quality of the texture when the tiling values are high.</li><li data-preserve-html="true"><strong>Bilinear &#124; Sharp</strong>: Simple bilinear filtering that smooths the texture slightly but try to preserve details.</li><li data-preserve-html="true"><strong>Nearest</strong>: No filtering, useful if the Bilinear filtering gives a blurry result and breaks fine details. Can introduce aliasing in the texture.</li></ul> |
| **UV Wrap** | Control how the texture repeats within the projection. Possible values are:<ul data-preserve-html="true"><li data-preserve-html="true"><strong>None</strong>: the texture doesn't repeat. Anything outside the texture is black/transparent.</li><li data-preserve-html="true"><strong>Repeat horizontally</strong>: the texture only repeats horizontally.</li><li data-preserve-html="true"><strong>Repeat vertically</strong>: the texture only repeats vertically.</li><li data-preserve-html="true"><strong>Repeat</strong> (default): the texture repeats on both axes.</li></ul> <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table_row-r2-column-c1_dynamic_grid_items_grid-cell_position-par_image" src="spherical-repeat.jpg" width="500px"/></div> |
| **Shape Crop** | Define if the projected texture should be visible outside of the projection area. Possible values are:<ul data-preserve-html="true"><li data-preserve-html="true"><strong>Project cropped to shape</strong>: the projection is confined within the projection area.</li><li data-preserve-html="true"><strong>Projection extends outside shape</strong> (default): the projection continues beyond the projection area.</li></ul> <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table_row-r3-column-c1_dynamic_grid_items_grid-cell_position-par_image" src="spherical-shape-crop.jpg" width="500px"/></div> |

### UV transformation

The UV transformation settings control the texture within the projection.

| *Setting* | *Description* |
| --- | --- |
| **Scale** | Define how many times the texture will repeat inside the projection. |
| **Rotation** | Control the angle of the texture applied to the projection. |
| **Offset** | Control the origin of the texture that is projected. The default value means the texture is in the middle of the projection. |

### 3D projection settings

The 3D projection settings control the transformation of the projection in 3D space.

| Setting | Description |
| --- | --- |
| **Offset** | Position of the origin of the projection in 3D space. The units are based on the bounding box of the whole scene. 0 is the center of this box. |
| **Rotation** | Angles in degrees to rotate the whole projection on each axes. |
| **Scale** | Size of the whole projection on each axes. |

## Contextual Toolbar

Several settings and tools are available from the [Contextual toolbar](../../../interface/toolbars/toolbars.md) sitting at the top of the viewport which give controls over the manipulator and the projection:

| Icon | Name | Description |
| --- | --- | --- |
| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table1_row-r1-column-c0_image" src="icon-hide-manipulator.png" width="50px"/></div> | Show/Hide manipulator | If enabled, the manipulator is visible and controllable in the viewport. |
| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table1_row-r2-column-c0_image" src="icon-manipulator-settings.png" width="50px"/></div> | Manipulator settings | This menu contains three settings:<ul data-preserve-html="true"><li data-preserve-html="true"><strong>Manipulator size</strong>: control how big the manipulator is in the viewport.</li><li data-preserve-html="true"><strong>Grid steps</strong>: define the size of the step when translating with a constraint.</li><li data-preserve-html="true"><strong>Angle steps</strong>: define the angle of the step when rotating with a constraint.</li></ul> |
| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table1_row-r3-column-c0_dynamic_grid_items_grid-cell_position-par_image" src="icon-translate.png" width="50px"/></div> | Translation manipulator | Allow to move the projection in the scene along the main axes (X, Y, Z). |
| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table1_row-r4-column-c0_dynamic_grid_items_grid-cell_position-par_image" src="icon-rotate.png" width="50px"/></div> | Rotation manipulator | Allow to rotate the projection in the scene along the main axes (X, Y, Z). |
| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table1_row-r5-column-c0_dynamic_grid_items_grid-cell_position-par_image" src="icon-scale.png" width="50px"/></div> | Scale manipulator | Allow to scale the projection in the scene along the main axes (X, Y, Z). |
| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table1_row-r6-column-c0_dynamic_grid_items_grid-cell_position-par_image" src="icon-surface.png" width="50px"/></div> | Surface manipulator | Allow to move the projection by snapping it on the 3D model surface.  **Note:**  This manipulator is only available with the Planar and Warp projection types. |
| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table1_row-r7-column-c0_dynamic_grid_items_grid-cell_position-par_image" src="icon-space.png" width="50px"/></div> | Manipulator space | Define in which space the transformation are performed. Possible values are:<ul data-preserve-html="true"><li data-preserve-html="true"><strong>Local space</strong>: axes are aligned with the current transformation.</li><li data-preserve-html="true"><strong>World space</strong>: axes are aligned with scene.</li></ul> |
| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table1_row-r8-column-c0_dynamic_grid_items_grid-cell_position-par_image" src="icon-flip-x.png" width="50px"/></div> | Mirror on X | Flip the transformation on the X axis. |
| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table1_row-r9-column-c0_dynamic_grid_items_grid-cell_position-par_image" src="icon-flip-y.png" width="50px"/></div> | Mirror on Y | Flip the transformation on the Y axis. |
| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table1_row-r10-column-c0_dynamic_grid_items_grid-cell_position-par_image" src="icon-flip-z.png" width="50px"/></div> | Mirror on Z | Flip the transformation on the Z axis. |
| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table1_row-r11-column-c0_dynamic_grid_items_grid-cell_position-par_image" src="icon-reset.png" width="50px"/></div> | Reset transformation | Restore the projection transformation back to its default state. |

## Manipulator

This projection manipulator is only available in the [3D viewport](../../../interface/viewport/3d-view/3d-view.md).

| Action | Shortcut | Description |
| --- | --- | --- |
| **Translation** | Mouse click | With the Translation manipulator, clicking on the axes move the projection:<ul data-preserve-html="true"><li data-preserve-html="true"><strong>One axis</strong>: only move in one direction the projection.</li><li data-preserve-html="true"><strong>Two axes</strong>: move the projection on the plans aligned with the axes.</li><li data-preserve-html="true"><strong>Three axes</strong>: move the projection in the space of the camera (plan facing it).</li></ul>   <table> <tr style="border: 0;"> <td style="border: 0;" valign="top">  <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table2_row-r1-column-c2_dynamic_grid_items_grid-cell_position-par_image" src="3d-translate.gif" width="200px"/></div>  </td> <td style="border: 0;" valign="top">  <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table2_row-r1-column-c2_dynamic_grid_items_grid-cell1_position-par_image" src="3d-translate-2axes.gif" width="200px"/></div>  </td> <td style="border: 0;" valign="top">  <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table2_row-r1-column-c2_dynamic_grid_items_grid-cell2_position-par_image" src="3d-translate-3axes.gif" width="200px"/></div>  </td> </tr> </table> |
| **Translation constrained** | SHIFT+Mouse click | With the Translation manipulator, move the projection along the selected axes but only at specific intervals (stepping). The size of the interval is defined via the manipulator settings. <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table2_row-r2-column-c2_dynamic_grid_items_grid-cell_position-par_image" src="3d-translate-step.gif" width="200px"/></div> |
| **Rotation** | Mouse click | With the Rotation manipulator, clicking on one axes rotate the projection. Click in-between the axes allow to rotate all the axes at the same time.   <table> <tr style="border: 0;"> <td style="border: 0;" valign="top">  <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table2_row-r3-column-c2_dynamic_grid_items_grid-cell_position-par_image" src="3d-rotate.gif" width="200px"/></div>  </td> <td style="border: 0;" valign="top">  <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table2_row-r3-column-c2_dynamic_grid_items_grid-cell1_position-par_image" src="3d-rotate-3axes.gif" width="200px"/></div>  </td> </tr> </table> |
| **Rotation constrained** | SHIFT+Mouse click | With the Rotation manipulator, clicking on one axis to rotate the projection will only happen at specific intervals. The step is defined by an angle via the manipulator settings. <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table2_row-r4-column-c2_dynamic_grid_items_grid-cell_position-par_image" src="3d-rotate-step.gif" width="200px"/></div> |
| **Scale** | Mouse click | With the Scale manipulator, clicking on one axis handle resize the projection along the given axis.   <table> <tr style="border: 0;"> <td style="border: 0;" valign="top">  <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table2_row-r5-column-c2_dynamic_grid_items_grid-cell_position-par_image" src="scale-one-axis.gif" width="200px"/></div>  </td> <td style="border: 0;" valign="top">  <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table2_row-r5-column-c2_dynamic_grid_items_grid-cell1_position-par_image" src="scale-two-axis.gif" width="200px"/></div>  </td> <td style="border: 0;" valign="top">  <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table2_row-r5-column-c2_dynamic_grid_items_grid-cell2_position-par_image" src="scale-3-axes.gif" width="200px"/></div>  </td> </tr> </table> |
| **Scale constrained** | SHIFT+Mouse click | With the Scale manipulator, clicking on one axis handle while maintaining the shortcut will resize the projection in steps. The step size is the same as for the Translation manipulator. <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table2_row-r6-column-c2_dynamic_grid_items_grid-cell_position-par_image" src="scale-1-axis-constrained.gif" width="200px"/></div> |
| **Surface** | Mouse click | With the Surface manipulator, clicking and dragging it over the 3D model will snap it on the surface. <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table2_row-r7-column-c2_dynamic_grid_items_grid-cell_position-par_image" src="surface.gif" width="200px"/></div> **Note:**  This manipulator is only available with the **Planar** and **Warp** projection types. |
