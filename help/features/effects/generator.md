---
helpx_url: 'https://helpx.adobe.com/substance-3d-painter/features/effects/generator.html'
breadcrumb-title: ''
description: Learn how to use generator effects in Substance 3D Painter to create procedural textures and patterns automatically.
helpx_creative_field: ''
helpx_description: Painter > Features > Effects > Generator
helpx_experience_level: ''
helpx_learn_topic: ''
helpx_tags: ''
title: Generators
user-guide-description: ''
user-guide-title: ''
---

# Generators

Generators are substances that generate a mask or textures based on the mesh topology [using baked utility maps like Position, Curvature, and World Space Normal](../../baking/baking.md).

>[!NOTE]
>
> Most generators output monochrome (black-and-white) textures, making them most useful for creating masks that control a material layer. However, there is nothing preventing you from using a monochrome generator as a fill layer, or a full color generator as a mask.

To add a generator to a mask:

1. In the **Layers panel**, right-click the mask.
1. Select **Add generator**.
1. When the mask is selected, the generator appears under the layer in the **Layers panel**.
1. With the generator selected, in the **Properties panel** click the **Generator** button to select the specific generator to apply.

To add a generator to a layer:

1. Right-click the layer.
1. Select **Add generator**.
1. The generator appears under the layer in the **Layers panel**.
1. With the generator selected, in the **Properties panel** click the **Generator** button to select the specific generator to apply.

>[!NOTE]
>
> It is possible to apply generators, filters, or other effects to a given layer or to its mask. When you select a layer, its effects will be visible under the layer. To see the effects applied to the mask, select the mask rather than just the layer.

![](../../assets/generators/generator_spectrum.png)

Each generator has a set of parameters allowing you to fine-tune the resulting mask.\
To add custom generators in the shelf, see: [Adding content to the shelf](https://helpx.adobe.com/substance-3d/unlisted/documentation/spdoc/adding-content-to-the-shelf-142213317.html)

>[!NOTE]
>
> When creating a new substance in Substance 3D Designer, you can choose the **Painter Generator template** to get a good starting point for your new generator.
