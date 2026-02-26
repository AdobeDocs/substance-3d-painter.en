---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/content/importing-assets/adding-content-on-the-hard-drive.html"
breadcrumb-title: ""
description: Learn how to add content from your hard drive to Substance 3D Painter to expand your resource library with local files.
helpx_creative_field: ""
helpx_description: Painter > Content > Importing assets > Adding content on the hard drive
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Adding content on the hard drive
user-guide-description: ""
user-guide-title: ""
---

# Adding content on the hard drive

It is possible to add resources to your libraries by placing new content directly on the hard drive at the right location.  
  
A default folder for user assets is provided by default where you can add your new content, either through the application interface or by manually dropping it in the following location. This default library is also used when creating new presets such as brushes, tools, smart materials, etc. For more information, see the [Presets](../../../painting/presets/presets.md) documentation.

## Where to put assets ?

Below are the locations of the default **Your Assets** library where your own custom content is created by default:

<table data-preserve-html="true" style="width: 100.0%;"><colgroup> <col style="width: 15.0%;"/> <col style="width: 15.0%;"/> <col style="width: 70.0%;"/> </colgroup><tbody><tr><th>Platform</th><th>Version</th><th>Path</th></tr><tr><td rowspan="2"><strong>Windows</strong></td><td><strong>7.2</strong> or newer</td><td colspan="1">C:&#92;Users&#92;username&#92;Documents&#92;Adobe&#92;Adobe Substance 3D Painter</td></tr><tr><td colspan="1">Legacy</td><td colspan="1">C:&#92;Users&#92;username&#92;Documents&#92;Allegorithmic&#92;Substance Painter</td></tr><tr><td rowspan="2"><strong>Mac</strong></td><td colspan="1"><strong>7.2</strong> or newer</td><td colspan="1">/Users/username/Documents/Adobe/Adobe Substance 3D Painter</td></tr><tr><td colspan="1">Legacy</td><td colspan="1">/Users/username/Documents/Allegorithmic/Substance Painter</td></tr><tr><td rowspan="2"><strong>Linux</strong></td><td colspan="1"><strong>7.2</strong> or newer</td><td colspan="1">/home/username/Documents/Adobe/Adobe Substance 3D Painter</td></tr><tr><td>Legacy</td><td colspan="1">/home/username/Documents/Allegorithmic/Substance Painter</td></tr></tbody></table>

>[!WARNING]
>
> The **Starter assets** shipped with the application are located within the installation folder and are replaced in each new version. We do not recommend putting personal content in this location, as it will be **erased with every update** and may even cause read/write permission issues.   
> It is best to use the **Your assets** location or another custom location. For more information on how to add a custom library location, see [Adding a new library](../../../interface/assets/adding-a-new-library/adding-a-new-library.md).

## File formats and usages

You can import different types of files to your Substance 3D Painter library. Placing them in the designated folders (such as *alphas*, *colorluts*, *effects*...) will assign a type of usage to the asset, so it is important to choose the right folder when adding new content. Note that if you add a custom library location, it will automatically create the appropriate folders at that location.

| *File format* | *Usage* | *Folder* |
| --- | --- | --- |
| **SBSAR** | Substance Material | assets / Materials |
| **SBSAR** | Filters | assets / Effects |
| **SBSAR** | Generators | assets / Generators |
| **PNG, TGA, JPEG, etc.** | Texture or Alpha | assets / Textures **or** Shelf / Alphas |
| **HDR, EXR** | Environment or Color Lut | assets / Environments **or** Shelf / Colorlut |
| **GLSL** | Shader | assets / Shaders |
| **SPPR** | Brush Preset | assets / Presets / Brush |
| **SPPR** | Particle Preset | assets / Preset / Particles |
| **SPPR** | Material Preset | assets / Presets / Materials **or** assets / Materials |
| **SPPR** | Tool preset | assets / Preset / Tools |
| **SPSM** | Smart Material | assets / Smart-materials |
| **SPMSK** | Smart Mask | assets / Smart-masks |
| **SPEXP** | Export Preset | Shelf / Export-presets |

>[!NOTE]
>
> As of version 7.2.0, custom folders and categories can be used in a library. They will be accessible in the Assets window via [Filter by path](../../../interface/assets/filter-by-path/filter-by-path.md) or [Breadcrumbs](https://helpx.adobe.com/substance-3d/unlisted/documentation/spdoc/navigating-in-the-shelf-147095659.html).

>[!WARNING]
>
> **SBS** (not SBSAR) files can't be used directly, they need to be exported as SBSAR from Substance 3D Designer.
