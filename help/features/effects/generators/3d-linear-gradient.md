---
title: 3D Linear Gradient
description: Learn how to use Substance 3D Painter's 3D Linear Gradient generator.
---

# 3D Linear Gradient

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="../../../assets/generators/icon_3d_linear_gradient.webp" alt=""/><br><strong>In:</strong> gradient, grayscale</td>
    <td style="border: 0;" valign="top"><strong>Description</strong><br>The 3D Linear Gradient generator uses the Position map to create a gradient between two points on the mesh. <br><br>3D Linear gradient outputs a monochrome (black and white) texture. As a result, it’s useful for generating masks to place a linear gradient in a specific area.<br><br>A baked position map is required as image input. <a href="../../../baking/baking.md">Learn more about baking here</a>.<br><br>The Position map assigns a color to each point on the mesh that corresponds to its position between 0 and 1 along the X, Y, and Z axes. This means that each point on the mesh has a unique color. You can set start and end points for the linear gradient by selecting the Position map color at the start and end locations.</td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| **Position** | Use the baked Position map. |

## Parameters

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the linear gradient. |
| **Balance** | Shift the linear gradient midpoint position. |
| **Contrast** | Adjust the contrast of the linear gradient. |
| **3D Position Start** | Set the start point of the gradient based on colors from the position map. To easily define the start point, display the position map on screen in the viewport and use the color picker to pick the start point. |
| **3D Position End** | Set the end point of the gradient based on colors from the position map. To easily define the end point, display the position map on screen in the viewport and use the color picker to pick the end point. |
