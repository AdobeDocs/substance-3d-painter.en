---
title: Curvature
description: Learn how to use Substance 3D Painter's Curvature generator.
---

# Curvature

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="../../../assets/generators/icon_curvature.webp" alt=""/><br><strong>In:</strong> mask, generator, grayscale, blend</td>
    <td style="border: 0;" valign="top"><strong>Description</strong><br>The Curvature generator creates a mask based on the baked Curvature map with the option to blend a texture or micro details into the mask.<br><br>The curvature generator outputs a monochrome (black and white) texture. As a result, it’s useful for generating masks rather than applying directly to a layer.<br><br>A baked position map is required as an input. <a href="../../../baking/baking.md">Learn more about baking here</a>.</td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| **Texture** Color | Use a custom texture or anchor point. |
| **Micro Normal** Color | Use a custom normal texture or anchor point. |
| **Micro Height** Color | Use a custom texture or anchor point. |
| **Curvature** Grayscale | Use the baked Curvature map. |
| **World Space Normals** Color | Use the baked World Space Normals map. |
| **Position Gradient** Color | Use the baked Position map. |

## Parameters

| Parameter name | Description |
| --- | --- |
| **Global Invert** | Inverts the final result after all effects are combined. |
| **Global Blur** | Softens the final mask uniformly after all effects are combined. |
| **Global Balance** | Shifts the balance of the final mask after all effects are combined between black or white, like a brightness adjustment. |
| **Global Contrast** | Adjusts the contrast of the final mask after all effects are combined. |
| **Use Texture** | Toggle usage of a custom texture map on or off. |
| **Use Micro Details** | Toggle usage of custom micro details map on or off. |

### Curvature

<table>
  <tr>
    <th>Parameter name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Invert</strong></td>
    <td>Invert the generated curvature map.</td>
  </tr>
  <tr>
    <td><strong>Mode</strong></td>
    <td>Set the Curvature mode. <br><ul><li><strong>Edges</strong>: Masks the edges (convex areas)</li><li><strong>Cavities</strong>: Masks the cavities (concave areas)</li><li><strong>Dual</strong>: Masks concave and convex areas.</li><li><strong>Unprocessed</strong>: Normal Curvature mask.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Sharp</strong></td>
    <td>Adjust the strength of the sharp curvature details.</td>
  </tr>
  <tr>
    <td><strong>Fine</strong></td>
    <td>Adjust the strength of the fine curvature details.</td>
  </tr>
  <tr>
    <td><strong>Soft</strong></td>
    <td>Adjust the strength of the soft curvature details.</td>
  </tr>
  <tr>
    <td><strong>Medium</strong></td>
    <td>Adjust the strength of the medium curvature details.</td>
  </tr>
  <tr>
    <td><strong>Large</strong></td>
    <td>Adjust the strength of the large curvature details.</td>
  </tr>
  <tr>
    <td><strong>Big</strong></td>
    <td>Adjust the strength of the big curvature details.</td>
  </tr>
  <tr>
    <td><strong>Huge</strong></td>
    <td>Adjust the strength of the huge curvature details.</td>
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

### Texture

<table>
  <tr>
    <th>Parameter name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Texture Opacity</strong></td>
    <td>Control the visibility of the custom texture.</td>
  </tr>
  <tr>
    <td><strong>Invert</strong></td>
    <td>Invert just the custom texture.</td>
  </tr>
  <tr>
    <td><strong>Grayscale Conversion</strong></td>
    <td>Select the method used to convert from color input to black and white.</td>
  </tr>
  <tr>
    <td><strong>Blending Mode</strong></td>
    <td>Set the blending mode for the custom texture.</td>
  </tr>
  <tr>
    <td><strong>Scale</strong></td>
    <td>Adjust the size of the custom texture.</td>
  </tr>
  <tr>
    <td><strong>Contrast</strong></td>
    <td>Set the contrast/falloff of the custom texture.</td>
  </tr>
  <tr>
    <td><strong>Brightness</strong></td>
    <td>Set the luminosity of the custom texture.</td>
  </tr>
  <tr>
    <td><strong>Triplanar</strong></td>
    <td>When Triplanar is enabled, the texture is projected from three directions (X, Y, Z axes) instead of relying only on UVs. <br><ul><li>Without triplanar enabled, the texture follows the UV layout.</li><li>With triplanar enabled, the texture is projected from multiple angles and blended.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Triplanar Contrast</strong></td>
    <td>Adjust how smoothly a texture blends when it is projected using triplanar mapping. This adjusts the softness of the blending between the projections from each direction.</td>
  </tr>
</table>

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
    <td>Adjust the strength of the Curvature in <strong>Standard </strong>and <strong>Sobel </strong>Curvature modes.</td>
  </tr>
  <tr>
    <td><strong>Height Details Intensity</strong></td>
    <td>Adjust the strength of the Micro Height details.</td>
  </tr>
</table>
