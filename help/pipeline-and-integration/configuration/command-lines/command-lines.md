---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/pipeline-and-integration/configuration/command-lines.html"
breadcrumb-title: ""
description: Learn how to use command line arguments with Substance 3D Painter for automation, scripting, and pipeline integration.
helpx_creative_field: ""
helpx_description: Painter > Pipeline and integration > Configuration > Command lines
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Command lines
user-guide-description: ""
user-guide-title: ""
---

# Command lines

This page list several command lines that can be used when launching the application to create or open projects for example.  
 These command lines can be used as follow:

```

"Adobe Substance 3D Painter.exe" --command [option] 
```


## List of commands

| Command | Description |
| --- | --- |
| **--help**  **-?**   **-h** | Display information about which command line are available and how to use them. |
| **--version**  **-v** | Display the current version of Substance 3D Painter. |
| **--mesh** | Mesh to load in a project.Example:  ``` // Create a new project with a specific mesh   "Adobe Substance 3D Painter.exe" --mesh "E:/MymeshFolder/MyMesh.obj"       // Update a mesh inside an existing project   "Adobe Substance 3D Painter.exe" --mesh "E:/MymeshFolder/MyMesh.obj" "E:/MyMeshFolder/Project.spp"  ``` |
| **--mesh-map** | Baked maps associated with the mesh (AO, Normal, Curvature). Can be specified multiple times. Nomenclature : TextureSetName\_AdditionalMapSlot<ul data-preserve-html="true"> <li data-preserve-html="true">Ambient occlusion = <strong> <em> ambient&#95;occlusion </em> </strong></li> <li data-preserve-html="true">Curvature = <strong> <em> curvature </em> </strong></li> <li data-preserve-html="true">Normal = <strong> <em> normal&#95;base </em> </strong></li> <li data-preserve-html="true">World Space Normal = <strong> <em> world&#95;space&#95;normals </em> </strong></li> <li data-preserve-html="true">Position = <strong> <em> position </em> </strong></li> <li data-preserve-html="true">Thickness = <strong> <em> thickness </em> </strong></li> <li data-preserve-html="true">ID = <em> <strong> id </strong> </em></li> </ul>Example:  ``` "Adobe Substance 3D Painter.exe" --mesh "E:/MyMeshFolder/MyMesh.obj" --mesh-map " E:/MyMeshFolder/DefaultMaterial_ambient_occlusion.png"  ``` |
| **--split-by-udim** | Create a texture set per UDIM tile. |
| **--export-path** | Default export path where the outputs of the project will be exported. |
| **--vram-budget** | Override the video memory (VRAM) budget defined by Substance 3D Painter engine. "Amount" is in megabytes.    Example:  ``` // Set the VRam budget to 2GB   "Adobe Substance 3D Painter.exe" --vram-budget 2048  ``` |
| **--disable-version-checking** | Don't check if a new version of the application is available when starting up |
| **--enable-remote-scripting** | Allow to run scripting commands from outside the application. See [Remote control with scripting](../../../scripting-and-development/scripts-and-plugins/remote-control-with-scr/remote-control-with-scripting.md) for more information. |
