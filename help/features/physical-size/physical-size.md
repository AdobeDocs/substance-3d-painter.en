---
title: "Physical size"
description: "Learn how to set physical size in Substance 3D Painter to define real-world dimensions for accurate texture scaling."
helpx_description: Painter > Features > Physical size
helpx_url: "https://helpx.adobe.com/substance-3d-painter/features/physical-size.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - scaling
  - painting
  - pbr
---




# Physical size

![](banner-physicalsize-2.png)

The physical size is a property inside Substance materials that defines their real size. It can be used to accurately match the size and look of materials over 3D surfaces. Painter uses centimeters as the default internal unit.

To use physical size, apply a material that has this property with a value other than 0,0,0 then enable the physical size mode in fill layer (or effect) under UV transformation &gt; Scale.

For more information, see:

* **Physical size** parameters in [Fill projections](../../help/painting/fill-projections/fill-projections.md)
* **Grid** parameters in [Viewport settings](../../help/interface/display-settings/viewport-settings/viewport-settings.md)

>[!NOTE]
>
> * From Painter version 8.3, physical size is available for all types of Projections.
> * Most mesh file formats specify the unit used during mesh creation, this unit will be converted to centimeters automatically during import.
> * Some formats, like .obj, do not have unit information, so when a project is created using an .obj mesh, it will be measured in centimeters by default without any conversions.
