---
title: Warp
description: Learn how to use Substance 3D Painter's Warp filter.
---

# Warp

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Warp icon](./Resources/icon_warp.png "Warp")

<b>In:</b> Effects/grayscale

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The Warp filter is used for various deformation effects. The Warp filter provides access to the regular warping, a directional warp which warps in a specific direction, and multidirectional warp for more variation.

Warp is used on a texture layer or inside a mask (black and white output) to deform materials, shapes, masks, outlines etc.

</td>
</tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| <b>Custom Noise</b> | Use a custom texture as noise input map. |

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Seed:</b> | Assign a random value to create a different variation without changing the overall settings. |
| <b>Warp Mode:</b> | Select the warp mode. |
| <b>Intensity:</b> | Adjust the warp intensity. |
| <b>Intensity Divider:</b> | Select how the warp intensity is divided. |
| <b>Angle:</b> | Adjust the warp angle. |
| <b>Blending Mode:</b> | Select the blending mode used by the warp. |
| <b>Directions:</b> | Select the number of warp directions. |

### Source Parameters

<table>
<tr>
<td><b>Source Mode:</b></td>
<td>Determines the source mode.<br><br> - Default Noise: Uses the default noise for the warp effect.<br> - Previous Input: Uses the previous input for the warp effect. When a fill layer has a specific noise pattern applied, using a warp effect in "Previous Input" mode will cause the effect to use that same noise pattern as the fill layer.<br> - Custom Noise: Uses the custom noise input for the warp effect.</td>
</tr>
<tr>
<td><b>Source Blur:</b></td>
<td>Blurs the source noise.</td>
</tr>
<tr>
<td><b>Source Balance:</b></td>
<td>Adjusts the balance of the source noise, shifting midpoint toward black or white like a brightness control.</td>
</tr>
<tr>
<td><b>Source Contrast:</b></td>
<td>Tweaks the contrast of the source noise.</td>
</tr>
<tr>
<td><b>Source Tilling:</b></td>
<td>Controls the tiling of the source noise.</td>
</tr>
</table>
