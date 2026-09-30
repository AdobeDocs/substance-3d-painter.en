---
title: MatFX Peeling Paint
description: Learn how to use Substance 3D Painter's MatFX Peeling Paint filter.
---

# MatFX Peeling Paint

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![MatFX Peeling Paint icon](./Resources/icon_matfx_peeling_paint.png  "MatFX Peeling Paint")

<b>In:</b> Effects/blur, grayscale

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The MatFX Peeling Paint filter creates flaking and peeling paint effects.

It is used on texture layers or material stacks to simulate peeling paint, chipped coatings, and expose underlying material.

</td>
</tr>
</table>

>[!NOTE]
>
> In order to expose an underlying material, use the MatFX Peeling Paint inside a group. Layers outside the group and below it in the layer stack will be exposed where the peeled paint pulls away from the surface.

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Blur Intensity:</b> | Adjust the strength of the blur effect. |
| <b>Blur Wrap:</b> | Toggle blur wrapping. When enabled, the effect samples pixels from the opposite side of the texture. |
| <b>Peeling Level:</b> | Adjust the overall peeling level. |
| <b>Peeling Distance:</b> | Adjust how far the paint appears to peel away. |
| <b>Flake Level:</b> | Adjust the amount of flaking. |
| <b>Air Bubble Density:</b> | Adjust the density of the air bubbles. |
| <b>Flaking Density:</b> | Adjust the density of the flaking. |
| <b>Flaking X Amount:</b> | Adjust the amount of flaking along the X axis. |
| <b>Flaking Y Amount:</b> | Adjust the amount of flaking along the Y axis. |
| <b>Use Curvature:</b> | Toggle use of the curvature input. |
| <b>Curvature Distance:</b> | Adjust the curvature sampling distance. |
| <b>Curvature Contrast:</b> | Adjust the contrast of the curvature input. |

### Technical parameters

These parameters allow you to modify the top surface of the peeled material.

| Parameter name | Description |
| --- | --- |
| <b>Luminosity:</b> | Adjust the luminosity. |
| <b>Contrast:</b> | Adjust the contrast or falloff of the result. |
| <b>Hue Shift:</b> | Adjust the hue shift. |
| <b>Saturation:</b> | Adjust the saturation. |
| <b>Normal Intensity:</b> | Adjust the normal intensity. |
| <b>Height Range:</b> | Adjust the height range used by the effect. |
| <b>Height Position:</b> | Adjust the height position used by the effect. |
| <b>Ambient Occlusion Intensity:</b> | Adjust the intensity of the ambient occlusion. |
