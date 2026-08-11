---
title: Mask Editor
description: Learn how to use Substance 3D Painter's Mask Editor generator.
---

# Mask Editor

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="../../../assets/generators/icon_mask_editor_dark.png" alt=""/><strong>In:</strong> mask, generator</td>
    <td style="border: 0;" valign="top"><strong>Description</strong><br>The Mask Editor generator is a multi-purpose mask generator that lets you combine Textures, Ambietn Occlusion, Curvature, World Space Normal, Gradient, Thickness, and Micro Details into a single mask.<br>The Mask Builder generator is very flexible, but due to its complexity, it can impact performance more than most generators.<br><br>The Mask Editor generator outputs a monochrome (black-and-white) texture. As a result, it’s useful for generating masks based on the various baked maps. <br><br>Baked position, thickness, curvature, ambient occlusion, and world space normal maps are required as image inputs. <a href="../../../baking/baking.md">Learn more about baking here</a>.</td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| **Texture** Color | Use a custom texture or an anchor point. |
| **Texture (Secondary)** Color | Use a custom texture or an anchor point. |
| **World Space Normals** Color | Use the baked World Space Normals map. |
| **Position Gradient** Color | Use the baked Position map. |
| **Thickness** Grayscale | Use the baked Thickness map. |
| **Curvature** Grayscale | Use the baked Curvature map. |
| **Ambient Occlusion** Grayscale | Use the baked Ambient Occlusion map. |
| **Micro Normal** Color | Use a custom normal texture or an anchor point. |
| **Micro Height** Color | Use a custom texture or an anchor point. |

## Parameters

| Parameter name | Description |
| --- | --- |
| **Global Invert** | Invert the final result after all layers are combined. |
| **Global Blur** | Blur the final mask uniformly after all layers are combined. |
| **Global Balance** | Adjust the balance of the final mask after all layers are combined between black or white, like a brightness adjustment. |
| **Global Contrast** | Adjust the contrast of the final mask after all layers are combined. |
| **Texture Opacity** | Adjust the visibility of the custom texture. |
| **Texture 2 Opacity** | Adjust the visibility of the second custom texture. |
| **Ambient Occlusion Opacity** | Adjust the visibility of the ambient occlusion details. |
| **Curvature Opacity** | Adjust the visibility of the curvature details. |
| **World Space Normal Opacity** | Adjust the visibility of the world space normal details. |
| **Position Gradient Opacity** | Adjust the visibility of the position details. |
| **Thickness Opacity** | Adjust the visibility of the thickness details. |

### Texture

<table>
  <tr>
    <th>Parameter name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Invert</strong></td>
    <td>Inverts the custom texture.</td>
  </tr>
  <tr>
    <td><strong>Grayscale Conversion</strong></td>
    <td>Set the method used to convert from full color into grayscale. The <a href="grayscale-conversion.md">Grayscale Conversion generator has more information about how each method works</a>.</td>
  </tr>
  <tr>
    <td><strong>Blending Mode</strong></td>
    <td>Select which <a href="../../../interface/layer-stack/blending-modes.md">blending mode</a> to use for the current layer.</td>
  </tr>
  <tr>
    <td><strong>Scale</strong></td>
    <td>Adjust the size of the custom texture.</td>
  </tr>
  <tr>
    <td><strong>Contrast</strong></td>
    <td>Adjust the contrast/falloff of the custom texture.</td>
  </tr>
  <tr>
    <td><strong>Brightness</strong></td>
    <td>Adjust the luminosity of the custom texture.</td>
  </tr>
  <tr>
    <td><strong>Triplanar</strong></td>
    <td>When <strong>Use Triplanar </strong>is enabled, the texture is projected from three directions (X, Y, Z axes) instead of relying only on UVs. <br><ul><li>Without triplanar enabled, the texture follows the UV layout.</li><li>With triplanar enabled, the texture is projected from multiple angles and blended.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Triplanar Contrast</strong></td>
    <td>Adjust how smoothly a texture blends when it is projected using triplanar mapping. This adjusts the softness of the blending between the projections from each direction.</td>
  </tr>
  <tr>
    <td><strong>Non-Square Tiling</strong></td>
    <td>Toggle Non-Square tiling on or off.</td>
  </tr>
</table>

### Texture 2

