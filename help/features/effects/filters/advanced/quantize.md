---
title: "Quantize"
description: "Learn how to use Substance 3D Painter's Quantize filter."
---

# Quantize

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Quantize icon](./Resources/icon_quantize.png "Quantize")

<b>In:</b> Effects/quantize, color

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The Quantize filter reduces an image to a limited set of colors.

It is used on a texture layer to create flatter, posterized, or stylized color regions.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Color Amount:</b> | Adjust the maximum number of colors used in the quantized image. This value also drives the extracted palette, although the actual count may be lower depending on the quantization method. Check the Palette Color Amount output for the final number of extracted colors. |
| <b>Contour Smoothing:</b> | Adjust the smoothing radius applied to the input image to simplify the quantized result into more solid, cohesive shapes. Higher values noticeably increase computation time. |
| <b>Dithering:</b> | Adjust the amount of dithering used to recreate gradients and color blends while still using only the colors left after quantization. Use a Contour Smoothing value of 0 for the expected dithering effect. |
| <b>Dithering Pattern:</b> | Select the dithering pattern used to recreate gradients and color blends in the original image. |
| <b>Distance Color Space:</b> | Select the color space used to compare and distribute colors during quantization. Use Lab (Color) for perceptual color images and RGB (Data) for raw data such as normal maps. |
| <b>Apply To Alpha:</b> | Toggle quantization of the layer's alpha channel. |
| <b>Alpha Threshold:</b> | Adjust the alpha threshold. |

