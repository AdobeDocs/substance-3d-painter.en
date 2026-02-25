---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/baking/mesh-map-settings.html"
breadcrumb-title: ""
description: Learn how to configure mesh map settings in Substance 3D Painter to control baking parameters and output quality.
helpx_creative_field: ""
helpx_description: Substance 3D Painter
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Mesh map settings
user-guide-description: ""
user-guide-title: ""
---


# Mesh map settings

<b>The Mesh map settings panel</b> is available in Baking mode, and has controls to prepare your mesh for baking. To adjust mesh map settings for a given map, select the map in the <b>Mesh map bakers panel</b>. Each Mesh map can have different settings available. A collection of <b>Common settings </b>shared by all mesh maps is available at the top of the Mesh Map Bakers panel.

Any settings that are shared across mesh maps will appear on the Common settings page, rather than on each individual mesh map.

## Common settings

The Common settings page holds controls that affect how all mesh maps are baked.

### Output settings

| Setting | Function |
| --- | --- |
| Output size | Define the X and Y resolution of generated mesh maps. Click the lock to allow for non-square resolutions. |
| Dilation width | Adjust how far the baked information extends beyond the boundaries of UV islands. |
| Apply diffusion | Enable this box to apply diffusion to the edges of generated information. |

### High-poly parameters

| Setting | Function |
| --- | --- |
| Use Low poly mesh as high poly mesh | Enable this setting to bake maps based on your project mesh. |
| High definition meshes | Add high poly meshes to your project to make from a high poly mesh onto the low poly mesh in your project. Multiple meshes can be imported. |
| Cage | Determine how the baking cage is generated.<ul data-preserve-html="true"> <li data-preserve-html="true">Distance based: Inflate the vertices away from the mesh a uniform distance across the model to create a cage.</li> <li data-preserve-html="true">Automatic (experimental): Painter will analyse your mesh and generate a cage automatically, trying to keep the cage close to the surface without creating intersections for best results.</li> <li data-preserve-html="true">Custom file: Import a file that you have created to use as the cage. Note that imported files must have the same number of vertices as the base mesh to work correctly.</li> </ul> |
| Ignore backface | Toggle whether back-faces are ignored while baking. This can help reduce artifacts, but can also cause errors in certain edge-cases. |
| Match | Change how the Baker determines whether to include objects while baking:<ul data-preserve-html="true"> <li data-preserve-html="true">Always: Include all high poly meshes that are hit within the cage while baking.</li> <li data-preserve-html="true">By mesh name: For each cage, only bake meshes with the corresponding mesh suffix.</li> </ul> |
| Low poly mesh suffix | When using Match By mesh name, use this suffix to define low poly meshes. |
| High poly mesh suffix | When using Match By mesh name, use this suffix to define high poly meshes and match them with the corresponding low poly mesh. |
| Antialiasing | Adjust the amount of antialiasing in the generated maps. |

## ID map settings

| Setting | Function |
| --- | --- |
| Color source | Change how the baked colors of the ID map are determined:<ul data-preserve-html="true"> <li data-preserve-html="true">Vertex Color</li> <li data-preserve-html="true">Material Color</li> <li data-preserve-html="true">File ID</li> <li data-preserve-html="true">Mesh ID/Polygroup</li> </ul> |
| Color Generator | When using File ID or Mesh ID/Polygroup as the color source, determine how colors are generated:<ul data-preserve-html="true"> <li data-preserve-html="true">Random</li> <li data-preserve-html="true">Hue shift</li> <li data-preserve-html="true">Grayscale</li> </ul> |

## Ambient occlusion map settings

