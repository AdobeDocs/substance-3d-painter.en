---
title: Blur Slope
description: Learn how to use the Blur Slop filter with Substance 3D Painter
---

# Blur Slope

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="./Resources/icon_blur_slope.png" alt="Blur Slope icon" title="Blur Slope"/><br><strong>In:</strong> Effects/blur, grayscale</td>
    <td style="border: 0;" valign="top">Description<br>The Slope Blur filter creates a smearing or fading effect, especially noticeable on high contrast edges between colors.<br>It is used either directly on a texture layer to blur full materials or specific textures, or on a mask to smear the mask. It can create effects such as chipped or weathered edges, leaking dirt, or smeared rust.</td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| **Custom Noise:** Grayscale | Use a custom texture or an anchor point as custom noise. |

## Parameters

| Parameter name | Description |
| --- | --- |
| **Seed:** | Assign a random value to create a different variation without changing the overall settings. |
| **Intensity:** | Adjust the blur intensity. |
| **Intensity Divider:** | Select how the blur intensity is divided. |
| **Blending Mode:** | Select the blending mode used by the slope blur. |
| **Quality:** | Adjust the quality of the effect. |

### Source Parameters

| Parameter name | Description |
| --- | --- |
| **Source Type:** | Select whether the source uses the default noise, the previous input, or a custom noise. |
| **Blur:** | Adjust the blur intensity of the source noise or input. |
| **Position:** | Adjust the midpoint of the source noise or input, similar to a brightness control. |
| **Contrast:** | Adjust the contrast of the source noise or input. |
| **Source Tilling:** | Adjust the tiling of the source noise or input. |
