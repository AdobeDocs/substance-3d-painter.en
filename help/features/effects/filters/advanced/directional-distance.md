---
title: Directional Distance
description: Learn how to use the Directional Distance filter in Substance 3D Painter.
---

# Directional Distance

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="./Resources/icon_directional_distance.png" alt="Directional Distance icon" title="Directional Distance"/><br><strong>In:</strong> Effects/color, distance, directional, leak, rain</td>
    <td style="border: 0;" valign="top">Description<br>The Directional Distance filter creates a distance gradient that travels in a chosen direction.<br>It is used on a texture layer to create directional streaks, leaks, and other distance-based effects. You can also use the Directional Distance filter as a mask for the height channel to add dimensionality to your normal channel.</td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| **Distance Map:** Grayscale | Use a custom texture or an anchor point. |

## Parameters

| Parameter name | Description |
| --- | --- |
| **Distance:** | Adjust the distance travelled by the distance gradient in normalized image space, where 1 is the length of the shorter side of the input image. |
| **Angle:** | Adjust the direction of the distance gradient in turns, where 0 points horizontally to the right, or along a (1,0) vector. |
| **Contrast:** | Adjust the contrast or falloff of the result. |
| **Distance Map Multiplier:** | Adjust how much the Distance Map affects the maximum distance. This parameter has no effect when the Distance Map input is not connected. |

## Examples

In the example below, we use the Directional Distance filter to make the Cells 2 generator appear 3 dimensional.

![](../../../../assets/filters/directional-distance/3d.png)

This is achieved by creating a fill layer with the height channel enabled and set to a value of 1.

Then add a black mask to the fill layer, and in the mask add a fill with the grayscale set to **Cells 2**. This creates the following mask.

>[!NOTE]
>
> You can view the mask in the **Viewport** by holding alt and clicking the mask icon, or with the fill layer selected, use the channel dropdown in the **Viewport** to select **Mask**.

![](../../../../assets/filters/directional-distance/cells2.png)

Next, add a Filter to the mask, and select the Directional Distance filter.

Adjust the Filter settings for the desired result, but the mask should look something like the example below.

![](../../../../assets/filters/directional-distance/result.png)

Switch back to material view to see the effect in the Viewport.
