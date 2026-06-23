---
helpx_url: 'https://helpx.adobe.com/substance-3d-painter/interface/viewport.html'
description: Learn how to use the viewport in Substance 3D Painter to visualize your 3D models and textures during the painting process.
helpx_description: Painter > Interface > Viewport
title: Viewport
---

# Viewport

![](../../assets/viewports-progress.jpg){width="600px"}

The viewport is where the 3D mesh and its textures are displayed. This is also where it is possible to paint on the 3D mesh surface.

## Overview

The viewport is divided into fours parts:

* **Contextual toolbar**: this toolbar sits at the top of the viewport and offer shortcut to various properties depending on the current context (brush parameters when painting for example).
* **3D view**: this view shows the 3D mesh from a specific angle, defined by a camera.
* **2D view**: this view shows UV unwrapping of the 3D mesh for the currently selected [Texture Set](../texture-set/texture-set-list.md).
* **Progress bar**: this gray/green bar at the bottom of the viewport appears when a computation is in progress (for example when the engine is generating textures).

For more details, see the dedicated pages:

* [2D view](2d-view.md)
* [3D view](3d-view.md)
* [Camera management](camera-management.md)

The 3D and 2D views can be adjusted to display additional or different information via the [Display settings](../../interface/display-settings/display-settings.md).

## Viewport navigation controls

Controls for moving around the viewport are similar in both 2D and 3D views.

<table>
  <tr>
    <th>Movement type</th>
    <th>Shortcut</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Orbit/rotate<br></td>
    <td><strong>Alt + Left click</strong></td>
    <td><ul><li>3D View: Orbit the camera around the cursor position.</li><li>2D View: Rotate the UV space around the cursor position.</li></ul></td>
  </tr>
  <tr>
    <td>Pan</td>
    <td><strong>Alt + Middle click</strong></td>
    <td>Move the camera up, down, left, or right.</td>
  </tr>
  <tr>
    <td>Zoom/dolly</td>
    <td><strong>Alt + Right click</strong></td>
    <td>Zoom closer to or further from the mesh/UVs.</td>
  </tr>
</table>

>[!NOTE]
> In both 2D and 3D views, you can snap to orthogonal angles when orbiting/rotating with **Alt + Shift + Left click**.

## Changing The Layout

The default layout puts the 3D view on the left and the 2D view on the right. A few parameters are available from the **Contextual Toolbar** which allow to change the layout:

<table>
  <tr>
    <th><em>Setting</em></th>
    <th><em>Description</em></th>
  </tr>
  <tr>
    <td><strong>Viewport Mode</strong><br>![](../../assets/viewport-viewmode.png)</td>
    <td>These settings control the layout of the viewport:<br><ul><li><strong>3D/2D</strong> (default): display both the 3D and 2D views in the viewport</li><li><strong>3D only</strong>: maximize the 3D view and hide the 2D view.</li><li><strong>2D only</strong>: maximize the 2D view and hide the 3D view.</li><li><strong>Swap 3D/2D</strong>: exchange the order in which the views are displayed. If the 3D view was on the left it will be on the right after choosing this action.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Perspective Mode</strong><br>![](../../assets/viewport-camera-projection.png)</td>
    <td>These setting control how the 3D mesh will appear in the 3D view:<br><ul><li><strong>Perspective view</strong> (default): displays the 3D mesh as it would be seen by the human eye or a camera.</li><li><strong>Orthographic view</strong>: displays the 3D mesh as every direction measure the same length.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Camera Rotation Mode</strong><br>![](../../assets/viewport-camera-axis.png)</td>
    <td>This settings control on how many axes the viewport camera can rotate.<br><ul><li><strong>Free rotation</strong>: the camera rotate on the X, Y and Z axes.</li><li><strong>Constrained rotation</strong> (default): the camera rotate only on the X and Y axes (no roll).</li></ul></td>
  </tr>
  <tr>
    <td><strong>Rendering Mode</strong><br>![](../../assets/viewport-rendering.png)</td>
    <td>Switch to the <a href="../../features/iray-renderer/iray-renderer.md">rendering mode</a>.</td>
  </tr>
</table>
