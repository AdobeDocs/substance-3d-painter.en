---
title: Inflate Shrinkwrap
description: Learn how to use Substance 3D Painter's Inflate Shrinkwrap generator.
---

# Inflate Shrinkwrap

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="../../../assets/generators/icon_inflate_shrinkwrap.webp" alt=""/><br><strong>In:</strong> shrinkwrap, inflate, generator, randomseed</td>
    <td style="border: 0;" valign="top"><strong>Description</strong><br>The Inflate Shrinkwrap generator adds wrinkles that mimic the effect of a thin material being stretched over the surface of your mesh.<br><br>The Inflate Shrinkwrap generator outputs a monochrome (black-and-white) texture. As a result, it’s useful for generating masks that create the shrinkwrap effect. However, it can also be placed directly on a fill layer to add wrinkles to the height and normal channels.<br><br>A baked curvature map is required as image input. <a href="../../../baking/baking.md">Learn more about baking here</a>.</td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| **Curvature** Grayscale | Use the baked Curvature map. |

## Parameters

<table>
  <tr>
    <th>Parameter name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Preset</strong></td>
    <td>Switch between Inflated, Vacuum Pulled and Tight presets.</td>
  </tr>
  <tr>
    <td><strong>Seed</strong></td>
    <td>Set the seed value used to generate the dirt texture. <br><ul><li>Click Random to switch to another random seed.</li><li>Click the pencil to see the current seed value, and enter a specific value if desired.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Inflate or Shrinkwrap</strong></td>
    <td>Switch between the inflate and shrinkwrap mode.</td>
  </tr>
  <tr>
    <td><strong>Seam Intensity</strong></td>
    <td>Adjust how pronounced the edges are.</td>
  </tr>
  <tr>
    <td><strong>Raised Edge Width</strong></td>
    <td>Adjust how much the inflated edges pucker up.</td>
  </tr>
  <tr>
    <td><strong>Raised Edge Intensity</strong></td>
    <td>Adjust the strength of the raised edge effect.</td>
  </tr>
  <tr>
    <td><strong>Wrinkle Density</strong></td>
    <td>Adjust the number of wrinkles.</td>
  </tr>
  <tr>
    <td><strong>Wrinkle Tightness</strong></td>
    <td>Adjust how tightly wrinkles are pulled together on the UV borders.</td>
  </tr>
  <tr>
    <td><strong>Wrinkle Range</strong></td>
    <td>Adjust how far the wrinkles reach from the UV borders.</td>
  </tr>
  <tr>
    <td><strong>Wrinkle Scale</strong></td>
    <td>Adjust the size of the wrinkles.</td>
  </tr>
</table>

### Technical Parameters

| Parameter name | Description |
| --- | --- |
| **Height Range** | Set the height range. |
| **Height Position** | Adjust the height towards black (0) or white (1). |
| **Surface Size (cm)** | Set the physical size of the surface. |
| **Surface Depth (cm)** | Set the physical depth of the surface. |
