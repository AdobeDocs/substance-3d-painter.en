---
title: "Creating Custom Dynamic Strokes"
description: "Learn how to create custom dynamic strokes in Substance 3D Painter to design unique brush stroke behaviors and effects."
helpx_description: Painter > Painting > Dynamic strokes > Creating Custom Dynamic Strokes
helpx_url: "https://helpx.adobe.com/substance-3d-painter/painting/dynamic-strokes/creating-custom-dynamic-strokes.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - brushes
  - painting
  - drawing
---




# Creating Custom Dynamic Strokes

In order to create custom Dynamic Strokes, two options are available:

* Using an existing Substance resource to create a new brush/tool preset
* Create a new Substance resource from scratch (requires  [Substance 3D Designer](https://substance3d.adobe.com/display/SDDOC/Substance+Designer)  ).

It is also recommended to read the [Dynamic Stroke Performances](../../../help/painting/dynamic-strokes/dynamic-stroke-per/dynamic-stroke-performances.md) before creating custom Substance files to avoid any culprits.

## Reusing existing resource

Creating new Dynamic Strokes from scratch can be difficult. Using existing resources, tweaking them, and then saving them as new presets can be a good enough starting point.

Find compatible resources in the Shelf that may fit your needs, then check out our page about [Presets](../../../help/painting/presets/presets.md).

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
| <b>stampStrokePosition</b> | <b>integer1</b> Used to specify the begin/start of a stroke. End value is only available on path stroke, not via manual painting. Possible value:<ul data-preserve-html="true"> <li data-preserve-html="true">0 = middle</li> <li data-preserve-html="true">1 = start</li> <li data-preserve-html="true">2 = end</li> </ul>Can be disabled using isstrokepositionactive user tag. |
| <b>distanceAlongCurve</b> | <b>float1</b> The current distance at the given stamp along a Path. This property can generate a lot of Substance variations and can therefor impact performance. Can be disabled with the <b>iscurvedistanceactive</b> user tag. |
| <b>distanceMaxCurve</b> | <b>float1</b> The total length of a Path made with the path tool. Can be disabled with the <b>iscurvedistanceactive</b> user tag. |
| <b>pathCorner</b> | <b>integer1</b> Indicate which type of corner a Ribbon is using. Possible value:<ul data-preserve-html="true"> <li data-preserve-html="true">0 = No corner</li> <li data-preserve-html="true">1 = Left corner</li> <li data-preserve-html="true">2 = Right corner</li> </ul> |
| <b>pathCornerAngle</b> | <b>float</b> Angle (in radian) of the corner on a Ribbon path. Can be used to compensate or adjust the look of a corner based on a precise angle value. |
| <b>patchLengthOnCurve</b> | <b>float</b> Size of a section (patch) on a Ribbon path. Combined with <b>distanceAlongCurve</b> and <b>distanceMaxCurve</b> it can be used to normalize the size of a patch for example. |
