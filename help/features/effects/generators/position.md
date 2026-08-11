---
title: Position
description: Learn how to use Substance 3D Painter's Position generator.
---

# Position

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="../../../assets/generators/icon_position.webp" alt=""/><br><strong>In:</strong> mesh, uv, distance</td>
    <td style="border: 0;" valign="top"><strong>Description</strong><br>The Position generator uses the baked position and world space normal maps to create a gradient mask based on the position of the material in 3D space (like top to bottom or side to side).<br><br>The Position generator outputs a monochrome (black-and-white) texture. As a result, it’s useful for generating gradient masks based on the position in world space.<br><br>Baked position and world space normal maps are required as image inputs. <a href="../../../baking/baking.md">Learn more about baking here</a>.</td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| **Texture** Color | Use a custom texture or an anchor point. |
| **Position Gradient** Color | Use the baked Position map. |
| **World Space Normals** Color | Use the baked World Space Normals map. |

## Parameters

| Parameter name | Description |
| --- | --- |
| **Global Invert** | Invert the final result after all effects are combined. |
| **Global Blur** | Blur the final mask uniformly after all gradients are combined. |
| **Global Balance** | Adjust the balance of the final mask after all gradients are combined between black or white, like a brightness adjustment. |
| **Global Contrast** | Adjust the contrast of the final mask after all gradients are combined. |
| **Use Texture** | Toggle usage of a custom texture map on or off. |

### Position Gradient

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert just the position gradient. |
| **Balance** | Adjust the balance of just the position gradient, shifting the midpoint toward black or white like a brightness control. |
| **Contrast** | Adjust the contrast/falloff of just the position gradient. |
| **Brightness** | Adjust the luminosity of just the position gradient. |
| **Right to Left** | Adjust how the effect is applied from left to right across the Mesh. |
| **Top To Bottom** | Adjust how the effect is applied from top to bottom across the Mesh. |
| **Front to Back** | Adjust how the effect is applied from front to back across the Mesh. |

#### Position Gradient/Right to Left

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the Right to Left gradient direction. |
| **Blending Mode** | Select which [blending mode](../../../interface/layer-stack/blending-modes.md) to use for right to left gradient. |

#### Position Gradient/Top To Bottom

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the Top To Bottom gradient direction. |
| **Blending Mode** | Select which [blending mode](../../../interface/layer-stack/blending-modes.md) to use for the top to bottom gradient. |

#### Position Gradient/Front to Back

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the Front to Back gradient direction. |
| **Blending Mode** | Select which [blending mode](../../../interface/layer-stack/blending-modes.md) to use for the front to back gradient. |

### Texture

<table>
  <tr>
    <th>Parameter name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Texture Opacity</strong></td>
    <td>Adjust the visibility of the custom texture.</td>
  </tr>
  <tr>
    <td><strong>Invert</strong></td>
    <td>Invert the custom texture map.</td>
  </tr>
  <tr>
    <td><strong>Grayscale Conversion</strong></td>
    <td>Set the method used to convert from full color into grayscale. The <a href="grayscale-conversion.md">Grayscale Conversion generator has more information about how each method works</a>.</td>
  </tr>
  <tr>
    <td><strong>Blending Mode</strong></td>
    <td>Select which <a href="../../../interface/layer-stack/blending-modes.md">blending mode</a> to use.</td>
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
</table>
