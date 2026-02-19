---
title: "Generic filter"
description: "Learn how to create generic filter effects for Substance 3D Painter to apply custom image processing and texture filters."
helpx_description: Painter > Content > Creating custom effects > Generic filter
helpx_url: "https://helpx.adobe.com/substance-3d-painter/content/creating-custom-effects/generic-filter.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - effects
  - creative-effects
  - appearance
---




# Generic filter

A generic effect will be applied on all the document channels, including opacity. A generic filter can be :

* **grayscale**, it will be applied to each component (R, G, B and A) of each channel (basecolor, metallic, roughness and so on)
* **color**, it will be applied on colored channel as-is, or converted to grayscale internally to affect grayscale channels

The input node of the effect must have the **identifier** or **usage** defined **input** and its output node must have **output**. Note that **color** based fitlers can't be used on the mask of a layer, only **grayscale** fitlers will be compatible.

>[!NOTE]
>
> It is possible to use either the **usage** or the **identifier** in an input node (the usage has the priority).

Example :

![](generic-filter.png)![](generic-rgba.png){width="575px"}
