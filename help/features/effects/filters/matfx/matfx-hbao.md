---
title: "MatFX HBAO"
description: "Learn how to use Substance 3D Painter's MatFX HBAO filter."
---

# MatFX HBAO

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![MatFX HBAO icon](./Resources/icon_matfx_hbao.png  "MatFX HBAO")

<b>In:</b> Effects/ambient occlusion, height, shading

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The MatFX HBAO filter generates horizon-based ambient occlusion from height information.

It is used on texture layers or masks to add depth and contact shadows based on the source channel or height information.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Blur Intensity:</b> | Adjust the blur intensity of the result. |
| <b>Blur Wrap:</b> | Toggle blur wrapping. When enabled, the effect samples pixels from the opposite side of the texture. |
| <b>Channel Source:</b> | Select the channel source used to generate the occlusion. |
| <b>Use World Units:</b> | Toggle use of world-space units. |
| <b>Height Depth:</b> | Adjust the perceived depth of the height input. |
| <b>Radius:</b> | Adjust the sampling radius of the occlusion effect. |
| <b>Intensity:</b> | Adjust the strength of the occlusion. |
| <b>Relief Balance:</b> | Adjust the balance of the relief contribution. |