<table>
  <tr>
    <th>Parameter name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Invert</strong></td>
    <td>Invert the custom secondary texture.</td>
  </tr>
  <tr>
    <td><strong>Grayscale Conversion</strong></td>
    <td>Set the method used to convert from full color into grayscale. The <a href="grayscale-conversion.md">Grayscale Conversion generator has more information about how each method works</a>.</td>
  </tr>
  <tr>
    <td><strong>Blending Mode</strong></td>
    <td>Select which <a href="../../../interface/layer-stack/blending-modes.md">blending mode</a> to use for the current layer.</td>
  </tr>
  <tr>
    <td><strong>Scale</strong></td>
    <td>Adjust the size of the custom texture.</td>
  </tr>
  <tr>
    <td><strong>Contrast</strong></td>
    <td>Adjust the contrast/falloff of the custom texture.</td>
  </tr>
  <tr>
    <td><strong>Brightness</strong></td>
    <td>Adjust the luminosity of the custom texture.</td>
  </tr>
  <tr>
    <td><strong>Triplanar</strong></td>
    <td>When <strong>Use Triplanar </strong>is enabled, the texture is projected from three directions (X, Y, Z axes) instead of relying only on UVs. <br><ul><li>Without triplanar enabled, the texture follows the UV layout.</li><li>With triplanar enabled, the texture is projected from multiple angles and blended.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Triplanar Contrast</strong></td>
    <td>Adjust how smoothly a texture blends when it is projected using triplanar mapping. This adjusts the softness of the blending between the projections from each direction.</td>
  </tr>
  <tr>
    <td><strong>Non-Square Tiling</strong></td>
    <td>Toggle Non-Square tiling on or off.</td>
  </tr>
</table>

### Ambient Occlusion

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the Ambient Occlusion and Micro Details layers. |
| **Blending Mode** | Select which [blending mode](../../../interface/layer-stack/blending-modes.md) to use for the current layer. |
| **Blur** | Adjust Ambient Occlusion and micro detail softness. |
| **Balance** | Adjust the balance of the Ambient Occlusion and micro details, shifting the midpoint toward black or white like a brightness control. |
| **Contrast** | Adjust the contrast/falloff of the Ambient Occlusion and micro details. |

### Curvature

<table>
  <tr>
    <th>Parameter name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Invert</strong></td>
    <td>Invert the Curvature.</td>
  </tr>
  <tr>
    <td><strong>Blending Mode</strong></td>
    <td>Select which <a href="../../../interface/layer-stack/blending-modes.md">blending mode</a> to use for the current layer.</td>
  </tr>
  <tr>
    <td><strong>Mode</strong></td>
    <td>Set the Curvature mode. <br><ul><li><strong>Edges</strong>: Masks the edges (convex areas)</li><li><strong>Cavities</strong>: Masks the cavities (concave areas)</li><li><strong>Dual</strong>: Masks concave and convex areas.</li><li><strong>Unprocessed</strong>: Normal Curvature mask.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Sharp</strong></td>
    <td>Adjust the visibility of the sharp curvature details.</td>
  </tr>
  <tr>
    <td><strong>Fine</strong></td>
    <td>Adjust the visibility of the fine curvature details.</td>
  </tr>
  <tr>
    <td><strong>Soft</strong></td>
    <td>Adjust the visibility of the soft curvature details.</td>
  </tr>
  <tr>
    <td><strong>Medium</strong></td>
    <td>Adjust the visibility of the medium curvature details.</td>
  </tr>
  <tr>
    <td><strong>Large</strong></td>
    <td>Adjust the visibility of the large curvature details.</td>
  </tr>
  <tr>
    <td><strong>Big</strong></td>
    <td>Adjust the visibility of the big curvature details.</td>
  </tr>
  <tr>
    <td><strong>Huge</strong></td>
    <td>Adjust the visibility of the huge curvature details.</td>
  </tr>
  <tr>
    <td><strong>Contrast</strong></td>
    <td>Adjust the contrast/falloff of the Curvature.</td>
  </tr>
  <tr>
    <td><strong>Brightness</strong></td>
    <td>Adjust the luminosity of the Curvature.</td>
  </tr>
</table>

