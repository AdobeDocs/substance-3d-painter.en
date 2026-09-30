---
title: "Blur Slope"
description: "Learn how to use Substance 3D Painter's Blur Slope filter."
---

# Blur Slope

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Blur Slope icon](./Resources/icon_blur_slope.png "Blur Slope")

<b>In:</b> Effects/blur, grayscale

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The Slope Blur filter creates a smearing or fading effect, especially noticeable on high contrast edges between colors.

It is used either directly on a texture layer to blur full materials or specific textures, or on a mask to smear the mask. It can create effects such as chipped or weathered edges, leaking dirt, or smeared rust.

</td>
</tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| <b>Custom Noise:</b> Grayscale | Use a custom texture or an anchor point as custom noise. |

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Seed:</b> | Assign a random value to create a different variation without changing the overall settings. |
| <b>Intensity:</b> | Adjust the blur intensity. |
| <b>Intensity Divider:</b> | Select how the blur intensity is divided. |
| <b>Blending Mode:</b> | Select the blending mode used by the slope blur. |
| <b>Quality:</b> | Adjust the quality of the effect. |

### Source Parameters

<table>
<tr>
<td><b>Source Type:</b></td>
<td>Select whether the source uses the default noise, the previous input, or a custom noise.</td>
</tr>
<tr>
<td><b>Blur:</b></td>
<td>Adjust the blur intensity of the source noise or input.</td>
</tr>
<tr>
<td><b>Position:</b></td>
<td>Adjust the midpoint of the source noise or input, similar to a brightness control.</td>
</tr>
<tr>
<td><b>Contrast:</b></td>
<td>Adjust the contrast of the source noise or input.</td>
</tr>
<tr>
<td><b>Source Tilling:</b></td>
<td>Adjust the tiling of the source noise or input.</td>
</tr>
</table>
