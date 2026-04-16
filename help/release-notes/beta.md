---
description: Learn about the current Substance 3D Painter beta including new features and a full changelog.
title: Beta release
---

# Version 12.1.0 (Beta)

Substance Painter 12.1.0 introduces major improvements to baking workflows, a new option to automatically unwrap hard surface models, and support for OpenPBR.

Release date: **31 March 2026** 

>[!NOTE]
>
>Beta releases can include unknown bugs or issues so stability is not guaranteed. As a result, we do not recommend using Beta builds for urgent or sensitive work.

## New baking features

![](../assets/v1210_baking_promotional.jpeg)

Enable automatic rebaking to save time while tweaking baking parameters.

### Fix distortion with a skew correction map

New Skew correction options are available when in Baking mode that allow you to directly fix distortion.

![](../assets/v1210_skewpainting_promotional.jpg)

With Cage set to **Distance-based**, under Skew correction, select **Paint skew correction** to start painting on your low-poly mesh.

![](../assets/v1210_skewpainting_enterpaintingmode.png)

While in skew painting mode, you can paint on the surface of your mesh to control the direction of surface normals for baking.

>[!NOTE]
>
>You can use the standard painting shortcuts while painting skew corrections, just like you would in a paint layer. For example, use **X** to switch between painting and erasing, or use **ctrl + right-click** to change the brush size.

Turn on **Edge protection** to ensure the baker still projects high-poly softness onto low-poly hard edges. You can adjust the **Edge distance** and **Edge contrast** for finer control over the edge protection.

![](../assets/v1210_skewpainting_comparison.png)

Above, the mesh on the left displays visible distortion due to surface normal misalignment near hard edges. The same mesh on the right with a painted skew map shows no more distortion, and normals are perpendicular to the surface, except near the edges thanks to edge protection.

### Updated Mesh map bakers panel

Instead of appearing like another channel, **Common settings** now has a dedicated button.

Additionally, new controls are available next to each channel so you can:

1. View the channel in the viewport.
1. Rebake the channel.
1. Toggle auto-rebake for the channel.
1. Sync settings across texture sets for the channel.

![](../assets/v1210_baking_meshmapbakers.png)

## OpenPBR support

Use the new industry standard for your projects. Import shader settings and textures from other apps and export your work with the USD format to ensure material consistency across your workflow.

![](../assets/v1210_OpenPBR.jpeg)

You can find the new OpenPBR shader in the **Shader settings panel**. Painter still defaults to the **Adobe Standard Material - PBR Metallic Roughness** shader.

## Automatic unwrapping for hard surface models

Hard-surface has been added as an optional **Unwrap mode** when using Auto-Unwrap. With hard surface mode selected, the unwrapper focuses on minimizing distortion of UV islands and creating an orthographically aligned UV map.  

![Hard surface unwrap produces cleaner, orthographic UVs for your hardsurface assets.](../assets/v1210_autounwrap_example.png)

## Changelog

Release date: 2026/03/31


### Added:
    
* &#91;Skew baking&#93; Skew Painting Tools
* &#91;Skew baking&#93; Change Polygon Fill behaviour to work on first channel of the current stack instead of basecolor or mask only
* &#91;Skew baking&#93; Add Skew Preview shader and Skew Direction Vector visuals when painting skew map
* &#91;Skew baking&#93; Split Mesh Map / Common Baking settings + Move Common Settings out of mesh map list
* &#91;Skew baking&#93; Auto rebake
* &#91;Skew baking&#93; Add Edge Protection option
* &#91;OpenPBR&#93; Add support for OpenPBR 1.1
* &#91;OpenPBR&#93; Export OpenPBR materials and textures via USD
* &#91;OpenPBR&#93; Import OpenPBR materials and textures via USD
* &#91;Iray&#93; Add new MDL to support OpenPBR 1.1 in Iray
* &#91;Auto Unwrap&#93; Integrate Hard Surface option
* &#91;Substance&#93; Add new "mesh_hard_edges_triangle" engine map input
* &#91;Substance&#93; Add new "mesh_hard_edges" engine map input
* &#91;UI&#93; Add warning in the viewport when trying to paint on another Texture Set

### Fixed:

* &#91;Polygon Fill Tool&#93; Does not work with non-PBR


