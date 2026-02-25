---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/painting/presets/photoshop-brush-presets-abr/photoshop-brush-parameters-compatibility.html"
breadcrumb-title: ""
description: Learn about Photoshop brush parameters compatibility in Substance 3D Painter when importing ABR brush presets.
helpx_creative_field: ""
helpx_description: Painter > Painting > Presets > Photoshop Brush Presets (ABR) > Photoshop Brush Parameters Compatibility
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Photoshop Brush Parameters Compatibility
user-guide-description: ""
user-guide-title: ""
---


# Photoshop Brush Parameters Compatibility

This page list all the Photoshop brush parameters and their compatibility with Substance 3D Painter brush engine.

## General Compatibility

When looking inside the ABR file, Substance 3D Painter will only retrieve specific Brush/Tool presets:

| *Preset Type* | *Support* | *Description* |
| --- | --- | --- |
| **Brush (bitmap)** | Imported | Brush presets based on bitmaps as their alphas will be imported. |
| **Brush (procedural)** | Ignored | Brush presets based on procedural shapes (like a circle) are not imported. |
| **Brush (Airbrush)** | Ignored | Brush presets with Airbrush settings are not imported. |
| **Brush (Bristle)** | Ignored | Brush presets with Bristle settings are not imported. |
| **Brush (Erodible)** | Ignored | Brush presets with Erodible settings are not imported. |
| **Pencil** | Ignored | Pencil presets are not imported. |
| **Mixer Brush** | Ignored | Mixer brush presets are not imported. |
| **Clone Stamp** | Ignored | Clone Stamp presets are not imported. |
| **Smudge** | Ignored | Smudge presets are not imported. |

## Parameters

