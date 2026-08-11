---
title: Grayscale Conversion
description: Learn how to use Substance 3D Painter's Grayscale Conversion generator.
---

# Grayscale Conversion

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="../../../assets/generators/icon_grayscale_conversion.png" alt=""/><br><strong>In:</strong> generator, grayscale, color</td>
    <td style="border: 0;" valign="top"><strong>Description</strong><br>The Grayscale Conversion generator converts a texture or map into grayscale values.<br><br>The Grayscale Conversion generator outputs a monochrome (black-and-white) texture. As a result, it’s useful for generating masks from a full color input map.</td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| **Source** Color | Use a custom color texture or an anchor point. |

## Parameters

<table>
  <tr>
    <th>Parameter name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Grayscale type</strong></td>
    <td>Set the grayscale conversion method: <br><ul><li><strong>Desaturation</strong>: Uses the value halfway between the strongest and weakest of the RGB channels.</li><li><strong>Luma</strong>: Uses weighted RGB coefficients matching perceived brightness by the human eye (favoring green).</li><li><strong>Average</strong>: Mixes the red, green, and blue channels in equal amounts.</li><li><strong>Max</strong>: Uses the highest value from the RGB channels.</li><li><strong>Min</strong>: Uses the lowest value from the RGB channels.<ul><li>Red channel: Uses only the red channel.</li><li>Green channel: Uses only the green channel.</li><li>Blue channel: Uses only the blue channel.</li></ul></li></ul></td>
  </tr>
  <tr>
    <td><strong>Invert</strong></td>
    <td>Inverts the mask.</td>
  </tr>
  <tr>
    <td><strong>Balance</strong></td>
    <td>Adjusts the balance of the converted source image, shifting midpoint toward black or white like a brightness control.</td>
  </tr>
  <tr>
    <td><strong>Contrast</strong></td>
    <td>Defines the contrast/falloff of the converted source image.</td>
  </tr>
  <tr>
    <td><strong>Tile</strong></td>
    <td>Sets the tiling of the converted source image.</td>
  </tr>
  <tr>
    <td><strong>Rotation</strong></td>
    <td>Tweaks the angle of the converted source image.</td>
  </tr>
  <tr>
    <td><strong>Safe Rotation</strong></td>
    <td>Toggles Safe rotation mode on or off. When true, Safe rotation locks rotation to 45 degree angles.</td>
  </tr>
</table>