| Setting | Function |
| --- | --- |
| Secondary rays | Change the number of secondary rays. More rays can yield better results at the cost of increased processing time. |
| Min Occluder distance | Adjust the minimum distance for rays to travel to hit high poly geometry and impact the resulting AO map. |
| Max occluder distance | Rays that extend further than this distance without hitting the high poly mesh are considered to not be occluded and will not affect the AO map. |
| Relative to bounding box | When this box is checked, other settings that refer to distance are based on the bounding box of the project mesh. So a distance of 1 is equal to the size of the bounding box. |
| Spread angle | Adjust the angular range of generated rays. A higher spread angle allows a surface to be occluded more easily by geometry that is not positioned perpendicularly away from the surface. |
| Distribution | Select how rays are distributed. |
| Ignore backface | Change whether backfaces are considered to occlude objects. |
| Self occlusion | Select which meshes should affect ambient occlusion for the current mesh. |
| Attenuation | Change how occlusion is attenuated by occluder distance. |
| Ground plane | Enable this to create a ground plane that acts as an occluder. |
| Ground plane offset | Change the position of the ground plane. |

## Curvature map settings

| Setting | Function |
| --- | --- |
| Method | Choose how to generate the curvature map. |
| Secondary rays | Adjust how many secondary rays are used to generate the curvature map. More secondary rays can produce better results at the cost of increased processing time. |
| Sampling radius | Adjust how far the baker searches to calculate the curvature of the current point. |
| Relative to Bounding box | When this is checked, all distances are based on the size of the mesh bounding box. |
| Self intersection | Choose which objects will be considered when determining curvature. |
| Auto tonemapping (per UV tile) | Leave this checked to automatically adjust the tonemap curvature maps on a per UV tile basis. |
| Tonemapping Min | If auto tonemapping is disabled, adjust the minimum value for tonemapping. |
| Tonemapping Max | If auto tonemapping is disabled, adjust the maximum value for tonemapping. |

## Position map settings

| Setting | Function |
| --- | --- |
| Mode | Select whether to generate an all axis position map, or only calculate position for a selected axis. |
| Axis | If Single Axis mode is selected, use this setting to choose which axis to calculate. |
| Normalization type | Change how position values are normalized, either with a Bounding Box, Bounding sphere, or disable normalization. |
| Normalization scale | Change what is considered the maximum bounds of the position space. |

## Thickness map settings

| Setting | Function |
| --- | --- |
| Secondary rays | Change the number of secondary rays. More rays can yield better results at the cost of increased processing time. |
| Min Occluder distance | Adjust the minimum distance for rays to travel to hit high poly geometry and impact the resulting thickness map. |
| Max Occluder distance | Rays that extend further than this distance without hitting the high poly mesh are considered to not be occluded and will not affect the thickness map. |
| Relative to bounding box | When this box is checked, other settings that refer to distance are based on the bounding box of the project mesh. So a distance of 1 is equal to the size of the bounding box. |
| Spread angle | Adjust the angular range of generated rays. A higher spread angle allows a surface to be occluded more easily by geometry that is not positioned perpendicularly away from the surface. |
| Distribution | Select how rays are distributed. |
| Self occlusion | Select which meshes should affect thickness for the current mesh. |
| Normalization | Change how thickness values are normalized. |

## Height map settings

| Setting | Function |
| --- | --- |
| Normalization | Change how height values are normalized. |
| Scaling divisor | If Normalization is set to Manual, use this slider to adjust the scaling divisor and adjust height map normalization. |

## Bent normals map settings

| Setting | Function |
| --- | --- |
| Secondary rays | Change the number of secondary rays. More rays can yield better results at the cost of increased processing time. |
| Min Occluder distance | Adjust the minimum distance for rays to travel to hit high poly geometry and impact the resulting bent normals map. |
| Max Occluder distance | Rays that extend further than this distance without hitting the high poly mesh are considered to not be occluded and will not affect the bent normals map. |
| Relative to bounding box | Whenn this box is checked, other settings that refer to distance are based on the bounding box of the project mesh. So a distance of 1 is equal to the size of the bounding box. |
| Spread angle | Adjust the angular range of generated rays. A higher spread angle allows a surface to be occluded more easily by geometry that is not positioned perpendicularly away from the surface. |
| Distribution | Select how rays are distributed. |
| Ignore backface | Choose whether to treat backfaces as occluders. |
| Self occlusion | Select which meshes should impact bent normals for the current mesh. |
