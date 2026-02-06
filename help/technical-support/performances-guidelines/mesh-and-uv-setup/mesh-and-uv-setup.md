---
title: "Mesh and UV setup"
description: ""
helpx_description: "Painter > Technical support > Performances guidelines > Mesh and UV setup"
---

# Mesh and UV setup

Taking a few minutes to prepare your mesh for Painter can make the texturing process faster and easier.

+++High polycount models
There is no specific benchmark for polycount that Painter can handle, as it largely depends on machine specifications, Texture Set assignment, and layer stack properties, but under 10 million polys should be handled fine if the layer stack optimizations are taken into account.

+++

+++Low polycount models
There is such a thing as too low poly. This is because the texture engine uses the Polygons to know which part of the mesh should be rendered to compute the brush strokes. Meshes with a very low Polycount can be fully re-rendered even with tiny brush strokes which can overwork the GPU unnecessarily.

For example, if texturing a single quad plane, it is better to subdivide the mesh, especially when hand painting with a lot of strokes, as information is spread over more vertices.

+++

+++Divide textures across multiple texture sets
It is best to split larger meshes with more complex material assignments into several Texture Sets. Texture sets allow you to assign different settings per Texture Set, like resolution and shader properties. For example, if only a part of the mesh uses translucency or SSS, it is best to assign another Texture Set and a different shader instance to that part. That way, these more complex properties don't have to be calculated where they are not used.

+++

+++Keep UV islands close together
Try to keep UV islands that are neighbors in 3D space close together. This applies both to UDIM layout and classic UV space layout. If they have shared paint strokes or texturing, it is easier to calculate them when they are huddled in the same area of the UV space, rather than if they are at opposing ends.

The texture engine works by dividing a texture into smaller chunks to speed up computation. This means that each stroke only updates the chunks that need to be changed, instead of updating the entire texture with every stroke. By keeping neighbouring UV islands close to each other, it minimizes the number of chunks that will be affected by a single stroke.

+++

+++Avoid having too many objects
Performance should remain comfortable when importing a mesh that has fewer than 8000 sub-objects. Going over this limit can impact the viewport and painting performance. If this limit is reached, we recommended merging objects together to reduce the rendering overhead.

+++
