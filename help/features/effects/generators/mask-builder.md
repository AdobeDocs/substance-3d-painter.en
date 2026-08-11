---
title: Mask Builder
description: Learn how to use Substance 3D Painter's Mask Builder generator.
---

# Mask Builder

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="../../../assets/generators/icon_mask_builder_dark.png" alt=""/><strong>In:</strong> mask, generator</td>
    <td style="border: 0;" valign="top"><strong>Description</strong><br>The Mask Builder generator is a legacy version of the Mask Editor generator. It's a multi-purpose mask generator that allows you to combine Grunge, AO, Curvature, Gradient, World Space Normal, Scratches, Scatter, and Micro Details in a single mask.<br><br>The Mask Builder generator is very flexible, but due to its complexity, it can impact performance more than most generators.<br><br>The Mask Builder generator outputs a monochrome (black-and-white) texture. As a result, it’s useful for generating masks based on the various baked maps. <br><br>Baked position, curvature, ambient occlusion and world space normal maps are required as image inputs. <a href="../../../baking/baking.md">Learn more about baking here</a>.</td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| **World space normal** Color | Use the baked World Space Normals map. |
| **Custom grunge 1** Grayscale | Use a custom texture or an anchor point. |
| **Custom grunge 2** Grayscale | Use a custom texture or an anchor point. |
| **Scatter input** Grayscale | Use a custom texture or an anchor point. |
| **Position** Color | Use the baked Position map. |
| **Curvature** Grayscale | Use the baked Curvature map. |
| **Ambient Occlusion** Grayscale | Use the baked Ambient Occlusion map. |
| **Micro Normal** Color | Use a custom normal texture or an anchor point. |
| **Micro Height** Color | Use a custom texture or an anchor point. |

## Parameters

<table>
  <tr>
    <th>Parameter name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Seed</strong></td>
    <td>Set the seed value used to generate the dirt texture. <br><ul><li>Click Random to switch to another random seed.</li><li>Click the pencil to see the current seed value, and enter a specific value if desired.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Level</strong></td>
    <td>Adjust the midpoint level of the final mask after all effects are combined between black or white, like a brightness adjustment.</td>
  </tr>
  <tr>
    <td><strong>Contrast</strong></td>
    <td>Adjust the contrast/falloff of the final mask.</td>
  </tr>
  <tr>
    <td><strong>Invert</strong></td>
    <td>Invert the final result of the combined mask.</td>
  </tr>
  <tr>
    <td><strong>Use Triplanar</strong></td>
    <td>When <strong>Use Triplanar </strong>is enabled, the texture is projected from three directions (X, Y, Z axes) instead of relying only on UVs. <br><ul><li>Without triplanar enabled, the texture follows the UV layout.</li><li>With triplanar enabled, the texture is projected from multiple angles and blended.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Triplanar Blending Contrast</strong></td>
    <td>Adjust how smoothly a texture blends when projected using triplanar mapping. It adjusts the softness of the blending between the projections from each direction.</td>
  </tr>
  <tr>
    <td><strong>Grunge</strong></td>
    <td>Adjust how much the Grunge settings impact the final mask result.</td>
  </tr>
  <tr>
    <td><strong>AO</strong></td>
    <td>Adjust how much the AO (Ambient Occlusion) settings impact the final mask result.</td>
  </tr>
  <tr>
    <td><strong>Curvature</strong></td>
    <td>Adjust how much the Curvature settings impact the final mask result.</td>
  </tr>
  <tr>
    <td><strong>Top/Down Gradient</strong></td>
    <td>Adjust how much the Top/Down Gradient impact the final mask result.</td>
  </tr>
  <tr>
    <td><strong>World Space Normal</strong></td>
    <td>Adjust how much the World Space Normal settings affect the final mask result.</td>
  </tr>
  <tr>
    <td><strong>Scratches</strong></td>
    <td>Adjust how much the Scratches settings affect the final mask result. For the Scratches to be visible, Grunge, AO, or Curvature need to be above 0.</td>
  </tr>
  <tr>
    <td><strong>Scatter</strong></td>
    <td>Tweaks how much the Scatter affects the mask.</td>
  </tr>
