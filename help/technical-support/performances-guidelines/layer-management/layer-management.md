---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/performances-guidelines/layer-management.html"
breadcrumb-title: ""
description: Learn best practices for layer management in Substance 3D Painter to optimize performance and maintain organized projects.
helpx_creative_field: ""
helpx_description: Painter > Technical support > Performances guidelines > Layer management
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Layer management
user-guide-description: ""
user-guide-title: ""
---

# Layer management

Painter computes the layer stack from the bottom to the top. So, if you make changes to the top layer on the stack, Painter only needs to compute the changes of that layer. However, if you make a change to a layer at the bottom of the stack, Painter needs to compute all of the layers above that layer to calculate the final result.

There are various options you can use to decrease the performance cost of making changes to layers lower in the stack:

+++Use Geometry masks
Geometry masks are your best optimization tool. Whenever you can isolate a part of your mesh to work on, do so, either by masking layers or folders. Geometry masks work by isolating either by UDIM or by mesh part, so areas that are not in the mask are not processed, improving performance. As a bonus, you can also isolate those parts visually in the viewport for easier texturing.

You can [learn more about geometry masks with this tutorial](https://www.youtube.com/watch?v=TGASuIGSUns), or by [referring to the documentation](../../../interface/layer-stack/geometry-mask/geometry-mask.md).

+++

+++Hide layers
In order to avoid slowdowns when making changes at a lower level in the layer stack, you can hide layers above the edited layer until you have finished making your adjustments. Painter doesn't process hidden layers, so if all the layers above your layer are hidden, it's as if you're editing the top layer in the stack. This way, the layers above will only be computed once, when you unhide them, rather than after every change you make.

+++

+++Disable layers
Just like hiding layers, the disable blend mode will prevent layers from being calculated. It can be helpful to set low impact layers to the disable blend mode while modifying areas where they are unimportant.

+++

+++Use folders
Try to group layers whenever possible, as folders act like an invisible caching point. If you are making any changes below or above a given folder, the layers inside the folder won't all be recalculated individually, but rather their group result will be recalculated.

+++

+++Limit the use of filters near the top of the layer stack
Filters can be expensive. If it's necessary to use a filter near the top of the layer stack, use geometry masks to decrease their performance cost.

+++

+++Limit the use of passthrough blending mode
Passthrough is frequently used with filters or brush stroke layers. It is a costly blending mode because it looks at all the layers underneath and transforms their result, instead of overriding the result like normal blending mode. Whenever using passthrough, try to combine it with Geometry masks and folders to minimize the performance impact.

+++

+++Keep projection depth small
With any tool or mode that has a Projection depth setting (warp, planar, path, etc), keep the Projection depth value as small as possible. The further the Projection depth extends, the less performant it is.

+++

+++Be careful with brushes that have dynamic strokes
Brushes and tools with an orange tag have a dynamic parameter. This dynamic parameter can be set to "Unlimited", which means that every stamp in a stroke will be unique. This can have a substantial performance impact if using hundreds or thousands of brush strokes. In most cases, it's difficult to tell the difference after 16-32 variations, so generally speaking going beyond that is unlikely to have much visual impact.

[Learn more about dynamic strokes in the documentation.](../../../painting/dynamic-strokes/dynamic-strokes.md)

+++

+++Work at a lower texture resolution
Decreasing document resolution is the fastest way to improve performance. Doubling the resolution means a 4 times larger map, so going from 1k to 2k means up to a 4 times increase in performance cost. As a result, it's often useful to work at a lower resolution for as long as possible.

+++

+++Set Decals to Planar projection mode
The default decal mode is Warp, but unless you are actually deforming the decal by moving its points, switching it to Planar mode is much less costly.

+++
