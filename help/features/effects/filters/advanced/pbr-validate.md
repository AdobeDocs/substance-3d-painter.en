---
title: "PBR Validate"
description: "Learn how to use Substance 3D Painter's PBR Validate filter."
---

# PBR Validate

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![PBR Validate icon](./Resources/icon_pbr_validate.png "PBR Validate")

<b>In:</b> Effects/pbr, metallic, roughness

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The PBR Validate filter validates PBR data by checking albedo dark values and metal reflectance ranges.

It is used on a fill layer to verify that material values stay within expected PBR ranges. PBR Validate should not be enabled when exporting materials.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Validation Mode:</b> | Select whether to validate albedo, metal reflectance, or both. |
| <b>Albedo Dark Range Threshold:</b> | Select the minimum allowed dark-value threshold for albedo validation. |
| <b>Metal Reflectance Range:</b> | Select the reflectance range used to validate metallic values. |
| <b>Overlay Map:</b> | Toggle the validation overlay over the map data. |

