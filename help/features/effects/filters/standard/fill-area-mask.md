---
title: "Fill Area Mask"
description: "Learn how to use Substance 3D Painter's Fill Area Mask filter."
---

# Fill Area Mask

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Fill Area Mask icon](./Resources/icon_fill_area_mask.png "Fill Area Mask")

<b>In:</b> Effects/fill, shape, outline, grayscale

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The Fill Area Mask filter converts outlines into filled shapes. Any area with a continuous border is filled.

It is used on a mask (black and white output) layer after adding a paint layer to fill closed painted strokes.

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
| <b>UV Border Detection Threshold:</b> | Adjust the threshold used to ignore UV areas that could otherwise be filled by the area-detection process. |
