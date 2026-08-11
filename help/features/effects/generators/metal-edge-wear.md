---
title: Metal Edge Wear
description: Learn how to use Substance 3D Painter's Metal Edge Wear generator.
---

# Metal Edge Wear

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="../../../assets/generators/icon_metal_edge_wear.webp" alt=""/><br><strong>In:</strong> mask, generator</td>
    <td style="border: 0;" valign="top"><strong>Description</strong><br>The Metal Edge Wear generator creates the appearance of damage and wear on areas of your mesh that are most likely to be knocked or scratched.<br><br>The Metal Edge Wear generator outputs a monochrome (black and white) texture. As a result, it’s useful for generating masks to add edge wear details to a layer.<br><br>Baked position, curvature, ambient occlusion, and world space normal maps are required as image inputs. <a href="../../../baking/baking.md">Learn more about baking here</a>.</td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| **World space normal** Color | Use the baked World Space Normal map. |
| **Position** Color | Use the baked Position map. |
| **Custom grunge** Grayscale | Use a custom texture or an anchor point. |
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
    <td><strong>Invert</strong></td>
    <td>Invert the metal edge wear mask.</td>
  </tr>
  <tr>
    <td><strong>Wear Level</strong></td>
    <td>Set the total amount of wear.</td>
  </tr>
  <tr>
    <td><strong>Wear Contrast</strong></td>
    <td>Adjust the contrast of the final wear result.</td>
  </tr>
  <tr>
    <td><strong>Use Triplanar</strong></td>
    <td>When <strong>Use Triplanar </strong>is enabled, the texture is projected from three directions (X, Y, Z axes) instead of relying only on UVs. <br><ul><li>Without triplanar enabled, the texture follows the UV layout.</li><li>With triplanar enabled, the texture is projected from multiple angles and blended.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Triplanar Blending Contrast</strong></td>
    <td>Adjust how smoothly a texture blends when it is projected using triplanar mapping. This adjusts the softness of the blending between the projections from each direction.</td>
  </tr>
  <tr>
    <td><strong>Grunge Amount</strong></td>
    <td>Adjust the amount of the grunge details.</td>
  </tr>
  <tr>
    <td><strong>Grunge Scale</strong></td>
    <td>Adjustthe scale of the grunge details.</td>
  </tr>
  <tr>
    <td><strong>Use Custom Grunge</strong></td>
    <td>Toggle usage of a custom grunge map on or off.</td>
  </tr>
  <tr>
    <td><strong>Edges Smoothness</strong></td>
    <td>Adjust the smoothness of the overall edges.</td>
  </tr>
  <tr>
    <td><strong>Ambient Occlusion Masking</strong></td>
    <td>Use the ambient occlusion as a mask to prevent occluded areas from receiving the weathering effect.</td>
  </tr>
  <tr>
    <td><strong>Curvature Weight</strong></td>
    <td>Adjust how much the curvature map affects the final result. The Curvature map is what the generator uses to define edges, so a very low Curvature weight can remove all edge wear, leaving only the grunge.</td>
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
    <td>Adjust the intensity of the Curvature in <strong>Standard </strong>and <strong>Sobel </strong>Curvature mode.</td>
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
