---
title: 3D Distance
description: Learn how to use Substance 3D Painter's 3D Distance generator.
---

# 3D Distance

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="../../../assets/generators/icon_3d_distance.webp" alt=""/><br><strong>In:</strong> mask, generator</td>
    <td style="border: 0;" valign="top"><strong>Description</strong><br>The 3D Distance generator defines a point in 3D space (source point) and displays the distance from that point with a monochrome gradient. Areas on the mesh surface closer to the point are darker, and areas farther away are lighter (by default).<br><br>A baked position map is required as image input. <a href="../../../baking/baking.md">Learn more about baking here</a>.<br><br>3D Distance outputs a monochrome (black and white) texture. As a result, it’s useful for generating masks that create a gradient away from a given position.<br><br></td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| **Position** | Uses the baked Position map to calculate the distance. |

## Parameters

| Parameter name | Description |
| --- | --- |
| **Invert** | Inverts the gradient. |
| **Position X** | Transform the source point along the x axis. |
| **Position Y** | Transform the source point along the y axis. |
| **Position Z** | Transform the source point along the z axis. |
| **Radius** | Adjusts the size of the distance falloff. |
| **Offset** | Shift the start and end positions of the gradient towards or away from the source point. Shifting away from the source point (increasing the offset) will result in a larger dark area near the source point. Shifting closer to the source point will lighten the gradient, potentially removing it altogether if Offset is set to 0. |
| **Contrast** | Adjusts the contrast of the spherical gradient. |
