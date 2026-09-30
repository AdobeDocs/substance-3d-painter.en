---
title: MatFX Edge Damages
description: Learn how to use Substance 3D Painter's MatFX Edge Damages filter.
---

# MatFX Edge Damages

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![MatFX Edge Damages icon](./Resources/icon_matfx_edge_damages.png  "MatFX Edge Damages")

<b>In:</b> Effects/blur, grayscale

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The MatFX Edge Damages filter creates chipped and damaged edge details. Edge Damage behaves differently to the MatFX Detail Edge Wear filter in that Edge damage doesn't change the color of the damaged area. This means that it can be more useful for simulating damage to materials like plastic or resin, rather than Edge Wear which is better used for materials like painted metal.

MatFX Edge Damages is used on texture layers or material stacks to add worn, scratched, and damaged edge details.

</td>
</tr>
</table>

>[!NOTE]
>
> In order for the MatFX Edge Damages filter to modify the height channel, there needs to be existing height data in the channel. In other words, if there are no layers below the filter layer that have height data, the filter won't have an observable effect on the height channel.

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Blur Intensity:</b> | Adjust the strength of the blur effect. |
| <b>Blur Wrap:</b> | Toggle blur wrapping. When enabled, the effect samples pixels from the opposite side of the texture. |
| <b>Level:</b> | Adjust the overall damage level. |
| <b>Contrast:</b> | Adjust the contrast or falloff of the result. |
| <b>Scratches Intensity:</b> | Adjust the intensity of the scratches. |
| <b>Damages Roughness:</b> | Adjust the roughness of the damaged areas. |
| <b>Damages Depth:</b> | Adjust the depth of the damaged areas. |
