---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/release-notes/know-issues.html"
breadcrumb-title: ""
description: Review known issues for Substance 3D Painter to stay informed about current limitations and workarounds in the latest version.
helpx_creative_field: ""
helpx_description: Substance 3D Painter
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Known issues
user-guide-description: ""
user-guide-title: ""
---

# Known issues

This page lists all the active known issues present in v12.1.3 of Substance 3D Painter:

* `[Baking]` Wrong AO on simple cubes
* `[Baking]` Matching by name suffix interpretation is wrong
* `[Baking]` Uv seams do not appear after mes reimport
* `[Baking]` Grid-like artifacts with some settings
* `[Baking]` Ambient Occlusion Ignore backface by mesh name doesn't work
* `[Baking]` `[AMD]` Device lost when baking with a heavy high poly meshes

* `[Substance]` Several misspell in resources
* `[Substance]` Blank space breaks condition for visibility
* `[Substance]` Presets for some materials take too long to load
* `[Substance]` Can not import resource with mixed usages

* `[Engine]` Error when using Smart Materials if Texture Set has no tile 1001
* `[Engine]` Painting with Clone tool in normal channel shift colors incorrectly
* `[Engine]` Geometry mask shows artifacts at UV borders with instanced layers

* `[Color Management]` Incompatible bindings with generator not used in mask
* `[Color Management]` Filter output are not properly taken into account
* `[Color Management]` HDR color space conversions with ACE on Linux produce clamped colors

* `[Shelf]` Resources get the wrong usage if placed in a folder with a specific name
* `[Shelf]` `[Substance]` Userdata not taken into account for shelf thumbnail generation

* `[Shader]` "camera_vp_matrix_inverse" parameter is not recognized
* `[Shader]` user0 channel always can not be read as sRGB with specific shader

* `[Scripting]` `[Javascript]` "Disbaled" typo when specifying dithering parameter in export functions
* `[Scripting]` `[Python]` Various typos in substance_painter.project module

* `[USD]` Wrong usda assignation in some cases
* `[USD]` Exported USD geometry is slip along the UV borders

* `[Single Channel View]` Project saved in base color view looks darker after Painter version update
* `[Single Channel View]` Project saved in base color view looks darker after Painter version update

* `[gltf]` Can not open files exported through Babylon Exporter
* `[Displacement]` Glitch when painting
* `[Polygon Fill Tool]` Wrong selection with symmetry
* `[2D view]` Strokes sometimes does not appear when painting
* `[Console]` Symboles associated to shortcut are not possible to write
* `[LOG]` Error message is wrong when failing export
* `[3D View]` Stencil does not work on duplicated objects
* `[Resource updater]` Different resources in the shelf with the same name are read as one resource
* `[Sample]` Broken camera in Preview sample
* `[Instancing]` `[Projection]` When selecting an instance in planar proj, another planar proj is selected on another texture set
* `[Slider]` Numerical inputs are deselected when cursor leaves the window
* `[Anchor point]` Broken references when copy and pasting Mask content
* `[Mesh export]` Do not take into account new texture set names
* `[Anchor Points]` Incorrect color when used in generator
* `[Bakers]` ID Map baker doesn't take into consideration 3ds Max 2021 Physical Material
* `[UV Tiles]` No error message on overlapping UV spaces with a specific mesh
* `[GLTF]` `[Crash]` Creating project with compressed gltf file causes a crash
* `[UV Tile sequence]` Position maps are not imported correctly
* `[UVTiles]` Height combination mask is not refresh with UV Tile mask
* `[Import]` Cannot import obj file with "nan" values
* `[Export]` GLTF exports at the wrong size
* `[Texture Set]` Name can be empty
* `[Layer stack]` Copy into mask switch to material mode
* `[UI]` Typo in brush maker settings
* `[Texture Set Settings]` Wrong shader instance name after a renaming
* `[Blending]` Color and saturation blending mode change brightness as well
* `[Librairies]` Width of Saved searches and filter by path windows not saved when changed
* `[Geometry mask]` Issue when reimporting mesh and instanced layer
* `[Color management]` Color space not found when tile 1001 is missing
* `[Export mesh]` Displacement not exported with specific UV tiles set up
* `[RedHat]` Color picker issues
* `[Regression]` `[UI]` Right Click Menu is too small on hd screen
* `[Resources]` Imported mesh maps are ignored by auto-update
* `[User Channels]` Color mixing space preview is wrong
* `[Mask]` geometry selection is still active after switching to bake mode
* `[Sonoma]` Icons do not appear in menus
* `[Path]` Height blending many paths can cause artifacts
* `[Polygon Fill]` Changing base color's color space does not update color picker
* `[UV Padding]` Artefacts when upscaling texture from 4k to 8k at export
* `[Performances]` Painter hogs VRAM usage
* `[Generator]` Setting "use texture" to false doesn't disable the use of the texture input
* Non-square resources are stretched when used in the brush channel's slots
* Failed to decode substance
* Not perfectly superposed UVs can create artefacts
* Invalid mesh normals with some fbx
* View is not updated when changing the channel affected by a level
* Project with one texture set are reopen in Base Color solo mode
* UI of channel button in Material/paint properties can be broken
* Order of channels in Properties can be broken
* Strokes made in L16F and RBG16F can display artifacts
* Restore button behaviour does not interact with lock key in camera settings
* Photoshop export ignores geometry mask selection
* Blur Slope and warp filter depends on texture set resolution
* Maps with no names are created outside export folder
* Stencil is not updated when changing brush preset
* Issue with transparency on PSD files
* Brush parameters modifies from contextual toolbar do not appear in history
* Can not rename or delete export presets if you already deleted and recreated it this session
* Channel mapping does not work for projection tool preview in some cases
* Viewport freeze when saving while editing 3d projection
* Material layering resolution is too low

## Stability

* `[Crash]` Clicking on Texture Set list after failed project creation causes a crash
* `[Crash]` Critical error crash when same project is open twice
* `[Crash]` Select "Export mesh" when mesh failed to load
* `[Crash]` Clicking on "Start painting" after trying to open an old project
* `[Crash]` Creating very long texts in Ribbon can crash
* `[Crash]` Returning to painting mode after device lost in baking
* `[Crash]` Exit Painter after cancel maps export
* `[Crash]` Exporting mesh with some special symbols in camera name
