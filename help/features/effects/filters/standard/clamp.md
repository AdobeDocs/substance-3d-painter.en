---
title: Clamp
description: Learn how to use Substance 3D Painter's Clamp filter.
---

# Clamp

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Clamp icon](./Resources/icon_clamp.png "Clamp")

<b>In:</b> Effects/adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The Clamp filter clamps values to defined limits.

It is used either directly on a fill layer to limit specific aspects of a material, or on a mask to constrain values to a given range.

</td>
</tr>
</table>

>[!NOTE]
>
> When used on a fill layer or as a passthrough for color information, the clamp affects each color channel individually. So, if a given pixel has a color of (R 0, G 0.5, B 1.0), and is clamped to 0.5, the resulting color of that pixel will be (R 0, G 0.5, B 0.5). This is because the Blue channel had a high enough value to be clamped, but the other channels didn't. This means that the Clamp filter can change the hue of colored content.
>
>If you do not want to modify hue, other filters such as Levels, may be a better choice.

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Min:</b> | Adjust the minimum value. |
| <b>Max:</b> | Adjust the maximum value. |