### World Space Normal

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the world space normals. |
| **Blending Mode** | Select which [blending mode](../../../interface/layer-stack/blending-modes.md) to use for the current layer. |
| **Blur** | Adjust the world space normal softness. |
| **Balance** | Adjust the balance of the world space normals, shifting midpoint toward black or white like a brightness control. |
| **Contrast** | Adjust the contrast/falloff of the world space normals. |
| **Brightness** | Adjust the luminosity of the world space normals. |
| **Right to Left** | Adjust how the effect is applied from left to right across the Mesh. |
| **Top To Bottom** | Adjust how the effect is applied from top to bottom across the Mesh. |
| **Front to Back** | Adjust how the effect is applied from front to back across the Mesh. |

### World Space Normal/Right to Left

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the Right to Left direction. |
| **Blending Mode** | Select which [blending mode](../../../interface/layer-stack/blending-modes.md) to use for the current layer. |

### World Space Normal/Top To Bottom

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the Top To Bottom direction. |
| **Blending Mode** | Select which [blending mode](../../../interface/layer-stack/blending-modes.md) to use for the current layer. |

### World Space Normal/Front to Back

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the Front to Back direction. |
| **Blending Mode** | Select which [blending mode](../../../interface/layer-stack/blending-modes.md) to use for the current layer. |

### Position Gradient

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the position gradient layer. |
| **Balance** | Adjust the balance of the position gradient layer, shifting midpoint toward black or white like a brightness control. |
| **Contrast** | Adjust the contrast/falloff of the position gradient layer. |
| **Brightness** | Adjust the luminosity of the position gradient layer. |
| **Blending mode** | Select which [blending mode](../../../interface/layer-stack/blending-modes.md) to use for the current layer. |
| **Right to Left** | Adjust how the effect is applied from left to right across the Mesh. |
| **Top To Bottom** | Adjust how the effect is applied from top to bottom across the Mesh. |
| **Front to Back** | Adjust how the effect is applied from front to back across the Mesh. |

>[!TIP]
>
> The Position gradient is made up of up to three gradients, right-to-left, top-to-bottom, and front-to-back. Each of the sub gradients has their own blending mode that can be used to create different effects or mask out different areas of the model. The blending modes for these gradients only interact with each other to create a final Position gradient layer, they do not interact directly with other layers in the generator outside the position gradient.

### Position Gradient - Right to Left

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the Right to Left gradient direction. |
| **Blending Mode** | Select which [blending mode](../../../interface/layer-stack/blending-modes.md) to use for right to left gradient. |

### Position Gradient - Top To Bottom

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the Top To Bottom gradient direction. |
| **Blending Mode** | Select which [blending mode](../../../interface/layer-stack/blending-modes.md) to use for the top to bottom gradient. |

### Position Gradient - Front to Back

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the Front to Back gradient direction. |
| **Blending Mode** | Select which [blending mode](../../../interface/layer-stack/blending-modes.md) to use for the front to back gradient. |

### Thickness

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the thickness. |
| **Blur** | Adjust the softness of details in the thickness layer. |
| **Contrast** | Adjust the contrast/falloff of the thickness layer. |
| **Brightness** | Adjust the luminosity of the thickness layer. |

### Micro Details

<table>
  <tr>
    <th>Parameter name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Micro Height</strong></td>
    <td>Toggle usage of a custom Micro Height map on or off.</td>
  </tr>
  <tr>
    <td><strong>Micro Normal</strong></td>
    <td>Toggle usage of a custom Micro Normal map on or off.</td>
  </tr>
  <tr>
    <td><strong>Curvature Type</strong></td>
    <td>Set the Curvature type. <br><ul><li><strong>Standard</strong>: Produces a usually quite sharp result, but can lack wider details.</li><li><strong>Sobel</strong>: Produces similar results compared to standard, but slightly blurrier because it evaluates the normal map using a Sobel filter.</li><li><strong>Smooth</strong>: Produces different levels of blur (like mipmaps) to accumulate information. This usually provides smoother curves, but details can get lost.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Curvature Intensity</strong></td>
    <td>Adjust the intensity of the Curvature in <strong>Standard</strong> and <strong>Sobel </strong>Curvature mode.</td>
  </tr>
  <tr>
    <td><strong>Height Details Intensity</strong></td>
    <td>Adjust the intensity of the Micro Height details.</td>
  </tr>
  <tr>
    <td><strong>AO Radius</strong></td>
    <td>Adjust the radius (range) of the Ambient Occlusion in micro details.</td>
  </tr>
  <tr>
    <td><strong>AO Depth</strong></td>
    <td>Adjust the depth (intensity) of the Ambient Occlusion in micro details.</td>
  </tr>
</table>
