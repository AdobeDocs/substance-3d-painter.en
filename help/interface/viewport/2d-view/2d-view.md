---
title: "2D view | Substance 3D Painter"
description: "Painter > Interface > Viewport > 2D view"
---

# 2D view

![](2d-view.jpg){width="450px"}

The 2D View displays the mesh UV islands from the currently selected [Texture Set](../../texture-set/texture-set.md). It allows to see the textures from the Layer Stack but also to paint on the mesh UV islands.

## Display Mode

![](display-mode-1.png)

At the top right of the viewport is the display mode dropdown. This control allows to change what information should be visible in the viewport. It allows to display single channels, mesh maps or the final material result with lighting.

## Axis Information

![](2d-axis.png)

At the bottom right of the viewport is the **Axis Information**, which indicates the direction of the two dimensional axes. In the case if the 2D view the axes are U and V.

## UV Tile Information

![](2d-view-button.png)

Next to the **Display Mode** is the **UV Tile information** button which allows to show/hide information related to UV Tiles. This button is not visible with regular projects.

## Project Workflow

Depending of the workflow defined when creating a project, the 2D view may look and behave differently:

| *Project Workflow* | *Behaviors* |
| --- | --- |
| **Regular project** | With regular project, only the UV withing the UV range &#91;0-1&#93; can be painted on. Anything outside this range will be visible but won't be interactive.In this example only the UV islands on the left can be painted on (with the light gray background behind). <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table_row-r1-column-c1_dynamic_grid_items_grid-cell_position-par_image" src="2d-view-range-regular.jpg" width="500px"/></div> |
| **UV Tile project** | With UV Tile project, each UV range is a new set of textures, which can be painted on. The 2D view displays as well a grid to see better how each tile is organized. Each tile will have a UDIM number assigned. <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table_row-r2-column-c1_dynamic_grid_items_grid-cell_position-par_image" src="2d-view-range-uvtiles.jpg" width="500px"/></div> |
