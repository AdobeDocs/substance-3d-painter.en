---
title: "Version 12.0"
description: ""
helpx_description: "Substance 3D Painter"
helpx_url: "https://helpx.adobe.com/substance-3d-painter/release-notes/version-12-0.html"
---

# Version 12.0

<b>Substance 3D Painter 12.0</b> offers texture flattening directly in the layer stack, a new automatic mode for warp projection, a revamped set of post-processing effects, and an improved project creation and settings workflow.

Release date: <b>9 March 2026</b>

>[!NOTE]
>
> In this version the support of <b>integrated GPUs</b> with <b>unified/shared memory</b> has been improved. Better detection of video memory can be expected which should lead to better performance and fewer graphical issues.

## Major features

### New flattening of LAYERS

![](../assets/v12_banner_flatten.jpg)

A new <b>Flatten</b> action is now available in the right-click context menu of the layer stack. Several layers can be quickly merged by grouping them (<b>Ctrl/Cmd + G</b>) and creating a flattened copy (<b>Ctrl/Cmd + M</b>). The source group is automatically disabled, leaving the choice to either delete it or alternatively save it as a <b>Smart Material</b> for later editing.

Flattened elements of the layer stack can also be exported directly to disk for quick iterations in other applications. Groups, layers, or masks can be exported individually or in batch via the right-click menu of the layer stack.

* <b>Flatten textures directly in the layer stack</b>  
  Any group can be flattened by pressing <b>Ctrl/Cmd + M</b> or by selecting the <b>Flatten group</b> entry in the right-click contextual menu. This generates a merged copy of the selected content while automatically disabling the source group, keeping the original layers intact until a decision is made to remove or restore them.

  ![](../assets/v12_flatten_menu.jpg)
* <b>Flatten and export textures to the disk</b>  
  A dedicated export action in the right-click menu bakes the flattened result of a layer, mask, or group and saves it directly to disk. This is useful for transferring baked content to other applications without going through the full texture export pipeline.
* <b>Batch operations</b>  
  Multiple layers, groups, or masks can be selected at once and flattened or exported individually in a single operation, making it efficient to process large portions of a layer stack in one step.

  ![](../assets/v12_flatten_batch.jpg)

>[!NOTE]
>
> More information about the flattening of layers is available in the [dedicated documentation page](../interface/layer-stack/flatten-layers.md).

### New warp to geometry mode for projections

![](../assets/v12_banner_warp_auto.jpg)

Decals can now automatically adapt to complex surfaces, reducing the need for manual adjustments. The <b>Warp to geometry</b> toggle is available in the contextual toolbar while the Warp projection is active.

* <b>New parameter in contextual toolbar</b>  
  A new <b>Warp to geometry</b> toggle is available in the contextual toolbar whenever the Warp projection mode is active. It can be turned off at any time without resetting the current projection setup.

  ![](../assets/v12_warp_toolbar.png)
* <b>Automatic wrapping to mesh surface</b>  
  When enabled, the warp projection automatically follows the curvature and topology of the underlying mesh. Dragging the projection across the surface will make it smoothly conform to the geometry, significantly reducing the amount of manual fine-tuning needed when placing decals on complex or curved shapes.

  ![](../assets/v12_warp_to_geometry.gif)
* <b>Preservation of local deformations</b>  
  When editing the warp projection grid vertices, the warp to geometry mode will try to retain the pre-defined deformation to ensure the same shape is always projected.

  ![](../assets/v12_warp_to_geometry_deformed.gif)

>[!NOTE]
>
> For more information about the warp projection, check out the [dedicated documentation page](../painting/fill-projections/warp-projection.md).

### New Post effects

![](../assets/v12_banner_post_effects2.jpg)

Renders inside Painter can now be enhanced with a brand new set of post-processing effects available in the <b>Display Settings</b> window. New additions such as <b>Lens flare</b> and <b>Film grain</b> are now available, alongside improved <b>Depth of field</b> and <b>Glare</b> effects among many others.

Here is an example of what you can achieve with the new effects:

![](../assets/v12_render_withpost.jpg)

