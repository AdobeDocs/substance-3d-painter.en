---
title: "Projects are really big"
description: ""
helpx_description: "Painter > Technical support > Workflow Issues > Project Issues > Projects are really big"
---

# Projects are really big

Substance 3D Painter project can be really big and use a lot of disk space. This page explains why and how to mitigate it.

## What kind of resource are stored in a project ?

Every asset or resource used during the texturing is stored into the project file, this include:

* **Source Mesh**  (not the original file, but a processed one)
* **Baked Mesh maps**
* **Materials**  (like Substance Materials)
* **Bitmaps**  or other resources used by any layers/preset/brush stroke.

The high-poly meshes are not included in the project. They are just linked.

## Why does a project store so many resources ?

Storing all the resources used makes a project completely autonomous and easily movable from one computer to one another without breaking it. The main downside is the potentially large file footprint on the disk.

The decision to have everything embedded into the project file comes from the fact that everything is non destructive. It means that the project "rebuilds" itself when it is reopened. If a single brush or material is missing from the shelf, the project could break and would not be able to correctly regenerate. Storing a duplicate of the resource ensure that the project can still be restored as it was saved.

## Is there a way to reduce the size of a project ?

There are a few ways to reduce the size of a project:

### Clean unused resources

When using many resource in project, Substance 3D Painter copy them. For example if you used an alpha to paint something. If you later delete the layer when the alpha was painted, Substance 3D Painter doesn't automatically remove the resource.

To remove unused resource, use the  **Clean**  action from the  [File menu](https://substance3d.adobe.com/display/DRAFTPAINTER/File+menu)  . Then save the project (this will trigger the actual removal of the resource).

Resource that are still used in a project cannot be removed. This means disabled Texture Set still reference resources and prevent them from being deleted. To avoid that, remove disabled Texture Sets in the [ Texture Set reassignment window](../../../../interface/texture-set/texture-set-reassignment/texture-set-reassignment.md).

### Reduce the Texture Set resolution

When a project is saved, the final result of the layer stack of a Texture Set is saved in the project. This allows to preserve a preview in in the viewport when the project is reopened without having to recompute the Texture Set. However the bigger the Texture set resolution is, the bigger the preview cache will be.

To reduce the cache footprint simply change the resolution to a lower number like 512 for example. Since Substance 3D Painter is non-destructive this resolution can be changed back up later without loosing quality.

### Compact the project

Saving a project incrementally (via CTRL+S) a lot can fragment the project file archive. While not a critical issue, this can introduce empty space in the project file which can increase the size.

Use the "Save and Compact" function in the [ File Menu](../../../../interface/main-menu/file-menu/file-menu.md) to re-save the project and remove wasted empty space. This save action will be longer than a regular save but can significantly reduce the file footprint.

### Reduce the baked Mesh maps size

In general, the biggest culprit and reason why a project take so much space on the disk is because the baked Mesh Maps are many and big themselves.

To reduce the Mesh Maps size they are a few things that can be done :

* *Use a lower baking resolution.*    
  While the Normal map may benefit to be baked in 4K, this might not be the case for the Position map which is usually just about colored gradients. Bake in two pass at two different resolutions to mix different file size.
* *Export the textures and manually reduce their footprint.*    
  By default Substance 3D Painter bake all the textures as RGBA images in 16bits, this include the grayscale bakers such as the Ambient Occlusion.   
    
  To reduce the bake textures foorprint use this step by step :
  1. Disable the "Apply Diffusion" setting in the Baker Window
  1. Set the "Dilation With" to a reasonable value (32 pixels for a 2048 resolution for example)
  1. Bake all your Textures at the same resolution
  1. Export the baked textures with the export preset "Mesh Maps" as 16bits PNG with the padding set to "No padding (passthrough)"
  1. Open each map in a photo editing software or Substance 3D Designer
  1. Reduce the resolution for the textures for which it seems fitted. Make sure to switch the Ambient Occlusion, Curvature and Thickness from color to grayscale.
  1. Save the new texture versions as 16bits PNG.
  1. Re-import the textures and replace them over the original bake textures in the Texture Set settings.
  1. Use the Clean action in the File menu to remove the old Mesh Maps.
  1. Use the Save and Compact action in the File menu to compress the project file.  
  After all these steps, the project footprint should be significantly reduced.

It is important that the Mesh maps remains at least 16bit textures. While 8bit textures may have a smaller footprint, they will introduce artifacts in Smart Materials and Mask Generators. We recommend PNG because it's a lossless compression format, meaning it will still compress the textures without introducing artifacts and it also support 16bits.
