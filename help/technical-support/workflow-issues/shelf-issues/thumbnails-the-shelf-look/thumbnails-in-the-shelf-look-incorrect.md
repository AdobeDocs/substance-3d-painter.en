---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/workflow-issues/shelf-issues/thumbnails-in-the-shelf-look-incorrect.html"
breadcrumb-title: ""
description: Learn how to fix incorrect thumbnail display in Substance 3D Painter shelf to ensure accurate resource previews.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Workflow Issues > Shelf Issues > Thumbnails in the shelf look incorrect
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Thumbnails in the shelf look incorrect
user-guide-description: ""
user-guide-title: ""
---

# Thumbnails in the shelf look incorrect

If the thumbnails in the shelf appear to be different than habitual it may be because of the shader used to render the previews.

| Broken thumbnails | Normal thumbnails |
| --- | --- |
| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table_row-r1-column-c0_dynamic_grid_items_grid-cell_position-par_image" src="../../../../assets/shelf-broken-preview.png"/></div> | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table_row-r1-column-c1_dynamic_grid_items_grid-cell_position-par_image" src="../../../../assets/shelf-normal-preview.png" width="300px"/></div> |

## 1 - Open the main settings window

Go to  **Edit**  and click on  **Settings**  :

![](../../../../assets/pref-menu.png)

## 2 - Remove the Shelf preview shader

In the  **General**  view scroll down until the "Preview options" section is visible.   
Click on the  **cross**  button in front of the "  **Material preview shader**  " to remove the current shader specified.

![](../../../../assets/remove-preview-shader.png){width="450px"}

## 3 - Restart Substance 3D Painter

In order to regenerate the thumbnails so that they can look correct Substance 3D Painter needs to be restarted.