* <b>New post-processing effects</b>  
  All post-processing effects can be enabled and configured individually from the <b>Display Settings</b> window. Effects are applied in stack order and each one can be toggled on or off independently, making it easy to combine and experiment with different results.

  ![](../assets/v12_display_settings_post_effects.png)
* <b>New list of effects:</b>

  * <b>Depth of field</b>: Blurs objects outside the focal range to simulate camera lens focus.
  * <b>Bloom</b>: Adds a soft glow emanating from bright areas of the image.
  * <b>Glare</b>: Creates light streaks around sources of light.
  * <b>Lens flare</b>: Simulates optical reflections of the lens when a bright light shines in the camera.
  * <b>Lateral aberration</b>: Simulates chromatic fringing at the image edges caused by lens imperfections.
  * <b>Vignette</b>: Darkens the corners and edges of the frame to draw focus toward the center.
  * <b>Sharpen</b>: Increases edge contrast to make the rendered image appear crisper.
  * <b>Film grain</b>: Overlays subtle noise to replicate the texture of analog film.
  * <b>Tone mapping</b>: Remaps HDR luminance values into a displayable range for a more cinematic look.
  * <b>Color correction</b>: Adjusts contrast, saturation, brightness, and temperature to fine-tune the overall color balance.

>[!NOTE]
>
> For more information about the new effects, take a look at the [dedicated documentation](../features/post-processing/post-processing.md).

### Improved new project and settings window

![](../assets/v12_banner_project_window.jpg)

The new project window and the project settings dialog have been redesigned to be easier to navigate. Parameters have been re-ordered and grouped for better readability, and the mesh re-importing workflow has been improved to reduce repetitive steps when iterating on a project.

* <b>Improved new project window</b>  
  Parameters in the new project window have been reorganized and re-ordered so that the most commonly used settings are more prominently placed. The overall layout is now easier to scan, reducing the time needed to configure a new project.
* <b>New workflow for re-importing meshes in project settings</b>  
  A new checkbox <b>Reimport mesh</b> in the project settings allows re-importing the project mesh more easily thanks to the file path of the previously loaded file now being saved and pre-filled automatically.

  ![](../assets/v12_project_settings.png)

## Release Notes

## Version 12

### 12.0.0

Release date: <b>2026/03/09</b>  
Summary: <b>This is a major release. This release contains the features flatten layers, warp on geometry, new post effects, improvement to the new project window and other improvements.</b>  
  
<b>Added</b>:

* &#91;Flatten Layers&#93; Flatten layers inside the layer stack
* &#91;Flatten Layers&#93; Export flattened layers to disk
* &#91;Warp to geometry&#93; Add new auto-warping functionality to Warp projections
* &#91;Post-effects&#93; Replace post effects with addition of new ones
* &#91;Post-effects&#93; Update tone mapper
* &#91;Post-effects&#93; Add new usage for Post-effects assets
* &#91;Content&#93;&#91;Post-effects&#93; Integrate default post-effects assets in library
* &#91;New Project&#93; Improve UI for Project Creation
* &#91;New project&#93; Changes to reimport mesh functionality
* &#91;New project&#93; Allow for \*.geo.usd files to be opened
* &#91;Project Configuration&#93; Improve UI for Project Configuration
* Update USD library to version 25.05
* Update Substance Engine to version 9.3.4
* Raise minimum drivers to 25.3.1/25.Q2 for AMD GPUs
* Update Qt to 6.8.6
* &#91;Scripting&#93; Update JavaScript API to version 1.1.20
* Update Python to 3.13

<b>Fixed:</b>

* &#91;Crash&#93; Changing a material channel output in a mask can crash
* &#91;Import&#93; EXR textures are forced into sRGB instead of linear when importing USD files
* &#91;UV Tiles&#93; Image sequence with a single image also fills other UV Tiles
* &#91;Baking&#93; AO is different between CPU and GPU baking
* &#91;Color Management&#93;&#91;MacOS&#93; Viewport BaseColor does not match colorpicker
* &#91;USD&#93; Uniform values are not imported in some cases
