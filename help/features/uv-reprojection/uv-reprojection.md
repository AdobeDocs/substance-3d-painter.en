---
title: "UV Reprojection"
description: "Learn how to use UV reprojection in Substance 3D Painter to transfer textures between different UV layouts."
helpx_description: Painter > Features > UV Reprojection
helpx_url: "https://helpx.adobe.com/substance-3d-painter/features/uv-reprojection.html"
helpx_creative_field:
  - video
  - 3d-immersive
  - painting-illustration
helpx_experience_level:
  - any
helpx_learn_topic:
  - projection
  - distortions
  - asset-warp
---




# UV Reprojection

UV Reprojection is an automatic process that happens when you changed the texture resolution or that you import a new mesh.   
 If you load a new mesh in your document (via the  [Project Configuration](https://substance3d.adobe.com/display/draftpainter/project%20configuration)  window ), all your actions will be reprojected on that new mesh. It doesn't matter if the topology changed (as long it's similar) or that the UVs have changed. Since the reprojection works by recomputing all the layers and brush strokes, it can take a bit of time (especially at high texture resolutions).

Painting in 2D View

Since every stroke made in the 2D view is performed in the UV space, there is no way to reproject it properly in case the UV of the mesh change dramatically after a reimport. The best way to make your project reprojection proof is to rely on masking by an ID map and other type of selection and painting instead the 3D View.

## How does the re-projection work ?

Substance 3D Painter saves its data in 3D in world space to keep everything non destructive. That means that when reimporting a mesh, Substance 3D Painter tries to paint where the mesh was before the reimport, it has no way to know where some pieces could have moved.

Also when Substance 3D Painter import a mesh, it computes it's bounding box to register the space and define a relative scale for the tools (paint brush, particles and so on). This Bounding Box is 1 unit wide on every axis. When you import a new mesh, if you uncheck the "preserve stroke" we re-normalize the bounding box to the new mesh. Therefore if your mesh changed dramatically in size, the strokes can move. If you check "preserve strokes" however, we scale the original bounding box to the new one in order to reproject properly the brush strokes.

>[!WARNING]
>
> Changing units of your 3D mesh can lead to UV reprojection not working; the old and new mesh, even though topology has not changed, can be interpreted as vastly different scales. Ideally you avoid changing your unit setup, as it can be difficult to fix.
