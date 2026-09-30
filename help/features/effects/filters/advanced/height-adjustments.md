---
title: Height Adjust
description: Learn how to use Substance 3D Painter's Height Adjust filter.
---

# Height Adjust

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Height Adjust icon](./Resources/icon_height_adjust.png "Height Adjust")

<b>In:</b> Effects/adjustments, scale, offset, invert

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The Height Adjust filter inverts, offsets, or multiplies the height channel by a chosen value.

It is used on a texture layer or inside a mask (black and white output) to adjust height information non-destructively.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Invert:</b> | Toggle inversion of the result. |
| <b>Offset:</b> | Adjust the height value by adding or subtracting the specified amount. |
| <b>Multiply:</b> | Multiply the height values by this value. As a multiplier, this makes higher areas higher, and lower areas lower. |

>[!NOTE]
>
> The **Multiply** and **Offset** parameters stack with Offset being applied first. If the offset results in a height value of zero at a given point, the multiplication will multiply by zero, meaning it will cause no change at that point. To multiply and then offset the multiplied values, you can add a second Height Adjust filter.
