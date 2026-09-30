---
title: "Fill Area Color"
description: "Learn how to use Substance 3D Painter's Fill Area Color filter."
---

# Fill Area Color

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Fill Area Color icon](./Resources/icon_fill_area_color.png "Fill Area Color")

<b>In:</b> Effects/fill, shape, outline, rgba, color

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The Fill Area Color filter converts outlines into filled shapes. Any area with a continuous border is filled. The color version uses alpha to determine area borders.

It is used on a paint layer (color channel) to fill closed painted strokes.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Area Detection:</b> | Select how the area to fill is identified. |
| <b>Area Detection Threshold:</b> | Adjust the area-detection threshold. |
| <b>Debug Area Detection:</b> | Toggle display of the outline detected by the Area Detection setting. This can help identify areas that may not be fully closed. |
| <b>UV Border Behavior:</b> | Select how UV borders are handled during area filling. |
| <b>UV Border Threshold:</b> | Adjust the threshold used to ignore UV areas that could otherwise be filled by the area-detection process. |
| <b>Color Mode:</b> | Select which method is used to fill the inside of the area. |
| <b>Fill Color:</b> | Adjust the fill color. |
| <b>Blur Intensity:</b> | Adjust the blur intensity. |
| <b>Blur Samples:</b> | Adjust the number of blur samples. |
| <b>Diffusion Iterations:</b> | Adjust the number of diffusion iterations to perform. Higher values improve the result but are slower. Useful values are in the [8, 48] range. |
