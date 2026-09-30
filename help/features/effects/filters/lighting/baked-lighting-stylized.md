---
title: "Baked Lighting Stylized"
description: "Learn how to use Substance 3D Painter's Baked Lighting Stylized filter."
---

# Baked Lighting Stylized

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Baked Lighting Stylized icon](./Resources/icon_baked_lighting_stylized.png "Baked Lighting Stylized")

<b>In:</b> Effects/stylized, light, color

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The Baked Lighting Stylized filter bakes material and lighting information into the color channel.

It is used on a paint layer set to passthrough mode and applied to all channels. It is useful for stylized workflows where accurate simulated lighting is not required, or when resources are limited, such as on mobile projects or assets that rely on a color map only.

</td>
</tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| <b>Ambient Occlusion:</b> Grayscale | Use the baked Ambient Occlusion map. |
| <b>Curvature:</b> Grayscale | Use the baked Curvature map. |
| <b>Normal:</b> Color | Use the baked Normal map. |
| <b>World Space Normals:</b> Color | Use the baked World Space Normals map. |

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Input:</b> | Select the input material workflow. |
| <b>Output:</b> | Select the output mode. |
| <b>Dielectric Reflectance:</b> | Adjust the dielectric reflectance. |
| <b>Diffuse AO:</b> | Adjust the ambient occlusion contribution to the diffuse lighting. |
| <b>Diffuse Cavity:</b> | Adjust the cavity contribution to the diffuse lighting. |
| <b>Specular AO:</b> | Adjust the ambient occlusion contribution to the specular lighting. |
| <b>Specular Cavity:</b> | Adjust the cavity contribution to the specular lighting. |
| <b>Cavity Smoothness:</b> | Adjust the smoothness of the cavity effect. |
| <b>Edges Intensity:</b> | Adjust the intensity of the edge effect. |
| <b>Edges Smoothness:</b> | Adjust the smoothness of the edge effect. |
| <b>Normal Details Type:</b> | Select which normal details are used. |
| <b>Height to Normal Intensity:</b> | Adjust the intensity of the height-to-normal conversion. |
| <b>Sun Intensity:</b> | Adjust the intensity of the sun light. |
| <b>Sun Horizontal Angle:</b> | Adjust the horizontal angle of the sun light. |
| <b>Sun Vertical Angle:</b> | Adjust the vertical angle of the sun light. |
| <b>Sun Color:</b> | Adjust the color of the sun light. |
| <b>Sky Intensity:</b> | Adjust the intensity of the sky light. |
| <b>Sky Color:</b> | Adjust the color of the sky light. |
| <b>Horizon Color:</b> | Adjust the color of the horizon light. |
| <b>Ground Color:</b> | Adjust the color of the ground light. |
| <b>Horizontal Angle:</b> | Adjust the intensity of the additional light. |
| <b>Vertical Angle:</b> | Adjust the vertical angle of the additional light. |
| <b>Intensity:</b> | Adjust the intensity of the additional light. |
| <b>Color:</b> | Adjust the color of the additional light. |
| <b>Horizontal Angle:</b> | Adjust the horizontal angle of the second additional light. |
| <b>Vertical Angle:</b> | Adjust the vertical angle of the second additional light. |
| <b>Intensity:</b> | Adjust the intensity of the second additional light. |
| <b>Color:</b> | Adjust the color of the second additional light. |

### Material

| Parameter name | Description |
| --- | --- |
| **Dielectric Reflectance:** | Set the dielectric reflectance amount. |
| **Diffuse AO:** | Control how much ambient occlusion affects the diffuse details. |
| **Diffuse Cavity:** | Control how much cavity areas influence the diffuse details. |
| **Specular AO:** | Control how much ambient occlusion affects the specular details. |
| **Specular Cavity:** | Adjust how much cavity areas influence the specular details. |
| **Cavity Smoothness:** | Adjust how smooth the cavity areas appear. |
| **Edges Intensity:** | Set the strength of the edge details. |
| **Edges Smoothness:** | Adjust the smoothness of the edge areas. |
| **Normal Details Type:** | Select which details are used for the normals: Mesh only, or Mesh + Height + Normal. |
| **Height to Normal Intensity:** | Adjust the strength of the generated normal details. |

### Sun & Sky

| Parameter name | Description |
| --- | --- |
| **Sun Intensity:** | Control the strength of the sun. |
| **Sun Horizontal Angle:** | Adjust the horizontal angle of the sun. |
| **Sun Vertical Angle:** | Adjust the vertical angle of the sun. |
| **Sun Color:** | Control the color of the sun. |
| **Sky Intensity:** | Adjust the strength of the sky. |
| **Sky Color:** | Set the color of the sky. |
| **Horizon Color:** | Adjust the color of the horizon. |
| **Ground Color:** | Set the color of the ground. |

### Light 1

| Parameter name | Description |
| --- | --- |
| **Horizontal Angle:** | Adjust the horizontal angle of the additional light. |
| **Vertical Angle:** | Adjust the vertical angle of the additional light. |
| **Intensity:** | Adjust the strength of the additional light. |
| **Color:** | Set the color of the additional light. |

### Light 2

| Parameter name | Description |
| --- | --- |
| **Horizontal Angle:** | Adjust the horizontal angle of the second additional light. |
| **Vertical Angle:** | Adjust the vertical angle of the second additional light. |
| **Intensity:** | Adjust the strength of the second additional light. |
| **Color:** | Set the color of the second additional light. |
