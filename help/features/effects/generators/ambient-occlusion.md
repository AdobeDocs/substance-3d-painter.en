---
title: Ambient Occlusion
description: Learn how to use Substance 3D Painter's Ambient Occlusion generator.
---

# Ambient Occlusion

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="../../../assets/generators/icon_ambient_occlusion.webp" alt=""/><br><strong>In:</strong> mask, generator, grayscale, blend</td>
    <td style="border: 0;" valign="top"><strong>Description</strong><br>The Ambient Occlusion generator creates a mask based on the baked Ambient Occlusion map with the option to blend a texture or micro details into the mask.<br><br>If using the Ambient Occlusion generator to create a layer mask, you may need to invert the Ambient Occlusion output. By default, the generator outputs occluded areas as dark and non-occluded areas as light. If used as a mask, the masked layer is visible only in non-occluded areas. Inverting the output will ensure the masked layer only appears in occluded areas.<br><br>Baked position, ambient occlusion, and world space normal maps are required as image inputs. <a href="../../../baking/baking.md">Learn more about baking here</a>.</td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| Texture Color | Use a custom texture or an anchor point. |
| Micro Normal Color | Use a custom normal texture or an anchor point. |
| Micro Height Color | Use a custom texture or an anchor point. |
| Ambient Occlusion Grayscale | Use the baked Ambient Occlusion map. |
| World Space Normals Color | Use the baked World Space Normals map. |
| Position Gradient Color | Use the baked Position map. |

## Parameters

| Parameter name | Description |
| --- | --- |
| **Global Invert** | Invert the final result after all effects are combined. |
| **Global Blur** | Smooth the final mask uniformly after all effects are combined. |
| **Global Balance** | Shift the balance of the final mask after all effects are combined between black or white, like a brightness adjustment. |
| **Global Contrast** | Adjust the contrast of the final mask after all effects are combined. |
| **Use Texture** | Toggle usage of a custom texture map on or off. |
| **Use Micro Details** | Toggle usage of custom micro details on or off. |

### Ambient Occlusion

| Parameter name | Description |
| --- | --- |
| **Invert** | Invert just Ambient Occlusion and micro details. |
| **Blur** | Smooth just Ambient Occlusion and micro details. |
| **Balance** | Adjust the balance of just the Ambient Occlusion and micro details, shifting midpoint toward black or white like a brightness control. |
| **Contrast** | Adjust the contrast/falloff of just the Ambient Occlusion and micro details. |

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
    <td>Invert just the custom texture.</td>
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
    <td>When Triplanar is enabled, the texture is projected from three directions (X, Y, Z axes) instead of relying only on UVs.<br><ul><li>Without triplanar, the texture follows the UV layout.</li><li>With triplanar, the texture is projected from multiple angles and blended.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Triplanar Contrast</strong></td>
    <td>Control how smoothly a texture blends when projected using triplanar mapping. This setting adjusts the softness of the blending between the projections from each direction.</td>
  </tr>
</table>

### Micro Details

| Parameter name | Description |
| --- | --- |
| **Micro Height** | Toggle usage of a custom Micro Height map on or off. |
| **Micro Normal** | Toggle usage of a custom Micro Normal map on or off. |
| **AO Radius** | Adjust the radius (range) of the Ambient Occlusion in micro details. |
| **AO Depth** | Adjust the depth (intensity) of the Ambient Occlusion in micro details. |
