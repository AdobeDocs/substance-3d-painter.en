---
title: Light
description: Learn how to use Substance 3D Painter's Light generator.
---

# Light

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="../../../assets/generators/icon_light.webp" alt=""/><br><strong>In:</strong> mask, generator</td>
    <td style="border: 0;" valign="top"><strong>Description</strong><br>The Light generator fakes a directional light shining on your mesh, based on the World Space Normal and Position maps.<br><br>The Light generator can be used on a fill layer or as to create a mask. When used in a fill layer, the generator outputs color, metalness, specular roughness, normal, and height channels which can be used in various combinations to create different effects. We recommend cycling through the channel views in the Viewport to understand how each channel is impacted by the light generator.<br><br>Baked position and world space normal maps are required as image inputs. <a href="../../../baking/baking.md">Learn more about baking here</a>.</td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| **World Space Normal** Color | Use the baked World Space Normals map. |
| **Position** Color | Use the baked Position map. |

## Parameters

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the output color map. |
| **Horizontal Angle** | Set the horizontal angle of the fake light. |
| **Vertical Angle** | Set the vertical angle of the fake light. |
| **Highlight Glossiness** | Adjust the falloff spread of the highlighted area. |
| **Highlight Level** | Adjust the contrast of the highlight. |
| **Light Attenuation** | Adjust the light falloff. |
