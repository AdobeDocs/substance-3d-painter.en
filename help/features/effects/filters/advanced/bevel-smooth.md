---
title: Bevel Smooth
description: Learn how to use Substance 3D Painter's Bevel Smooth filter.
---

# Bevel Smooth

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Bevel Smooth icon](./Resources/icon_bevel_smooth.png "Bevel Smooth")

<b>In:</b> Effects/bevel, smooth, distance, grayscale

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The Bevel Smooth filter draws a gradient from the borders of a mask outward, inward or both.

It is used on a texture layer or inside a mask (black and white output) to create a smooth beveled gradient from the edges of a mask.

</td>
</tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| <b>Distance Map:</b> Grayscale | Use a custom texture or an anchor point. |

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Direction:</b> | Select the side of the mask border which should be dilated. |
| <b>Distance:</b> | Adjust the distance of bevel dilation. |
| <b>Smoothing:</b> | Adjust the intensity of the smoothing applied to the mask. |
| <b>Curve Offset:</b> | Adjust the mask borders inward or outward. |
| <b>Curve Shape:</b> | Select whether the bevel slope uses a pinched or rounded curve. |
| <b>Mask Threshold:</b> | Adjust the value used to detect the borders of the mask from the Input. |
| <b>Distance Map Multiplier:</b> | Adjust the impact of the Distance Map over the Maximum Distance. |
| <b>Bevel Wrap:</b> | Toggle whether the bevel tiles horizontally and vertically. |
