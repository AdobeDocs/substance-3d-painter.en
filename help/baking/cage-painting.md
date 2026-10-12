---
title: Cage painting
description: Learn how to avoid artifacts and customize the cage during the baking process with cage painting in Substance 3D Painter.
hold: true
---

# Cage painting

**Cage painting** lets you paint areas to push the baking cage farther away or bring it closer to the low-poly surface. Cage painting helps prevent artifacts during baking while still capturing all the high-poly details of your mesh.

## Set up Cage painting

For **Cage painting** to be available, the project must have at least one High-poly scene file to bake from, and the Cage type must be set to **Distance-based**.

>[!NOTE]
>
> Support for **Cage painting** will be added for the **Automatic Cage type** in a future release.

We recommend setting the **Max frontal distance** and **Relative to bounding box** values before starting to paint your cage, as changing these values after painting may require touchups or even repainting the cage from scratch.

>[!TIP]
>
> If you want to start cage painting again from scratch, you can reset the cage painting parameters, cage painting strokes, or all baking settings.
>
> ![](../assets/baking/cage-painting/resetcage.png)

## Start Cage painting

To start Cage painting:

1. Switch to [**Baking mode**](baking.md).
1. Ensure that you have selected at least one **High-poly scene** file to bake from.
1. In the **Common settings** **panel**, navigate to the **Cage section**.
1. Set the **Cage type** to **Distance-based**.
1. Click **Paint cage**.

>[!NOTE]
>
> By default, **Auto-rebake** is turned on for the normal channel when you first enter **Cage painting**. This means that the normal map will automatically be rebaked each time you modify the cage. If you would prefer, you can turn off **Auto-rebake** in the [**Mesh map bakers panel**](../interface/baking-panels/mesh-map-bakers.md).

Once you enter Cage painting mode, the default visualization in the **Viewport** shows:

* The cage around the mesh in transparent beige.
* Areas where the high poly intersects the cage in bright red.
* Cage painted areas in green (positive) and blue (negative) on the low-poly mesh surface.

While in Cage painting mode, you can use the [**Baking visualization menu**](baking-visualization-settings.md) in the **Viewport** to modify the visualization color and opacity for each element, or turn visualization on or off for specific elements.

>[!NOTE]
>
> The bright red visualization of high-poly intersections with the cage is an approximate preview and doesn’t exactly match the final bake results. In most cases, the visualization is quite accurate, but for low-poly meshes with long, thin polygons, it can be inaccurate, and it’s better to use **Quick Bake** or **Auto-Rebake** to check the final result.

## Cage painting tools

When painting the cage, you can use many of the tools and shortcuts you're used to from **Painting mode**, including the **Paintbrush**, **Eraser** and **Polygon fill** tools.

* You can switch between **Paintbrush**, **Eraser**, and **Polygon fill** from the toolbar, or use the standard [keyboard shortcuts](../interface/settings/shortcuts.md) from Painting mode.
* While using the **Paintbrush** or **Eraser** tools, you can adjust the tool's size, flow, opacity, and spacing using the parameters at the top of the **Viewport**. You can also use the relevant [keyboard shortcuts](../interface/settings/shortcuts.md) where available.

### Paintbrush

Using the **Paintbrush** at full **Strength**, **Flow** and **Opacity** will have a huge impact on the cage surface. We recommend setting a very low **Strength** value and using the Flow and Opacity parameters to control the strength of the brush.

TODO: Animation/video showing the difference in strength effect

### Eraser

The Eraser tool allows you to remove paint from the cage, effectively reverting erased areas to the default cage size.

### Polygon fill

In **Cage painting** **mode**, the **Polygon fill tool** has an additional feature, a **Strength slider** appears in the **Viewport** when making changes that you can use to adjust the value for the last set of selected polygons.

This is particularly useful for making per-element adjustments using **Mesh fill mode** in scenes with multiple separate meshes.

>[!NOTE]
>
> This feature works by redoing the last operation (applying the polygon fill) with a different strength value. As a result, performing a different operation or changing tools will cause the slider to disappear.

It can often be useful to apply the same **Polygon fill** value to multiple areas of the mesh. To do this:

1. Select the first set of polygons.
1. Use the **Cage strength** slider to adjust the strength of the effect.
1. Copy the **Cage strength** value from the temporary slider in the **Viewport**.
1. Paste the value into the **Strength** slider at the top of the **Viewport**.
1. Select subsequent sets of polygons to apply the same strength value.

The video below shows this workflow in action, using the **Polygon fill** **tool** with **Mesh fill** selected.

TODO: VIDEO

>[!NOTE]
>
> When following these steps, it may be helpful to select **Normal blend mode** so that the Polygon fill tool overwrites the existing painted values, rather than adding to them.

### Blend modes

By default, both the **Paintbrush** and **Polygon fill** tools default to the **Linear dodge (add) blend mode**, but you can also use the **Normal** and **Lighten (Max) blend modes**.

* **Linear dodge (add)**
  * Each stroke/stamp adds or subtracts the given strength value from the existing value. 
  * This blend mode works similarly to 3D sculpting applications, where each stroke you paint adds to the mesh surface.
* **Normal**
  * Each stroke/stamp sets the value to the specified strength, overwriting the existing value. 
  * This blend mode behaves like the default paintbrush in painting mode, allowing you to cover the existing surface with a different value.
* **Lighten (Max)**: 
  * Each stroke/stamp chooses the maximum value between the strength and the existing value. 
  * With this blend mode, the edges of the brush take longer to build on subsequent strokes, helping to create a more gradual transition.