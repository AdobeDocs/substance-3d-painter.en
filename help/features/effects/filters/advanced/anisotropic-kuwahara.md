---
title: "Anisotropic Kuwahara"
description: "Learn how to use Substance 3D Painter's Anisotropic Kuwahara filter."
---

# Anisotropic Kuwahara

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Anisotropic Kuwahara icon](./Resources/icon_anisotropic_kuwahara.png "Anisotropic Kuwahara")

<b>In:</b> Effects/grayscale, kuwahara, anisotropic, stylized

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The Anisotropic Kuwahara filter creates painterly stylization effects while preserving strong directional features.

It is used on a texture layer or inside a mask (black and white output) to create a stylized look for full materials, noises, and masks.

</td>
</tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| <b>Radius Map:</b> Grayscale | Use a custom texture or an anchor point. |
| <b>Custom Input:</b> Color | Use a custom texture or an anchor point. |

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Extract Direction:</b> | Select how the filter derives the blur direction. |
| <b>Radius:</b> | Adjust the blur radius. Higher values produce a stronger blur effect. The maximum value is 32. |
| <b>Smoothness:</b> | Adjust how much colors blend along the computed direction. At 0, colors are mostly displaced in that direction with very little blending. |
| <b>Sharpness:</b> | Adjust the contrast in blurred areas to make them appear flatter and more clearly defined. |
| <b>Tensor Smoothness:</b> | Adjust the amount of blur applied to the directions computed from the image and stored in the direction map. Higher values produce a smoother result when the image contains a lot of high-frequency detail. |
| <b>Anisotropy:</b> | Adjust how strongly the direction map influences the blur. The direction map and its modifiers still affect the result even when this value is 0, because the map is used in the Kuwahara filter kernel. |
| <b>Anisotropy Angle:</b> | Adjust the rotation applied to the direction map in turns. This rotation is added to the value from the Anisotropy Angle Map input. |

