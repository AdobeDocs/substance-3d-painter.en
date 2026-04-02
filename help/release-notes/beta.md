---
breadcrumb-title: ""
description: Learn about the current Substance 3D Painter beta including new features and a full changelog.
title: Beta release
user-guide-description: ""
user-guide-title: ""
---

# Version 12.1.0 (Beta)

Substance Painter 12.1.0 introduces major improvements to baking workflows, a new option to automatically unwrap hard surface models, and support for OpenPBR.

Release date: **31 March 2026** 

>[!NOTE]
>
>Beta releases can include unknown bugs or issues so stability is not guaranteed. The saved .SPP file format is incompatible with previous versions. As a result, we do not recommend using Beta builds for urgent or sensitive work.


## New baking features

![](<../assets/12.1.0-baking-promotional.jpeg>)

Enable automatic rebaking to save time while tweaking baking parameters. Auto rebake can be toggled for a single mesh map a time. Any change to baking settings, triggers this map to rebake.

### Fix distortion with a skew correction map

New Skew correction options are available when in Baking mode that allow you to directly fix baking-induced distortion of your mesh maps.

![](<../assets/12.1.0-skewpainting-promotional.jpg>)

With a **Highpoly loaded**, Cage set to **Distance-based** and **Average Normals** on, under Skew correction, select **Paint skew correction** to start painting on your low-poly mesh.

![](<../assets/12.1.0-skewpainting-enterpaintingmode.png>)

While in skew painting mode, you can paint on the surface of your mesh to control the direction of the rays for baking.

>[!NOTE]
>
>You can use the standard painting shortcuts while painting skew corrections, just like you would in a paint layer. For example, use **X** to switch between black and white, or use **ctrl + right-click** to change the brush size.

Turn on **Edge protection** to ensure you don't end up with seams on hard edges after baking. You can adjust the **Edge distance** and **Edge contrast** for finer control over the edge protection.

![](<../assets/12.1.0-skewpainting-comparison.png>)
Above, the mesh on the left displays visible distortion due to surface normal misalignment near hard edges. The same mesh on the right with a painted skew map shows no more distortion, and normals are perpendicular to the surface, except near the edges thanks to edge protection.

### Updated Mesh map bakers panel

Instead of appearing like another mesh map, **Common settings** now has a dedicated button.

Additionally, new controls are available next to each mesh map entry so you can:

1. **View** the mesh map in the viewport.
1. **Rebake** that individual mesh map.
1. **Toggle auto-rebake** for the mesh map.
1. **Sync** settings across texture sets for the mesh map (already existing option).

The icons for these features are temporary and pending changes.

![](<../assets/12.1.0-baking-meshmapbakers.png>)

## OpenPBR support

Use the new industry standard for your projects. Import shader settings and textures from other apps and export your work with the USD format to ensure material consistency across your workflow.

![](<../assets/12.1.0-OpenPBR.jpeg>)

You can find the new OpenPBR shader in the **Shader settings panel**. Painter still defaults to the **Adobe Standard Material - PBR Metallic Roughness** shader.


## Automatic unwrapping for hard surface models

Hard-surface has been added as an optional **Unwrap mode** when using Auto-Unwrap. With hard surface mode selected, the unwrapper focuses on minimizing distortion of UV islands and creating an orthographically aligned UV map.  This new method also computes faster than the default method. 

![Hard surface unwrap produces cleaner, orthographic UVs for your hardsurface assets.](<../assets/12.1.0-autounwrap-example.png>)

## Changelog

Release date: 2026/04/02

### Added

* [Skew baking] Auto rebake
* [Skew baking] Skew Painting Tools
* [Skew Baking] Add Edge Protection option
* [Skew baking] Change Polygon Fill behaviour to work on first channel of the current stack instead of basecolor or mask only
* [Skew Baking] Add Skew Preview shader and Skew Direction Vector visuals when painting skew map
* [Skew Baking] Split Mesh Map / Common Baking settings + Move Common Settings out of mesh map list
* [Auto Unwrap] Integrate Hard Surface option
* [OpenPBR] Add support for OpenPBR 1.1
* [Substance] Add new "mesh_hard_edges" engine map input
* [Substance] Add new "mesh_hard_edges_triangle" engine map input
* [UI] Add warning in the viewport when trying to paint on another Texture Set


### Fixed

* [Crash] [Baking] crash when .assbin file can't be written in folder
* [Crash] Saving with insufficient disk space can crash or corrupt projects
* [UI] Updated ID map color source tooltip
* [Stencil] Preview has lower resolution than painted result
* [Display] Shadows appear inverted


