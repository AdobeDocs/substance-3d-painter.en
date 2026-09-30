---
title: Tri-Planar Advanced
description: Learn how to use Substance 3D Painter's Tri-Planar Advanced filter.
---

# Tri-Planar Advanced

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Tri-Planar Advanced icon](./Resources/icon_tri_planar_advanced_filter.png "Tri-Planar Advanced")

<b>In:</b> Effects/projection

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The Tri-Planar Advanced filter is the filter version of the Tri-Planar Advanced generator, with manual controls for the full projection. It gives you control over the rotation and offset values for each axis. Unlike the generator, this filter works directly on the layer content, while the generator requires a custom mask input for blending.

It is used on a texture layer or inside a mask to add tri-planar blending.

</td>
</tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| <b>World Space Normal:</b> | Use the baked World Space Normal map. |
| <b>Position:</b> | Use the baked Position map. |

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Projection:</b> | Select which axes to project across. |
| <b>Blending Mode:</b> | Select how the axis projections blend together. |
| <b>Blending Contrast:</b> | Adjust the contrast of the projection blending. |
| <b>Texture Tiling:</b> | Adjust the tiling of the projected texture. |
| <b>Rotation X:</b> | Adjust the rotation of the X-axis projection. |
| <b>Offset X:</b> | Adjust the offset of the X-axis projection. |
| <b>Rotation Y:</b> | Adjust the rotation of the Y-axis projection. |
| <b>Offset Y:</b> | Adjust the offset of the Y-axis projection. |
| <b>Rotation Z:</b> | Adjust the rotation of the Z-axis projection. |
| <b>Offset Z:</b> | Adjust the offset of the Z-axis projection. |

### Axis X

| Parameter name | Description |
| --- | --- |
| **Rotation X:** | Adjust the rotation of the X-axis texture projection. |
| **Offset X X:** | Adjust the X-axis projection offset along the X axis. |
| **Offset X Y:** | Adjust the X-axis projection offset along the Y axis. |

>[!NOTE]
>
> The offset parameters contain two axes in their title. The first defines the projection axis, and the second defines the offset axis. So **Offset X Y** specifically looks at the projection on the X axis, and offsets that projection along the projections local Y axis.
>
>Another way of thinking about it is that **Offset X X** offsets the X projection **horizontally**, and **Offset X Y** offsets the X projection **vertically**.

### Axis Y

| Parameter name | Description |
| --- | --- |
| **Rotation X:** | Adjust the rotation of the Y-axis texture projection. |
| **Offset Y X:** | Adjust the Y-axis projection offset along the X axis. |
| **Offset Y Y:** | Adjust the Y-axis projection offset along the Y axis. |

>[!NOTE]
>
> The offset parameters contain two axes in their title. The first defines the projection axis, and the second defines the offset axis. So **Offset Y X** specifically looks at the projection on the Y axis, and offsets that projection along the projections local X axis.
>
>Another way of thinking about it is that **Offset Y X** offsets the Y projection **horizontally**, and **Offset Y Y** offsets the Y projection **vertically**.

### Axis Z

| Parameter name | Description |
| --- | --- |
| **Rotation X:** | Adjust the rotation of the Z-axis texture projection. |
| **Offset Z X:** | Adjust the Z-axis projection offset along the X axis. |
| **Offset Z Y:** | Adjust the Z-axis projection offset along the Y axis. |

>[!NOTE]
>
> The offset parameters contain two axes in their title. The first defines the projection axis, and the second defines the offset axis. So **Offset Z Y** specifically looks at the projection on the Z axis, and offsets that projection along the projections local Y axis.
>
>Another way of thinking about it is that **Offset Z X** offsets the Z projection **horizontally**, and **Offset Z Y** offsets the Z projection **vertically**.
