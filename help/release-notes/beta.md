---
breadcrumb-title: ""
description: Learn about the current Substance 3D Painter beta including new features and a full changelog.
title: Beta release
user-guide-description: ""
user-guide-title: ""
---

# Version 12.1.0 (Beta)

Substance Painter 12.1.0 introduces major improvements to baking workflows, a new option to automatically unwrap hard surface models, and support for OpenPBR.

Release date: **26 March 2026** 

## New baking features

### Paint skew correction when baking

New Skew correction options are available when in Baking mode that allow you to directly fix distortion problems when baking.

![alt text](<../assets/12.1.0 skew painting - comparison.png>)

With Cage set to **Distance-based**, under Skew correction, select **Paint skew correction** to start painting on your low-poly mesh.

![alt text](<../assets/12.1.0 skew painting - enter painting mode.png>){width="300"}

While in skew painting mode, you can paint on the surface of your mesh to control how the surface normals impact the bake. 

>[!NOTE]
>
>You can use the standard painting shortcuts while painting skew corrections, just like you would in a paint layer. For example, use **X** to switch between painting and erasing, or use **ctrl + right-click** to change the brush size.

Turn on **Edge protection** to ensure the baker still projects high-poly softness onto low-poly hard edges. You can adjust the **Edge distance** and **Edge contrast** for finer control over the edge protection.

### Updated Mesh map bakers panel

Instead of appearing like another channel, **Common settings** now has a dedicated button.

Additionally, new controls are available next to each channel so you can:

1. View the map in the viewport.
1. Rebake the map.
1. Toggle auto-rebake for the channel.
1. Sync settings (available when the project has multiple texturesets).

![alt text](<../assets/12.1.0 baking - mesh map bakers.png>)

## OpenPBR support

Use the new industry standard for your projects. Import shader settings and textures from other apps and export your work witht he USD format to preserve material consistency throughout your workflow.

* new post processing = improved visuals in viewport
* matching visuals across multiple OpenPBR applications
* USD for portability

## Automatic unwrapping for hard surface models

Hard-surface has been added as an Unwrap mode when using Auto-Unwrap. 

With hard-surface mode selected, the unwrapper focuses on minimizing distortion of UV islands, and creating an orthographically aligned UV map. 

[image]
