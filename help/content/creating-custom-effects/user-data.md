---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/content/creating-custom-effects/user-data.html"
breadcrumb-title: ""
description: Learn how to use user data in custom effects for Substance 3D Painter to pass custom information to shader effects.
helpx_creative_field: ""
helpx_description: Painter > Content > Creating custom effects > User data
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: User data
user-guide-description: ""
user-guide-title: ""
---

# User data

This page describes custom properties (user data) that can be added on Substance graph to execute specific behaviors.  
The user data settings are usually applied to input or output nodes of a graph to indicate how the application should interpret them. This allows to request input of a graph to be in a certain way to apply effects is a known context (ex: requesting a specific color space) or to indicate how an output was made in case the application need to apply extra conversions afterward.

* Use data settings are defined as **key = value**
* Multiple settings are separated by a semicolon (  **;**  )

## Color space

The **colorspace** setting can be used to request Substance graph inputs with a specific color space or to define an output configured in a certain way. For example specifying the format of the normal map output.

Syntax example: **colorspace=$working**

Contexts overview:

* **Color button**: A color button widget in the properties of a Substance graph.
* **Graph input/output**: input or output node of a graph connected to a channel (ex: BaseColor).
* **Image input**: generic input of a graph, unrelated to specific channels.

>[!NOTE]
>
> With the introduction of color management, several behaviors related to color spaces setting have changed:
> 
> * The table below list first the color space settings compatible prior to version 8.1. The second section is exclusive to version 8.1 and newer.
> * Regarding the contexts in which the color space setting can be used, only since version 8.1 can color button define a color space. In previous versions they were assumed to be in display space (sRGB).
> 
> The **snorm** and **unorm** color space/transformations should not be mixed with GPU texture formats, their purpose are different.

| ColorSpace | Context availability | Description |
| --- | --- | --- |
| **auto** | Color button Graph input/output Image input | Default. The application decides the color space conversion to perform depending on the input node properties and the image plugged in the input. |
| **linear** | Color button Graph input/output Image input | Standard sRGB IEC 61966-2-1:1999 color space with a linear gamma/tone-curve. Only available with **Legacy** color management mode. |
| **srgb** | Color button Graph input/output Image input | Standard sRGB IEC 61966-2-1:1999 color space. Only available with **Legacy** color management mode. |
| **passthru** | Color button Graph input/output Image input | Deprecated. Interpreted as **linear** in Legacy color management mode and **raw** with OCIO/ACE. Should be replaced by **raw** instead. |
| **snorm** | Graph input/output Image input | Signed normalized. Request input image to be in range &#91;0, 1&#93;. For 8bit input images this means the middle value is 127. For floating image inputs the middle is 0.5 and does not perform any clamping. |
| **normalxyzright** | Graph input/output Image input | OpenGL normal map format. |
| **normalxyzleft** | Graph input/output Image input | DirectX normal map format. |
|  |  |  |
| **unorm** | Graph input/output Image input | Floating input, without range/clamping. |
| **data** | Color button Graph input/output Image input | Unsigned normalized or float. Non-color information. |
| **raw** | Color button Graph input/output Image input | No color transformations are applied when this setting is used. |
| **$standardsrgb** | Color button Graph input/output Image input | Standard sRGB IEC 61966-2-1:1999 color space. |
| **$working** | Color button Graph input/output Image input | Working color space, depends on the color management settings. Will be identical to data for non-color managed channels and mono-channel (stencil, alpha, mask) |
| **$raw** | Color button Graph input/output Image input | Alias for **raw**. |
| **$auto** | Color button Graph input/output Image input | Alias for **auto**. |

## Alpha mode

The **alpha** setting can be used to specify how the alpha of a color input or output (RGBA) is combined.

Syntax example: **alpha=premultiplied**

| Setting | Description |
| --- | --- |
| straight | Request or define the alpha as straight. |
| premultiplied | Request or define the alpha as pre-multiplied. |
| none | Passthrough, use the given alpha as-is. |

>[!NOTE]
>
> The channel **Opacity** is considered as **straight** by default.

## Image input default color

The default color of a Substance graph image input is black with its alpha set to 0. The **defaultcolor** setting allow to define a different value when the image input of a graph is empty

Floating values (range &#91;0, 1&#93;) or integer values (range &#91;0, 255&#93;) can be used to specify the color. Each component value is separated by a comma, while floating point value use a dot as the decimal separator. If a floating has not point it will be considered as an integer.

Syntax example:

* **defaultcolor=(1.0,0.5,0.0)**
* **defaultcolor=(0,128,255)**

## Image input padding

By default image inputs of a Substance graph don't have any padding, the area outside the UV island is usually filled with a uniform color for performance reasons. The padding setting can be used to request infinite dilation instead, which can be used for filters to avoid creating seams for example.

Syntax example: **p****adding=extend**

## Disable an output by default

When adding a substance into a slot (like the material slot of the tool of a fill layer), it is possible to specify via the metadata text field to not enable a specific channel :

* On a specific output node (like a material) :  **disable=(true)**
* On a generic output node (like a filter) :  **disable=(height,diffuse,specular)**

When loading the substance, this channel will not be enabled in the user interface and therefore will have no effect in the layer stack. The user can still enabled back the channel.

## Designate an output as a common mask/alpha

The output of a Substance graph can be used a shared alpha channel/mask on the other outputs.

There are two ways to do so:

* Create an ouput node with the identifier **channels\_Alpha**
* Or add the following userdata on a specific output node:  **IsChannelsAlpha=true**

Some conditions may apply:

* If an output node with the identifier **channels\_Alpha** exists and other outputs don't have the userdata, this node will be used as the channels mask.
* If an output has the userdata it will be used as the channels mask as long no **channels\_Alpha** node exists.
* If both a **channels\_Alpha** node and a node with the userdata exist, then the **channels\_Alpha** output node will be used first.
* If multiple nodes have the userdata, the first node found by the application will be used as the channels mask. The order in which the outputs are found is not guaranteed to the same as defined by the Substance graph.

>[!NOTE]
>
> This settings only applies to Substance graph used in **material mode**. It doesn't apply to filters, generator, etc.

## Set default blending mode for Material outputs

It is possible to define what the blending mode of a specific output in a Substance graph should be when drag and dropping materials from the Shelf into the viewport or layer stack.

* On a specific output node:  **blendingmode=normal**

List of supported blending modes:

* normal
* passthrough
* disable
* replace
* multiply
* divide
* inversedivide
* darken
* lighten
* lineardodge
* subtract
* inversesubtract
* difference
* exclusion
* signedaddition
* overlay
* screen
* linearburn
* colorburn
* colordodge
* softlight
* hardlight
* vividlight
* pinlight
* tint
* saturation
* color
* value
* normalcombine
* normaldetail
* normalinversedetail
