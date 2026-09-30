---
title: Color Match
description: Learn how to use the Color Match Filter in Substance 3D Painter.
---

# Color Match

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="./Resources/icon_color_match.png" alt="Color Match icon" title="Color Match"/><br><strong>In:</strong> Effects/adjustments</td>
    <td style="border: 0;" valign="top">Description<br>The Color Match filter matches a defined source color range to a target color range, with support for input slots to define both source and target values. Color Match allows you to maintain details while changing the color of a surface, with control over how the Hue, Chroma, and Luma are handled.<br>Color Match is used on a fill layer to make fine color adjustments.</td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| **Source Color:** | Input slot for the source color. Use a custom color map or an anchor point. |
| **Target Color:** | Input slot for the target color. Use a custom color map or an anchor point. |

## Parameters

<table>
  <tr>
    <th>Parameter name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Source Color Mode:</strong></td>
    <td>Select the source of the source color.<br><ul><li><strong>Average</strong>: Use the existing material color as the source color. Note, this requires that the layer blend mode be set to <strong>Passthrough</strong>.</li><li><strong>Parameter</strong>: Set the source color using a parameter.</li><li><strong>Input</strong>: Set the source color with an image input.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Source Color:</strong></td>
    <td>Adjust the source color when <strong>Source Color Mode</strong> is set to <strong>Parameter</strong>.</td>
  </tr>
  <tr>
    <td><strong>Target Color Mode:</strong></td>
    <td>Select the source of the target color.<br><ul><li><strong>Parameter</strong>: Set the target color using a parameter.</li><li><strong>Input</strong>: Set the target color with an image input.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Target Color:</strong></td>
    <td>Adjust the target color when <strong>Target Color Mode</strong> is set to <strong>Parameter</strong>.</td>
  </tr>
  <tr>
    <td><strong>Custom Color Variation:</strong></td>
    <td>Toggle custom hue, chroma, and luma variation controls.</td>
  </tr>
  <tr>
    <td><strong>Hue:</strong></td>
    <td>Adjust the hue variation applied to the result.</td>
  </tr>
  <tr>
    <td><strong>Chroma:</strong></td>
    <td>Adjust the chroma variation applied to the result.</td>
  </tr>
  <tr>
    <td><strong>Luma:</strong></td>
    <td>Adjust the luma variation applied to the result.</td>
  </tr>
</table>