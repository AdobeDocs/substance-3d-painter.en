---
title: UV Texel Density
description: Learn how to use Substance 3D Painter's UV Texel Density generator.
---

# UV Texel Density

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="../../../assets/generators/icon_uv_texel_density.png" alt=""/><br><strong>In:</strong> uv, size, utility</td>
    <td style="border: 0;" valign="top"><strong>Description</strong><br>The UV Texel Density generator visualizes a mesh's texel density by applying a colored gradient from low to high.<br>The UV Texel Density Generator outputs a full color texture, and is best used on a fill layer to identify inconsistent UV scaling and ensure uniform texture detail across a model.</td>
  </tr>
</table>

>[!NOTE]
>
> Texel density refers to the number of texels (texture pixels) in a given surface area of your model. A high texel density means that you’re able to pack a lot of detail into a small area of your model, where a low texel density might limit the amount of detail but improve performance. In general, regardless of your materials' resolution, it’s recommended to maintain a consistent texel density across your mesh, as large differences in texel density are often noticeable to viewers and can make an asset feel lower-quality or less realistic.

## Parameters

| Parameter name | Description |
| --- | --- |
| **Color Low** | Set the color used for areas with **low** texel density. |
| **Color Medium** | Set the color used for areas with **medium** texel density. |
| **Color High** | Set the color used for areas with **high** texel density. |
