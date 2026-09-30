---
title: "Baked Lighting Environment"
description: "Learn how to use Substance 3D Painter's Baked Lighting Environment filter."
---

# Baked Lighting Environment

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Baked Lighting Environment icon](./Resources/icon_baked_lighting_environment.png "Baked Lighting Environment")

<b>In:</b> Effects/lighting, bake, environment, PBR

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The Baked Lighting Environment filter bakes material and environment lighting information into the color channel.

It is used on a paint layer set to passthrough mode and applied to all channels. It is useful for stylized workflows where accurate simulated lighting is not required, or when resources are limited, such as on mobile projects or assets that rely on a color map only.

</td>
</tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| <b>Ambient Occlusion:</b> Grayscale | Use the baked Ambient Occlusion map. |
| <b>Environment Map:</b> Grayscale | Use the environment map. |
| <b>Normal:</b> Color | Use the baked Normal map. |

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Horizontal Rotation:</b> | Adjust the horizontal rotation of the environment lighting. |
| <b>Vertical Rotation:</b> | Adjust the vertical rotation of the environment lighting. |
| <b>Exposure:</b> | Adjust the exposure of the baked result. |
| <b>Height Intensity:</b> | Adjust how strongly height information affects the result. |
| <b>Ambient Occlusion Intensity:</b> | Adjust the intensity of ambient occlusion in the bake. |
| <b>Specular Occlusion Intensity:</b> | Adjust the intensity of specular occlusion in the bake. |
