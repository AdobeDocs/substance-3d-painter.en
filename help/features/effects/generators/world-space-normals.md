---
description: Learn how to use Substance 3D Painter's World Space Normals generator.
title: World Space Normals
---

# World Space Normals

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="../../../assets/generators/icon_world_space_normals.png" alt=""/><br><strong>In:</strong> mask, generator, grayscale, blend</td>
    <td style="border: 0;" valign="top"><strong>Description</strong><br>The World Space Normal generator uses the baked world-space normal map to color your model or apply effects based on the direction each surface is facing in 3D space. For example, from top to bottom.<br><br>The World Space Normals generator outputs a monochrome (black-and-white) texture. As a result, it’s useful for generating masks to apply various effects like dirt, dust, snow, or rust based on face directions.<br><br>Baked position and world space normal maps are required as image inputs. <a href="../../../baking/baking.md">Learn more about baking here</a>.</td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| **Texture** Color | Use a custom texture or an anchor point. |
| **World Space Normals** Color | Use the baked World Space Normals map. |
| **Position Gradient** Color | Use the baked Position map. |

## Parameters

| Parameter name | Description |
| --- | --- |
| **Global Invert** | Invert the final result after all effects are combined. |
| **Global Blur** | Soften the final mask uniformly after all effects are combined. |
| **Global Balance** | Shift the balance of the final mask after all effects are combined between black or white, like a brightness adjustment. |
| **Global Contrast** | Adjust the contrast of the final mask after all effects are combined. |
| **Use Texture** | Toggle usage of a custom texture map on or off. |

### World Space Normal

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert just the world space normals. |
| **Blur** | Smooth the world space normals only. |
| **Balance** | Adjust the balance of the world space normals only, shifting the midpoint toward black or white like a brightness control. |
| **Contrast** | Adjust the contrast/falloff of world-space normals only. |
| **Brightness** | Adjust the luminosity of just the world space normals. |
| **Right to Left** | Adjust how the effect is applied from left to right across the Mesh. |
| **Top To Bottom** | Adjust how the effect is applied from top to bottom across the Mesh. |
| **Front to Back** | Adjust how the effect is applied from front to back across the Mesh. |

#### World Space Normal/Right to Left

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the Right to Left gradient direction. |
| **Blending Mode** | Select which [blending mode](../../../interface/layer-stack/blending-modes.md) to use for the current layer. |

#### World Space Normal/Top To Bottom

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the Top to Bottom gradient direction. |
| **Blending Mode** | Select which [blending mode](../../../interface/layer-stack/blending-modes.md) to use for the current layer. |

#### World Space Normal/Front to Back

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert the Front to Back gradient direction. |
| **Blending Mode** | Select which [blending mode](../../../interface/layer-stack/blending-modes.md) to use for the current layer. |

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
    <td>Invert the custom texture only.</td>
  </tr>
  <tr>
    <td><strong>Grayscale Conversion</strong></td>
    <td>Set the method used to convert from full color into grayscale. The <a href="grayscale-conversion.md">Grayscale Conversion generator has more information about how each method works</a>.</td>
  </tr>
  <tr>
    <td><strong>Blending Mode</strong></td>
    <td>Adjust the blending operation to be used. See the dedicated page about blending modes.</td>
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
    <td>When Triplanar is enabled, the texture is projected from three directions (X, Y, Z axes) instead of relying only on UVs.<br><ul><li>Without triplanar, the texture follows the UV layout.</li><li>With triplanar, the texture is projected from multiple angles and blended.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Triplanar Contrast</strong></td>
    <td>Adjust how smoothly a texture blends when it is projected using triplanar mapping. This adjusts the softness of the blending between the projections from each direction.</td>
  </tr>
</table>