To learn more about what those parameters can do, refer to the official  [Photoshop documentation](https://helpx.adobe.com/photoshop/using/creating-modifying-brushes.html)  .

Not all Photoshop brush parameters are supported. Refer to the legend to know the status of each parameter described below:

* **Square (■)**  : indicates the parameter is supported, refer to the description to know how to access it.
* **Cross (✖)**  : indicates the parameter is not supported.

>[!NOTE]
>
> While control parameters in brush presets can be controlled via various methods such as Pen Tilt, Fade and Pen pressure, only the  **Pen Pressure**  is currently supported.

| *Group* | *Parameter* | *Support* | *Description* |
| --- | --- | --- | --- |
| Brush Tip Shape | **Size** | ■ | Matched with Paint tool Size parameter.  **Note:**  Photoshop defines size in Pixels, while Substance 3D Painter size is based on the project Bounding Box. An exact match is therefore not possible and will only be relative. |
| **Flip X** | ■ | Handled via "Brush Maker Photoshop" Substance file. |  |
| **Flip Y** | ■ | Handled via "Brush Maker Photoshop" Substance file. |  |
| **Angle** | ■ | Matched with Paint tool Angle parameter. |  |
| **Roundness** | ■ | Handled via "Brush Maker Photoshop" Substance file. |  |
| **Hardness** | ■ | Handled via "Brush Maker Photoshop" Substance file. |  |
| **Spacing** | ■ | Matched with Paint tool Spacing parameter. |  |
|  |  |  |  |
| Shape Dynamics | **Size Jitter** | ■ | Matched with Paint tool Size Jitter parameter. |
| **Control (for Size)** | ■ | Matched with Paint tool Pressure setting for Size parameter . |  |
| **Minimum Diameter** | ■ | Matched with Paint tool Minimum Size parameter. |  |
| **Tilt Scale** | ✖ |  |  |
| **Angle Jitter** | ■ | Matched with Paint tool Angle Jitter parameter. |  |
| **Control (for Angle)** | ✖ |  |  |
| **Roundness Jitter** | ■ | Handled via "Brush Maker Photoshop" Substance file. |  |
| **Minimum Roundness** | ■ | Handled via "Brush Maker Photoshop" Substance file. |  |
| **Flip X Jitter** | ■ | Handled via "Brush Maker Photoshop" Substance file. |  |
| **Flip Y Jitter** | ■ | Handled via "Brush Maker Photoshop" Substance file. |  |
| **Brush Projection** | ✖ |  |  |
|  |  |  |  |
| Scattering | **Scatter** | ■ | Matched with Paint tool Position Jitter parameter. |
| **Both Axes** | ■ | Matched with Paint tool Position Jitter Axis parameter. |  |
| **Control (for Scatter)** | ✖ |  |  |
| **Count** | ■ | Compensated via Paint tool Spacing parameter. |  |
| **Count Jitter** | ✖ |  |  |
| **Control (for Count Jitter)** | ✖ |  |  |
|  |  |  |  |
| Texture | **Texture Pattern** | ✖ |  |
| **Invert** | ✖ |  |  |
| **Scale** | ✖ |  |  |
| **Brightness** | ✖ |  |  |
| **Contrast** | ✖ |  |  |
| **Texture Each Tip** | ✖ |  |  |
| **Mode** | ✖ |  |  |
| **Depth** | ✖ |  |  |
| **Minimum Depth** | ✖ |  |  |
| **Depth Jitter** | ✖ |  |  |
| **Control (for Depth Jitter)** | ✖ |  |  |
|  |  |  |  |
| Dual Brush | **Mode** | ✖ |  |
| **Size** | ✖ |  |  |
| **Spacing** | ✖ |  |  |
| **Scatter** | ✖ |  |  |
| **Both Axes** | ✖ |  |  |
| **Count** | ✖ |  |  |
|  |  |  |  |
| Color Dynamics | **Apply Per Tip** | ✖ |  |
| **Foreground/Background Jitter** | ✖ |  |  |
| **Control (for F/B Jitter)** | ✖ |  |  |
| **Hue Jitter** | ✖ |  |  |
| **Saturation Jitter** | ✖ |  |  |
| **Brightness Jitter** | ✖ |  |  |
| **Purity** | ✖ |  |  |
|  |  |  |  |
| Transfert | **Opacity Jitter** | ■ | Matched with Paint tool Stamps Blending parameter set to "Lighten". |
| **Control (for Opacity)** | ■ | Matched with Paint tool Pressure setting for Flow parameter. |  |
| **Minimum (for Opacity Control)** | ■ | Matched with Paint tool Minimum Flow parameter. |  |
| **Flow Jitter** | ■ | Matched with Paint tool Flow Jitter parameter. |  |
| **Control (for Flow)** | ■ | Matched with Paint tool Pressure setting for Flow parameter (if lower than Opacity) . |  |
| **Minimum (for Flow Control)** | ■ | Matched with Paint tool Minimum Flow parameter (if lower than Opacity). |  |
| **Wetness Jitter** | ✖ |  |  |
| **Control (for Wetness Jitter)** | ✖ |  |  |
| **Minimum (for Wetness Control)** | ✖ |  |  |
| **Mix Jitter** | ✖ |  |  |
| **Control (for Mix)** | ✖ |  |  |
| **Minimum (for Mix Control)** | ✖ |  |  |
|  |  |  |  |
| Brush Pose | **Tilt X** | ✖ |  |
| **Override Tilt X** | ✖ |  |  |
| **Tilt Y** | ✖ |  |  |
| **Override Tilt Y** | ✖ |  |  |
| **Rotation** | ✖ |  |  |
| **Override Rotation** | ✖ |  |  |
| **Pressure** | ✖ |  |  |
| **Override Pressure** | ✖ |  |  |
|  |  |  |  |
| Other | **Noise** | ✖ |  |
| **Wet Edges** | ✖ |  |  |
| **Build-up** | ✖ |  |  |
| **Smoothing** | ■ | Not directly matched, but can be handled via the [ Lazy Mouse](../../../../painting/lazy-mouse/lazy-mouse.md) setting. |  |
| **Protect Texture** | ✖ |  |  |