</table>

### Grunge

| Parameter name | Description |
| --- | --- |
| **Scale** | Adjust the size of the grunge texture. |
| **Use Custom Grunge** | Toggle usage of a custom Grunge map on or off. It's just the visibility of the Custom Grunge 1. To control the visibility of the Custom Grunge 2, adjust the Secondary Custom Grunge slider. |
| **Secondary Custom Grunge** | Adjust the visibility of the Custom Grunge 2 texture. |
| **Invert** | Invert the grunge maps. |

### Ambient Occlusion

| Parameter name | Description |
| --- | --- |
| **Range** | Adjust the range of the AO mask. |
| **Contrast** | Adjust the contrast/falloff of the AO mask. |
| **Noisiness** | Add noise to the AO result, effectively decreasing the brightness of the mask. |
| **Invert** | Invert the AO mask. |

### Curvature

| Parameter name | Description |
| --- | --- |
| **Convex Range** | Adjust the minimum convex angle required to be highlighted by the mask. |
| **Convex Contrast** | Adjust the convex mask contrast. |
| **Convex Invert** | Inverts the convex mask. |
| **Concave Range** | Adjust the minimum concave angle to be highlighted by the mask. |
| **Concave Contrast** | Adjust the concave mask contrast. |
| **Concave Invert** | Invert the concave mask. |
| **Smoothness** | Adjust the blend between light and dark areas of the Curvature mask. |
| **Level Boost** | Use this to extend the range of the masked area. This acts like a multiplier for the **Convex Range** and **Concave Range** parameters. |
| **Noisiness** | Add noise to the Curvature result, effectively decreasing the brightness of the mask. |

### Gradient

Gradient position is based on the Position map which can either be baked with Full Scene or Per Material normalization scale. If your material only appears in a small area of your scene, but the position map is baked with a Full Scene Normalization scale, it may be difficult to adjust the Gradient Range to get the desired result.

| Parameter name | Description |
| --- | --- |
| **Range** | Adjust the gradient range. |
| **Contrast** | Tweaks the gradient contrast. |
| **Invert** | Inverts the gradient. |

### World Space Normal

**Front**, **back**, **left**, and **right** values may not correspond with the front, back, left, and right side of your mesh. By default, **Front** corresponds to the positive X-axis, and Right corresponds to the positive Z-axis.

| Parameter name | Description |
| --- | --- |
| **Top Intensity** | Adjust the range (intensity) of the top down gradient. |
| **Bottom Intensity** | Adjust the range (intensity) of the bottom up gradient. |
| **Front Intensity** | Adjust the range (intensity) of the front back gradient. |
| **Back Intensity** | Adjust the range (intensity) of the back front gradient. |
| **Right Intensity** | Adjust the range (intensity) of the right left gradient. |
| **Left Intensity** | Adjust the range (intensity) of the left right gradient. |

### Scratches

| Parameter name | Description |
| --- | --- |
| **Amount** | Adjust the density of the scratches. |
| **Scale** | Adjust the size of the scratches. |

### Scatter

| Parameter name | Description |
| --- | --- |
| **Scale** | Adjust the size of the scatter effect. A higher scale results in more, smaller stamps while a lower scale increases individual stamp size with fewer visible. |
| **Density** | Adjust the number of the scattered stamps. |
| **Size** | Adjust the size of the scattered stamps. |
| **Size Variation** | Adjust how much randomness there is in the size of each instance of the scattered stamp. A higher Size Variation randomly reduces stamp sizes, so increasing Size Variation may mean you also need to increase the Size value to maintain the same average size. |
| **Opacity Variation** | Adjust how much randomness there is in the opacity of each instance of the scattered stamp. |

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
    <td>Adjust the intensity of the Curvature in <strong>Standard </strong>and <strong>Sobel </strong>Curvature mode.</td>
  </tr>
  <tr>
    <td><strong>Height Details Intensity</strong></td>
    <td>Adjust the strength of the Micro Height details.</td>
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
