---
title: UV Random Color
description: Learn how to use Substance 3D Painter's UV Random Color generator.
---

# UV Random Color

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="../../../assets/generators/icon_uv_random_color.png" alt=""/><br><strong>In:</strong> utility, mask</td>
    <td style="border: 0;" valign="top"><strong>Description</strong><br>The UV Random Color generator assigns solid unique colors to each UV island. This is often useful as a diagnostic tool with complex meshes.<br><br>UV Random color can be used either to create a mask (black and white output) or directly as a fill layer for applying color variation to your mesh based on UV islands, for example to randomize each plank of a wooden floor.</td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| **Custom Gradient** | Use a Gradient map to define the color range. |

## Parameters

<table>
  <tr>
    <th>Parameter name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Seed</strong></td>
    <td>Set the seed value used to generate the dirt texture. <br><ul><li>Click Random to switch to another random seed.</li><li>Click the pencil to see the current seed value, and enter a specific value if desired.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Color Source Mode</strong></td>
    <td>Determines the used Color Source Mode. <br><ul><li><strong>Random</strong>: In Random mode the colors are defined and assigned randomly.</li><li><strong>Custom Gradient</strong>: In Custom Gradient mode, you have an additional input to add a custom gradient map where the colors are picked from.</li></ul></td>
  </tr>
</table>
