---
title: "Paint Tool bleeds on other UV islands"
description: ""
helpx_description: "Painter > Technical support > Workflow Issues > Tools Issues > Paint Tool bleeds on other UV islands"
---

# Paint Tool bleeds on other UV islands

Some default behaviors of the [ Paint tool](../../../../features/effects/paint/paint.md) may seem counter-intuitive in some specific situations. Substance 3D Painter is an application that mainly work in 3D space, this applies to painting as well. The default setting of the paint brush is to try to be seamless across UVs when painting. This is why when interacting with the 2D view some results may seem unexpected.

To avoid the bleeding on other UV islands when painting in the 2D view simply change the  **Alignment**  setting in the tool parameters:

| *Alignment Mode* | *Preview* |
| --- | --- |
| **Tangent Wrap** | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table_row-r1-column-c1_dynamic_grid_items_grid-cell_position-par_image" src="paint-mode-tangent-optim.gif"/></div> |
| **UV** | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table_row-r2-column-c1_dynamic_grid_items_grid-cell_position-par_image" src="paint-mode-uv.gif" width="450px"/></div> |
