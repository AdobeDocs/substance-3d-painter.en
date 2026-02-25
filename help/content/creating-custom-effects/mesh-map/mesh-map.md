---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/content/creating-custom-effects/mesh-map.html"
breadcrumb-title: ""
description: Learn how to use mesh maps in custom effects for Substance 3D Painter to access geometry-based texture information.
helpx_creative_field: ""
helpx_description: Painter > Content > Creating custom effects > Mesh Map
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Mesh Map
user-guide-description: ""
user-guide-title: ""
---


# Mesh Map

To automatically connect mesh maps (baked textures) when an effect is added on a layer, a specific naming convention must be followed.

>[!NOTE]
>
> It is possible to use either the **usage** or the **identifier** in an input node (the usage has the priority).

Here is the naming convention for each mesh map:

| Mesh map | Usage | Identifier |
| --- | --- | --- |
| *Ambient occlusion* | **ambientOcclusionBase** | **ambient\_occlusion** |
| *ID* | **id** | **id** |
| *Curvature* | **curvature** | **curvature** |
| *Normal* | **normalBase** | **normal\_base** |
| *World space normals* | **normalWS** | **world\_space\_normals** |
| *Position* | **position** | **position** |
| *Thickness* | **thickness** | **thickness** |
| *Height* | **heightBase** | **height\_base** |
| *Bent Normals* | **bentNormalsBase** | **bent\_normals\_base** |
| *Opacity* | **opacityBase** | **opacity\_base** |
