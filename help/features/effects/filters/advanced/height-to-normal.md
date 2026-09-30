---
title: Height To Normal
description: Learn how to use Substance 3D Painter's Height To Normal filter.
---

# Height To Normal

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Height To Normal icon](./Resources/icon_height_to_normal.png "Height To Normal")

<b>In:</b> Effects/

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The Height To Normal filter generates accurate normal data based on the height channel.

It is used on a texture layer to convert height information into normal data.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Overwrite Existing Normal:</b> | Toggle overwriting the existing normal data. |
| <b>Use World Units:</b> | Toggle the use of world units for the conversion. |
| <b>Normal Intensity:</b> | If **Use World Units** is **False**, use this to adjust the intensity of the generated normal data. |
| <b>Surface Size (cm):</b> | If **Use World Units** is **True**, use this to adjust the width or height, whichever is greater, of the represented surface. |
| <b>Height Depth (cm):</b> | If **Use World Units** is **True**, use this to adjust the maximum height range of the surface. |
