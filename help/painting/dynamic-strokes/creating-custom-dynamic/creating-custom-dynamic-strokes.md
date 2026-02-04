---
title: "Creating Custom Dynamic Strokes | Substance 3D Painter"
description: "Painter > Painting > Dynamic strokes > Creating Custom Dynamic Strokes"
---

# Creating Custom Dynamic Strokes

In order to create custom Dynamic Strokes, two options are available:

* Using an existing Substance resource to create a new brush/tool preset
* Create a new Substance resource from scratch (requires  [Substance 3D Designer](https://substance3d.adobe.com/display/SDDOC/Substance+Designer)  ).

It is also recommended to read the [Dynamic Stroke Performances](../dynamic-stroke-per/dynamic-stroke-performances.md) before creating custom Substance files to avoid any culprits.

## Reusing existing resource

Creating new Dynamic Strokes from scratch can be difficult. Using existing resources, tweaking them, and then saving them as new presets can be a good enough starting point.

Find compatible resources in the Shelf that may fit your needs, then check out our page about [Presets](../../presets/presets.md).

## Creating custom Substance files for Dynamic Strokes

Below is a list of the supported parameters for Dynamic Strokes in Substance graphs.

| Variable Identifier | Description |
| --- | --- |
| <b>Random Seed</b> | If a Substance file is cooked with the Random Seed exposed, it will be controllable with the Dynamic Stroke feature. |
| <b>stampIndex</b> | <b>Integer1</b> Will be fed by Substance 3D Painter when painting the brush stroke. The min and max value have no effect, Substance 3D Painter will ignore them. |
| <b>stampCycleCount</b> | <b>Integer1</b> Painter will read the parameter default, min and max value to expose the Stamp Cycle Count parameter. This parameter controls how many unique Substance variations will be created. |
| <b>$time</b> | <b>Float1</b> Will be fed by Substance 3D Painter when painting the brush stroke based on the elapsed painting time (per stroke). This property can generate a lot of Substance variations and can therefor impact performance. |
| <b>strokeSpacing</b> | <b>float1</b> The current spacing value for the whole stroke painted. |
| <b>strokeSize</b> | <b>float1</b> The current size value for the whole stroke painted. |
| <b>stampStrokePosition</b> | <b>integer1</b> Can be disabled using isstrokepositionactive user tag.  Painter will be the value 0 (middle), 1 (start) or 2 (end) to specify if the current stamp location inside the stroke. This allow to create a beginning and an end. The end property is only available with the Path tool. |
| <b>distanceAlongCurve</b> | <b>float1</b> The current distance at the given stamp along a Path. This property can generate a lot of Substance variations and can therefor impact performance. Can be disabled with the <b>iscurvedistanceactive</b> user tag. |
| <b>distanceMaxCurve</b> | <b>float1</b> The total length of a Path made with the path tool. Can be disabled with the <b>iscurvedistanceactive</b> user tag. |
