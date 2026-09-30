--- 
title: "Stylization"
description: "Learn how to use Substance 3D Painter's Stylization filter."
---

# Stylization

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Stylization icon](./Resources/icon_stylization.png "Stylization")

<b>In:</b> Effects/stylized, stylisation, realistic, hand, painted, brush

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The Stylization filter gives a material a hand-painted, stylized appearance.

It is used on a texture layer to add painterly brush strokes, smoothness variation, color remapping, and baked-lighting effects.

</td>
</tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| <b>Ambient Occlusion Base:</b> Color |  |
| <b>Curvature:</b> Color |  |
| <b>Normal Base:</b> Color |  |

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Stylization:</b> | Adjust the global intensity of the filter. |
| <b>Brush Strokes:</b> | Adjust the overall intensity of the brush stroke effect. |
| <b>Smoothness:</b> | Adjust the overall intensity of the smoothness effect. |
| <b>Colorize:</b> | Adjust the overall intensity of the colorize effect. |
| <b>Gradient:</b> | Adjust the overall intensity of the gradient effect. |
| <b>Baked Lighthing:</b> | Adjust the overall intensity of the baked lighting effect. |
| <b>Edges and Cavities:</b> | Adjust the overall intensity of the edges and cavities effect. |

### Brush Strokes

| Parameter name | Description |
| --- | --- |
| <b>Strokes Amount:</b> | Adjust the amount of brush strokes used by the filter. |
| <b>Strokes Mode:</b> | Select the type of brush strokes used by the filter. |
| <b>Strokes Select:</b> | Select the brush stroke shapes to project when using multiple strokes. |
| <b>Strokes Select:</b> | Select the brush stroke shape to project when using a single stroke. |
| <b>Strokes Scale:</b> | Adjust the scale of the brush strokes. |
| <b>Non-Uniform Size:</b> | Toggle non-uniform scaling for the projected brush strokes. |
| <b>Strokes Size:</b> | Adjust the aspect ratio of the projected brush strokes. |
| <b>Strokes Scale Random:</b> | Adjust the amount of random scale variation applied to the brush strokes. |
| <b>Strokes Follow Surface:</b> | Toggle alignment of the brush strokes to the mesh orientation. |
| <b>Strokes Rotation:</b> | Adjust the brush stroke rotation angle. |
| <b>Strokes Rotation Random:</b> | Adjust the amount of random rotation applied to the brush strokes. |
| <b>Projection Hardness:</b> | Adjust the hardness of the stamp projection. |
| <b>Normal Threshold:</b> | Adjust the normal threshold used for stroke projection. |

### Brush Strokes Effects

| Parameter name | Description |
| --- | --- |
| <b>Color Custom:</b> | Toggle use of a custom color on the brush strokes. |
| <b>Color Variation:</b> | Adjust how much the brush strokes blend with the base color. |
| <b>Color Opacity:</b> | Adjust the opacity of the custom color applied to the brush strokes. |
| <b>Color:</b> | Adjust the custom color applied to the brush strokes. |
| <b>Color Random:</b> | Adjust the amount of random color variation applied to the brush strokes. |
| <b>Roughness Custom:</b> | Toggle use of a custom roughness value on the brush strokes. |
| <b>Roughness Variation:</b> | Adjust roughness variation across the brush strokes. |
| <b>Roughness:</b> | Adjust the roughness value of the brush strokes. |
| <b>Metallic Custom:</b> | Toggle use of a custom metallic value on the brush strokes. |
| <b>Metallic Variation:</b> | Adjust metallic variation across the brush strokes. |
| <b>Metallic:</b> | Adjust the metallic value of the brush strokes. |
| <b>Normal Custom:</b> | Toggle additional normal-mapping options for the brush strokes. |
| <b>Normal Variation:</b> | Adjust the intensity of the brush strokes in the normal channel. |
| <b>Normal Random:</b> | Adjust the amount of random normal variation applied to the brush strokes. |
| <b>Blending Mode (Normal):</b> | Select the normal blending mode used for the brush strokes. |

### Smoothness

| Parameter name | Description |
| --- | --- |
| <b>Color Smoothness:</b> | Adjust the Kuwahara smoothing effect applied to Base Color. |
| <b>Roughness Smoothness:</b> | Adjust the Kuwahara smoothing effect applied to Roughness. |
| <b>Metallic Smoothness:</b> | Adjust the Kuwahara smoothing effect applied to Metallic. |
| <b>Height Smoothness:</b> | Adjust the Kuwahara smoothing effect applied to Height. |
| <b>Normal Smoothness:</b> | Adjust the Kuwahara smoothing effect applied to Normal. |
| <b>Ambient Occlusion Smoothness:</b> | Adjust the Kuwahara smoothing effect applied to Ambient Occlusion. |

