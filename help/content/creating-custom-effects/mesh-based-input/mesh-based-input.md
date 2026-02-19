---
title: "Mesh Based Input"
description: "Learn how to use mesh-based inputs in custom effects for Substance 3D Painter to create geometry-aware texture effects."
helpx_description: Painter > Content > Creating custom effects > Mesh Based Input
helpx_url: "https://helpx.adobe.com/substance-3d-painter/content/creating-custom-effects/mesh-based-input.html"
helpx_creative_field:
  - web
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - baking
  - pbr
  - blending
---




# Mesh Based Input

Mesh Based Input are texture provided by the engine of Substance 3D Painter extracted from the mesh inside the current project. These textures can be used to create advanced effects based on the mesh topology.

>[!NOTE]
>
> These Mesh information are based on the topology itself and don't take into account the Mesh map (baked textures).
> 
> The input provided by the engine is a 32 bits floating point texture which will be downscaled/clamped to the value of the input in the Substance graph.

| Mesh Information | Identifier | Usage | Description |
| --- | --- | --- | --- |
| *Position (RGB)* | **mesh\_position** | **meshPosition** | Retrieve a texture containing the vertex position. |
| *World Space Normal (RGB)* | **mesh\_world\_space\_normal** | **meshNormalWS** | Retrieve a texture containing the vertex normal in world space. |
| *World Space Tangent (RGB)* | **mesh\_world\_space\_tangent** | **meshTangentWS** | Retrieve a texture containing the vertex tangent in world space. |
| *World Space Bitangent (RGB)* | **mesh\_world\_space\_bitangent** | **meshBitangentWS** | Retrieve a texture containing the vertex bi-tangent (bi-normal) in world space. |
| *Texel Size (Grayscale)* | **mesh\_texel\_size** | **meshTexelSize** | Retrieve a texture containing the texel size (difference between pixel density and mesh UV). |
| *UV Mask (Grayscale)* | **mesh\_uv\_mask** | **meshUVMask** | Retrieve a texture as black (outside) and white (inside) mask of the mesh UV islands. |
