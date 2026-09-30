---
title: MatFX Detail Edge Wear
description: Learn how to use the MatFX Detail Edge Wear filter in Substance 3D Painter.
---

# MatFX Detail Edge Wear

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="./Resources/icon_matfx_detail_edge_wear.png" alt="MatFX Detail Edge Wear icon" title="MatFX Detail Edge Wear"/><br><strong>In:</strong> Effects/wear, edge, material</td>
    <td style="border: 0;" valign="top">Description<br>The MatFX Detail Edge Wear filter creates worn edge details that can be blended into a material.<br>It is used on a texture layer or material stack to add edge wear, grunge breakup, and supporting material adjustments driven by masks and curvature data.</td>
  </tr>
</table>

>[!NOTE]
>
> For the MatFX Detail Edge Wear filter to have a visible effect, there needs to be existing varied normal information in the layer stack below the filter. If there is no data or no variety in the normal channel, the filter will not be able to find edges to damage and will have no visible effect.

## Parameters

| Parameter name | Description |
| --- | --- |
| **Blur Intensity:** | Adjust the strength of the blur effect. |
| **Blur Wrap:** | Toggle blur wrapping. When enabled, the effect samples pixels from the opposite side of the texture. |
| **Input Mode:** | Select the input mode used to drive the wear effect. |
| **Wear Level:** | Adjust the overall wear level. |
| **Wear Contrast:** | Adjust the contrast of the wear mask. |
| **Edges Smoothness:** | Adjust the smoothness of the worn edges. |
| **Grunge Amount:** | Adjust the amount of grunge added to the wear. |
| **Grunge Scale:** | Adjust the scale of the grunge pattern. |

### Material

**PBR Metallic Roughness**

|  |  |
| --- | --- |
| **Base Color:** | Adjust the base color contribution. |
| **Metallic:** | Adjust the metallic value. |
| **Roughness:** | Adjust the roughness value. |

**PBR Specular Glossiness**

|  |  |
| --- | --- |
| **Diffuse:** | Adjust the diffuse contribution. |
| **Specular Color:** | Adjust the specular color. |
| **Glossiness:** | Adjust the glossiness value. |

### Settings

|  |  |
| --- | --- |
| **Generator Mask Control:** | Adjust the generator mask influence. |
| **Generator Mask Contrast:** | Adjust the contrast of the generator mask. |
| **Generator Mask Blur:** | Adjust the blur applied to the generator mask. |
| **Alpha Background Value:** | Adjust the background alpha value. |
| **Curvature Intensity:** | Adjust the intensity of the curvature input. |
| **Invert Curvature:** | Toggle inversion of the curvature input. |
| **Combine Curvature:** | Toggle combining the inverted and non-inverted curvature data. |
| **Normal Intensity:** | Adjust the normal intensity. |
| **AO Spreading:** | Adjust the spread of the ambient occlusion effect. |