### Colorize

| Parameter name | Description |
| --- | --- |
| <b>Color Opacity:</b> | Adjust the opacity of the color override applied to Base Color. |
| <b>Color:</b> | Select the color used to override Base Color. |
| <b>Grunge Variation:</b> | Select the pattern shape used for color variation. |
| <b>Grunge Opacity:</b> | Adjust the amount of pattern-based color variation in Base Color. |
| <b>Grunge Color:</b> | Adjust the tint of the pattern-based color variation in Base Color. |
| <b>Tilling Amount:</b> | Adjust the number of patterns mapped into the color variation. |
| <b>Pattern Scale:</b> | Adjust the scale of the patterns mapped into the color variation. |

### Gradient

| Parameter name | Description |
| --- | --- |
| <b>Gradient Mode:</b> | Select whether the gradient uses one color or two colors. |
| <b>Color:</b> | Adjust the first gradient color. |
| <b>Color Opacity:</b> | Adjust the opacity of the first gradient color. |
| <b>Color Blending Mode:</b> | Select the blending mode of the first gradient color. |
| <b>Color 2:</b> | Adjust the second gradient color. |
| <b>Color 2 Opacity:</b> | Adjust the opacity of the second gradient color. |
| <b>Color 2 Blending Mode:</b> | Select the blending mode of the second gradient color. |
| <b>Horizontal Rotation:</b> | Adjust the horizontal rotation of the gradient. |
| <b>Vertical Rotation:</b> | Adjust the vertical rotation of the gradient. |
| <b>Gradient Invert:</b> | Toggle inversion of the gradient mask. |
| <b>Gradient Offset:</b> | Adjust the offset of the gradient mask. |
| <b>Gradient Contrast:</b> | Adjust the contrast of the gradient mask. |

### Baked Lighting

| Parameter name | Description |
| --- | --- |
| <b>Brush Strokes In Lighting:</b> | Adjust how much brush stroke variation appears in the baked lighting. |
| <b>Diffuse Intensity:</b> | Adjust the intensity of the diffuse light. |
| <b>Diffuse Color:</b> | Adjust the color of the diffuse light. |
| <b>Diffuse Radius:</b> | Adjust the radius of the diffuse light. |
| <b>Diffuse Contrast:</b> | Adjust the contrast of the diffuse light. |
| <b>Specular Intensity:</b> | Adjust the intensity of the specular light. |
| <b>Specular Color:</b> | Adjust the color of the specular light. |
| <b>Specular Radius:</b> | Adjust the radius of the specular light. |
| <b>Specular Contrast:</b> | Adjust the contrast of the specular light. |
| <b>Horizontal Rotation:</b> | Adjust the horizontal rotation of the light source. |
| <b>Vertical Rotation:</b> | Adjust the vertical rotation of the light source. |
| <b>Color Sharpen:</b> | Adjust the sharpening applied to Base Color. |
| <b>Surface Sharpen:</b> | Adjust the mesh-based surface detail effect on Base Color. |

### Edges And Cavities

| Parameter name | Description |
| --- | --- |
| <b>Mode:</b> | Select whether to map cavities, edges, or both on Base Color. |
| <b>Edges and Cavities Contrast:</b> | Adjust the contrast of the edges and cavities mask. |
| <b>Cavities Opacity:</b> | Adjust the intensity of the cavities blended into Base Color. |
| <b>Cavities Spread:</b> | Adjust the spread of the cavities blended into Base Color. |
| <b>Brush Strokes In Cavities:</b> | Adjust how much the brush strokes mask the cavities blending. |
| <b>Custom Cavities Color:</b> | Toggle use of a custom color in the cavities. |
| <b>Cavities Color:</b> | Adjust the custom color blended into the cavities. |
| <b>Edges Opacity:</b> | Adjust the intensity of the edges blended into Base Color. |
| <b>Edges Spread:</b> | Adjust the spread of the edges blended into Base Color. |
| <b>Brush Strokes In Edges:</b> | Adjust how much the brush strokes mask the edges blending. |
| <b>Custom Edges Color:</b> | Toggle use of a custom color on the edges. |
| <b>Edges Color:</b> | Adjust the custom color blended into the edges. |

#### Helpers

| Parameter name | Description |
| --- | --- |
| <b>Display Helpers:</b> | Select the helper mask or debug information to display in Base Color. |

