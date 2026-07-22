---
helpx_url: 'https://helpx.adobe.com/substance-3d-painter/interface/project-configuration.html'
breadcrumb-title: ''
description: 'Learn how to configure project settings in Substance 3D Painter to set up texture resolution, channels, and project properties.'
helpx_creative_field: ''
helpx_description: Painter > Interface > Project configuration
helpx_experience_level: ''
helpx_learn_topic: ''
helpx_tags: ''
title: Project configuration
user-guide-description: ''
user-guide-title: ''
---

# Project configuration

![](../assets/project-configuration-full.png)

The Project configuration window has controls to modify project settings. Project settings are generally set when creating a new project, but sometimes it may be necessary to make changes to these settings later in the project.

## 3D mesh

If changes have been made to the 3D mesh or mesh file, you can reimport the mesh while still maintaining the other project data. Check **Reimport mesh** and ensure that the correct file is being imported.

Reimporting the mesh is often useful when you need to:

* Update the 3D model topology
* Update the UVs
* Add or Remove [Texture Sets](texture-set/texture-set.md)

| **Parameter** | **Description** |
| --- | --- |
| **3D mesh** | Indicates the path to the 3D model file. Use the **Select button** to change the source file for the project. |
| **Reimport mesh** | If enabled, the mesh file will be re-imported when clicking OK at the bottom of the interface. This parameter is automatically checked if the Select button is used to specify a mesh file that is different from the original mesh file. |

>[!NOTE]
>
> If the material ids change or are renamed when reimporting the project mesh, the previous Texture Sets in the project can become disabled, giving the appearance of missing textures. This can be fixed with the [Reassignment Window](texture-set/texture-set-reassignment.md) from the **Texture Set List**.

## Project Settings

This section controls several settings related to the project:

<table>
  <tr>
    <th><em>Setting</em></th>
    <th><em>Description</em></th>
  </tr>
  <tr>
    <td><strong>Normal Map Format</strong></td>
    <td>Defines the format of the normal map used for the mesh in the viewport. This parameter only affects the <a href="shader-settings/shader-settings.md">shaders</a> in the viewport and mesh maps in the <a href="../baking/baking.md">bakers</a>. The layer stack is independent. Recommended value for common applications:<br><br><ul><li><strong>Unity</strong>: OpenGL</li><li><strong>Unreal Engine</strong>: DirectX</li><li><strong>Maya</strong>: OpenGL</li><li><strong>3DS Max</strong>: DirectX</li><li><strong>Blender</strong>: OpenGL</li></ul></td>
  </tr>
  <tr>
    <td><strong>Compute Tangent Space Per Fragment</strong></td>
    <td>Determines how to compute and display normal maps in the viewport for shading and lighting. If enabled, the tangent and binormals of the mesh will be computed per pixel instead of per vertex.<br>Recommended value for common applications:<br><br><ul><li><strong>Unity</strong>: Disabled (Enabled if using HDRP)</li><li><strong>Unreal Engine</strong>: Enabled</li></ul></td>
  </tr>
</table>

>[!NOTE]
>
> Changing the normal format or the tangent computation requires re-baking the mesh maps to ensure that the appearance in the viewports is correct.

### File type-specific settings

When a USD mesh format is selected, other file type-specific settings become available.

![](../assets/image2023-1-30-11-16-6.png){width="473px"}

<table>
  <tr>
    <th><em>Parameter</em></th>
    <th><em>Description</em></th>
  </tr>
  <tr>
    <td><strong>Scope and variants</strong></td>
    <td>Select a specific part of a USD file. By default, it is set to 'Root', which means the entire USD file will be used in the Painter project. <strong>Change...</strong> opens a new window that displays the contents of the USD. If variants are detected, you can select a specific variant to load into the project.<br><br>Note:<br><ul><li>Only the modeling variant selection will have any impact.</li><li>Variants nested within variants are not currently detected.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Subdivision level</strong></td>
    <td>Applies to geometry that has subdivision. Specify how much to subdivide your mesh for texturing in Painter. If subdivision is explicitly set to 'none' within the USD file, this setting is grayed out. Subdivision is applied after UV unwrapping, so it would not alter the shape of the mesh's UVs.</td>
  </tr>
  <tr>
    <td><strong>Frame</strong></td>
    <td>Applies to USDs in which animation is detected. Select the frame that will be loaded into the Painter project. If there is no animation in the selected USD file, this setting is grayed out.</td>
  </tr>
</table>

## UV Tiles settings

This section has controls to toggle the use of UDIMs in the project. It is not possible to change these settings after the project has been created, but you can view the settings for the project here. For more information see the [UV Tiles documentation](../features/uv-tiles/uv-tiles.md).

## Import settings

These settings control how the selected mesh will be imported:

| *Setting* | *Description* |
| --- | --- |
| **Import Cameras** | If enabled, cameras present in the mesh file will also be imported and available in the 3D viewport. |
| **Preserve strokes positions on mesh** | This setting controls how brush strokes will be recomputed after importing a new 3D mesh. It is recommended to keep this setting enabled in most cases. For more details see the [UV Reprojection](../features/uv-reprojection.md) documentation. |
| **Auto-Unwrap** | Automatic UV Unwrapping. Click on the Option button to configure the process. For more information see the [Automatic UV Unwrapping documentation](../features/automatic-uv-unwrapping.md). |

### Physical size settings

Adjust the [Physical size](../features/physical-size.md) of the imported mesh.

| *Setting* | *Description* |
| --- | --- |
| **Use mesh file’s internal unit scale** | If the mesh was created with physically accurate measurements, leave this selected to maintain the same physical size in Painter. |
| **Custom unit scale** | If the mesh was not created with physical size in mind, use this option to customize the size of the mesh. You will need to know the desired physical size and the size in units of the imported mesh to determine this value. |
| **Switch fill layer scaling to Physical size when assigning materials** | When enabled, fill layers and effects will automatically switch the scale method to Physical size when assigning a material that has Physical size properties. |

### Color management settings

This section controls the settings regarding how to convert colors. For more information, see the [Color management](../features/color-management/color-management.md) documentation.
