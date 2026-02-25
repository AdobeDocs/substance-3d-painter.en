---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/features/uv-tiles/image-sequence.html"
breadcrumb-title: ""
description: Learn how to use image sequences with UV tiles in Substance 3D Painter for animated texture workflows.
helpx_creative_field: ""
helpx_description: Painter > Features > UV Tiles > Image Sequence
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Image Sequence
user-guide-description: ""
user-guide-title: ""
---


# Image Sequence

Image sequences are a collection of images that are grouped as a single resource in the Shelf. Images are grouped together based on a specific pattern in their filenames.

## How to import images as a sequence

When [importing an image file](https://helpx.adobe.com/substance-3d/unlisted/documentation/spdoc/adding-content-via-the-import-window-151584824.html), if the filename matches a specific pattern it will be imported automatically as a sequence. If additional images sit next to the imported file, they will be taken into account as well. It is therefore not necessary to import all the files from a sequence manually, picking the first file is enough.

Filename matching examples:

The following filenames will successfully import an image sequence because they can recognize that the last part of the filename is referring to a UDIM number 1032:

* file\_22.1032.jpg
* file\_22-223.1032.jpg
* file\_22-223-1032.jpg
* file\_22-223\_1032.jpg

The following filenames will not be imported as an image sequence because they are not structured correctly:

* file\_22-2232032.jpg
* file\_22-223PM2032.jpg
* file\_22-223-0032.jpg
* file\_22-223\_Rec2020.jpg

The filename matching is based on the following regular expression:

```

 ^(.+?)[\.\-\_](?
```


## How to use image sequences

Image Sequences can be loaded into any resource slot in the interface like any other resource. However in some cases they may require additional settings to be used properly.

In [Fill layers](../../../painting/fill-projections/fill-projections.md) (and fill effects), make sure that the projection mode is set to **Fill (Match Per UV Tile)** to ensure that each image from the sequence is assigned to the right [UV Tile](../../../features/uv-tiles/uv-tiles.md) in the Texture Set.
