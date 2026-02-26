---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/workflow-issues/tools-issues/paint-tool-bleeds-on-other-uv-islands.html"
breadcrumb-title: ""
description: Learn how to fix paint tool bleeding across UV islands in Substance 3D Painter to maintain clean texture boundaries.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Workflow Issues > Tools Issues > Paint Tool bleeds on other UV islands
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Paint Tool bleeds on other UV islands
user-guide-description: ""
user-guide-title: ""
---

# Paint Tool bleeds on other UV islands

Some default behaviors of the [ Paint tool](../../../../features/effects/paint/paint.md) may seem counter-intuitive in some specific situations. Substance 3D Painter is an application that mainly work in 3D space, this applies to painting as well. The default setting of the paint brush is to try to be seamless across UVs when painting. This is why when interacting with the 2D view some results may seem unexpected.

To avoid the bleeding on other UV islands when painting in the 2D view simply change the  **Alignment**  setting in the tool parameters:

| *Alignment Mode* | *Preview* |
| --- | --- |
| **Tangent Wrap** | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table_row-r1-column-c1_dynamic_grid_items_grid-cell_position-par_image" src="../../../../assets/paint-mode-tangent-optim.gif"/></div> |
| **UV** | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table_row-r2-column-c1_dynamic_grid_items_grid-cell_position-par_image" src="../../../../assets/paint-mode-uv.gif" width="450px"/></div> |
