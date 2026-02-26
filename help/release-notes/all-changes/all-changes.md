---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/release-notes/all-changes.html"
breadcrumb-title: ""
description: Review all changes and updates across Substance 3D Painter versions to track feature evolution and improvements over time.
helpx_creative_field: ""
helpx_description: Painter > Release notes > All Changes
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: All Changes
user-guide-description: ""
user-guide-title: ""
---

# All Changes

This page contains release notes for all previous releases of Substance 3D Painter, sorted from most recent to oldest.

>[!NOTE]
>
> To view known issues that may affect Painter, see the [dedicated documentation page](../../release-notes/know-issues/know-issues.md).

## Version 11

### 11.1.3

Release date: <b>2026/02/12</b>  
Summary: <b>Minor release</b>  
  
<b>Fixed</b>:

* &#91;Paint&#93; Stencil and symmetry do not work in some cases
* &#91;Path&#93; No update when changing smudge stroke opacity slider
* &#91;Project&#93; Unable to paint on some geometry
* &#91;Ribbon&#93; Instantiated path disappears when changing Texture Set resolution
* &#91;UI&#93; Color picker can shrink and disappear in some cases

### 11.1.2

Release date: <b>2026/01/13</b>  
Summary: <b>Minor release</b>

<b>Added</b>:

* &#91;Baking&#93; Improve baking time for UV Tiles project with asynchronous saving
* &#91;Shaders&#93; Mention in Shader API changelog changes following Vulkan migration
* Update OpenEXR to version 3.4.4

<b>Fixed</b>:

* &#91;Crash&#93; Crash during startup on Nvidia GTX 10xx series
* &#91;Crash&#93; Using the color picker on different Texture Sets can result in a crash when quitting the application
* &#91;Performance&#93; Performance issue when painting in project with many layers
* &#91;Performance&#93; Lag when painting with graphic tablet pen
* &#91;UI&#93; Camera settings stay disabled in render mode (Iray)
* &#91;Ribbon&#93; Path can overlap itself unexpectedly after a corner in some cases
* &#91;Ribbon&#93; Performance issue with UV Tiles
* &#91;Substance&#93;&#91;UI&#93; Image inputs disappears when collapsed
* &#91;Substance&#93;&#91;UI&#93; Nested groups can remain even if Visible If hides them
* &#91;Baking&#93;&#91;UI&#93; Unable to set Curvature Sampling Radius beyond 0.01
* &#91;Baking&#93;&#91;UI&#93; Unable to set Max Occluder Distance beyond 1
* &#91;Baking&#93; AO setting "Self Occlusion" is ignored with several Texture Set and Low as High baking
* &#91;Baking&#93; ID map does not bake vertex colors from FBX in Low as High mode
* &#91;Content&#93; Highpass filter results in washed out colors in color managed channels

### 11.1.1

Release date: <b>2025/12/09</b>  
Summary: <b>Minor release</b>  
  
<b>Added</b>:

* &#91;Performance&#93; Improve UV Tiles performance when computing partial textures
* &#91;Bakers&#93; Update to version 3.15.4

<b>Fixed</b>:

* &#91;Crash&#93;&#91;MacOS&#93; Saving project from previous version always crash
* &#91;Crash&#93; Closing a project can sometimes result in a crash
* &#91;Project&#93; Error "members count mismatch" when opening project made in previous version
* &#91;Baking&#93; UV Tiles are not combined with previous bake results if present
* &#91;Baking&#93; Device lost even with raytracing disabled on Nvidia GTX 10XX series
* &#91;Baking&#93; AO with normal has artefacts at edges because no padding
* &#91;Baking&#93; AO setting "Self Occlusion" is ignored with several Texture Sets and "match by name" on
* &#91;Baking&#93; ID Map is fully black if any high-poly meshes are missing vertex colors
* &#91;Ribbon&#93; Tooltip for Alpha blending mode mentions Screen blend mode instead of Linear Dodge
* &#91;Path&#93; Tangents create unexpected loop when point is moved closely to the path ends
* &#91;Tool&#93; Material preview does not work when projection is used in a mask
* &#91;Engine&#93; Painting small strokes can result in blocky artifacts
* &#91;Shader&#93; Undoing shader instance creation does not remove it properly
* &#91;Export&#93; Alpha mode for GLTF export is always set to MASK
* &#91;Python&#93; Unexpected error when editing layer stack outside of scoped modification block

<b>Known Issues</b>:

* &#91;Ribbon&#93; Performance issue with UV Tiles
* &#91;Ribbon&#93; Path can overlap itself unexpectedly after a corner in some cases
* &#91;Crash&#93;&#91;Ribbon&#93; Creating very long texts in Ribbon can crash
* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Regression&#93;&#91;UI&#93; Right-click Menu is too small on HD screens
* &#91;Crash&#93;&#91;Python&#93; USD export triggered by TextureStateEvent
* &#91;Engine&#93; Painting with Clone tool in normal channel shift colors incorrectly
* &#91;Python&#93; Ghost widget appears deleted by script still functioning

### 11.1.0

Release date: <b>2025/11/18</b>  
Summary: <b>This update is a major release, it contains the new Ribbon tool with dedicated new content, symmetry support for fill layers, physical size parameter for displacement, improved performance through the updated bakers, full Vulkan support for Windows and Linux and other improvements.</b>

<b>Added</b>:

* New ribbon tool
* &#91;Tool&#93; Add new Ribbon tool to make seamless paths
* &#91;Ribbon&#93; Add Ribbon preset shortcuts in Properties window
* &#91;Ribbon&#93; Allow to change the opacity of the Ribbon per vertex on the path
* &#91;Ribbon&#93; Allow to change the size of the Ribbon per vertex on the path
* &#91;Ribbon&#93; Remove begin/end defined in a Substance when paths are closed
* &#91;Ribbon&#93; Remove Path/Material preview in properties window for Paint/Eraser/Smudge path tools
* &#91;Ribbon&#93; Add blending modes for the alpha and some channels when self-overlapping
* Fill symmetry
* &#91;Fill&#93; Add support for symmetry on fill layers and effects
* &#91;Fill&#93;&#91;UI&#93; Expose symmetry settings in properties window for fill layer and effects
* &#91;Fill&#93; Rework symmetry settings UI in both viewport menu and properties window
* &#91;Fill&#93; Properly reorient normal textures when projecting in warp mode
* Physical size displacement
* &#91;Displacement&#93; Use physical size as displacement unit
* Performance improvement
* &#91;Performance&#93; Improve rendering of small brush strokes on big triangles
* &#91;Performance&#93; Improve Shader compilation time
* &#91;Performance&#93; Full Vulkan support for Windows and Linux
* &#91;Performance&#93; Updated bakers with faster GPU rendering and support of AMD raytracing
* &#91;UI&#93; Re-organize tools properties into groups and collapse some by default
* &#91;Engine&#93; Update Substance Engine to version 9.2.5
* &#91;Substance&#93; Expose resolution override for Substance resources in Tools and Fills
* &#91;Export&#93; Update Mesh Maps export preset to export grayscale textures
* Python
* &#91;Baking&#93;&#91;Python&#93; Indicate in changelog breaking changes following bakers update
* &#91;Python&#93; Expose fill symmetry settings in Python
* Content and new content
* &#91;Content&#93; Add 75 new tool presets for the Ribbon tool
* &#91;Content&#93; Update gradient builder resource to be compatible with Ribbon

<b>Fixed</b>:

* &#91;Crash&#93; Loading another project while path snapping is enabled can crash
* &#91;Crash&#93; Right click in Path panel with info from another session in clipboard can crash
* &#91;UI&#93; Interface scrolls up in tool properties when creating a path
* &#91;UI&#93; Mouse cursor disappear when path viewport visualization is hidden
* &#91;Path&#93; Copy/pasting different Tool properties in Path panel lead to unstable properties
* &#91;Tool&#93; Eraser and Smudge tool presets do not always update channel selection
* &#91;Tool&#93; Painted value is gray but UI shows white after loading colored tool preset in mask
* &#91;Tool&#93; Preset created from mask retains channels values loaded from another preset
* &#91;Substance&#93; Normal color space override defined in graph is not taken into account
* &#91;Content&#93; Default brush shape resource uses an outdated Substance

<b>Known Issues</b>:

* Shader instance history not tracked properly
* &#91;Ribbon&#93; Performance issue with UV Tiles
* &#91;Ribbon&#93; Path can overlap itself unexpectedly after a corner in some cases
* &#91;Ribbon&#93; Tangents create unwanted loop when point is moved closely to the path ends
* &#91;Crash&#93;&#91;Ribbon&#93; Creating very long texts in Ribbon can crash
* &#91;Tool&#93; Material preview does not work when projection is used in a mask
* &#91;Baking&#93; AO setting "Self Occlusion" is ignored with several Texture Sets and "match by name" enabled
* &#91;Baking&#93; AO with normal has artifacts at edges because of missing padding
* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Regression&#93;&#91;UI&#93; Right-click Menu is too small on HD screens
* &#91;Crash&#93;&#91;Python&#93; USD export triggered by TextureStateEvent
* &#91;Engine&#93; Painting with Clone tool in normal channel shift colors incorrectly
* &#91;Python&#93; Ghost widget appears deleted by script still functioning

### 11.0.3

Release date: <b>2025/08/05</b>  
Summary: <b>Minor release</b>

<b>Added</b>:

* &#91;Substance 3D Assets&#93; Add a notification dot to the 3D Assets panel
* &#91;VFX Platform 2025&#93; Add ACES 2.0 config in color management settings
* &#91;VFX Platform 2025&#93; Update OCIO to version 2.4.2
* Update Iray to version 2024.10
* &#91;Engine&#93; Update to Substance Engine v.9.2.3
* &#91;Nvidia&#93; Raise Nvidia minimum drivers version to 572.60 (Win) and 570.169 (Linux)

<b>Fixed</b>:

* &#91;Python&#93; Scoped Modification does not appear in History window

<b>Known Issues</b>:

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Regression&#93;&#91;UI&#93; Right-click Menu is too small on HD screens
* &#91;Crash&#93;&#91;Python&#93; USD export triggered by TextureStateEvent
* &#91;Engine&#93; Painting with Clone tool in normal channel shift colors incorrectly
* &#91;Python&#93; Ghost widget appears deleted by script still functioning

### 11.0.2

Release date: <b>2025/06/10</b>  
Summary: <b>Minor release</b>

<b>Added</b>:

* &#91;Mac&#93; Add warning about specific operating system version leading to artifacts
* &#91;Auto-update&#93; Minor UX improvements to Assets error log
* &#91;Auto-unwrap&#93; Update to version 1.3.2 with seaming improvements
* &#91;USD&#93;&#91;FBX&#93; Add support for multiple UV sets with sparse data
* &#91;Export&#93; Meshes exported as FBX are missing their additional UV sets if any were present at import

<b>Fixed</b>:

* &#91;MacOS&#93;&#91;Linux&#93; Crash when saving on network drive
* &#91;Win&#93;&#91;Tablet&#93; Flickering when panning
* &#91;SpaceMouse&#93; Issue when working with Path Tool
* &#91;Auto-cage&#93; Cannot bake after a mesh reload
* &#91;Auto-update&#93; Image sequence is not reloaded when first tile is missing
* &#91;Path&#93; Custom tangent can affect other tangent
* &#91;Path&#93; Path does not appear on Texture Set if the first point is on another Texture Set
* &#91;UI&#93; Some menus are always disabled after opening a project (ex: symmetry)
* &#91;Properties&#93; Cannot use/load tool presets with Filled path tool
* &#91;USD&#93; Multiple UV sets are not recognized in custom shader when using USD files
* &#91;USD&#93; Cameras with the same names are overridden
* &#91;Export&#93; Send to Photoshop results in incorrect color space for both color and grayscale results
* &#91;Export&#93; Grayscale channels with alpha are exported as color instead of grayscale with PNG format
* &#91;Export&#93; Exporting grayscale channel as PSD result in invalid/truncated file
* &#91;Content&#93; Warp filter in multi-directional mode does not work
* &#91;Python&#93; Cannot allocate list error when crawling layer stack nodes

<b>Known Issues</b>:

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Regression&#93;&#91;UI&#93; Right-click Menu is too small on HD screens
* &#91;Crash&#93;&#91;Python&#93; USD export triggered by TextureStateEvent
* &#91;Engine&#93; Painting with Clone tool in normal channel shift colors incorrectly
* &#91;Python&#93; Ghost widget appears deleted by script still functioning

### 11.0.1

Release date: <b>2025/04/10</b>  
Summary: <b>Minor release</b>

Note: <b>Linux CCD version will be delayed until April 29</b>

<b>Added:</b>

* Update to Qt 6.5.8
* &#91;Substance&#93; Add log message for filters when several image inputs share the same usage
* &#91;Nvidia&#93; Add warning about latest Nvidia drivers (572.47)

<b>Fixed:</b>

* &#91;Crash&#93; When drag and dropping an sbsar with an usage in a single channel slots
* &#91;Crash&#93;&#91;Path&#93; Change path type option is not grayed out when not clicking on specific path
* &#91;Fill Path&#93; Should not be able to select substance material
* &#91;Engine&#93; Artifacts along brush strokes
* &#91;Engine&#93; Paths can be broken with specific settings
* Issue with drop down for eye dropper color space
* &#91;Auto-update&#93; &#91;Python&#93; Wrong error message when using ResourceID without version
* &#91;Shader&#93; Crash when opening some projects

<b>Known Issues:</b>

* &#91;SpaceMouse&#93; Issue when working with Path Tool
* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Regression&#93;&#91;UI&#93; Right-click Menu is too small on HD screens
* &#91;Crash&#93;&#91;Python&#93; USD export triggered by TextureStateEvent
* &#91;Engine&#93; Painting with Clone tool in normal channel shift colors incorrectly
* &#91;Python&#93; Ghost widget appears deleted by script still functioning

### 11.0.0

Release date: <b>2025/03/11</b>  
Summary: <b>Major release, new Auto-update feature, Filled path tool and other path improvements, as well as new filters and an experimental Auto-cage generation for baking</b>

<b>Added</b>:

* Auto Update
* &#91;Auto-update&#93; Auto-update modified assets in the Assets panel
* &#91;Auto-update&#93; Auto-update modified assets across the project
* &#91;Auto-update&#93; Keep auto-update off by default
* &#91;Auto-update&#93; Make update optional if resource parameters do not match (.sbsar, .glsl, .ai, .svg)
* &#91;Auto-update&#93; Add environment variable to disable auto-update feature
* &#91;Auto-update&#93;&#91;SBSAR&#93; Make update optional if resource parameters do not match
* Filled Path
* &#91;Path&#93;&#91;Fill&#93; Add new tool to create filled paths
* Path improvements
* &#91;Path&#93; Create path which snaps to polygons
* &#91;Path&#93; Allow to switch Path types
* &#91;Path&#93; Allow to copy paste path vertex data between content and mask
* &#91;Path&#93; Allow to constrain angle when creating a new point
* &#91;Path&#93; Allow to constraint point creation to a line
* &#91;Path&#93; Close shape with a single click
* &#91;Path&#93; Display path information
* &#91;Path&#93; Allow to scale and rotate path vertices
* &#91;Path&#93;&#91;UX&#93; Make transformation gizmos easier to access
* &#91;Path&#93; Add path preview
* &#91;Path&#93; Disable Path preview with Shift + P
* &#91;Path&#93; Improve tangent edition from side view
* &#91;Path&#93; Allow to focus on a 3D path
* &#91;Path&#93; Vertices should retain selection status when toggling UI off and on again
* &#91;Path&#93; Allow to delete Path using Backspace
* &#91;Path&#93; Keep path list open if user expands it
* &#91;Path&#93;&#91;Layer Stack&#93; Correctly rename duplicates on copy/paste
* &#91;Path&#93; UI and tooltip improvements
* Performance
* &#91;Performance&#93; Improve viewport performance when using high tessellation level
* &#91;Performance&#93; Enable only the first channel on new fill layers/effects
* &#91;Performance&#93; Parallelize brush stroke computation
* Baking
* &#91;Baking&#93; Add new fully automatic cage generation option for baking with high-poly meshes (Experimental)
* Content
* &#91;Content&#93; Add 6 new filters: stylization, quantize, anisotropic kuwahara, bevel smooth, directional distance, grayscale conversion
* &#91;Content&#93; Update Noises and Grunges to latest version from Designer (with new 2D Voronoi)
* &#91;Content&#93; Add 3 new texture generators (Tile Random, Triangle Grid, Scratches Generator)
* &#91;Content&#93; Rename Unreal Engine template and export presets
* Python
* &#91;Shelf&#93;&#91;Python&#93; Save smart material or smart mask to disk from Python
* &#91;Python&#93; Add baking auto-cage to Python API
* &#91;Python&#93; Allow to edit Texture Sets/UV Tiles names and descriptions
* &#91;Python&#93; Share resolution settings on Vector &amp; Font sources
* &#91;Auto-update&#93;&#91;Python&#93; Expose project auto-update functionalities in Python
* Misc
* &#91;Export&#93; Make Send to options easier to access with a new panel
* &#91;Nvidia&#93; Add warning about latest Nvidia drivers (572.16)
* Angle snapping should be affected by Object/World space selection​
* &#91;Texture Set list&#93; Allow to add custom name to UV Tiles and use them at export
* Mac
* &#91;Mac&#93; Use Metal instead of OpenGL for graphics rendering
* &#91;Mac&#93; Drop Mac Intel support

<b>Fixed</b>:

* &#91;Crash&#93; Delete image input
* Cannot add smart mat through layer stack button
* &#91;Python&#93; Effects on GroupLayerNode cannot be found

<b>Known Issues</b>:

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Regression&#93;&#91;UI&#93; Right-click Menu is too small on HD screens
* &#91;Crash&#93;&#91;Python&#93; USD export triggered by TextureStateEvent
* &#91;MacOS Intel&#93; Crash when importing some presets
* &#91;Engine&#93; Painting with Clone tool in normal channel shift colors incorrectly
* &#91;Python&#93; Ghost widget appears deleted by script still functioning
* &#91;RedHat&#93; Color picker issues

## Version 10

### 10.1.2

Release date: <b>2024/12/3</b>  
Summary: <b>Minor release, bug fixes</b>  
  
<b>Fixed</b>:

* &#91;Crash&#93; Delete image input
* Cannot add smart mat through layer stack button
* &#91;Python&#93; Effects on GroupLayerNode cannot be found

<b>Known Issues</b>:

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Regression&#93;&#91;UI&#93; Right-click Menu is too small on HD screens
* &#91;Crash&#93;&#91;Python&#93; USD export triggered by TextureStateEvent
* &#91;MacOS Intel&#93; Crash when importing some presets
* &#91;Engine&#93; Painting with Clone tool in normal channel shift colors incorrectly
* &#91;Python&#93; Ghost widget appears deleted by script still functioning
* &#91;RedHat&#93; Color picker issues

### 10.1.1

Release date: <b>2024/11/5</b>  
Summary: <b>Minor release, bug fixes</b>

<b>Added</b>:

* &#91;Project&#93; Keep current project open until new project selection is validated
* &#91;Auto-unwrap&#93; Texel density allows to better split UV islands into UDIMs
* &#91;Baking&#93; Fix ambiguous copy in contextual menu of Mesh Maps
* &#91;Warp&#93; Remove scaling in viewport for Z (depth) axis
* &#91;Import/Export&#93; Remove support of unused image file formats
* Update Substance Engine to 9.1.4

<b>Fixed</b>:

* &#91;Crash&#93; After relocating resource in Assets and saving project
* &#91;Crash&#93; Issues with aiserver library
* &#91;Crash&#93; Illustrator server crash in some rare cases
* &#91;Crash&#93; When exiting application in some rare cases
* Cannot send crash reports on some machines
* &#91;Baking&#93; Vertex color is not read properly
* &#91;UI&#93; Location of windows and What's New on startup is shifted
* &#91;Assimp&#93; Maya's StandardSurface not recognized in ID baking
* &#91;Python&#93; Missing SSL lib outputs an error
* &#91;Python&#93;&#91;Win&#93; Error when calling QColorConstants.Transparent
* &#91;Python&#93; Layers thumbnails created via Python do not refresh until clicking inside the layer stack
* &#91;Shader&#93; Broken link in Shader API changelog
* &#91;3D Assets&#93; Use OS proxy settings when accessing 3D Assets

<b>Known Issues</b>:

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Regression&#93;&#91;UI&#93; Right-click menu is too small on HD screens
* &#91;Crash&#93;&#91;Python&#93; USD export triggered by TextureStateEvent
* &#91;MacOS Intel&#93; Crash when importing some presets
* &#91;Engine&#93; Painting with Clone tool in normal channel shift colors incorrectly
* &#91;Python&#93; Widget that seems deleted via script still working
* &#91;RedHat&#93; Color picker issues

### 10.1.0

Release date: <b>2024/09/17</b>  
Summary: <b>Major release, new content: Fill area mask/color filter, embroidery decal filter and six generic Substance filters, import USD with material and shader properties, performance improvement, VFX platform 2024 compliant and migration to Linux RedHat</b>

<b>Added</b>:

* &#91;Content&#93; Add new Fill area mask/color filter
* &#91;Content&#93; Add new Embroidery decal filter
* &#91;Content&#93; Add 6 new generic Substance filters (FXAA, pixelate, highpass, posterize, smoothstep, threshold)
* &#91;USD&#93; Export USD layer with a defined ASM material
* &#91;USD&#93; Import USD with material and shader properties
* &#91;Performance&#93; Enable optimized layer stack thumbnails by default
* &#91;Performance&#93; Reduce project file opening time and memory consumption (data decoding)
* VFX platform 2024 compliant
* &#91;VFX Platform 2024&#93; Update to Python 3.11
* &#91;VFX Platform 2024&#93; Update to OpenEXR 3.2
* &#91;VFX Platform 2024&#93; &#91;USD&#93; Update OpenSubdiv 3.6.0
* &#91;VFX Platform 2024&#93;&#91;Color Management&#93; Update to OCIO 2.3.2
* &#91;Linux&#93; Migration to Linux RedHat
* &#91;Linux&#93; Update Nvidia driver min version to 535.171.04
* &#91;Import&#93; Add an option to flip normal map when importing a GLTF mesh
* &#91;UI&#93; Use operating system default value for drag event detection distance
* &#91;Substance Engine&#93; Add call strip function to remove the symbols from the executable
* &#91;Splash screen&#93; Update to new splash screen format
* Update Substance Engine to version 9.1.3
* &#91;Python&#93; Show link to examples in the layer stack documentation menu
* &#91;JavaScript&#93; Move Javascript plugins into javascript/plugins subfolder

<b>Fixed</b>:

* &#91;Illustrator&#93; Crash exporting a UV Tile with .ai graphic in specific cases
* &#91;Dynamic Strokes&#93;&#91;Path&#93; Random per stroke does not work on a path
* &#91;UI&#93;&#91;Properties&#93; Lock is enabled when tiling is non-uniform
* ​Debug TXT file is created when double clicking on Painter project
* &#91;USD&#93;&#91;Export&#93; Some textures may be missing
* &#91;ASM&#93; Scattering Color channel ignores metallic
* &#91;Content&#93; Blur filter doesn't work in "working" color space
* &#91;Content&#93; Height Adjust filter also modifies the alpha of the layer

<b>Known Issues</b>:

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Win&#93;&#91;Crash&#93; &#91;ACE&#93; Not using sRGB ICE color space for display transform
* &#91;Regression&#93;&#91;UI&#93; Right-click Menu is too small on HD screens
* &#91;Crash&#93;&#91;Python&#93; USD export triggered by TextureStateEvent
* &#91;MacOS Intel&#93; Crash when importing some presets
* &#91;Crash&#93; Relocate resource and save project
* &#91;Engine&#93; Painting with Clone tool in normal channel shift colors incorrectly
* &#91;Python&#93; Ghost widget appears deleted by script still functioning
* &#91;RedHat&#93; Color picker issues

### 10.0.1

Release date: <b>2024/06/11</b>  
Summary: <b>Minor release, bug fixes</b>

<b>Added:</b>

* &#91;Library&#93; Convert Substance fonts into regular font files​
* &#91;Illustrator&#93;&#91;SVG&#93; Give thumbnails in scope selection a light gray background​
* &#91;Python&#93; Add function on bitmap source to list available color spaces

<b>Fixed</b>:

* &#91;Layer Stack&#93; Folder always closed when moved in or out of other folders
* &#91;Save&#93; Project file is lost when "save as copy" or autosave fails​ in specific cases
* &#91;Import&#93; Assets with same name but different extensions are overridden​
* &#91;Properties&#93; Settings missing when using anchor point in image inputs
* &#91;Illustrator&#93; Cannot import Illustrator files after server crash without restarting Painter
* &#91;Python&#93; Instance parent cannot be set with type "properties"​
* &#91;Python&#93; Setting the high poly as a baking parameter does not load the high poly​
* &#91;Python&#93; Error message for set\_color\_space() is too generic​
* &#91;Python&#93; Reference sources allow to create cycles​

<b>Known Issues</b>:

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Regression&#93;&#91;UI&#93; Right-click Menu is too small on HD screens
* &#91;Crash&#93;&#91;Python&#93; USD export triggered by TextureStateEvent
* &#91;MacOS Intel&#93; Crash when importing some presets
* &#91;Illustrator&#93; Crash exporting a UV Tile with .ai graphic in specific cases
* &#91;Dynamic Strokes&#93;&#91;Path&#93; Random per stroke does not work on a path

### 10.0.0

Release date: <b>2024/05/16</b>  
Summary: <b>Major release, edition of the layer stack with Python API, read native Illustrator files, integration of 3D Assets and new text resource</b>  
  
<b>Added</b>:

* &#91;Illustrator&#93; Use Illustrator files with art boards in Painter
* &#91;Illustrator&#93;&#91;SVG&#93; Add previews in scope selection
* &#91;Substance 3D Assets&#93; Browse, select and download 3D Assets directly in Painter
* &#91;Substance 3D Assets&#93;&#91;UI&#93; New panel
* &#91;Substance 3D Assets&#93; Support environment maps and materials
* &#91;Substance 3D Assets&#93; Allow to reload and navigate and open location folder in new Substance 3D Assets panel
* &#91;Substance 3D Assets&#93; Addition of a download manager
* &#91;Text Resource&#93; Allow to use embeddable fonts
* &#91;Text Resource&#93; Allow to render a font/text on a mesh
* &#91;Text Resource&#93; Display fonts from user and other shared paths in Assets panel with a new category
* &#91;Text Resource&#93;&#91;Properties&#93; Add support for advanced font properties
* &#91;Text Resource&#93; Allow to search/view fonts in mini-shelves
* &#91;Text Resource&#93; Add error message/dialog when importing an incompatible font
* Miscellaneous
* &#91;Fill projection&#93; Improve Scale manipulator behavior when using small values
* &#91;Manipulators&#93; Add new precise mode when pressing CTRL shortcut
* &#91;Manipulators&#93; Improve surface manipulator stability when translating
* &#91;Export&#93; Add colorspace name in SBSAR outputs
* &#91;Performance&#93; Improve library discovery time of assets on disk
* &#91;Substance&#93; Update to Substance engine version 9.1.2
* &#91;Drag and Drop&#93; Align decal rotation to camera when dropping in viewport
* &#91;Python&#93; Edition of the layer stack
* &#91;Python&#93; Allow to select layer, effect, mask, geo mask in UI
* &#91;Python&#93; Allow to get/set layer blending modes
* &#91;Python&#93; Allow to get/set fill layer projection settings
* &#91;Python&#93; Allow to query Substance material color from a fill layer
* &#91;Python&#93; Allow to query and set uniform colors and resources in layers and effects
* &#91;Python&#93; Allow to create and edit text resources in layer stack
* &#91;Python&#93; Allow to edit active channels on layers and effects
* &#91;Python&#93; Allow to batch actions to have a single undo/redo
* &#91;Python&#93; Allow to load/edit vectorial source parameters
* &#91;Python&#93; Allow to edit layer and effects color properties with color management
* &#91;Python&#93; Allow to query and create instanced layers
* &#91;Python&#93; Allow to add color selection effect
* &#91;Python&#93; Allow to control bitmap image color management
* &#91;Python&#93; Allow to pause/unpause engine
* &#91;Python&#93; Allow to navigate to siblings and parent nodes
* &#91;Python&#93; Allow to create filter/generator effect
* &#91;Python&#93; Allow to add level effect
* &#91;Python&#93; Allow to add smart mask on a layer
* &#91;Python&#93; Allow to create/edit anchor points
* &#91;Python&#93; Allow to get/Set mask on layers
* &#91;Python&#93; Allow to create compare mask effect
* &#91;Python&#93; Allow to query and use presets from Substance resources
* &#91;Python&#93; Allow to list presets and their values via internal\_properties function for Substance resources
* &#91;Python&#93; Allow to list predefined export presets
* &#91;Python&#93; Allow to list export presets available in the library
* &#91;Python&#93; Allow to retrieve the content of export presets

<b>Fixed</b>:

* &#91;Crash&#93; Undoing "Remove shader instance" with Ctrl-Z
* &#91;Crash&#93; Create a layer on empty stack if last selection was an effect
* &#91;SVG&#93; Issue with custom cropped area value
* &#91;Auto-Unwrap&#93; Recomputing only the packing without any change to UV orientation results in crash
* &#91;Drag and drop&#93; Lag due to external resources are preloaded multiple times
* &#91;UI&#93; Drag and drop resource thumbnail can hide warning message in layer stack
* &#91;Performance&#93; Masked UV tiles are still computed
* &#91;USD&#93; Wrong highlight for scope selection
* &#91;Resource&#93; Bitmap image gets corrupted after painting in normal channel and saving project
* &#91;USD&#93; Support left-handed vertex mesh ordering
* &#91;Substance&#93; Reset to default always go back to zero for angle widget
* &#91;Engine&#93; Painting with an SVG in a stencil doesn't work
* &#91;Engine&#93; Normal map brush strokes break after an undo
* &#91;Content&#93; Graphic to Material filter has incorrect alpha blending and color space
* &#91;Content&#93; Blending modes on Tile Generator are not working
* &#91;Content&#93; Histogram scan filter produces banding in some cases
* &#91;Content&#93; Baked lighting stylized does not take painted height into account
* &#91;Python&#93; Unexpected error when retrieving instanced layer information after shader change
* &#91;Save&#93; Project file is lost when "save as" fails in specific cases

<b>Known Issues</b>:

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Crash&#93;&#91;Linux&#93;&#91;AMD&#93; Dragging and dropping resources in layer stack on Wayland OS
* &#91;Regression&#93;&#91;UI&#93; Right Click Menu is too small on HD screens
* &#91;Crash&#93;&#91;Python&#93; USD export triggered by TextureStateEvent
* &#91;Save&#93; Spp project file is lost when "save as copy" fails in specific cases
* &#91;MacOS Intel&#93; Crash when importing some presets
* &#91;Illustrator&#93; Cannot import Ai files after server crash without restarting Painter
* &#91;Import&#93; Assets with same name but different extensions are overridden

## Version 9

### 9.1.2

Release date: <b>2024/01/30</b>  
Summary: <b>Minor release, bug fixes</b>  
  
<b>Added</b>:

* &#91;Performance&#93; Improve first fill layer creation time in new projects
* &#91;Performance&#93; Reduce loading time of heavy environment maps
* &#91;Substance&#93; Allow to save/close projects even when thumbnails are generating

<b>Fixed</b>:

* Save fails on previous version projects when viewport is modified​
* &#91;Crash&#93; Reimporting mesh when using custom AO and color management​
* &#91;Fill projection&#93; Clicking on Scale manipulator gives "not paintable" message​
* &#91;Brush&#93; Painting with UV alignment causes artefacts​
* &#91;Layer stack&#93; Renaming layer is slow when stack is very long​
* &#91;Layer Stack&#93; Incorrect error message when using incompatible filter in mask
* &#91;Layer stack&#93; Selection switches back to top layer after deletion
* &#91;Export&#93; Generated normal texture is always in 3D Space Neighbor padding mode​
* &#91;Export&#93; Texture alpha is not generated with 2D View export preset​
* &#91;Export&#93; SBSAR export has incorrect usages with converted maps​
* &#91;Shader&#93; Shader API changelog is not up to date with latest ASM changes

<b>Known Issues</b>:

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Crash&#93;&#91;Linux&#93;&#91;AMD&#93; Dragging and dropping resources in layer stack on Wayland OS
* &#91;Regression&#93;&#91;UI&#93; Right Click Menu is too small on HD screens
* &#91;Crash&#93;&#91;Python&#93; USD export triggered by TextureStateEvent

### 9.1.1

Release date: <b>2023/12/05</b>  
Summary: <b>Minor release, bug fixes and send to After Effects functionality</b>  
  
<b>Added:</b>

* &#91;Interop&#93; Allow to send a textured mesh to After Effects (Ae 24.1)

<b>Fixed:</b>

* &#91;Fill&#93; UV set to UV set projection does not read more than 2 UV sets
* &#91;Crash&#93; Using 16K environment map
* &#91;Crash&#93; Exr used as image input
* &#91;Crash&#93; Copy and pasting Paths across projects
* &#91;QoL&#93; Drag and drop of Alpha resource in decal mode creates UV projection in mask
* &#91;Path&#93; Copying path vertices also rename target path when reopening project
* &#91;Linux&#93; Color picking can be broken with multiple screens
* &#91;Auto Unwrap&#93; UI issue for texel density control
* &#91;Color Management&#93; UI feedback is sensible to case but engine is not
* &#91;Color Management&#93; Incorrect color space selection in mask with user data override

<b>Known Issues:</b>

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Crash&#93;&#91;Linux&#93; with Linux Wayland on AMD when drag and dropping resource in the Layer Stack
* &#91;Crash&#93;&#91;Mac&#93; Changing Anisotropic filtering value on Monterey OS
* &#91;Regression&#93;&#91;UI&#93; Right Click Menu is too small on hd screen
* &#91;Python&#93; Crash exporting USD triggered by TextureStateEvent

### 9.1.0

Release date: <b>2023/11/07</b>  
Summary: <b>Major release introducing SVG and transparency support, as well as drag and drop and path tool improvements</b>

<b>Added:</b>

* &#91;SVG&#93; Allow to import vectorial files (SVG)
* &#91;SVG&#93;&#91;UI&#93; Add support for SVG-specific properties
* &#91;SVG&#93; Add an option to easily preserve original image proportions
* &#91;SVG&#93; Allow to automatically use alpha of SVG with transparency
* &#91;Interop&#93; Allow to send a textured mesh to After Effects (Ae 24.1 beta)
* &#91;Interop&#93; Add settings for Send to After Effects
* &#91;QoL&#93;&#91;Assets&#93;&#91;UI&#93; Auto-import asset when drag and dropping into UI slot
* &#91;QoL&#93; Allow to drag and drop external assets into the layer stack
* &#91;QoL&#93;&#91;Layer Stack&#93; Drag and drop textures from Assets Panel into the Layer Stack
* &#91;QoL&#93;&#91;Viewport&#93; Allow to drag and drop generator, filters on the mesh
* &#91;QoL&#93;&#91;Viewport&#93; Allow to drop external assets onto the mesh
* &#91;QoL&#93;&#91;Projection&#93; Add new UV set to UV set projection mode
* &#91;QoL&#93; Drag and drop Smart Masks as new layers in viewport and Layer Stack
* &#91;QoL&#93; Add selector for Generators with multiple outputs when used in mask
* &#91;QoL&#93; Allow to drag and drop single channel images over a fill effect
* &#91;QoL&#93;&#91;Layer stack&#93; Use CTRL/ALT modifiers with drag and drop to specify where/how to create effects/layer
* &#91;Path&#93; Toggle paths visibility individually in path panel
* &#91;Path&#93; Allow to use transformation manipulators for path points
* &#91;Path&#93; Allow to control tangents per vertex manually
* &#91;Path&#93; Copy/paste path properties
* &#91;Path&#93; Introduce an empty shortcut for break tangent button
* &#91;Shader&#93; Add support for Opacity &amp; Translucency in ASM shader
* &#91;Shader&#93; Add support for Absorption color channel with ASM shader
* &#91;Shader&#93; Improve ASM shader parameters tooltips
* &#91;Shader&#93; Change Translucency channel default color to black
* &#91;Display settings&#93; Enable Temporal Anti-Aliasing by default
* &#91;Display settings&#93; Enable Sub-surface scattering setting by default
* &#91;Substance&#93; Add support for ColorSpace property from graph input/output
* &#91;Substance&#93; Update Substance engine to version 9.0.3
* &#91;UI&#93; Make contextual toolbar button accessible even if the app window is small
* &#91;Auto Unwrap&#93; Control UV Tiles number with Texel Density
* &#91;Baking&#93; Deactivate GPU raytracing on AMD GPUs by default
* &#91;Performance&#93; Apply lossless compression on 16bit images to reduce project footprint
* &#91;Python&#93; Allow to manipulate the default Camera in 3D View
* &#91;Python&#93; Expose the ability to export mesh via scripting
* &#91;Content&#93;&#91;Samples&#93; Add new sample project "French Restaurant Table"
* &#91;Content&#93; Update Substance logo alpha to new version
* &#91;Content&#93; Add three SVG focused material filters (Custom Sticker, Custom Spray and Graphic to Material)

<b>Fixed:</b>

* &#91;Crash&#93; Changing manipulator size when not using symmetry tool
* &#91;Crash&#93; &#91;Layer stack&#93; Creating layer when nothing is selected
* &#91;Project&#93; Mesh maps can be corrupted after a removing unused resources
* &#91;Project&#93; Resource corruption after re-importing or re-baking image
* &#91;Assets&#93; Reloading an asset removes it from Favorites
* &#91;Import&#93; Can not import resources when there is "No result found" in asset panel
* &#91;UI&#93; Contextual toolbar arrow does not appear in some cases
* &#91;Substance&#93; Side by side button for boolean values is not supported
* &#91;Level&#93; Wrong channel label when used in mask
* &#91;Export&#93;&#91;glTF&#93; glTF/GLB files exported from Painter do not have a physical size unit
* &#91;Content&#93; Blur filter intensity is clamped to 16
* &#91;Content&#93; Color Match filter "target color" image input is not visible

<b>Known issues:</b>

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Crash&#93;&#91;Linux&#93; with Linux Wayland on AMD when drag and dropping resource in the Layer Stack
* &#91;Crash&#93;&#91;Mac&#93; Changing Anisotropic filtering value on Monterey OS
* &#91;Crash&#93; Exr used as image input
* &#91;Crash&#93; Using 16K environment map
* &#91;Auto Unwrap&#93; UI issue for texel density control
* &#91;Regression&#93;&#91;UI&#93; Right Click Menu is too small on hd screen
* &#91;Python&#93; Crash exporting USD triggered by TextureStateEvent
* &#91;QoL&#93; Drag and drop of Alpha resource in decal mode creates UV projection in mask

### 9.0.1

Release date: <b>2023/09/19</b>  
Summary: <b>Minor bugfix release with several improvements</b>  
  
<b>Added:</b>

* &#91;Import&#93; Set default import location in import window
* &#91;Baking Mode&#93; Allow to reset parameters to their default values
* &#91;Baking&#93; Set baking to paint resolution when creating a project
* &#91;Symmetry&#93; Unbind symmetry-specific manipulator from shortcut Q
* &#91;Menu&#93; Add "show log" option in help menu
* &#91;Viewport&#93; Improve shadow rendering speed
* &#91;Substance&#93; Update engine to version 9.0.1
* &#91;Color Management&#93; OCIO config file can have any extension type
* &#91;Assets&#93; Sbsar resource with 'decal' usage should be auto-set to warp projection
* &#91;Path&#93; Display a message when trying to interact with the Path tool while UI and Gizmos are hidden

<b>Fixed:</b>

* &#91;Crash&#93; Alt + Drag on Path panel
* &#91;Import Resources&#93; Random crash when removing resources to import
* Crash when importing a compressed GLB file
* Issue while painting on meshes sharing UVs
* Mesh flash black when recomputing or loading cache
* &#91;Properties&#93; Right-click menu to reset parameters doesn't appear on dropdowns
* &#91;Level&#93; Input sliders locked by previous level
* &#91;AMD&#93;&#91;Sparse&#93; SVT option if activated generates artefacts
* &#91;Projection&#93;&#91;Warp&#93; Crash when double clicking on vertices
* &#91;Path&#93; UI and path visible in baking mode
* &#91;AMD&#93; Texture lost when playing with visibility
* &#91;Sparse&#93; Resolution too low when turning around the mesh

<b>Known Issues:</b>

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors

### 9.0.0

Release date: <b>2023/06/20</b>  
Summary: <b>Major release with Paint along path allowing 3D Curves, new base materials and cleaning of legacy materials and new presets for 3D Curves</b>

<b>Added:</b>

* &#91;Path&#93; Add new Paint along Path tool
* &#91;Path&#93; Add an empty shortcut for the path tool
* &#91;Path&#93; Allow to add new points to an existing path
* &#91;Path&#93; Add shortcut to exit current path creation
* &#91;Path&#93; Allow to edit brush properties for paths
* &#91;Path&#93; Adjust tangents automatically when placing a point
* &#91;Path&#93; Recompute tangents when a point is moved
* &#91;Path&#93; Snap newly created points to the surface of a mesh
* &#91;Path&#93; Allow to edit pressure per vertex
* &#91;Path&#93; Adjust newly created point's pressure from neighboring points
* &#91;Path&#93; Allow to convert points to smooth/corner (tangent break)
* &#91;Path&#93; Allow to move a newly added point immediately
* &#91;Path&#93; Allow to remove points from existing path
* &#91;Path&#93; Allow to reverse the direction of a path
* &#91;Path&#93; Allow to select a path in the viewport
* &#91;Path&#93; Allow to select path points with marquee selection
* &#91;Path&#93; Introduce CTRL-A shortcuts to select all points of a path
* &#91;Path&#93; Allow to close path
* &#91;Path&#93; Allow to specify path up axis in Properties
* &#91;Path&#93; Add a vertex control menu to the contextual toolbar
* &#91;Path&#93; Introduce paint/erase/smudge modes to the path tool
* &#91;Path&#93; Create visual feedback for paths in the viewport
* &#91;Path&#93; Add a visual indicator for path direction
* &#91;Path&#93; Add line thickness to path display settings
* &#91;Path&#93; Allow to hide paths UI
* &#91;Path&#93; Add Path panel to list paths of currently selected layer
* &#91;Path&#93; Add visual feedback when hovering over a path in the Path panel
* &#91;Path&#93; Display path panel whenever the Path tool is selected
* &#91;Path&#93; Allow to rename, delete, copy, cut, duplicate path in Path panel
* &#91;Path&#93; Display message when trying to interact in the 2D viewport with the Path tool
* &#91;Library&#93; Integrate new content (path tools and base materials)
* &#91;Dynamic Strokes&#93; Add distance property for dynamic strokes
* &#91;Dynamic Strokes&#93; Add size and spacing properties to dynamic strokes
* &#91;Dynamic Strokes&#93; Add start/middle/end property for dynamic strokes
* &#91;Python&#93;&#91;USD&#93; Expose project configuration parameters for the USD format
* &#91;Python&#93;&#91;USD&#93; Expose project creation parameters for the USD format
* &#91;Export&#93;&#91;USD&#93; Add project path information inside exported USD file
* &#91;GLTF&#93; Update textures in library when reloading a GLTF file
* &#91;Shader&#93; Reduce seam artifacts for UV islands with different orientation
* &#91;Engine&#93; Update to Substance engine version 9.0

<b>Fixed:</b>

* &#91;Import&#93; Some GLB with textures do not get textures in Painter
* &#91;AMD&#93; Artefacts on borders for all 3D projection fills
* &#91;Engine&#93; Textures break when toggling layer visibility
* &#91;Engine&#93; Textures are empty in some places when changing blending mode
* &#91;Engine&#93; Texture/Projection is empty warp mode in some cases
* &#91;Iray&#93; Iteration reset to 0 when saving render
* &#91;Log&#93; USD error message when doing File &gt; New

<b>Known Issues:</b>

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Layer Stack&#93; Input source not saved per layer

## Version 8

### 8.3.1

Release date: <b>2023/04/27</b>

<b>Added:</b>

* &#91;Baking Mode&#93; Add (empty) shortcut to show/hide the viewport visualization
* &#91;Baking Mode&#93; Always show Low Poly when using "Hide baking meshes" button
* &#91;Baking Mode&#93; Show suffix for Matching By Name based on current Texture Set
* &#91;Import&#93; Add support for GLTF binary files (glb)
* &#91;Texture Set list&#93; Add menu to select or create shader instances
* &#91;Texture Set list&#93; Allow to quickly change Texture Set and UV Tile resolution
* &#91;Physical Size&#93; Improve manipulator behavior when using physical size in UV projection
* &#91;UI&#93; Bring back 'Save as' to main File menu
* &#91;UI&#93; Save view selection (2D only, 3D only, both) in UI layout
* &#91;USD&#93; Less vague error message at project creation with unsupported USD shapes
* &#91;Python&#93; Add baking events to follow Baking progress
* &#91;Python&#93; Allow to cancel a bake
* &#91;Python&#93; Expose 'Based on output template' for File Type and Bitdepth in export
* &#91;Python&#93; Expose refresh time for TextureStateEvent.Update

<b>Fixed:</b>

* &#91;Crash&#93; Rare crash when closing a project
* &#91;Crash&#93; &#91;Baking&#93; Activate mesh map sync with Height or curvature on specific project
* &#91;Crash&#93;&#91;Scripting&#93; Crash when adding a material after shader instance creation
* &#91;Baking Mode&#93; AO intensity in neutral material has no effect
* &#91;Baking Mode&#93; Crash when switching to baking mode before model is loaded
* &#91;Baking Mode&#93; Missing error message in Baking Process tab
* &#91;Baking Mode&#93; Neutral material settings have no effect after re-importing a mesh
* &#91;Baking Mode&#93; Viewport separator is saved globally and not per mode
* &#91;Baking Mode&#93; Visualisation issue: average normal doesn't change the cage surface
* &#91;Color Management&#93; Auto detect color space setting is disabled when OCIO env var is present
* &#91;Content&#93; Mask Outline filter has artefact with height input
* &#91;Content&#93; Slope blur filter intensity slider is clamped at 1.0
* &#91;Interop&#93; Unable to create project with GLTF from Sampler
* &#91;Layer Stack&#93; Projection tiling value is not updated correctly with manipulator
* &#91;Linux&#93; Offset between graphic tablet pen and cursor with HDPI higher than 100%
* &#91;Python&#93; Crash when re-importing a mesh after creating a project
* &#91;Substance&#93; 3D noises are broken after re-importing a mesh
* &#91;UV Tiles&#93; Offset for UV projection is clamped to 1
* &#91;Viewport&#93; Straight lines visual feedback is not visible anymore
* &#91;WhatsNew&#93; Incorrect line return on feature titles

<b>Known Issues:</b>

* &#91;Import&#93; Some GLB with textures do not get textures in Painter

### 8.3.0

*(Released: January 10, 2023)*  
Summary: <b>Major release with new baking mode, new import and export of USD files, and physical size support for UV projection</b>

<b>Added:</b>

* &#91;Baking Mode&#93; New baking mode dedicated to baking process
* &#91;Baking Mode&#93; Set shortcut to switch to baking mode to F8
* &#91;Baking Mode&#93; Add Start and Cancel baking button in the viewport
* &#91;Baking Mode&#93; Add baking selection in Texture Set list
* &#91;Baking Mode&#93; Add new Mesh Map Bakers window to select bakers
* &#91;Baking Mode&#93; Add new Mesh Map Settings window to edit baking settings
* &#91;Baking Mode&#93; Add new Baking Log window to follow baking process
* &#91;Baking Mode&#93; Add baking parameters and undo actions to history window
* &#91;Baking Mode&#93; Add breadcrumbs in Mesh Map Settings
* &#91;Baking Mode&#93; Add mesh maps thumbnails in the Mesh Map Bakers window
* &#91;Baking Mode&#93; Add visualization settings collapsible menu in 3D viewport
* &#91;Baking Mode&#93; Add visualization setting to show/hide the high-poly mesh
* &#91;Baking Mode&#93; Add visualization setting to show/hide the cage mesh and wireframe
* &#91;Baking Mode&#93; Add visualization setting to show/hide the low-poly mesh
* &#91;Baking Mode&#93; Add visualization setting to show hard edges without UV seams as errors
* &#91;Baking Mode&#93; Inform in viewport about mesh and bake errors if Baking Log is not visible
* &#91;Baking Mode&#93; Add action to synchronize baker settings across all Texture Sets

  In the Mesh Map Bakers window, each baker (as well as the common settings) can be synced across Texture Sets by clicking on the link icon next to their name. This action will open a window which allows to select which Texture Sets will share the same parameters.
* &#91;Baking Mode&#93; Add actions to copy and paste baker settings

  In the Mesh Map Bakers window are available actions to copy and past each baker settings across Texture Sets either via the dedicated menu at the top of the window or the right-click contextual menu.
* &#91;Baking Mode&#93; Add button in Baking Log to jump from error to the right settings

  When a baker fails or a mesh doesn't load properly, an error message appears in the Baking Log. A button next to the message allows to change the Mesh Map Bakers and Mesh Map Settings window to show the related settings. This help isolate more easily the source of an issue to be able to fix it.
* &#91;Baking Mode&#93; Add menus to manage Texture Sets and Baker selections

  In both the "Texture Set list" and "Mesh Map Bakers" window have been added a little action menu to help copy, invert selections.
* &#91;Baking Mode&#93; Split baker selection list per Texture Set
* &#91;Baking Mode&#93; Split common settings per Texture Set
* &#91;Baking mode&#93; Load high-poly and cage meshes without freezing the interface
* &#91;Baking Mode&#93; Use the viewport progress bar to show mesh loading
* &#91;Baking Mode&#93; Add mesh loading state in Baking Log
* &#91;Baking Mode&#93; Allow to turn around mesh in viewport during baking
* &#91;Baking Mode&#93; Set baking order based on current mesh viewport visibility
* &#91;Baking Mode&#93; Display implicit baking cage in viewport

  When not using a custom cage mesh file, an automatic cage mesh will be generated and displayed in the viewport. Its size will we based on the Max Frontal Distance parameter from the baking common settings. The cage mesh is used to indicate how far the matching between the low and high poly will go.
* &#91;Baking Mode&#93; Show matching list of mesh names for Matching By Name in Baking Log
* &#91;Baking Mode&#93; Use neutral material to display 3D model in viewport
* &#91;Baking Mode&#93; Disable engine computation while in baking mode
* &#91;Baking Mode&#93; Display a warning when quitting the app while a bake is in progress
* &#91;Bakers&#93; Update anti-aliasing setting labels

  The anti-aliasing setting values have been renamed to "Supersampling" and with an explicit multiplier number to clarify their behavior.
* &#91;Bakers&#93; Update bakers to version 2.5.7.
* &#91;USD&#93; Import and export Universal Scene Description (USD) files
* &#91;USD&#93; Add USD options to the New Project window when selecting a USD file
* &#91;USD&#93; Add new Scope and Variants selection window

  When importing a USD file, clicking on the change button in the New Project or Project Configuration window allow to select which part and variants of a USD file to import.
* &#91;USD&#93; Add subdivision levels option

  When creating a new project with a USD mesh file that contains subdivisions, it is possible to select the level of subdivisions using a slider. The project will be created with the subdivided mesh. The level can be modifier via Project Configuration.
* &#91;USD&#93; Import USD skinned meshes at specific frame

  When creating a new project with a USD mesh file that contains animation, it is possible to select the frame using a slider which reflects the embedded timeline sequence. The frame can be modifier via Project Configuration.
* &#91;USD&#93;&#91;Export&#93; Add an option to export USD files

  New Export USD check box added to Export textures window. When it is checked, it allows to export USD files as well as texture maps using any template.
* &#91;USD&#93;&#91;Export&#93; Add USD file format to mesh export
* &#91;USD&#93; Rename the existing "USD PBR Metal Roughness" export preset to be more explicit

  The USD export template previously known as 'USD PBR Metal Roughness' is still accessible via Export textures &gt; Output template &gt; USDz (Apple AR).
* &#91;Auto Unwrap&#93; Add Lock orientation for packing

  New option for auto-unwrap settings which allows to preserve the orientation of existing UV islands when using the packing feature. It can be accessed via New project &gt; Auto-unwrap options &gt; UV island orientation.
* &#91;Physical Size&#93; Add setting to automatically use Physical Size in fill effect/layer

  A new option to automatically switch to physical size scale when using a material with embedded physical size has been added. It can be enabled per project via New project or via Edit &gt; Project configuration &gt; Physical size &gt; Switch fill layer scaling to Physical size when assigning materials.
* &#91;Physical Size&#93; Expose physical size for UV projection

  Physical size scaling is now available for UV projections - it enable auto-resizing for a material based on the physical size of a mesh. It can be selected via Scale &gt; Physical size in the Fill layer or effect Properties window.
* &#91;Scripting&#93;&#91;Python&#93; Allow to query the application version
* &#91;Scripting&#93;&#91;JavaScript&#93; Update API to match new baking parameters
* &#91;Scripting&#93;&#91;Python&#93; Baking module: edit baking parameters
* &#91;Scripting&#93;&#91;Python&#93; Baking module: launch/cancel baking
* &#91;Scripting&#93;&#91;Python&#93; Baking module: select curvature method
* &#91;Scripting&#93;&#91;Python&#93; Baking module: selection of bakers/uv tiles
* &#91;Scripting&#93;&#91;Python&#93; Baking module: synchronize baker settings across all Texture Sets
* &#91;SVT&#93; Enable sparse hardware support on AMD GPUs

  Hardware acceleration for the Sparse Virtual Textures system can now be enabled with AMD GPUs. This setting is automatically enabled in the general preferences.
* &#91;Projection&#93; Rename Cylindrical projection parameters

  The parameter "Cylinder Cap Culling" has been renamed to "Backface Culling" to better represent its action. The associated tooltip as been adjusted accordingly.
* &#91;Project&#93; Save application version in project and retrieve it via scripting

  Since version 8.2, the version of the application is now stored inside the spp file when saving.  
  This version number can be retrieved with the function last\_saved\_substance\_painter\_version() in the project module of the Python API.  
  For project made before 8.2, the returned value will be null.
* &#91;Import&#93; Improve general import time of 3D models

  We improved the general import time of meshes. For example reducing the waiting time when loading high-poly meshes for baking. This optimization applies in particular to the loading of OBJ files.

<b>Fixed:</b>

* &#91;Crash&#93; Changing channels on filter with specific stack
* &#91;Mac&#93;&#91;M1&#93; Crash when creating a fill layer and leaving the layer stack

  This issue can be fixed by updating to Mac OS 13 (Ventura).
* &#91;Scripting&#93;&#91;Python&#93; Crash when using ui.add\_dock\_widget() with wrong type
* &#91;Baking&#93; Incomplete error message in log when a bake fails
* &#91;Baking&#93; Memory is not freed when baking is finished
* &#91;Engine&#93; Texture cache doesn't update when changing effect visibility
* &#91;Export&#93; 2D View exports randomly uniform map
* &#91;Project&#93; Memory allocation error when saving project with big mesh
* &#91;Viewport&#93; TAA causes artifacts when painting in some cases

<b>Known Issues:</b>

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Layer Stack&#93; Input source not saved per layer

### 8.2.0

*(Released: October 06, 2022)*   
Summary: **Major release with new onboarding panels (new welcome panel and what's new panel), export to SBSAR, effects for folder, several improvements for quality of life and bug fixes.**

**Added:**

* &#91;Onboarding&#93; Onboarding panel to welcome new users

  Added a new Welcome screen when new CC users open Painter for the very first time.
* &#91;Onboarding&#93; What's new panel to improve new features discoverability

  Added a new What's New screen which displays main new features. It is shown automatically the very first time Painter is opened after a major update, and can be accessed again via Help &gt; What's new.
* &#91;Onboarding&#93; Rename old Welcome to "Home screen"

  Old Welcome screen renamed Home screen to avoid confusion with the new Welcome screen.
* &#91;UI&#93; Resolve scaling issues for high-DPI screens

  Improved Painter UI adaptation on high definition screens with custom display scaling.
* &#91;UI&#93; Avoid persistent error messages in the UI

  Error messages from previous projects are now removed from the bottom status bar.
* &#91;UI&#93; Rework save menu

  Additional save options are now grouped in a sub-menu and some are renamed for consistency.
* &#91;UI&#93; Save and Export/Share UI layouts

  Inside the Window menu are new actions to save the UI layout into files and to reload them. The Painting and Rendering layouts are saved separately.  
   Various functions have been added to "substance\_painter.ui" to save, reset and load UI layouts as well.
* Add copy/paste actions for blending modes/opacity of a layer

  Added a new entry 'Blending options' in layers' right-click menu. It allows to copy and paste the blending mode and opacity of all channels from one layer to another.
* Apply blending mode/opacity to all channels of a layer

  Added a right-click functionality to layers' blending mode and opacity which allows to apply the currently clicked setup to all channels.
* Reload mesh with a keyboard shortcut (CTRL+SHIFT+R)

  Added an editable shortcut to reload the mesh file with last available settings. Can also be accessed via Edit &gt; Reimport mesh.
* Reset Substance parameters to default

  Added a new button in Properties at the bottom of .sbsar resources which allows to reset the resource to default.
* Reset paint brush to default

  Added a new menu to the Brush section in Properties which allows to reset to default basic brush.
* Right click to reset individual Substance parameters to default

  Added the possibility to reset individual parameters within an .sbsar resource via right-click.
* &#91;Assets panel&#93; "Pin" favorite assets to appear on top of asset panel

  Added a new right-click option to library assets that allows to pin them as favorites to the top of the panel. You can also view all your favorite assets via Saved Searches.
* &#91;Assets panel&#93; Delete, reload and rename assets

  Added right-click menu options to delete, reload and rename assets in the user library. They are deleted directly from their library location on disk and reloaded from original location. Assets that are part of a package like .abr or .sbsar cannot be edited individually.
* &#91;Color Selection&#93; Add blending modes to Color Selection effect
* &#91;Layer Stack&#93; Add blending mode and opacity on filters
* &#91;Layer stack&#93; Allow tiling values bigger than 128 for fill layer/effects
* &#91;Layer stack&#93; Cylinder caps for cylindrical projection in fill layer/effect

  Cylindrical projection in Fill layer properties now has the option to remove cylinder caps.
* &#91;Log&#93; Show an error message if mesh part are in negative space when trying to create a UV Tile project

  Added a clearer error message when failing to create a UV Tile project because UV parts are found in negative spaces.
* &#91;Project&#93; Indicate version in error message "data too recent" when opening a project

  When opening a project that is too recent for the application, the error message will now indicate the version of the project to make it easier to identify the right application version.
* &#91;Viewport&#93; Allow to light the mesh from underneath

  Added a new Environment Alignment parameter in Display Settings &gt; Camera &gt; Environment settings to align the environment map lighting to the camera when set to "Local".
* &#91;Viewport&#93; View R, G, B and Alpha in viewport (solo display mode)

  Under Display Settings &gt; Viewport Settings &gt; Channel display there is a new Color channels setting that allows to only display the R, G, B or Alpha component of a channel when in single display mode.
* &#91;Shader&#93; Allow to set User channels as RGBA in Material Layering shaders

  When setting the Texture Set channels configuration inside a shader for material layering, it is now possible to specify the format of the channel to deviate from the default value. This allows notably to request color user channels instead of grayscale only.
* &#91;Export&#93; Allow to export textures as SBSAR

  When exporting textures via the File &gt; Export Textures window the SBSAR (Substance Archive) file format can be chosen to regroup them together. The content of the SBSAR is driven by the output template used.  
   The SBSAR file format can also be set in the export presets. When using hybrid configuration (SBSAR + Other format) textures that target an SBSAR are grouped together while the rest is exported alongside.
* &#91;Export&#93; Expose 16bit option for EXR file format

  When exporting EXR texture files, it is now possible to chose 16f bit (Half-Float) or 32f bit (Float) in the Export Textures window (both for export settings and export presets). Old projects and old export presets will default to 16f bit to reflect the old behavior.
* &#91;Python&#93; Add event to know when Texture Sets are modified

  The new "substance\_painter.event.TextureStateEvent" allows to know when a Texture Set has been modified either because of a paint stroke, a new channel added or a channel removed.
* &#91;Python&#93; Allow to get and set Mesh Map resources in Texture Set settings

  New functions have been added in "substance\_painter.project" module to get and set mesh maps resources. These functions can be used to update the mesh maps referenced by the Texture Set settings.
* &#91;Plugins&#93; Remove option to get other JS plugins

  Removed the option to get JavaScript plugins since they were hosted on the deprecated Share website.
* &#91;Content&#93; Add new Roblox template and export preset

  A new Roblox "Material Variant" and "Surface Appearance" project template and export preset have been added to make it easier to export PBR textures to Roblox. The template can be accessed via the File &gt; New project window.
* Update Substance Engine to last version (8.6.3)
* &#91;Steam&#93; Optimized build for Apple Silicon chipset (Apple M1 / M2)

**Fixed:**

* Crash when using 16k exr
* &#91;Crash&#93; Ctrl Z After deleting a shader instance
* &#91;Iray&#93; IoR is blocked to 1 for some shaders
* &#91;Win&#93;&#91;Baking&#93; Some high-poly fail to load
* &#91;Color Management&#93; Incorrect color space name in UI with filters
* &#91;Python&#93; Resource objects returned by import function don't have a type

  When importing a Substance package in Python the function was returning the package instead of its graph(s). The resource module now provides functions and parameters to retrieve the graph(s) of a Substance package.

**Known Issues:**

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Layer Stack&#93; Input source not saved per layer
* &#91;Painting&#93; Temporal anti aliasing causes artifacts when painting in some cases
* &#91;Export&#93; 2D View exports randomly uniform map

### 8.1.3

*(Released: August 25, 2022)*   
Summary: **Minor bugfix release**

**Added:**

* Update to Iray SDK 1.6

**Fixed:**

* &#91;Shader&#93; Crash with old faulty shader
* &#91;Material Layering&#93; Materials can disappear when reopening a project

**Known Issues:**

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Layer Stack&#93; Input source not saved per layer
* &#91;Crash&#93; Ctrl Z After deleting a shader instance
* &#91;Iray&#93; IoR is blocked to 1 for some shaderss

### 8.1.2

*(Released: July 19, 2022)*   
Summary: **Minor bugfix release**

**Added:**

* &#91;Auto Unwrap&#93; New option "Optimize for organic meshes" to select the segmentation algorithm
* &#91;Physical Size&#93; Expose unit options in New Project and Project Configuration
* &#91;Color Management&#93; Use monitor Display by default when using ACE
* &#91;Color Management&#93;&#91;Python&#93; Take into account ACE env-var preset file when creating project
* &#91;Color Management&#93; Reset Color Management settings in New Project window when the configuration changes
* &#91;Color Management&#93; Disable OCIO settings access when env-var is present
* &#91;Color Management&#93; Safely update ACE settings when a parameter does not exist anymore
* Update Substance Engine to version 8.6.0
* &#91;Export&#93; Add new GLTF export preset with Displacement support
* &#91;Scripting&#93;&#91;Python&#93; Retrieve resource information (including custom metadata)
* &#91;Scripting&#93;&#91;Python&#93; Add function to query list of mesh names per Texture Set
* &#91;Content&#93; Add new Blender template and export preset

**Fixed:**

* &#91;MacOS&#93; Crash when launching Iray in some cases
* &#91;Thumbnails&#93; Shelf thumbnails do not load properly
* Multiple UV channels are ignored
* &#91;Auto Unwrap&#93; Unnecessary computation when splitting long islands
* &#91;Auto Unwrap&#93; Option avoid elongated islands not taken into account
* &#91;Auto Unwrap&#93; Loss of extra data (vertex colors) when repacking UVs
* &#91;UI&#93; Horizontal scrollbar in properties window when Color Management is enabled
* &#91;Color Management&#93; OCIO configs are missing substance\_3d\_painter\_standard\_srgb role
* &#91;Generator&#93; Wrong usage of User data "disabled"
* &#91;Color Management&#93; Color Space "Not Compatible" dropdown should not be clickable
* &#91;Color Management&#93;&#91;Shader&#93; sRGB override define doesn't work anymore
* &#91;Generator&#93; Wrong usage of User data "disable"
* &#91;Layer stack&#93; Broken previews with UV Tiles projects
* &#91;Shader&#93; API documentation is not fully up to date with Bent Normals
* &#91;Export&#93;&#91;Interoperability&#93; Cannot send to Stager with special characters
* &#91;Content&#93; Some brush presets thumbnails are empty or too dark

**Known Issues:**

* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors
* &#91;Layer Stack&#93; Input source are not saved per layer
* &#91;Crash&#93; Ctrl Z After deleting a shader instance
* &#91;Iray&#93; IoR is blocked to 1 for some shaders
* &#91;Shader&#93; Crash with old faulty shader

### 8.1.1

*(Released: June 28, 2022)*   
Summary: **Minor release hotfix**

**Added:**

* &#91;Layer Stack&#93; Alt click on mask does not deselect effects anymore

**Fixed:**

* &#91;Crash&#93; Opening old project saved in solo view mode
* &#91;Crash&#93; Delete a Generator in properties
* &#91;Texture Set Settings&#93; Normal/Ambient Occlusion mixing and height to normal methods are broken
* &#91;Export&#93; Export textures using diffusion padding renders black maps

**Known Issues:**

* &#91;MacOS&#93; Crash when launching Iray on Monterey
* &#91;Preview Thumbnail&#93; Simplified thumbnails are not updated when an anchor is used
* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors

### 8.1.0

*(Released: June 07, 2022)*   
Summary: **Major release with ICC support, material scaling based on physical size data, new bakers, color eye dropper improvements, and a range of additional content**

**Added:**

* &#91;Color Management&#93; Add support for ICC profiles with Adobe Color Engine (ACE)
* &#91;Color Management&#93; Add support for "Adobe 98 RGB" as working color space for ICC
* &#91;Color Management&#93; Allow to configure ACE/ICC settings via a configuration file
* &#91;Color Management&#93; Allow to input linear color values in Color Picker with Legacy mode
* &#91;Color Management&#93; Allow to specify the color profile used for picking color outside the UI
* &#91;Color Management&#93; Remember the last Display value chosen in the viewport
* &#91;Color Management&#93;&#91;Substance&#93; Make generators/filters work properly with Color Management
* &#91;Color Management&#93;&#91;Substance&#93; Add new colorspace override keywords $working and $standardsrgb
* &#91;Physical Size&#93;&#91;Engine&#93; Extract physical size info from mesh
* &#91;Physical Size&#93;&#91;Engine&#93; Physical size computation
* &#91;Physical Size&#93; Expose options to use physical size in the UI
* &#91;Physical Size&#93; Add visual helpers in the viewport
* &#91;Baking&#93; Add Height baker
* &#91;Baking&#93; Add Bent Normals baker
* &#91;Baking&#93; Add Opacity baker
* &#91;Eye Dropper&#93; New color eye dropper preview next to the mouse and color managed
* &#91;Eye Dropper&#93; Color picker panel reappears at its last position when reopened
* &#91;Eye Dropper&#93; A new icon for the Material Picker
* &#91;Eye Dropper&#93; Color manage the channel preview of the color picker
* &#91;Eye Dropper&#93; Add click-to-select functionality to the eyedropper
* &#91;Eye Dropper&#93; Material picker no longer activates non-active channels
* &#91;Eye dropper&#93; Allow to use eyedropper with a shortcut
* &#91;Eye dropper&#93; Eyedropper picks up the relevant channel, when applicable
* &#91;Eye dropper&#93; Entering the color picker mode deactivates all shortcuts
* &#91;Eye dropper&#93; Remove auto selection of the hex field
* &#91;Eye dropper&#93; Don't close the panel when using the material picker
* &#91;Eye dropper&#93; New disabled state when channel is unavailable to pick
* &#91;Export&#93; Add tangent attribute to glTF export
* Update Substance Engine to v8.4
* Update Auto Unwrap to 0.9.0
* Update to Qt 5.15.8
* Update to Python 3.9
* &#91;Shader&#93; Add support for Bent Normals shading
* &#91;MacOS&#93; Support of 3DConnexion SpaceMouse
* &#91;Python&#93; Document the Python version used in the API
* &#91;Content&#93; Add 6 new 3D noises with 105 presets
* &#91;Content&#93; 20 new grunge maps and 2 cloth folds patterns
* &#91;Content&#93; Update "Mesh maps" export preset to use new bakers
* &#91;Content&#93; Blur Slope and warp filter depends on texture set resolution
* &#91;Content&#93; Update sample projects to use the 3 new bakers

**Fixed:**

* &#91;glTF&#93; Cannot open glTF with special character
* &#91;Engine&#93; Artefacts with anisotropy and SVT disabled
* &#91;MacOS&#93;&#91;M1&#93; Smart materials are not displayed correctly
* &#91;Mesh Processing&#93; Cannot import meshes from Modeler
* &#91;UI&#93; Horizontal scrollbar in new project window with Color Management enabled
* &#91;Color Management&#93; Working space value missing in color picker with some OCIO configs
* &#91;Color Management&#93; Brush preview in the viewport is not color managed
* &#91;SpaceMouse&#93; Pivot is not updated immediately with focus change and sometimes out of the model
* &#91;Export&#93;&#91;USD&#93; Exported USD files have a wrong structure
* &#91;USD&#93; Ambient Occlusion issue when exporting
* &#91;Content&#93; Update thumbnail's mesh to match Preview Sphere sample project

**Known Issues:**

* Export textures using diffusion padding renders black maps
* Normal/Ambient Occlusion mixing is broken
* &#91;MacOS&#93; Crash when launching Iray in some rare cases
* &#91;Preview Thumbnail&#93; Simplified thumbnails aren't updated when an anchor is used
* &#91;Color Management&#93; HDR color space conversions with ACE on Linux produce clamped colors

## Version 7

### 7.4.3

*(Released: April 11, 2022)*   
Summary: **Bugfix with support of 3Dconnexion SpaceMouse in 2D Viewport**

**Added:**

* &#91;SpaceMouse&#93; Support of 3DConnexion SpaceMouse in 2D Viewport

**Fixed:**

* &#91;Color Picker&#93; Cannot write in hexadecimal field
* &#91;Color Management&#93; Resources used in projection mode are not color managed in the overlay
* &#91;Color Management&#93; Errors are not reported in log
* &#91;SpaceMouse&#93; Remove generic error message if user does not have a SpaceMouse
* &#91;SpaceMouse&#93; When loading a project, pivot point is always hidden
* &#91;Bakers&#93; "Average normals" setting has no effect in UV Tile projects
* &#91;UV Tile&#93; Inactive uv tiles overlays disappear when reloading mesh with different tiles
* &#91;Scripting&#93;&#91;Python&#93; Remote scripting is broken
* &#91;Scripting&#93;&#91;Python&#93; Several channels cannot be queried from API and it raises an error
* &#91;Scripting&#93;&#91;Python&#93; Crash when using ProjectEditionEntered event
* &#91;Scripting&#93;&#91;Python&#93; Crash when calling get\_active\_stack()

**Known Issues:**

* 3Dconnexion SpaceMouse not supported on MacOS
* &#91;UI&#93; Horizontal scroll bar with color management appearing in some cases in new project window
* &#91;Mac M1&#93; Smart materials are not displayed correctlys

### 7.4.2

*(Released: March 08, 2022)*   
Summary: **Bugfix with support of 3Dconnexion SpaceMouse and color management (OCIO) improvements**

**Added:**

* &#91;SpaceMouse&#93;&#91;Windows&#93; Support of the 3Dconnexion SpaceMouse in the 3D Viewport for navigation
* &#91;SpaceMouse&#93;&#91;Windows&#93; Basic shortcuts/keys for Pro and Enterprise SpaceMouse models in the 3D Viewport
* &#91;SpaceMouse&#93;&#91;Windows&#93; Dedicated rotation center icon in the 3D Viewport
* &#91;Color Management&#93; Use roles from OCIO configuration to change default settings
* &#91;Color Management&#93; Color manage the properties window for color widgets
* &#91;Color Management&#93; Color manage the properties window for material preview
* &#91;Color Management&#93; Color manage swatches in color picker
* &#91;Color Management&#93; Add a setting to define the standard sRGB color space
* &#91;Color Management&#93; Add the Standard sRGB color space from OCIO config in color picker Display selector list
* &#91;Color Management&#93; Improvements for color space override menu
* &#91;Color Management&#93; Allow to override the environment map color space in Display Settings
* &#91;Color Management&#93; Draw color picker gradients based on current Display
* &#91;Color Management&#93; Clamp HDR values by default in color editor
* &#91;Color Management&#93; Use passthrough (no color space) for filters in Legacy mode
* &#91;Color Management&#93; Limit gradients display in color editor to match &#91;0-1&#93; range
* &#91;Color Management&#93; Hide Display selector in color picker in Legacy mode
* &#91;Color Management&#93; Make color picker hexadecimal field always in sRGB color space
* &#91;Color Management&#93; Disable color picker Display dropdown for data channels
* &#91;Optimization&#93; Warp grid recomputes only covered UV tiles
* &#91;Export&#93; Allow to export UV Tile projects for Sketchfab, USD and glTF
* &#91;Scripting&#93;&#91;Python&#93; Allow to change tonemapping function

**Fixed:**

* &#91;Sketchfab&#93; Updating existing model ends up creating new model
* &#91;Sketchfab&#93; Crash when searching for previously updated model
* Crash when exporting to USD
* Crash when creating a new shader instance in Geometry Mask or when geometry is hidden
* &#91;Import Asset Window&#93; Crash when changing the type of imported resources
* Normal mesh maps are inverted when used in layer stack
* &#91;Substance&#93; User data blending mode is not taken into account
* &#91;Color Management&#93; Bitmaps with color space in filename are imported as UV Tile sequences
* &#91;Color Management&#93; Color managed outputs of Substance graph are in wrong color space
* &#91;Color Management&#93; Polygon Fill tool displays the wrong color
* &#91;Color Management&#93; ACES tonemapper is applied to channels in solo mode
* &#91;Color Management&#93; Tool preview sphere lighting is not color managed
* &#91;Color management&#93;&#91;Export&#93; Converted maps applies an incorrect conversion
* &#91;Scripting&#93;&#91;Python&#93;&#91;Color Management&#93; Projects created with template &amp; OCIO environment variable are in Legacy mode
* &#91;Scripting&#93;&#91;Python&#93; Cannot use the JavaScript evaluate function on startup
* &#91;3D Adobe Offer&#93; Can not launch Painter when using regional settings with languages not supported by default

**Known Issues:**

* 3Dconnexion SpaceMouse not supported on MacOS
* &#91;UI&#93; Horizontal scroll bar with color management appearing in some cases in new project window
* &#91;Bakers&#93; "Average normals" setting has no effect in UV Tile projects
* &#91;Mac M1&#93; Smart materials are not displayed correctly
* &#91;Color Management&#93; Resources used in projection mode are not color managed in the overlay
* &#91;Color Picker&#93; Cannot write in hexadecimal field

### 7.4.1

*(Released: December 14, 2021)*   
Summary: **Bugfix with color management improvements**

**Added:**

* &#91;Color Management&#93; Use data role in exported filenames
* &#91;Color Management&#93; Expand the section Color Management, by default, when OCIO is selected in new project and project settings windows
* &#91;Color Management&#93; Add ACES tonemapper in legacy mode
* &#91;Color Management&#93; Adjust default configuration settings
* &#91;Color Management&#93;&#91;Export&#93; Fill $colorSpace in filenames for data channels
* &#91;Export&#93; Export UV Tile project to Stager
* &#91;Interoperability&#93; Not available for Steam and Substance editions
* &#91;Interoperability&#93; Allow to send a UV Tile project to Stager

**Fixed:**

* &#91;MacOS&#93;&#91;Crash&#93; Painter does not start with Catalina
* &#91;Color Management&#93;&#91;Crash&#93; Random crash when playing with data type/color management on user channel
* &#91;Color management&#93; Resources used as grayscale in mask display color space new menu
* &#91;Color Management&#93; User channel is darker in the viewport in legacy mode + solo view
* &#91;Color Management&#93; Env map is always linear when used in iRay
* &#91;Color Management&#93; Color picker does not pick the right value for data channel in legacy mode
* &#91;Color management&#93; Color picker is broken inside of a Substance in legacy mode
* &#91;Color management&#93; Switching between solo channel views in the viewport does display with the right color space when using the dropdown menu
* &#91;Color Management&#93; Export applies the wrong conversion on color managed user channels in legacy mode
* Strokes made in solo view mask are not shown when switching back to material view
* &#91;Export&#93; Converted maps are not exported as color managed channels
* &#91;Texture Set&#93; Tooltip with original name is missing on renamed user channels
* &#91;Steam&#93; Files missing when checking file integrity with Steam

**Known Issues:**

* &#91;Mac M1&#93; Smart materials are not displayed correctly

### 7.4.0

*(Released: November 24, 2021)*   
Summary: **Major release. Introduction of the 1st version of color management, undock 2D or 3D view, new option for auto UV unwrapping for avoiding elongated islands, call JavaScript functions from Python API and new content**

**Added:**

* &#91;Color Management&#93; Support of Color Management OpenColorIO version 2
* &#91;Color Management&#93; Add color management settings to project settings
* &#91;Color Management&#93; Warning window about Color Management configuration changes when opening a project
* &#91;Color Management&#93; Display an error message if an invalid OCIO config file is selected
* &#91;Color Management&#93; Allow to override configuration with OCIO environment variable
* &#91;Color Management&#93; Multiple OCIO configurations integrated by default with the application
* &#91;Color Management&#93; Extract color space name from imported bitmap filename
* &#91;Color Management&#93; Allow to override the color space with one color space from the configuration in Properties window
* &#91;Color Management&#93; Add color management options in Texture Set Settings
* &#91;Color Management&#93;&#91;Viewport&#93; Allow to color manage 2D and 3D views separately
* &#91;Color Management&#93; Load and convert environment map to the working color space
* &#91;Color Management&#93; Adjust color picker and editor with current color space
* &#91;Color Management&#93; Allow to select the display transform color space in the viewport with a new dropdown menu
* &#91;Color Management&#93; Apply display transform with Iray rendering results
* &#91;Color Management&#93; Export textures with different color spaces
* &#91;Color Management&#93;&#91;Python&#93; Apply color management settings from Environment variable (OCIO) to new projects
* &#91;Viewport&#93; Allow to undock the 2D or 3D viewport
* &#91;Auto Unwrap&#93; New option to avoid elongated islands
* &#91;Scripting Python&#93; Call JavaScript functions from Python API
* &#91;New Project Window&#93; Make the imported maps section collapsible
* &#91;Projection&#93;&#91;Warp&#93; Allow to hide normals as an option in the Warp settings
* &#91;Content&#93; 11 new grunge maps
* &#91;Content&#93; 8 new tool presets (zipper, tightening cord, glitter)
* &#91;Content&#93; 8 new materials (scar, pocket, ...)
* &#91;Content&#93; 1 new generator (inflate shrinkwarp)

**Known Issues:**

* &#91;Mac M1&#93; Smart materials are not displayed correctly
* &#91;Color Management&#93;&#91;Crash&#93; Random crash when playing with data type/color management on user channel
* &#91;Color Management&#93; Color picker does not pick the right value for data channel in legacy mode
* &#91;Color management&#93;&#91;Iray&#93; Saving the render in EXR or TIFF while Color Management is activated in the viewport will always save in linear
* &#91;Color management&#93; Resources used as grayscale in mask display the wrong Color Space menu
* &#91;Color Management&#93;&#91;Iray&#93; Env map is always linear when used in Iray
* &#91;Color Management&#93;&#91;Export&#93; Converted maps are not exported as a color managed channels
* &#91;Color Management&#93;&#91;Export&#93; Export ignores if user channel is color managed or not with legacy mode

### 7.3.1

*(Released: November 24, 2021)*   
Summary: **Bugfix**

**Added:**

* &#91;Projection&#93; Scaling should only work in Object Space

**Fixed:**

* &#91;Mac M1&#93; Material layering not working
* &#91;Mac M1&#93;&#91;Projection&#93; Warp does not work
* Micro details are not displayed properly
* &#91;Projection&#93;&#91;Crash&#93; Switching to warp mode with a layer created with a previous version
* &#91;Projection&#93;&#91;Warp&#93; Flip does not work when transformation is set to world space
* &#91;Projection&#93;&#91;Warp&#93; Split option remains selected after splitting is done
* &#91;Projection&#93;&#91;UV&#93; Pivot point is reset when flipping projection
* &#91;Filter&#93; Bake Lighting environment is changing when reloading or changing a parameter
* &#91;Interoperability&#93; Not available for Steam and Substance editions
* &#91;Interoperability&#93; The "Browse 3D assets in Marketplace" button should always open CCD in the Stock &amp; Marketplace 3D tab

**Known Issues:**

* &#91;Mac M1&#93; Smart materials are not displayed correctly

### 7.3.0

*(Released: October 13, 2021)*   
Summary: **Major release. It contains a new 3D warp projection, a new cylindrical projection, improvements of the color picker, new functions in Python API and bug fixes**

**Added:**

* &#91;Projection&#93;&#91;Warp&#93; Expose 3D warp as a new projection mode
* &#91;Projection&#93;&#91;Warp&#93; Allow decal mode for Alphas, Textures and Procedurals with drag and drop in the viewport
* &#91;Projection&#93;&#91;Warp&#93; Use warp projection with decal shortcut (ALT)
* &#91;Projection&#93;&#91;Warp&#93;&#91;Toolbar&#93; Transform warp as whole or per vertices
* &#91;Projection&#93;&#91;Warp&#93;&#91;Toolbar&#93; Add grid points with split warp cross wise, horizontally or vertically options
* &#91;Projection&#93;&#91;Warp&#93;&#91;Toolbar&#93; Dedicated menu for reset actions
* &#91;Projection&#93;&#91;Warp&#93;&#91;Toolbar&#93; Option to automatically adjust tangents when moving points
* &#91;Projection&#93;&#91;Warp&#93;&#91;Toolbar&#93; Dedicated menu for grid edition (size, reset, color and handle size)
* &#91;Projection&#93;&#91;Warp&#93; New keyboard shortcut to switch whole-vertices warp edition mode (SHIFT+V)
* &#91;Projection&#93;&#91;Warp&#93; Click+Ctrl allows to switch between surface tool and other tools
* &#91;Projection&#93;&#91;Cylindrical&#93; Expose the cylindrical projection mode
* &#91;Projection&#93;&#91;Toolbar&#93; Group manipulator settings (size, grid steps, angle steps)
* &#91;Color Picker&#93; New color picker UI
* &#91;Color Picker&#93; Use sRGB values in color picker widgets
* &#91;Color Picker&#93; Allow to save and delete color swatches
* &#91;Color Picker&#93; Eyedropper accessible from color and normal slots
* &#91;Color Picker&#93; Allow to edit dynamic color between 0 and 255 values
* &#91;Color Picker&#93; Make HSV/RGB state common across the app
* &#91;Color Picker&#93; Color Picker window is semi persistent
* &#91;Color Picker&#93; Pressing Esc closes the color picker window
* Performance improvement for UI interaction and while painting
* &#91;Engine&#93; Update to new Substance engine version (8.3.0)
* &#91;Scripting&#93;&#91;Python&#93; Allow to reload the mesh of the current project
* &#91;Scripting&#93;&#91;Python&#93; Allow to update resources in projects
* &#91;Scripting&#93;&#91;Python&#93; Allow to set and query the resolution of UV Tiles
* &#91;Interoperability&#93; Not available for Steam and Substance editions
* &#91;Interoperability&#93; Receive multiple resources from Bridge

**Fixed:**

* Color picker does not display the right color
* &#91;Baking&#93; Texture set list are not ordered correctly
* &#91;FBX import&#93; 3ds Max group pivot transformations are not taken into account
* &#91;Substance Engine&#93; Crash with import of corrupted SBSAR
* &#91;MacOS&#93; Project configuration option in different languages is not present
* Autosaves can freeze Painter during long processes

**Known Issues:**

* &#91;Projection&#93;&#91;Warp&#93; Split option remains selected after splitting is done
* &#91;Projection&#93;&#91;Warp&#93; Flip does not work when transformation is set to world space
* &#91;Projection&#93;&#91;Warp&#93; Artifact lines between patches in some rare cases
* &#91;Projection&#93;&#91;UV&#93; Pivot point is reset when flipping projection
* &#91;Mac M1&#93; Smart materials are not displayed correctly
* &#91;M1&#93;&#91;Regression&#93; Material layering not working

### 7.2.3

*(Released: August 24, 2021)*   
Summary: **Minor release, bugfix**

**Added:**

* &#91;Libraries&#93; Add a way to exclude unwanted files from being crawled

**Fixed:**

* &#91;Win&#93; Multi screens and sleep issues
* &#91;MacOS&#93;&#91;Crash&#93; Switching shader when using effects
* &#91;Viewport&#93; Full preview mode no longer shows brush cursor without alpha
* &#91;UI&#93; Angle widget turns the wrong way
* &#91;Layer Stack&#93; Many sub folders create very long freeze
* &#91;Iray&#93; Different views in Iray and OpenGL: Visible if not working
* &#91;Iray&#93; Index of refraction not taken into account and does not appear in mdl properties
* &#91;JavaScript&#93; ShowExportDialog() never returns true
* Can't read mtl from Adobe Stock

### 7.2.2

*(Released: July 27, 2021)*   
Summary: **Minor release, bugfix**

**Added:**

* Upgrade AMD driver requirements version

**Fixed:**

* &#91;Mac M1&#93; Wrong Memory detection
* &#91;Export&#93; Very long paths are not displayed properly

**Known Issues:**

* &#91;Content&#93; Outdated shaders of the samples

### 7.2.1

*(Released: July 02, 2021)*   
Summary: **Minor release, Hotfix**

**Added:**

* &#91;Interop&#93; Add tooltip to inform that sending UV Tile projects to Stager is not yet supported
* &#91;Plugin&#93;&#91;UI&#93; Update of the Livelink icon

**Fixed:**

* &#91;Nvidia&#93; Driver version starting with 30 are considered outdated
* &#91;Libraries&#93; Asset panel state is not saved unless a project is open
* &#91;Libraries&#93; New saved search retains keyword from old saved search
* &#91;Bakers&#93;&#91;UVTiles&#93; ID maps per meshID also take UV Tiles in consideration
* &#91;Export&#93; gLTF files do not import vertex color
* &#91;Iray&#93; Some tooltips missing
* &#91;Interop&#93; Send to Stager is not always disabled when Stager is not detected
* &#91;Resource Updater&#93; Photoshop brush maker cannot be updated
* &#91;Content&#93; Fiber glass edge wear generator is broken

### 7.2.0

*(Released: June 23, 2021)*   
Summary: **Major release, it provides an update to the asset panel, a new shader with access to new channels and parameters, an overall refresh of the UI, some much-requested performance improvements, expanded language support, and more!**

**Added:**

* &#91;Libraries&#93; New Asset panel to replace the shelf
* &#91;Libraries&#93;&#91;UI&#93; New Asset panel layout
* &#91;Libraries&#93;&#91;UI&#93; Change default Asset panel orientation and UI
* &#91;Libraries&#93;&#91;UI&#93; Introduce a list view option to library
* &#91;Libraries&#93;&#91;UI&#93; New breadcrumbs navigation in the Asset panel
* &#91;Libraries&#93;&#91;UI&#93; Select "All libraries" when selecting a saved search
* &#91;Libraries&#93;&#91;UI&#93; Select "All libraries" when all folders are deselected
* &#91;Libraries&#93;&#91;UI&#93; New tag for particle brushes
* &#91;Libraries&#93;&#91;UI&#93; Replaced "shelf" by "All libraries" across the app
* &#91;Libraries&#93;&#91;UI&#93; Allow to hide empty folders
* &#91;Libraries&#93;&#91;UI&#93; Default user library should be visible even if empty
* &#91;Libraries&#93;&#91;UI&#93; New filtering method via asset type icons
* &#91;Libraries&#93; Shortcut "CTRL" to select multiple asset types
* &#91;Libraries&#93; New environment variable to control the asset preview memory budget
* &#91;Libraries&#93;&#91;Content&#93; New environment maps
* &#91;Libraries&#93;&#91;Content&#93;&#91;UI&#93; Render displacement on default materials
* &#91;Libraries&#93;&#91;Content&#93; Set Adobe Standard Material (ASM) shader as default for previews generation
* &#91;Libraries&#93;&#91;Content&#93;&#91;ASM&#93; New Project Templates for new ASM shader
* &#91;Libraries&#93;&#91;Thumbnail&#93; Use new Studio 6 environment map
* &#91;Libraries&#93;&#91;Thumbnail&#93; Read thumbnail in resource instead of generating it
* &#91;Libraries&#93;&#91;Thumbnail&#93; Add displacement to thumbnail generation
* &#91;Texture Set Settings&#93;
* &#91;Texture Set Settings&#93;&#91;UI&#93; Expose new height to normal conversion method
* &#91;Texture Set Settings&#93;&#91;UI&#93; Rework of the channels' UI organization
* &#91;Texture Set Settings&#93; User Channels limit raised to 16 channels
* &#91;Texture Set Settings&#93;&#91;UI&#93; Indicate which channels are compatible with currently selected shader
* &#91;Shader&#93;&#91;ASM&#93; New Adobe Standard Material shader
* &#91;Shader&#93;&#91;ASM&#93; Added support for Anisotropy, Clear Coat, Subsurface Scattering, Specular Edge Color, and Sheen
* &#91;Shader&#93;&#91;ASM&#93; Change default channels' color values
* &#91;Shader&#93;&#91;ASM&#93;&#91;Export&#93; Updated export template Adobe Dimension to Adobe Substance 3D Stager
* &#91;Shader&#93;&#91;ASM&#93; Added labels and tooltips for shader and MDL parameters
* &#91;Shader&#93;&#91;ASM&#93; Make the Scatter Color visible in 2D View even if SSS is not supported
* &#91;Shader&#93;&#91;ASM&#93;&#91;Iray&#93; Support ASM shader in Iray with new MDL
* &#91;Shader&#93;&#91;ASM&#93;&#91;Iray&#93; Updated Subsurface Scattering in legacy PBR spec gloss &amp; coated
* &#91;Shader&#93;&#91;ASM&#93;&#91;Content&#93; Changed the default SSS type for samples
* &#91;Shader&#93;&#91;ASM&#93; Added documentation for ASM API
* &#91;Shader&#93;&#91;ASM&#93; Optimize shaders to ignore unused channels
* &#91;Shader&#93; Expose new Texture Set channels
* &#91;Shader&#93; Improved Subsurface Scattering
* &#91;Shader&#93; Hided new shader parameters for some shaders
* &#91;Shader&#93; Visible if for shader parameters
* &#91;Performance&#93;
* &#91;Libraries&#93; Resource preview loading time and calculation performance improvements
* &#91;Engine&#93; Painting performance improvements
* &#91;Auto Unwrap&#93;
* &#91;Auto Unwrap&#93; Packing performance improvements
* &#91;Auto Unwrap&#93; Auto unwrap compatible with UV Tile workflow
* &#91;Auto-Unwrap&#93; New option to position UVs according to mesh orientation
* &#91;Other&#93;
* &#91;Settings&#93; Changed default zoom direction
* &#91;UI&#93; Overall refresh of the UI
* &#91;UI&#93; Rework of the Help Menu
* &#91;UI&#93; Replace invert icon
* &#91;UI&#93;&#91;Plugin&#93; Replace icon for the plugin dcc link
* &#91;UI&#93;&#91;AMD&#93; Update minimum required version and popup message
* &#91;Layer Stack&#93; Create new layer inside selected empty folder
* Update Python Documentation
* &#91;Branding&#93;
* &#91;Branding&#93;&#91;UI&#93; Updated application name to Adobe Substance 3D Painter
* &#91;Branding&#93;&#91;UI&#93; Updated standalone version to 'Substance edition'
* &#91;Branding&#93;&#91;UI&#93; Updated application executable name, installation path, package and icons
* &#91;Branding&#93;&#91;UI&#93; Renamed default library and path
* &#91;Branding&#93;&#91;UI&#93; Updated About Window
* &#91;Branding&#93;&#91;UI&#93; Updated Welcome screen
* &#91;Branding&#93;&#91;UI&#93; Removed year-based version number
* &#91;Localization&#93; New translations in German, French, and Simplified Chinese
* &#91;Interoperability&#93; Not available for Steam and Substance editions
* &#91;Interoperability&#93; Interoperability with Adobe Ecosystem: Designer, Sampler, Stager, and Bridge
* &#91;Interoperability&#93;&#91;UI&#93; Receive and update asset from Designer
* &#91;Interoperability&#93;&#91;UI&#93; Receive asset from Sampler
* &#91;Interoperability&#93;&#91;UI&#93; Send asset to Stager
* &#91;Interoperability&#93;&#91;UI&#93; Show in Adobe Bridge
* &#91;Interoperability&#93;&#91;UI&#93; Allow to quickly access Adobe 3D Assets
* &#91;Interoperability&#93; New usage tags of sbsar
* &#91;Interoperability&#93; Handle received asset types
* &#91;Interoperability&#93; Asset received from Adobe Substance 3D Designer or Adobe Substance 3D Sampler are stored in user's default chosen library
* &#91;Interoperability&#93;&#91;UI&#93; New icon in left toolbar to send to Stager or Photoshop

**Fixed:**

* &#91;Tablet&#93; Low performance when Painting with pressure
* &#91;Tablet&#93; Issue on tablets with slider controls
* &#91;Crash&#93; Name mismatch between Texture Set list and Exporter
* &#91;Crash&#93;&#91;Libraries&#93; Double click on a sub-library
* &#91;Libraries&#93; Issue when Crawling library directories
* &#91;Libraries&#93; Force preview generation command line does not work as expected
* &#91;Libraries&#93;&#91;Content&#93; Baked Light Environment filter is black by default
* &#91;Linux&#93;&#91;MacOS&#93;&#91;Export Mesh&#93; Cannot import glTF created on Linux/MacOS
* &#91;Linux&#93; Dragging and dropping a file into the Asset panel can lead to a crash
* &#91;Auto-Unwrap&#93; Auto-Unwrap is available even if a mesh has not been selected for reloading
* &#91;Particles&#93; Wrong particle behavior with gravity
* &#91;Layer Stack&#93; Level histogram can only use Luminance with some channels
* &#91;Geometry Mask&#93; Right-click menu on a folder when editing the geometry mask does not work
* &#91;Projection&#93; Seam with spherical projection &amp; bilinear filtering
* &#91;UV Tiles&#93; Export mask to file only exports tile 0, 0
* &#91;Export Mesh&#93; FBX mesh export is empty
* &#91;Iray&#93; Normal map is not taken into account in new projects when rendering
* &#91;Save&#93; Save issues on shared drives
* &#91;Baking&#93; Rebaking a mesh with modified parameters displays a warning
* &#91;Baking&#93;&#91;Regression&#93; Incorrect result when high poly meshes' global bounding box does not include the scene origin
* &#91;Python&#93; Custom user libraries are not taken into consideration

**Known Issues:**

* &#91;Libraries&#93; Saved searches not saved if no project opened
* &#91;NVIDIA&#93; Message for outdated driver even if the driver is up to date

### 7.1.1 (2021.1.1)

*(Released: March 23, 2021)*   
Summary: **Minor release, Bugfix with possibility to enter hexadecimal values in the color picker**

**Added:**

* &#91;Log&#93; Warn users about incompatible AMD GPU drivers
* &#91;Color Picker&#93; Allow to type hexadecimal values

**Fixed:**

* &#91;Baker&#93; Drop in performance
* &#91;Geometry mask&#93; Alt click on mesh name can lead to a crash
* &#91;Engine&#93; Painting does not refresh the entire view when necessary
* &#91;Layer stack&#93; Selection is stuck after changing shader
* &#91;MacOS&#93;&#91;Color picker&#93; Color is slightly different than the one picked
* &#91;Export&#93; Using PSD file format does not generate one file per UV Tile
* &#91;Scripting&#93;&#91;Javascript&#93; alg.mapexport.getPathsExportDocumentMaps() doesn't return all the values
* &#91;Scripting&#93;&#91;Python&#93; Disabled plugins are enabled again when reopening Painter

### 7.1.0 (2021.1.0)

*(Released: January 28, 2021)*   
Summary: **Major release, new Geometry Mask which allows to select and paint parts of the geometry, copy/paste effects in the layer stack, improvement of UV Tile workflow, update of Iray, Bakers, Substance Engine and new content**

**Added:**

* New geometry mask and paint selected parts of the geometry
* &#91;Geometry Mask&#93; Allow to paint selected parts of geometry by mesh names
* &#91;Geometry Mask&#93; Rectangular selection in both viewports
* &#91;Geometry Mask&#93; Allow to hide/ignore excluded geometry on any layer
* &#91;Geometry Mask&#93;&#91;Properties&#93; Quick selection for checkboxes with click and drag
* &#91;Geometry Mask&#93;&#91;Properties&#93;&#91;UI&#93; Include/Exclude all with a dropdown in Properties window
* &#91;Geometry Mask&#93;&#91;Properties&#93; Allow to quickly select one item in a list with ALT+LEFT CLICK
* &#91;Geometry Mask&#93;&#91;Properties&#93; Overlay in viewports when hovering Mesh names/UV Tiles in Properties window
* &#91;Geometry Mask&#93;&#91;Layer Stack&#93; Add Copy/Paste options to the geometry mask
* &#91;Geometry Mask&#93; New icon for Hide/ignore excluded geometry button
* &#91;Geometry Mask&#93; New tooltip for Hide/ignore excluded geometry
* &#91;Geometry Mask&#93; Keyboard shortcut ALT+H to toggle on/off "hide ignore excluded geometry" button
* &#91;UV Tiles&#93;&#91;Layer Stack&#93; New Fill layer sphere preview thumbnail for UV Tiles and simplified mode
* &#91;UV Tiles&#93;&#91;Layer Stack&#93; Allow to easily exit the UV Tile mask
* &#91;UV Tiles&#93;&#91;Texture Set List&#93; Allow to give a description per UV Tile
* &#91;UV Tiles&#93;&#91;Texture Set Settings&#93;&#91;UI&#93; Two new section titles in the dropdown menu to change UV Tile resolution
* &#91;UV Tiles&#93;&#91;Viewport&#93; Exit UV Tile Mask when dragging a material into the viewport
* &#91;Layer Stack&#93; Add Copy/Paste options for effects
* &#91;Layer Stack&#93; Allow to copy/paste effects from one Texture Set to another
* &#91;Layer Stack&#93; Allow multi-selection of effects
* &#91;Layer Stack&#93; Add copy/paste options as shortcuts for layer effects
* &#91;Layer Stack&#93; Automatically switch between mask and content when dragging effects to another layer
* &#91;Layer Stack&#93; Automatically create a mask when pasting a mask from another layer
* &#91;Layer Stack&#93; Add move effect actions inside the effects' contextual right click menu
* &#91;Layer Stack&#93; Allow to drag and drop effects from one layer to another
* &#91;Layer Stack&#93; Dragging items onto a folder places them on the top of the folder
* Update Iray to version 2020.1.0
* &#91;Bakers&#93; Update Bakers to version 2.5.4
* &#91;Bakers&#93; Display individual UV Tiles in the baking progress window
* &#91;Bakers&#93;&#91;UI&#93; Allow to quickly bake the current Texture Set with a new button
* &#91;Bakers&#93; Allow user to quickly select one of the bakers with ALT+LEFT CLICK
* Update Substance Engine to version 8.0.8
* &#91;Substance Engine&#93; Support Default Color in new .sbsar files
* &#91;Auto Unwrap&#93; Performance improvement
* &#91;Export&#93; Add visual feedback to indicate which UV Tile's resolution differs from project's default
* &#91;Export&#93; Add scene size factor into exported shader json file
* &#91;Language&#93; Add Japanese translation
* &#91;UI&#93; Update About window with versioning of internal dependencies
* &#91;Scripting&#93;&#91;Python&#93; Allow to manage Shelf resources
* &#91;Scripting&#93;&#91;Python&#93; Allow to know when a project is ready for baking and exporting
* &#91;Scripting&#93;&#91;Python&#93; Allow to know when a Shelf has finished crawling resources on disk
* &#91;Scripting&#93;&#91;Python&#93; Allow to query the list of UV tiles per Texture Sets
* &#91;Scripting&#93;&#91;Python&#93; Allow to assign custom preview to Shelf resources
* &#91;Scripting&#93;&#91;Python&#93; Allow to manage custom shelves
* &#91;Scripting&#93;&#91;Python&#93; Add a method index in each submodule in the documentation
* &#91;Scripting&#93;&#91;Python&#93; New style for the documentation
* &#91;Scripting&#93;&#91;Python&#93; Improvement of resources and Shelf documentation
* &#91;Content&#93; Three new tool presets to make stitches
* &#91;Shelf&#93; Temporarily remove "Export to Substance Share" while transitioning to the new Substance Share platform

**Fixed:**

* Crash when using monitors with different resolutions
* Crash in Substance Engine with some rare projects
* Viewport refresh fails with Hide/Ignore Excluded Geometry when switching layers
* &#91;2D View&#93; 2D Viewport can be missing on some projects
* &#91;Baking&#93; "Match by mesh name" ignores parts of the object
* &#91;Layer Stack&#93; Clicking on a layer effect opens folder
* &#91;Geometry Mask&#93; UV Tile is still counted in mask even when reimporting the mesh without it
* &#91;Geometry Mask&#93; Right click menu in the viewport does not provide the correct tools
* &#91;Engine&#93; Heavy lags on particular projects
* &#91;Scripting&#93; High latency with remote JSON POST requests on Windows
* &#91;Linux&#93; Vram amount is not detected properly with specific integrated GPUs
* &#91;Auto Unwrap&#93; Crashes or long unwrap on some projects

## Version 6

### 6.2.2 (2020.2.2)

*(Released: September 28, 2020)*   
Summary: **Minor release, Bugfix with some functions in Python API**

**Added:**

* &#91;Performance&#93; Do not compute all UV Tiles when using the color ID selection
* &#91;Bakers&#93;&#91;UI&#93; Display Texture Set descriptions
* &#91;Bakers&#93; Allow to save bake settings
* &#91;Bakers&#93; Add collapse all/expand all options to the Selection tab
* &#91;Texture Set List&#93; Hide description when empty
* &#91;UV Tiles&#93;&#91;Texture Set List&#93; Clicking on UV Tile should expand/collapse list
* &#91;Export&#93;&#91;UI&#93; Allow to resize the Texture Set List panel horizontally
* &#91;Export&#93;&#91;UI&#93; Consistent tooltip text for both UV Tiles and Texture Set workflow with unselected textures
* &#91;Scripting&#93;&#91;Python&#93; Allow to use export presets to export textures
* &#91;Scripting&#93;&#91;Python&#93; Add a changelog in documentation
* &#91;Scripting&#93;&#91;Python&#93; Allow to query all the available channels on a given stack
* &#91;Scripting&#93;&#91;Python&#93; Console UI improvements

**Fixed:**

* &#91;AMD&#93; Incorrect detection of outdated driver version
* Crash when reimporting a mesh with different UV Tiles layout in some cases
* Crash when using particles with UDIMs on very heavy meshes
* &#91;UV Tiles&#93; Crash when exporting a mesh with displacement information in some cases
* &#91;Export&#93;&#91;Crash&#93; Exporting 2D view in psd format can cause a crash
* Importing images as sequences when creating a project does not work
* Engine stuck in an endless loop
* &#91;Shortcut&#93; Camera rotates always in snap mode when changing snap mode shortcuts
* Meshes are always auto-unwrapped when re-imported even if option is off
* &#91;Texture Set List&#93; Description text field is sometimes not fully visible during edition
* &#91;Texture Set List&#93; Dropdown menu to hide/unhide Texture Sets is not fully visible
* &#91;Texture Set List&#93; Clicking on eye icon should not enter the "Edit Texture Set name"
* &#91;Texture Set Settings&#93; Removing a Channel also removes the Channel below
* &#91;Export&#93; Include all and Reset all does not take UV Tiles into consideration
* &#91;Bakers&#93; Deselected bakers appear during the baking process
* Resolution update is not taken into account for baked maps used as input
* &#91;UV Tiles&#93;&#91;Viewport&#93; 3D Viewport freeze when adding Smart Material after folder with UV Tile mask selected
* &#91;UV Tiles&#93;&#91;Viewport&#93; Wireframe is still visible for hidden tiles with paint through mode
* &#91;Export&#93;&#91;Sketchfab&#93; Issues with "plus" subscription type
* &#91;Sketchfab&#93; "This asset is private" checkbox is not displayed after switching account
* &#91;Export&#93;&#91;Content&#93; "Wiggly" brush presets can lead to performance issues
* &#91;Plugin Photoshop&#93; Message in log: not compatible with UV Tile workflow
* &#91;Scripting&#93;&#91;Python&#93; PYTHONPATH env var prevents the application from starting
* &#91;Scripting&#93;&#91;Python&#93; Typo in Python documentation

### 6.2.1 (2020.2.1)

*(Released: July 29, 2020)*   
Summary: **Minor release, Hotfix**

**Added:**

* Add environment variable "SUBSTANCE\_PAINTER\_VRAM\_BUDGET" to override GPU VRam amount
* &#91;UV Tiles&#93;&#91;Performance&#93; Do not compute all UV tiles when using the Polygon Fill tool

**Fixed:**

* &#91;Iray&#93; Save render returns an error results in a black image
* &#91;Linux&#93; Crash after the splash screen on CentOS 7.3
* &#91;Linux&#93; Vram amount is not detected properly with specific configurations
* &#91;Crash&#93; Opening a project with duplicated texture set's name
* &#91;Engine&#93; Cache invalidation issue when modifying a mask
* &#91;Texture Set List&#93; Wrong font effect when Texture Set is deactivated

**Known Issues:**

* &#91;Texture Set List&#93; Cannot hide description
* &#91;Texture Set List&#93; UI issues
* &#91;Iray&#93; PSD render does not open
* &#91;Plugin Photoshop&#93; Not compatible with UV Tiles workflow

### 6.2.0 (2020.2.0)

*(Released: July 23, 2020)*   
Summary: **Major release with new UV Tiles workflow, paint across UV Tiles and performance improvement**

**Added:**

* UV Tiles (UDIMs)
* &#91;UV Tiles&#93; Paint across UV tiles
* &#91;UV Tiles&#93; Allow to choose between new and legacy workflow for UV Tiles
* &#91;UV Tiles&#93; Import UDIMs/UV Tile image sequences as a resource
* &#91;UV Tiles&#93; Add list of UV Tiles per Texture Set in Texture Set List window
* &#91;UV Tiles&#93; Allow to edit the resolution of multiple UV Tiles at once in Texture Set Settings
* &#91;UV Tiles&#93;&#91;2D View&#93; Display UV Tiles as a grid
* &#91;UV Tiles&#93;&#91;2D View&#93; New viewport button to display or hide UV Tiles information
* &#91;UV Tiles&#93; Switch painting tool to single channel by default for UV Tile projects
* &#91;UV Tiles&#93; New button in contextual toolbar to ignore masked UV Tiles while painting
* &#91;UV Tiles&#93;&#91;Layer Stack&#93; New layer stack icons to improve performance
* &#91;UV Tiles&#93;&#91;Layer Stack&#93; Improve Paint and Fill icons in the toolbar
* &#91;UV Tile Mask&#93;&#91;2D View&#93; Allow to include or exclude multiple UV Tiles at once (left click, CTRL+left click)
* &#91;UV Tile Mask&#93; New UV Tile mask to include, exclude tiles per layer with a new icon
* &#91;UV Tile Mask&#93;&#91;Layer Stack&#93; Display the number of UV Tiles in the UV Tiles mask icon when not all are included
* &#91;UV Tile Mask&#93;&#91;2D/3D View&#93; Add hover effect to visualize UV Tiles under the cursor
* &#91;UV Tiles&#93;&#91;Bakers&#93; Allow to select and bake specific UV Tiles
* &#91;UV Tiles&#93;&#91;Bakers&#93; Add selection options for Texture Sets/UV Tiles
* &#91;UV Tiles&#93;&#91;Bakers&#93; Right click menu option to select UV Tiles within a Texture Set
* &#91;UV Tiles&#93;&#91;Bakers&#93; Allow quick selection in the Texture Set/UV Tiles by dragging
* &#91;UV Tiles&#93;&#91;Bakers&#93; Replace "All" and "None" buttons in Mesh Maps by more explicit selection options
* &#91;UV Tiles&#93;&#91;Bakers&#93; Display number of textures to be baked
* &#91;UV Tiles&#93;&#91;Export&#93; Allow to select and export specific UV Tiles
* &#91;UV Tiles&#93;&#91;Export&#93; Allow quick selection of UV Tiles by dragging
* &#91;UV Tiles&#93;&#91;Export&#93; Add dropdown menu options for UV Tiles
* &#91;UV Tiles&#93;&#91;Export&#93; Make some export presets unavailable if they do not work with UV Tiles (Adobe Dimension, Sketchfab, glTF, USD)
* &#91;UV Tiles&#93;&#91;Content&#93; Update export presets to use the new $udim tag
* &#91;UV Tiles&#93; Improve error reporting when importing meshes with overlapping UV islands
* &#91;UV Tiles&#93; UV Tiles compatible in Iray
* &#91;UV Tiles&#93;&#91;Scripting&#93; Add UV Tile export documentation to Python doc
* Performance
* &#91;Performance&#93; New button in contextual toolbar to pause engine computation when working (SHIFT+ESC)
* &#91;Performance&#93; Faster project opening by delaying Texture Set cache computation
* &#91;Performance&#93; Don't wait for mesh maps to load when opening project
* &#91;Performance&#93;&#91;2D/3D View&#93; Don't compute Mask channel in viewport when it is not used
* &#91;Performance&#93; Do not block the application when loading mesh maps displayed in the viewports
* &#91;Performance&#93; Improve incremental save speed when saving a project
* &#91;Performance&#93;&#91;Bakers&#93; Change default dilation settings to improve saving time and project size
* &#91;Performance&#93;&#91;Bakers&#93; Switch to grayscale on specific Bakers to improve saving time and project size
* &#91;Performance&#93;&#91;Export&#93; Improve engine performance to export textures faster
* &#91;Performance&#93;&#91;Export&#93; Improve responsiveness when opening the export dialog with a lot of Texture Sets
* &#91;Performance&#93;&#91;Export&#93; Improve performance when switching to tab "List of Exports"
* &#91;Performance&#93;&#91;Iray&#93; Reduce Iray startup time
* Other
* &#91;Bakers&#93; Add selection options for Texture Sets
* Move shader instance management to Texture Set Settings
* &#91;2D/3D View&#93; Add message at bottom of the viewport to indicate which mask type is edited
* &#91;Layer Stack&#93; New option in settings to switch between legacy and new thumbnails
* &#91;Layer Stack&#93; Add visual feedback to indicate loading state of the thumbnails
* &#91;Proj&#93; New projection mode "Fill (Match Per UV-Tile)" to load image sequences
* &#91;Proj&#93; Change fill layers projection mode to "Fill (Match Per UV-Tile)" in specific cases
* &#91;Content&#93; Optimize Charcoal brush presets to improve performance
* Update Iray to version 2020.0.0
* &#91;Export&#93; Disable List of Exports tab when nothing is selected
* Auto Unwrap
* &#91;Auto Unwrap&#93; Improve success rate of the automatic unwrap process
* &#91;Auto Unwrap&#93; Improved parameterization to increase speed and stability

**Fixed:**

* &#91;Alembic&#93; Facesets are ignored when importing files
* &#91;Alembic&#93; Infinite loading time with specific files
* &#91;Import&#93; Incorrect UDIM image sequence is imported when only the file extension differs
* &#91;Crash&#93; Trying to open project locked by another process leads to a crash
* &#91;Projection&#93; Artefacts on duplicated mesh when using triplanar projection
* &#91;Export&#93; Emissive channel is not exported with USD format
* &#91;Content&#93; Smart Material "Charcoal" contains paint strokes

**Known Issues:**

* &#91;Texture Set List&#93; Cannot hide description
* &#91;Texture Set List&#93; UI issues

### 6.1.3 (2020.1.3)

*(Released: June 16, 2020)*   
Summary: **Bugfix**

**Added:**

* &#91;Export&#93; Add displacement settings in Shader parameters json file

**Fixed:**

* &#91;Crash&#93;&#91;Engine&#93; Crash when trying to erase and replace existing channels
* &#91;Crash&#93; Changing shader after painting a mask in material layering
* &#91;Crash&#93;&#91;Engine&#93; Crashes with some heavy projects
* &#91;Bakers&#93; Matching By Name doesn't work with OBJs exported from zBrush
* &#91;Displacement&#93;&#91;SVT&#93; Textures are not displayed at project opening when displacement is on
* &#91;Export&#93; Some textures are exported uniform gray
* &#91;Export&#93; Disabled Texture Sets should not be exported for Dimension and Sketchfab export presets
* &#91;Scripting&#93;&#91;JavaScript&#93; Crash while using the JavaScript API to access the export config in the onProjectOpened event
* &#91;Scripting&#93;&#91;Javascript&#93; onExportFinished() is not called after an export

### 6.1.2 (2020.1.2)

*(Released: May 28, 2020)*   
Summary: **Bugfix with Substance Engine and Bakers update**

**Added:**

* &#91;Bakers&#93; Update to the most recent version
* &#91;Bakers&#93; New Sampling method in Ambient Occlusion, Curvature, Thickness bakers
* Update to the most recent version of Substance Engine
* &#91;Scripting&#93;&#91;Python&#93; Allow creation of ResourceID for project resources
* &#91;Scripting&#93;&#91;Python&#93; Allow querying channel information
* &#91;Scripting&#93;&#91;Python&#93; Add dryrun and callback functions to simulate texture export

**Fixed:**

* &#91;Bakers&#93; Incorrect normals in World Space Normals baker using a tangent Normal map in specific cases
* &#91;Bakers&#93; Error baking Ambient Occlusion with Optix when no high poly
* &#91;Dynamic Strokes&#93; Lag when loading specific Texture Set
* &#91;Export&#93; Should not export the disabled texture sets for USD, glTF
* &#91;Scripting&#93;&#91;JavaScript&#93; Cannot edit new Curvature baker settings
* &#91;Scripting&#93;&#91;JavaScript&#93; alg.texturesets.addChannel() does not return an error in some cases
* &#91;Scripting&#93;&#91;JavaScript&#93; Typo in Javascript API documentation for setProjectExportOptions()
* &#91;Scripting&#93;&#91;JavaScript&#93; Always exports all texture sets
* &#91;Scripting&#93;&#91;Python&#93; sys.executable returns a path to python.exe instead of Substance Painter
* Texture cache not compatible across Mac OS and Windows/Linux
* &#91;Livelink UE4&#93; Only last material is used for all texture sets in a combined mesh

**Known Issues:**

* &#91;Export&#93;&#91;Dimension&#93;&#91;Skecthfab&#93; Should not export the disabled texture sets
* &#91;Crash&#93; Change shader after having painted a mask in material layering

### 6.1.1 (2020.1.1)

*(Released: May 05, 2020)*   
Summary: **Hotfix**

**Added:**

* &#91;Export&#93; Overridden state visual feedback on TextureSet

**Fixed:**

* &#91;Export&#93; Exporter window size too large on special resolution monitor and can not be resized
* &#91;Export&#93; Options are not saved after export
* &#91;Export&#93; Crash or cannot export with "from cache" export preset
* &#91;Export&#93; Cancelling export generates an unexpected additional empty map
* &#91;Export&#93; Fix virtual export preset settings
* &#91;Python&#93; PYTHONPATH env var is not taken into account
* &#91;Python&#93;&#91;Export&#93; Cancelling export via Python returns an exception error
* &#91;Python&#93;&#91;Export&#93; export\_project\_textures incorrect result with psd file format
* &#91;Bakers&#93; Crash on Linux with GPU raytracing

**Known Issues:**

* &#91;JavaScript&#93; Cannot edit new Curvature baker settings
* &#91;JavaScript&#93;&#91;Export&#93; Always exports all texture sets
* &#91;Export&#93;&#91;USD&#93; Should not export the disabled texture sets
* &#91;Crash&#93; Change shader after having painted a mask in material layering

### 6.1.0 (2020.1.0)

*(Released: April 22, 2020)*   
Summary: **Major release with New texture and mesh exporter (with displacement and tessellation), updated UV unwrapping with more controls, new bakers, new scripting python API, better UX for decal projection and new content**

**Added:**

* New texture and mesh exporter
* &#91;Export&#93; New exporter interface
* &#91;Export&#93;&#91;Export tab&#93; Allow selection of which maps channels are exported per Texture Set
* &#91;Export&#93;&#91;Export tab&#93; Allow modification of the Texture Set size for all Texture Sets in one action
* &#91;Export&#93;&#91;Export tab&#93; Allow a different template per Texture Set (except for USD, glTF, Sketchfab and Dimension)
* &#91;Export&#93;&#91;Export tab&#93; Quick activation and deactivation of maps and Texture Sets
* &#91;Export&#93;&#91;Export tab&#93; Export resolution 8192x8192 no longer experimental
* &#91;Export&#93;&#91;Export tab&#93; Allow modification of the file format and bit depth per map
* &#91;Export&#93;&#91;Export tab&#93; Allow reset to the default parameters' values
* &#91;Export&#93;&#91;Export tab&#93; Allow settings to be saved without exporting
* &#91;Export&#93;&#91;Output templates tab&#93; Rename "Configuration" tab to "Output templates" tab
* &#91;Export&#93;&#91;Output templates tab&#93; Allow definition of file format and bit depth per preset map
* &#91;Export&#93;&#91;List of exports tab&#93; New preview tab to summarize and view export process
* &#91;Import/Export Mesh&#93; Import/Export time performance optimization
* &#91;Export Mesh&#93; Export mesh in FBX
* &#91;Export Mesh&#93; Export mesh with displacement and tessellation
* &#91;Export Mesh&#93;&#91;UI&#93; New settings for recomputing normal vertex, apply triangulation
* &#91;Export Mesh&#93; Export original mesh topology with new UVs generated by auto unwrapping
* Updated auto UV unwrapping with more controls
* &#91;UV Unwrapping&#93;&#91;UI&#93; Add setting to activate auto UV unwrapping in new project window
* &#91;UV Unwrapping&#93;&#91;UI&#93; New Options to control the unwrapping steps (seams, unwrapping, packing)
* &#91;UV Unwrapping&#93;&#91;UI&#93; Allow conservation of existing unwrapping seams/unwrapping/packing
* &#91;UV Unwrapping&#93;&#91;UI&#93; New Options to fully recompute unwrapping steps
* &#91;UV Unwrapping&#93;&#91;UI&#93; New Option to control the margin size (none, small, medium and large)
* New Bakers
* &#91;Bakers&#93; Replace old Curvature by new Curvature from mesh
* &#91;Bakers&#93; Add match by name option to ignore backface in "Ambient Occlusion" baker
* &#91;Bakers&#93; Add ground plane option in "Ambient Occlusion" baker
* New scripting Python API (3.7.6)
* &#91;Python&#93;&#91;UI&#93; New scripting menu for Python
* &#91;Python&#93;&#91;UI&#93; New Python documentation in Help menu
* &#91;Python&#93; Expose Substance Painter python modules: substance\_painter, alg, display, project.setting, project, texturesets, ui
* &#91;Python&#93; Expose new "substance\_painter" Python module
* &#91;Python&#93; Expose new Python sub-module: alg, display, log, project, resource, texturesets, ui
* &#91;Python&#93; Listener for project changes
* &#91;Python&#93; New examples in Python documentation
* &#91;JavaScript&#93;&#91;UI&#93; Plugins menu replaced by JavaScript
* &#91;Viewport&#93; Allow creation of a decal projection by "drag/dropping + ALT" a resource from the shelf
* New Content
* &#91;Content&#93; 5 new decal materials from Substance Source
* &#91;Content&#93; Add new project templates and export presets for Maxwell renderer
* &#91;Content&#93; Add project template for Keyshot 9 export
* &#91;Content&#93; Update Keyshot 9 export preset to support displacement and emissive
* &#91;Content&#93;&#91;Exporter&#93; Update of all export presets to match latest versions of game engines and renderers
* &#91;Content&#93;&#91;Exporter&#93; Update export presets files to use new format and dithering settings
* &#91;Content&#93; New templates and shaders to support VRay material (VRayMtl)
* &#91;Layer Stack&#93; Allow deletion of layer effects using trash icon or keyboard shortcut Delete
* Remove plugin Substance Source (use launcher with "send to" functionality)
* &#91;Windows&#93; Do not display TDR warning on high-end GPUs

**Fixed:**

* Translation issues in new project file dialog
* &#91;Bakers&#93; Setting "Save preprocessed scene file" does not work anymore
* &#91;Planar Projection&#93; Projection does not work on meshes with repeating UVs
* &#91;Decal&#93; Difference of behavior in normal channel when using different fill layer projection modes
* &#91;Smudge&#93;&#91;Clone&#93; Artifact may appear when painting in mask
* &#91;Engine&#93; Crash with specific layer content
* &#91;Engine&#93; Random crash when painting in some cases
* &#91;Anchor point&#93; Reference to an empty mask always returns white
* &#91;Export&#93; Layer not taken into account in some particular stack configurations
* &#91;Export mesh&#93; Cannot export with path containing special characters
* &#91;Export Mesh&#93; Cannot read glTF files when exported from Linux or MacOS
* &#91;Import mesh&#93; Re-importing DAE, PLY or glTF does not work as intended

**Known Issues:**

* &#91;Scripting&#93;&#91;JavaScript&#93; Cannot edit new Curvature baker settings
* &#91;Bakers&#93; Crash on Linux with GPU raytracing
* &#91;Export&#93;&#91;USD&#93; Should not export the disabled texture sets
* &#91;Crash&#93; Change shader after having painted a mask in material layering

## Version 5

### 5.3.3 (2019.3.3)

*(Released: February 06, 2020)*   
Summary: **Bugfix with upgrade to Iray 2019.3**

**Added:**

* Upgrade to Iray 2019.3
* &#91;Log&#93; Indicate outdated bios for Ryzen CPU leading to crash during baking
* &#91;ABR&#93; Extract ABR alphas to shelf

**Fixed:**

* &#91;Baker&#93; Baking fail if High-poly mesh does not have UVs
* &#91;Linux&#93; Custom mouse shortcuts are not saved
* &#91;Brush&#93; Outline disappears with some alpha shapes
* &#91;Tablet&#93; Bad detection when moving sliders
* &#91;Shortcuts&#93; Can not set up any shortcut with "Ctrl+Alt+MouseClick"
* &#91;Shelf&#93; Can not see resource tooltip when using a pen tablet
* &#91;2D View&#93;&#91;Export&#93; 2D View preset does not take into account the normal information
* Freeze when painting in UV alignment with certain brushes
* Painting under a filter creates artifact on the ongoing stroke
* &#91;Viewport&#93; Incorrect texture cache in viewport after re-importing a mesh
* &#91;Crash&#93; Error when saving after exporting to Photoshop
* &#91;Crash&#93; Writing special symbols in prefix when importing resources
* &#91;Crash&#93; Click on the reference in Anchor Point Properties
* &#91;Anchor Points&#93; Channel does not update when there is a filter between Anchor point and reference
* Iray url link in Help menu does not work

**Known Issues:**

* &#91;UV Unwrapping&#93; Processing high poly meshes can take a long time
* &#91;UV Unwrapping&#93; Vertices at the exact same coordinates are merged
* &#91;UV Unwrapping&#93; UV Generation may fail on some mesh parts in some rare cases
* &#91;UV Unwrapping&#93; Non uniform or highly distorted texel ratio in a single UV island in some cases
* &#91;UV Unwrapping&#93; Non uniform texel ratio between Texture Sets
* &#91;UV Unwrapping&#93; UV island generated can be very elongated and do not fit into UV space in some cases
* &#91;UV Unwrapping&#93; Degenerated faces or non-triangular mesh faces with small or overlaping edges may not get UV unwrapped

### 5.3.2 (2019.3.2)

*(Released: January 21, 2020)*   
Summary: **Bugfix**

**Fixed:**

* Opening a project that was saved in solo channel mode does not display the mesh
* Viewport is not always updated when painting under layer using clone tool

**Known Issues:**

* &#91;Bakers&#93; Crash related to multi-threading on Ryzen CPUs
* &#91;UV Unwrapping&#93; Processing high poly meshes can take a long time
* &#91;UV Unwrapping&#93; Vertices at the exact same coordinates are merged
* &#91;UV Unwrapping&#93; UV Generation may fail on some mesh parts in some rare cases
* &#91;UV Unwrapping&#93; Non uniform or highly distorted texel ratio in a single UV island in some cases
* &#91;UV Unwrapping&#93; Non uniform texel ratio between Texture Sets
* &#91;UV Unwrapping&#93; UV island generated can be very elongated and do not fit into UV space in some cases
* &#91;UV Unwrapping&#93; Degenerated faces or non-triangular mesh faces with small or overlaping edges may not get UV unwrapped

### 5.3.1 (2019.3.1)

*(Released: December 20, 2019)*   
Summary: **Hotfix**

**Fixed:**

* Crash when working on meshes with specific UV projections
* &#91;ABR&#93; Crash when switching between Photoshop presets
* &#91;Linux&#93; Cannot start Substance Painter on CentOS 7.4 because of libGLX dependency issue
* &#91;Bakers&#93; Crash when baking after using File &gt; Clean
* &#91;Bakers&#93; Baking progress dialog freeze after cancel
* &#91;Bakers&#93; Baking mesh after exporting textures does not work
* &#91;Bakers&#93; Using "Match By Name" results with black Mesh Maps
* &#91;Bakers&#93; Cage is not taken into account
* &#91;Shelf&#93; Importing PSD files leads to broken images
* &#91;Sample&#93; "Mat" sample project has broken cameras and incorrect export preset

**Known Issues:**

* &#91;Bakers&#93; Crash related to multi-threading on Ryzen CPUs
* &#91;UV Unwrapping&#93; Processing high poly meshes can take a long time
* &#91;UV Unwrapping&#93; Vertices at the exact same coordinates are merged
* &#91;UV Unwrapping&#93; UV Generation may fail on some mesh parts in some rare cases
* &#91;UV Unwrapping&#93; Non uniform or highly distorted texel ratio in a single UV island in some cases
* &#91;UV Unwrapping&#93; Non uniform texel ratio between Texture Sets
* &#91;UV Unwrapping&#93; UV island generated can be very elongated and do not fit into UV space in some cases
* &#91;UV Unwrapping&#93; Degenerated faces or non-triangular mesh faces with small or overlaping edges may not get UV unwrapped

### 5.3.0 (2019.3.0)

*(Released: December 17, 2019)*   
Summary: **Major release with improvment of handpainting user experience, working with tablets, automatic UV unwrapping in beta (0.3.0) and diverse new content for handpainting**

**Added:**

* Integrate Automatic UV unwrapping 0.3.0 version in Substance Painter
* &#91;UV unwrapping&#93; Automatic UV unwrapping in Substance Painter when No UVs present or partial UVs
* &#91;UV unwrapping&#93; One Global setting to activate and deactivate it
* &#91;UV unwrapping&#93; Version reported in log file
* &#91;UV unwrapping&#93;&#91;UI&#93; Indicate UV Unwrapping progress
* &#91;UI&#93; New settings in contextual toolbar to select the brush preview: Full preview, Brush outline and Crosshair
* &#91;Tool&#93; New advanced blending mode in alpha section: Lighten (Maximum) in addition to Normal
* &#91;Layer Stack&#93; Gamma correction option per layer for alpha or mask (right click menu)
* &#91;Layer Stack&#93;&#91;UI&#93; Add 'i' icon when a layer alpha is gamma corrected
* &#91;Tablet&#93;&#91;Tool&#93; Expose minimum pressure for size and flow
* &#91;Tablet&#93;&#91;UI&#93; New setting in contextual toolbar to select the curve pressure: linear, easy-in, easy-in-out
* &#91;Tablet&#93;&#91;UX&#93; Add Ctrl+Alt+click to scroll
* Import Photoshop brush presets (ABR format)
* &#91;ABR&#93; Support Shape parameters
* &#91;ABR&#93; Support Shape dynamics parameters
* &#91;ABR&#93; Support Transfer parameters
* &#91;ABR&#93; Support Scattering parameters
* &#91;ABR&#93;&#91;Dynamic strokes&#93; Support Roundness and Flip
* &#91;ABR&#93;&#91;Shelf&#93; Expose the brush folder structure in the Filter Editor
* &#91;ABR&#93;&#91;Shelf&#93; Add Photoshop icon in thumbnails
* &#91;ABR&#93;&#91;Shelf&#93; Add list of unsupported parameters in the ABR detailed thumbnail
* &#91;Tool&#93;&#91;Dynamic Strokes&#93; New dynamic stroke setting to control how many random seed to generate
* &#91;Tool&#93;&#91;UI&#93; Add new distribution and axis settings for Scattering jitter
* &#91;Shortcut&#93; Add Ctrl+Shift+B to open the Baking window
* &#91;UI&#93;&#91;Menu&#93; Add entry in 'Edit' menu to open Baking window
* &#91;UI&#93;&#91;Settings&#93; Improvement alignment of the shortcuts list
* &#91;UI&#93; Replace pressure controls (size and flow) icons by on/off buttons
* &#91;Viewport&#93; Allow to focus 2D and 3D viewport separately
* Update to QT 5.12.5
* &#91;UI&#93; Indicate mesh loading progress
* &#91;Substance&#93; Add support for non-clamped and soft range with sliders
* &#91;Substance&#93; Increase Substance parameters precision up to 6 decimals
* &#91;Substance&#93; Take into account the step defined by a parameter
* &#91;Substance&#93; Optimize Dynamic Stroke generation with support of conditions in userdata
* &#91;Substance&#93; Allow to designate a graph output as a mask for all channels via userdata
* &#91;Content&#93; Update 'Mat' sample project with displacement friendly topology, new ID map and new cameras
* &#91;Content&#93; Integrate 3 new filters (MatFx): Comic Book, Watercolor, Oil Paint (inspired by Emrecan Cubukcu work)
* &#91;Content&#93; Integrate 102 Photoshop brush presets from Kyle T. Webster's packs
* &#91;Content&#93; Integrate 18 new brush presets: Paint Roller Arrow, Paint Roller Warning text, Charcoal Fine and more
* &#91;Content&#93; Integrate 9 new alphas: Brush Maker Paint Roller, Brush Maker Photoshop, Brush patterns and more
* &#91;Content&#93; Integrate 2 new tool presets: Gouache Dense and Gouache Faded
* &#91;Content&#93; Integrate 1 new generator : UV checker (highlight UV islands and seams)
* &#91;Content&#93; Integrate 2 new export preset: Keyshot 9+ and Spark AR Studio
* &#91;Content&#93; Integrate 1 new project template : Spark AR Studio (Facebook)

**Fixed:**

* &#91;Tablet&#93; Undoing stylus strokes (Ctrl+Z) lags more than undoing mouse strokes
* &#91;Tablet&#93; Start and end pressure not taken into account when drawing a straight line
* &#91;Tablet&#93; First stamp is drawn twice when using a straight line
* &#91;Tablet&#93; Improve support for Huion tablet shortcuts
* &#91;Tablet&#93; Improve support for Huion pen buttons
* &#91;Tablet&#93; Offset between the brush preview and the drawn stamp
* &#91;Tablet&#93; Shortcuts to modify brushes with pen lead to low performance in rare cases
* &#91;Tablet&#93; Lag when painting on a specific layer
* Blurry textures may occur in rare cases when switching viewport
* &#91;UI&#93;&#91;Substance&#93; Image inputs are not always displayed
* Clean does not remove presets from shelf which have been imported in a project
* &#91;Tool&#93;&#91;Dynamic Stroke&#93; Performance issue when tweaking Stamp Cycle Count
* Refresh issues while painting in 3D/2D viewport mode in rare cases
* Painting one very long stroke can lead to a freeze
* &#91;Tool&#93; Performance issue when painting with specific dynamic strokes
* &#91;UI&#93; Contextual toolbar still display brush properties when selecting a folder
* Symmetry axis values do not reset
* Import of EXR textures with floating point values are fully black
* Alt+click on a channel to isolate does not work for filter and generator
* &#91;Export&#93; Specific project crashes at export
* &#91;Substance&#93; Incorrect default value on dropdown if parameter is hidden by Visible If
* &#91;Shader&#93; Channels defined via Material Layering are not sorted the same way in the UI
* &#91;Shelf&#93; Presets metadata are not saved on disk

**Known Issues:**

* &#91;UV Unwrapping&#93; Processing high poly meshes can take a long time
* &#91;UV Unwrapping&#93; Vertices at the exact same coordinates are merged
* &#91;UV Unwrapping&#93; UV Generation may fail on some mesh parts in some rare cases
* &#91;UV Unwrapping&#93; Non uniform or highly distorted texel ratio in a single UV island in some cases
* &#91;UV Unwrapping&#93; Non uniform texel ratio between Texture Sets
* &#91;UV Unwrapping&#93; UV island generated can be very elongated and do not fit into UV space in some cases
* &#91;UV Unwrapping&#93; Degenerated faces or non-triangular mesh faces with small or overlaping edges may not get UV unwrapped
* Meetmat sample has some issues with imported cameras

### 5.2.3 (2019.2.3)

*(Released: October 23, 2019)*   
Summary: **Bugfix release**

**Added:**

* &#91;Texture Set List&#93; Add button to quickly enable/disable focus mode
* &#91;Log&#93; Add Windows 10 version number in the log file
* Update to latest version of Substance Engine
* &#91;MacOS&#93; Notarized the software to follow new MacOS Catalina distribution requirements

**Fixed:**

* &#91;Plugin&#93; Plugin Source does not work
* &#91;MacOS&#93;&#91;Shader&#93; Mac OS 10.14.5 and AMD: material layering does not work as intended

**Known Issues:**

* Alembic files with subdivisions cannot be imported
* Rare crashes when importing some Alembic files
* UI temporarily unresponsive when baking with DXR on Pascal GPUs

### 5.2.2 (2019.2.2)

*(Released: September 20, 2019)*   
Summary: **Bugfix release**

**Fixed:**

* Import resource by scripting can lead to a crash
* &#91;Plugin&#93; Downloading material from source can lead to a crash

**Known Issues:**

* Alembic files with subdivisions cannot be imported
* Rare crashes when importing some Alembic files
* UI temporarily unresponsive when baking with DXR on Pascal GPUs

### 5.2.1 (2019.2.1)

*(Released: September 17, 2019)*   
Summary: **Bugfix release**

**Fixed:**

* &#91;Mac&#93;&#91;USD&#93; Exported USDZ files from MacOS cannot be opened
* &#91;Texture Set&#93; Not possible to isolate a texture set with the ALT modifier
* &#91;Shelf&#93; Presets, Smart Materials and Smart Masks are always modified when exiting application
* &#91;Layer Stack&#93; Cannot select effect after deleting another effect
* Flickering when using a slider inside the tool properties panel
* Crash when exporting presets to shelf
* Crash when exporting a preset with insufficient space
* Crash when creating a preset with insufficient space

**Known Issues:**

* Alembic files with subdivisions cannot be imported
* Rare crashes when importing some Alembic files
* UI temporarily unresponsive when baking with DXR on Pascal GPUs

### 5.2.0 (2019.2.0)

*(Released: July 25, 2019)*   
Summary: **Major release with updates of the bakers in terms of performance and a new previsualization mode + new content**

**Added:**

* &#91;Bakers&#93; Added support for GPU Raytracing with DXR and OptiX (Ambient Occlusion, Thickness)
* &#91;Bakers&#93; Optimizations and accelerations for CPU Raytracing
* &#91;Bakers&#93;&#91;Vis mode&#93;&#91;UI&#93; New baking visualization mode in viewport
* &#91;Bakers&#93;&#91;Preferences&#93;&#91;UI&#93; New baking option for enabling-disabling GPU Raytracing
* &#91;Bakers&#93;&#91;UI&#93; Rework of the progress bar dialog
* &#91;Bakers&#93; Improvement of warning and error messages
* &#91;Bakers&#93; Allow more responsive cancelling of baking process
* &#91;Bakers&#93; Reopen bake window after clicking cancel
* &#91;Proj&#93;&#91;UX&#93; Usability improvement of rotation manipulator
* &#91;Settings&#93; Option to improve performance by reducing viewport resolution for HDPI screens
* &#91;Scripting&#93; Change texture set resolution
* &#91;Scripting&#93; Get selected texture set
* &#91;Scripting&#93; Allow the user to select a texture set
* &#91;Scripting&#93; Function to know when texture set selection has been changed
* &#91;Shelf&#93; Added 40 new smart materials
* &#91;Shelf&#93; Added 20 new smart masks

**Fixed:**

* &#91;Layer stack&#93; Freeze of UI when multi-selecting layers
* &#91;Layer stack&#93; Grouping lots of layers freezes the UI for longer than usual
* &#91;Layer stack&#93; A layer and an effect can be both selected at the same time in some cases
* Substance graphs used inside painting tools are not generated at the right resolution
* &#91;Baker&#93; "Bake All Texture Sets" button is not disabled when no bakers are selected
* &#91;MacOS&#93; Deactivate the warning message about tessellation
* Projection tool has no preview when used with a mask
* Crashes and corrupted projects when trying to save with insufficient disk space
* &#91;Shelf&#93; Crash when importing a resource on disk via shelf with insufficient space
* &#91;Shelf&#93; Crash when restoring session preset
* &#91;Shelf&#93; Importing a preset with a name that ends with a space leads to a crash
* &#91;Shelf&#93; Importing a resource with a prefix that ends with an empty space leads to a crash

**Known Issues:**

* Alembic files with subdivisions cannot be imported
* Rare crashes when importing some Alembic files
* UI temporarily unresponsive when baking with DXR on Pascal GPUs

### 5.1.3 (2019.1.3)

*(Released: July 01, 2019)*   
Summary: **Bugfix with 2 new features**

**Added:**

* Allow to specify the VRam budget with a command line (e.g. --vram-budget 4096)
* &#91;QML&#93; Expose wrapMode and elide properties of QML buttons and checkboxes

**Fixed:**

* "Follow path" does not work all the time
* Channel mapping doesn't work with SBSAR used in single channel slots
* &#91;Layer Stack&#93; Low performance when scrolling with hidden layers
* &#91;TextureSet&#93; Crash when clicking between masks
* &#91;SVT&#93; Displacement in not displayed properly and flickers in some cases
* &#91;Alembic&#93; Crash with mesh using point normals instead of vertex normals
* &#91;Alembic&#93;&#91;Log&#93; Report error in Log if Alembic file is not supported during import

**Known Issues:**

* Alembic files with subdivisions cannot be imported
* Rare crashes when importing some Alembic files

### 5.1.2 (2019.1.2)

*(Released: May 21, 2019)*   
Summary: **Hotfix**

**Fixed:**

* Crash when selecting two resources with an image input

### 5.1.1 (2019.1.1)

*(Released: May 20, 2019)*   
Summary: **Hotfix**

**Added:**

* Update to latest version of Substance Engine with last release of Substance Designer 2019.1

**Fixed:**

* &#91;Substance&#93; Visible If is not taken into account for Input Images
* &#91;SVT&#93;&#91;Engine&#93; Changing texture set resolution leads to a crash in some cases
* &#91;Engine&#93; Random black textures appear in some cases
* &#91;Layer Stack&#93;&#91;UI&#93; Toggling a mask with SHIFT can select multiple layers at the same time
* &#91;Layer Stack&#93; Opacity has no effect on Paint effect with Pass-Through blending mode
* &#91;Layer Stack&#93; Height To Normal filter input doesn't update properly with eraser brush stroke
* &#91;LayersStack&#93; Crash when undoing the drop of a smart mask
* Wireframe flickering with shadows and temporal anti aliasing activated
* &#91;Displacement&#93; Lag on AMD with some heavy meshes
* &#91;Windows&#93; Crash when opening some projects via the file explorer
* &#91;Histogram&#93; Crash when removing mask with anchor point in some cases
* Crash in preview generation in some rare cases
* &#91;Crash&#93; Can not reopen a project using too many clone and smudge tools
* No mesh displayed in material mode after saving in some cases
* &#91;Scripting&#93; alg.mapexport.documentStructure() returns incorrect values for folders

**Known Issues:**

* Double clicking texture set name will select it before entering renaming mode

### 5.1.0 (2019.1.0)

*(Released: April 23, 2019)*   
Summary: **Dynamic Stroke with dedicated new content, Displacement and Tessellation in real-time and Iray, Compare Mask effect, Radial symmetry, Planar and Spherical projection**

**Added:**

* &#91;Tool&#93; Dynamic stroke: Substance variation alongside a brush stroke
* &#91;Dynamic stroke&#93; Expose new stamp index parameter with options
* &#91;Dynamic stroke&#93; Take into account $time parameter
* &#91;Dynamic stroke&#93; Generate new $randomseed parameter per stroke and per stamp
* &#91;Dynamic stroke&#93; Start a dynamic stroke index from a random number
* &#91;Dynamic stroke&#93;&#91;Shelf&#93; Help finding a dynamic stroke resource with dedicated new icon
* Displacement and tessellation in real-time viewport
* Displacement and tessellation in Iray
* &#91;Shader settings&#93;&#91;UI&#93; New tab for controlling displacement and tessellation
* &#91;Layer stack&#93; New CompareMask effect: generate a mask by comparing two channels
* &#91;Layer stack&#93;&#91;UI&#93; New entry in right-click menu "Add mask with height combination" to insert a CompareMask effect
* &#91;Symmetry&#93; New symmetry mode: radial painting
* &#91;Symmetry settings&#93; Expand both sections "Settings" and "Display"
* &#91;Symmetry settings&#93;&#91;UI&#93; Preview for radial painting
* Expose two new projection modes: planar and spherical
* &#91;Proj&#93; New shape crop mode for all projections
* &#91;Proj&#93; Planar mode with new manipulator: Surface tool
* &#91;Proj&#93;&#91;Shortcut&#93; Shortcut SHIFT+W for Surface tool
* &#91;Proj&#93; Planar projection masking with depth culling and backface culling
* &#91;Manipulator&#93; Improvment of rotation manipulator on all three axes for triplanar
* &#91;Tool&#93;&#91;UX&#93; Alt-clicking on a channel focuses that channel (enables it or disables all others)
* &#91;Engine&#93; Update to latest version of Substance Engine
* &#91;Texture set&#93; Multiple selection and change resolution
* &#91;Texture set&#93; Quick activation and deactivation of the texture sets
* &#91;Texture set&#93; Combine solo and all options into a new menu
* &#91;Texture set&#93;&#91;Layer stack&#93; New icon for activation and deactivation
* &#91;Layer stack&#93;&#91;UX&#93; Insert effects above those already selected
* &#91;Layer stack&#93;&#91;UI&#93; Rework layer stack view selection style
* &#91;Layer Stack&#93; Blending mode for instanced layers is now in Pass Through mode by default
* &#91;Export&#93; Option to activate and deactivate dithering
* &#91;Plugin&#93; Support precision modifier for sliders (SHIFT)
* &#91;Plugin&#93;&#91;UI&#93; New icon for autosave
* &#91;Scripting&#93; List the contents of a folder
* &#91;Scripting&#93; Allow deletion of files
* &#91;Scripting&#93; Read all stack information including used resources
* &#91;Content&#93;&#91;Dynamic stroke&#93; New tools and brush presets
* &#91;Content&#93;&#91;Dynamic stroke&#93; Two new procedural gradients: Gradient Hue and Gradient Builder
* &#91;Content&#93; 11 new Filters: MatFx Peeling Paint, MatFx Water Drops and more
* &#91;Content&#93; 7 new generators: Auto Stitcher, UV Random Color, UV Texel Density and more
* &#91;Content&#93; 93 new alphas: new texts, arrows and various other shapes
* &#91;Content&#93; 2 new procedurals: Gradient Hue, Gradient Builder and more
* &#91;Content&#93; 21 new Tool and Brush presets for Dynamic Strokes : Pebbles, Footprints, Spray and more
* &#91;Content&#93; 2 New HDRis: Canopus Ground and Autumn Forest
* &#91;Content&#93; Update content with random seed curation in shelf
* &#91;Content&#93; New icon with exposed random seed parameter in shelf

**Fixed:**

* &#91;Layers stack&#93; Layer stack keeps dragging forever
* &#91;Mac&#93; "Show in Finder" can lead to freezing
* &#91;Scripting&#93; Settings saved via Custom UI are lost if shader file is moved
* &#91;Scripting&#93; API version number is incorrect and not up to date
* &#91;Effect&#93; Histogram content is not displayed correctly
* &#91;Effect&#93; Histogram effect does not update in some cases
* &#91;Shelf&#93; Stitches are not properly aligned on material "Plastic Fabric Pyramid"

**Known Issues:**

* Double clicking texture set name will select it before entering renaming mode
* &#91;Layer Stack&#93;&#91;UI&#93; Toggling a mask with SHIFT can select multiple layers at the same time

## Version 4

### 4.3.3 (2018.3.3)

*(Released: March 07, 2019)*   
Summary: **bugfix**

**Added:**

* &#91;Content&#93; Integrate new project template: "PBR - Metallic Roughness Alpha-blend"
* Linux Dynamic library search order changed to prioritize libraries in the installation directory ahead of what is installed on the system

**Fixed:**

* Mesh sometimes disappears from the 3D viewport (press F to reset camera)
* Update Substance Painter Sketchfab uploader with the new Sketchfab license types
* &#91;Import&#93;&#91;glTF&#93; Wrong handling input texture modulation as defined in glTF files
* &#91;Import&#93;&#91;glTF&#93; Ground plane is incorrectly displayed with glTF import in some cases
* &#91;Export&#93;&#91;USD&#93; Opacity does not work in Arkit
* &#91;Export&#93;&#91;USD&#93; USDz export crashes in some cases
* &#91;Export&#93;&#91;USD&#93; Export to USD without saving leads to crash
* &#91;Export&#93;&#91;USD&#93; Incorrect tiling mode for textures, subdivision mode for meshes and output types for shaders
* &#91;Export&#93;&#91;USD&#93; Sparse exports of only some texture sets with all geometry
* &#91;Instance&#93; Crash when trying to delete a broken instance layer
* &#91;Regression&#93;&#91;Export&#93; Some maps not exported in the chosen bit depth
* &#91;Linux&#93; Issue with library libtbb.so.2

**Known Issues:**

* Computation freeze in some cases on AMD VEGA GPUs
* Huion tablet issue with shortcuts on Windows OS

### 4.3.2 (2018.3.2)

*(Released: January 24, 2019)*   
Summary: **Hotfix with new features (USDZ export and Texture filtering in viewport)**

**Added:**

* &#91;Export&#93; Allow export to USDZ
* &#91;Viewport&#93; Allow to control the texture quality in the Display Settings
* &#91;Viewport&#93; Added mip bias setting in Display Settings
* &#91;Viewport&#93; Added anisotropic filtering in Display Settings
* &#91;plugins&#93; Update official plugins to use the style of Substance Painter 2018
* &#91;License&#93; Install license by default in a user folder

**Fixed:**

* Crash linked to decompression
* Add TAA on solo material
* Noise with shadow, TAA and alpha test shader with dithering
* Remove specular dithering for all classic PBR shaders
* Crash in the shader settings in some cases
* Scattering activation is not synchronized between OpenGL and Iray renders
* Smudge and clone tools do not work anymore on specific meshes
* Some texture sets can not appear in Iray render
* Renamed Texture Sets are not saved after closing project
* Wireframe artefacts when drag and dropping materials on ID maps
* &#91;Scripting&#93; File path creation not forced when saving a project
* &#91;Scripting&#93; Callback "onProjectAboutToSave()" doesn't work anymore
* Forum links broken in report bug window

**Known Issues:**

* Computation freeze in some cases on AMD VEGA GPUs
* Huion tablet issue with shortcuts on Windows OS

### 4.3.1 (2018.3.1)

*(Released: December 06, 2018)*   
Summary: **Hotfix**

**Added:**

* &#91;Symmetry&#93;&#91;Viewport&#93; Symmetry painting in the 2D view is back and now features a clone brush preview fixed

**Fixed:**

* &#91;Export&#93; 2D view export outputs a black texture in some cases
* &#91;Iray&#93; Normal information becomes incorrect in Iray after instancing a material layer
* Non square texture sets can lead in some cases to crash
* &#91;Undo&#93; Several Ctrl+Z can randomly lead in few cases to crash
* &#91;QML&#93; AlgScrollView can create a warning in the log in some cases (binding loops)

**Known Issues:**

* Computation freeze in some cases on AMD VEGA GPUs
* Huion tablet issue with shortcuts on Windows OS
* Anti-aliasing and shadows when active together may give unexpected results

### 4.3.0 (2018.3.0)

*(Released: November 20, 2018)*  
Summary: <b>Viewport upgrades, proper 2D view export, new UI helpers, an enhanced symmetry tool, new content and a huge boost in performance</b>

<b>Added:</b>

* &#91;Anti-aliasing&#93;&#91;Viewport&#93; New temporal anti-aliasing filtering for 3D viewport (via Display Settings)
* &#91;Export&#93; Export the content of the 2D viewport as a single texture
* &#91;Export&#93;&#91;Dithering&#93; Expose dithering at export
* &#91;Layer stack&#93; Colors on layers and folders
* &#91;Layer stack&#93; Quick activation and deactivation of multiple layers and effects
* &#91;Layer stack&#93; Easier navigation for blending modes with up down keys and mouse scroll
* &#91;Proj&#93;&#91;UI&#93; Additional rotation manipulator on all three axis for triplanar
* &#91;Proj&#93;&#91;Shorcuts&#93; - and + to change the UV projection manipulator size
* &#91;Shader&#93; Control coated layer parameters with channels in the PBR-coated shader
* &#91;Substance&#93; Expose new mesh-based texture inputs for filters and generators
* &#91;Symmetry&#93;&#91;Viewport&#93;&#91;UI&#93; Control symmetry offset with manipulators
* &#91;Symmetry&#93;&#91;Contextual toolbar&#93;&#91;UI&#93; New symmetry panel with options
* &#91;Symmetry&#93; New symmetry line intersection mode
* &#91;Symmetry&#93; New symmetry clone cursor
* &#91;Symmetry&#93;&#91;Shortcuts&#93; Q to hide and -, + to change size and shift to snap
* &#91;Log&#93; Improve error messages when unable to export textures
* &#91;Scripting&#93; Allow to change or update the resources in Display Settings
* &#91;Scripting&#93; Allow to create or remove channels in Texture Sets
* &#91;Content&#93;&#91;Shaders&#93; Add support for anisotropy with a dedicated shader (pbr-metal-rough-anisotropy-angle)
* &#91;Content&#93; Update of the preview sphere with anisotropy and modified angle
* &#91;Content&#93; Updated matFx shutline
* &#91;Content&#93; New Texturing.XYZ seamless face scan
* &#91;Content&#93; New anisotropic procedurals
* &#91;Content&#93; New filter: baked lighting environment
* &#91;Content&#93; New environment map: studio automotive neutral
* &#91;Content&#93; New project template: PBR - metallic roughness Anisotropy angle (with anisotropy channels)
* &#91;Content&#93; New project template: PBR - metallic roughness Coated
* &#91;SVT&#93;&#91;Engine&#93; Sparse Virtual Textures (SVT)
* &#91;SVT&#93;&#91;Preferences&#93;&#91;UI&#93; SVT hardware support acceleration option
* &#91;SVT&#93;&#91;Log&#93; Additional information for Sparse Virtual Texturing feature (e.g. size disk)
* &#91;SVT&#93;&#91;UI&#93; Message window at start if size on disk too low for the cache
* &#91;SVT&#93;&#91;Preferences&#93;&#91;UI&#93; Substance Painter global cache location
* &#91;SVT&#93; New environment variable to specify the path of the cache of Substance Painter
* &#91;SVT&#93; New environment variable to activate the SVT hardware support acceleration
* &#91;SVT&#93; Detect sparse support by hardware
* &#91;SVT&#93;&#91;Hardware Sparse&#93; Raise minimum driver version for Nvidia GPU
* &#91;SVT&#93;&#91;Shader&#93;&#91;Viewport&#93;&#91;UI&#93; Warn user if artefacts present with Sparse Virtual Texturing at project opening

<b>Fixed:</b>

* &#91;Color Picker&#93; Painting cursor appearing when trying to pick a color
* Crash by Selecting or Unselecting layers in a specific order can lead to crash
* Crash when pasting as an instance a layer with a mask
* &#91;User Channel&#93;&#91;Regression&#93; Crash when renaming user channel
* &#91;User Channel&#93; Grayed brush preview
* &#91;Alembic&#93; Only one texture set from several materials after import
* &#91;Engine&#93; Exported texture differs from viewport for brush stamps
* &#91;Engine&#93; Invert with a level effect does not fully affect a texture
* Material picker is applying a brush stroke while picking
* Switching resolution to 128x128px leads to a crash
* Mesh map links are not updated properly when rebaking or instancing layers
* &#91;Substance&#93; UserData ColorSpace does not work on Baked Mesh Normal requested as input
* MDL association mismatch when using multiple shaders instances
* &#91;Symmetry&#93;&#91;Fill Layer&#93; Symmetry plane and its manipulator active in Fill Layer
* &#91;Viewport&#93; Pivot point for translation not always updated after clicking
* &#91;UI&#93; Fixed icons and removal of placeholders for HDPI monitors

<b>Known Issues:</b>

* Computation freeze in some cases on AMD VEGA GPUs
* Huion tablet issue with shortcuts on Windows OS
* Anti-aliasing and shadows when active together may give unexpected results

### 4.2.3 (2018.2.3)

*(Released: September 25, 2018)*

**Fixed:**

* &#91;2D View&#93; 2D View is broken with some meshes when creating a new project
* &#91;Crash&#93; Switching from UV projection to tri-planar projection leads to a crash
* &#91;RayCollider&#93; Multiple crashes due to "RayCollider"
* &#91;Tool&#93; Switching layers lose the modified brush properties
* Brush settings are reseted when switching to the eraser

**Known Issues:**

* Computation freeze on AMD VEGA GPUs
* Huion tablet issue with shortcuts on Windows OS

### 4.2.2 (2018.2.2)

*(Released: September 11, 2018)*   
Summary: **Hotfix with content update, new scripting functionalities and being able to disable the auto update**

**Added:**

* &#91;Content&#93;&#91;Shelf&#93; Add a Skin shelf preset
* &#91;Content&#93;&#91;shelf&#93; Conversion of 19 skin normals into materials for subsurface scattering
* &#91;Scripting&#93; Create a project template from an open project
* &#91;Scripting&#93; Get/Set export settings of an opened project
* &#91;Updates&#93; Be able to disable the auto update pop-up from settings and environment variable
* &#91;Updates&#93; Have a not display until next version on the maintenance outdated pop-up

**Fixed:**

* &#91;Camera&#93; Wrong zoom by switching from orthographic to perspective
* &#91;Display&#93; Some maps are displayed in linear instead of sRGB
* &#91;Viewports&#93; Mesh focus does not behave properly
* &#91;2D View&#93; Project with broken camera has disappearing UVs Shells
* &#91;SSS&#93;&#91;Tooltip&#93; subsurface scattering tooltips appear in the log
* Some projects cannot be opened in 2018.2 and error message can't save a null substance package
* &#91;Mask&#93; Paint tool color can be stuck in some cases when working in a mask
* &#91;Material&#93; Maps not appearing in specific situations
* &#91;Proj&#93;&#91;Tools&#93; Manipulator active with a generator
* &#91;Substance&#93; Missing Substance groups of parameters
* &#91;Scripting&#93; Incorrect software name in documentation
* &#91;UDIMs&#93; No information in log about UVs shells on multiple UVs tiles

**Known Issues:**

* Computation freeze on AMD VEGA GPUs
* Huion tablet issue with shortcuts on Windows OS

### 4.2.1 (2018.2.1)

*(Released: August 03, 2018)*

**Fixed:**

* Missing subsurface scattering shader parameters from upgrading projects

**Known Issues:**

* Computation freeze on AMD VEGA GPUs
* Huion tablet issue with shortcuts on Windows OS

### 4.2.0 (2018.2.0)

*(Released: August 02, 2018)*   
Summary: **Summer release, subsurface scattering Support, projection and fill improvements, camera import and selection, Alembic and glTF support, drag and drop on ID map, improved Substance format support and new content**

**Added:**

* &#91;SSS&#93;&#91;Viewport&#93;&#91;Iray&#93; Generic subsurface scattering
* &#91;SSS&#93; Sync MDL and subsurface scattering parameters
* &#91;SSS&#93; Added a new grayscale channel named Scattering
* &#91;SSS&#93;&#91;Shader Settings&#93; Scattering type parameter for subsurface scattering (skin or translucent)
* &#91;SSS&#93;&#91;Shader Settings&#93; Scattering scale parameter for subsurface scattering
* &#91;SSS&#93;&#91;Shader Settings&#93; Scattering color parameter for subsurface scattering
* &#91;SSS&#93;&#91;Display Settings&#93; Scattering Sample count for subsurface scattering
* &#91;Shader&#93;&#91;Iray&#93; Integrate subsurface scattering MDL for Iray
* &#91;Shader&#93; Shader update via the resource updater
* &#91;Shader&#93; Update change log API and documentation
* &#91;Tool Properties&#93;&#91;Proj&#93; New parameters for the triplanar projection
* &#91;Viewport&#93;&#91;Proj&#93; Control Fill Layer properties in 3D view directly with manipulators (triplanar projection)
* &#91;Shortcuts&#93;&#91;Proj&#93; New shortcuts Q, W, E, R, T for triplanar projection manipulators
* &#91;Viewport&#93;&#91;Proj&#93; Control Fill Layer properties in 2D view directly with manipulators (UV projection)
* &#91;Shortcuts&#93;&#91;Proj&#93; New shortcut Q for UV projection manipulators
* &#91;Contextual Toolbar&#93;&#91;Proj&#93; Control triplanar projection manipulators
* &#91;Contextual Toolbar&#93;&#91;Proj&#93; Control UV projection manipulators
* &#91;Tool Properties&#93; Disable texture tiling with projection and Stencil tool
* &#91;Stencil&#93; Use non-squared images with the projection tool/stencil
* &#91;Stencil&#93; Allow control of tiling mode in Properties window
* &#91;Stencil&#93; Zoom is not centered on a non-tiling stencil
* &#91;Cameras&#93; Import cameras from Maya, Max, Blender, Modo, DAE
* &#91;Cameras&#93;&#91;Viewport&#93; Select and control imported cameras in viewport
* &#91;Cameras&#93;&#91;Iray&#93; Select and control imported cameras in Iray
* &#91;Cameras&#93;&#91;UI&#93;&#91;New project&#93;&#91;Project configuration&#93; Import cameras is checked by default
* &#91;Cameras&#93;&#91;Shortcuts&#93; Add shortcuts to switch between cameras
* &#91;Cameras&#93;&#91;Viewport&#93; Add frame in viewport
* &#91;Cameras&#93;&#91;Viewport Settings&#93; Control of frame opacity
* &#91;Cameras&#93;&#91;Camera Settings&#93; Maximum focal length at 500mm
* &#91;Cameras&#93;&#91;Camera Settings&#93; Expose ratio
* &#91;Cameras&#93;&#91;Camera Settings&#93; Add a lock option
* &#91;Cameras&#93;&#91;Camera Settings&#93; Add a restore option
* &#91;Cameras&#93;&#91;Camera Settings&#93; Add focus distance attribute
* &#91;glTF&#93; Import of a glTF file
* &#91;glTF&#93; Import ambient occlusion map
* &#91;Alembic&#93; Import Alembic 1 frame with static geometry
* &#91;Shelf&#93; Drag and drop materials directly onto the mesh using ID maps with a modifier (CTRL/Command)
* &#91;Layer Stack&#93; Automatic ID mask creation with drag and drop of materials on mesh with ID maps
* &#91;Layer Stack&#93; Automatic scroll of layers with drag and drop across the layer stack
* &#91;UI&#93;&#91;Tool Properties&#93; Expose Substance's preset
* &#91;UI&#93;&#91;Help menu&#93; Improvement of the Help menu
* &#91;UI&#93;&#91;New Project&#93;&#91;Project Configuration&#93; Reorganization of the window
* &#91;UI&#93;&#91;New Project&#93;&#91;Project Configuration&#93; Replace Mesh term by File
* &#91;UI&#93;&#91;Substance&#93; Display Substance attributes in UI
* &#91;Shortcuts&#93; F4 switches between 2D and 3D view
* &#91;Shortcuts&#93; New shortcuts for toggle stencil N and quick mask U
* &#91;Substance integration&#93; Take into account 'visible if' statements in the Substance parameters
* &#91;Viewport&#93; Shadows not forced to be computed after camera move
* &#91;Content&#93; Update MeetMat with imported cameras
* &#91;Content&#93; Add a sample with subsurface scattering enabled - JadeToad
* &#91;Content&#93; Add a new PBR project template with subsurface scattering enabled
* &#91;Content&#93; Updated export presets to add new Scattering channel
* &#91;Content&#93;&#91;Shelf&#93; Added subsurface scattering support for: pbr-metal-rough, pbr-metal-rough-alpha-test, pbr-coated, pbr-spec-gloss
* &#91;Content&#93;&#91;Shelf&#93; Added Scattering channel to 5 smart materials (marbles and skins)
* &#91;Content&#93;&#91;Shelf&#93; 1 new jade Material
* &#91;Content&#93;&#91;Shelf&#93; 1 new wax Material

**Fixed:**

* &#91;CMD&#93; Different results using same command line with different versions
* &#91;TDR&#93; If TdrLevel is set up you don't have any errors in your log
* &#91;Baker&#93; Ambient occlusion map is flipped
* &#91;ID Map&#93; Crashing when picking outside of 0-1 range
* &#91;Iray&#93; Crash when switching texture sets and going back to Paint mode
* &#91;Viewport&#93; Sync drop areas between viewports for drag and drop
* &#91;Engine&#93; Moire artifact when tiling fill layers or painting small brush
* &#91;License&#93; License service bad software version check
* &#91;License&#93; Rework the way we handle authentication
* &#91;API&#93; Call the onNewProjectCreated scripting API event even when creating with a template
* &#91;Shader&#93; Compiled shader is not loaded from cache when shader file doesn't compile
* &#91;Shelf&#93; Exporting HDR file from the shelf will output a file with clamped values
* &#91;Export&#93; EXR export clamps RGB color values between 0-1
* &#91;Content&#93; Procedural noise 3D Perlin Noise Fractal is pixelated

**Known Issues:**

* Computation freeze on AMD VEGA GPUs
* Huion tablet issue with shortcuts on Windows OS

### 4.1.3 (2018.1.3)

*(Released: June 28, 2018)*

**Added:**

* &#91;Preferences&#93; Propose to save project when Painter restarts

**Fixed:**

* &#91;Plugin&#93; Search Substance Source does not work
* &#91;Smart Materials&#93; Importing Smart Materials leads to a crash in some cases
* &#91;Smart Materials&#93; Deleting Smart Materials leads to a crash in some cases
* &#91;Save&#93; Saving leads to a crash in some rare cases
* &#91;Shelf&#93; Invert does not work on Cells 2 and Cells 3
* &#91;Shelf&#93; Typo in some Alphas
* &#91;Shelf&#93; Some substance materials do not render properly

**Known Issues:**

* Computation freeze on AMD VEGA GPUs

### 4.1.2 (2018.1.2)

*(Released: June 12, 2018)*   
Summary: **Improved Baking Speed, Improved Save System, Updated Sliders, Updated Plugin API, Chinese Translation, Improved Padding now Optional**

**Added:**

* &#91;Bakers&#93; Performance improvement with new baker version
* Force display dialog with incompatible GPU
* &#91;Save&#93; Expose new compact project functionality (full/compact save mode)
* &#91;Save&#93; Inform user in case of saving error
* &#91;Clean&#93; Next save in full/compact mode
* &#91;Sliders&#93; Improvement of the precision of the color/grayscale bars and sliders
* &#91;Sliders&#93; Addition of Up/Down arrow controls
* &#91;Sliders&#93; Same detection zone for color and grayscale bar sliders
* &#91;Plugin&#93; Autosave always in incremental mode
* &#91;Plugin&#93; Option to switch plugins to new interface style
* &#91;Language&#93; Add Chinese translation
* &#91;Padding&#93; Option to switch between UV and 3D space neighbor padding per Texture Set in Texture Set Settings
* &#91;Script&#93; Expose save mode: full/compact or incremental
* &#91;Script&#93; Update scripting/QML documentation
* &#91;Log&#93; Indicate save mode in log (full/compact or incremental)

**Fixed:**

* &#91;Tool&#93; Channel slot transforms into a material slot on single-channel fills
* Crash when loading a mesh (FBX) with some faces not assigned by a material
* Crash in Iray with NVIDIA GRID 5.2 on virtual machine
* Crash when undoing a material preset deletion
* Crash when loading some projects
* &#91;Command line&#93; New command line for UDIMs meshes split-by-udim
* &#91;Toolbar&#93; Shrinking of the toolbar
* &#91;Instancing&#93; Cannot instantiate bitmaps across multiple texture sets
* &#91;Viewport&#93; Refresh is not complete when painting on mesh with tiled UVs
* &#91;Iray&#93; Normal Map is applied twice for dielectrics
* &#91;Shelf&#93; Typos in some Substance parameters (alphas, procedurals and matfx)
* &#91;Shelf&#93; Typo for the bitmap "Authorized Personnel Only"
* &#91;Script&#93; Function alg.shaders.materials() does not work anymore

**Known Issues:**

* Computation freeze on AMD VEGA GPUs

### 4.1.1 (2018.1.1)

*(Released: April 03, 2018)*

**Fixed:**

* &#91;Tablet&#93; Issue when changing default interaction choices
* &#91;Bakers&#93; Crash with Assimp library
* &#91;Bakers&#93; Regression on performance with A.O. map
* &#91;Iray&#93; Lens Distortion is not applied to the Alpha channel
* &#91;Drivers&#93; Update of minimum drivers requirements
* &#91;3Dview&#93; Normals not correctly generated on UDIM meshes without normals information
* &#91;Intel&#93; Crash with Substance Painter 2018.1.0
* &#91;Intel&#93;&#91;Viewport&#93; Issue with padding (black artefacts)

**Known Issues:**

* Computation freeze on AMD VEGA GPUs

### 4.1.0 (2018.1.0)

*(Released: March 15, 2018)*

**Added:**

* New overall style (icons, color, behavior)
* New default layout
* &#91;Tablet&#93; User experience enhancement while painting
* &#91;Main menu&#93; Sort native items in views and toolbars first
* &#91;Main menu&#93; Move quick mask actions in viewport section
* &#91;Main menu&#93; Move right-click actions into viewport section
* &#91;Main menu&#93; Rename "View" menu as "Window"
* &#91;Quick menu&#93; New tool properties by right click in viewport
* &#91;Dock widget&#93; New dock toolbar for quick reduce/recall
* &#91;Display settings&#93; Camera and viewer settings window merged
* &#91;Layer stack&#93; Contextual right click menu
* &#91;Layer stack&#93; Drag and drop to move any effect within the same layer
* &#91;Toolbar&#93; Reorganization of toolbar and new contextual toolbar
* &#91;Tools toolbar&#93; Split clone tool into two separate tools
* &#91;Tools properties&#93; Lighter background grayscale value in the preview
* &#91;Tools properties&#93; Organization in tabs (fill and tools)
* &#91;Tool&#93; Painting result matches the stencil
* &#91;Viewport&#93; New cursor for fill layer
* &#91;Viewport&#93; Smoother navigation and painting (higher frame rate)
* &#91;Viewport&#93; Material/Channel/Map selection combobox in viewport
* &#91;Viewport&#93; Reduce flickering while rotating (shadow on)
* &#91;Shelf&#93; Display materials by default when opening Painter
* &#91;Shelf&#93; Loading time improvement of Substance textures and materials (2 to 6 times faster)
* &#91;Shelf&#93; Reorganize materials folders to fit Substance Source structure
* &#91;Shelf&#93; Drag and drop materials directly on the mesh in the viewport
* &#91;Shelf&#93; New 3D Noises (Perlin, Perlin Fractal, Simplex and Worley)
* &#91;Shelf&#93; New 3D Linear Gradient mask generator using mesh position
* &#91;Shelf&#93; Updated base Noises to support non square expansion
* &#91;Shelf&#93; Added new template and export preset for Lens Studio (Snap application)
* &#91;Shelf&#93; Updated Smart Materials and Smart Masks to use latest version of the Mask Editor (micro details)
* &#91;Shelf&#93; New sample project "TilingMaterial" to create seamless tiling materials
* &#91;Shelf&#93; New brush presets (Calligraphy, Wet, Hatching and so on)
* &#91;Sliders&#93; New sliders and grayscale/color bars style and behavior
* &#91;Bakers&#93; Allow use of full scene bounding box to compute the position map
* &#91;Shader&#93; Remove height force parameter from the default shader parameters
* &#91;Engine&#93; Substance engine updated
* &#91;Engine&#93; No or less discontinuities across UV chunks
* &#91;Plugins&#93; Import materials downloaded from Substance Source more quickly
* &#91;Plugins&#93; Update all plugins to match new overall style
* &#91;Preferences&#93; Preview background color changes automatically
* &#91;Clean&#93; Reduced risk of project corruption
* &#91;Open&#93; Opening project time improvement
* &#91;New project&#93; New project - mesh update time improvement
* &#91;Save&#93; Saving Project time improvement
* &#91;Log&#93; License type reported in log
* &#91;TextureSet&#93; Rename "Bake Textures" button as "Bake Mesh Maps"
* Rename "Additional maps" as "Mesh maps"

**Fixed:**

* &#91;Viewport&#93; Bad performances with meshes containing a lot of sub-objects
* &#91;Tools properties&#93; Channel disabled when dragging and dropping an image into the material slot
* &#91;Tools properties&#93; Brush preview is broken with smudge and clone tools
* &#91;Texture set&#93; Channels order is wrong when using templates
* &#91;Shelf&#93; Missing icon for Grayscale Conversion generator
* &#91;Shelf&#93; Sign Circle Number alpha is broken (missing font)
* Incorrect detection of integrated GPUs at launch
* &#91;Crash&#93; Drag-and-droping an imported ressource named with a # character
* &#91;Engine&#93; Vram detection issue on integrated GPU
* &#91;Engine&#93; Fixed numerous crashes in Substance Engine Linker
* &#91;Engine&#93; Square artefacts when changing resolution
* &#91;Post Effects&#93; Interface resize is slow when post effects are on
* &#91;Bakers&#93; Scene unit is not correctly respected for Ray Distance values
* &#91;Bakers&#93; AO from Mesh Occluder distance is clamped to 1 no matter the input value
* &#91;Bakers&#93; Match by name ignores some meshes with specific names
* &#91;Bakers&#93; Color from mesh Polygroup and Submesh ID setting always return a black image
* &#91;Bakers&#93; ID Baking fails with binary FBX meshes from Blender
* &#91;Shader&#93; Noise in the 2D View with dota-2 and non-pbr-spec-gloss
* &#91;Linux&#93; Only one CPU thread is used when baking
* &#91;MacOS&#93; Crash with brush cursor moving over the viewport

**Known Issues:**

* Computation freeze on AMD VEGA GPUs
* Distorsion post process not taken into account while exporting in IRay (alpha)

## Version 3

### 3.4.2 (2017.4.2)

*(Released: January 24, 2018)*

**Added:**

* &#91;Export&#93; Get the status of an export with step progress
* &#91;Export&#93; Allow cancelling an export
* &#91;Export&#93; Export textures to Sketchfab without loosing normal map quality
* &#91;Export&#93; Export in glTF binary format (glb)
* &#91;Export&#93; Allow resizing columns in configuration tab of the export window
* &#91;Shader&#93; Add a changelog for the shader API
* &#91;Scripting&#93; Add Before and After callback functions when exporting textures
* &#91;Iray&#93; Upgrade to SDK 2017.1 (support of Volta GPUs)

**Fixed:**

* Crash when quitting the application before the main window is displayed
* &#91;MAC&#93; Crash when loading grayscale maps with IRAY
* &#91;MAC&#93; VRAM detection is not correct with the new High Sierra OS
* &#91;Plugin&#93; Downloading assets from Substance Source does not work anymore
* &#91;Scripting&#93; Incorrect minimum plugin version detection
* &#91;Export&#93; Fail to save export preset after exporting textures
* &#91;Instancing&#93; Issue on generators instantiated in a TextureSet with no Additional Maps
* &#91;Viewport&#93; Dithering does not work with resolution above 4k
* &#91;Viewport&#93; 2D View material display is covered with noise
* &#91;Shelf&#93; Improve loading time for shelf presets
* &#91;Engine&#93; Incorrect blending when painting under color selection

### 3.4.1 (2017.4.1)

*(Released: December 15, 2017)*

**Added:**

* &#91;Scripting&#93; Export mesh through the scripting API
* &#91;Import&#93; Disable import of unsupported mesh file format (allow only obj, fbx, dae, ply)
* &#91;Log&#93; Indicate more precisely the TDR issue in the log file

**Fixed:**

* Crash if application is closed before resources crawling has finished
* Crash when opening projects with Smudge/Clone tool
* Crash when using redo after an undo of a Shader change in Viewer Settings
* &#91;Engine&#93; Texturing differs between Painter 2017.2 and 2017.4
* &#91;Viewport&#93; Picking on an ID map from an instance samples the wrong color
* &#91;Export&#93; Crash when exporting an invalid normal or occlusion texture
* &#91;Export&#93; PSD files have their groups locked when opened in Photoshop CS6
* &#91;Plugin&#93; Photoshop plugin ignores channel selection and always export everything
* &#91;Layers&#93; Anchors break when copy/pasted across Texture Sets
* &#91;Layers&#93; Some anchor's references cannot be restored if broken
* &#91;Shader&#93; pbr-coated secondary roughness parameter is broken
* &#91;Steam&#93; Version checker pop-up shouldn't be visible at launch

**Known Issues:**

* &#91;AMD&#93; Crashes/Freezes when trying to paint on a mesh. Can be fixed with a GPU Driver update.

### 3.4.0 (2017.4.0)

*(Released: November 23, 2017)*

**Added:**

* &#91;Instancing&#93; Allow to instantiate parameters across layers
* &#91;Instancing&#93; Allow to jump between a source layer and an instance
* &#91;Instancing&#93; Add a "instantiate across texture sets" action
* &#91;Instancing&#93; Indicate in the layer stack re-entrant instances (cycles)
* &#91;Instancing&#93; Delete instances when a source is removed
* &#91;Instancing&#93; Don't allow Anchor's references from outside an instanced folder
* &#91;UI&#93; Move the Undo Stack into its own window named "History"
* &#91;Plugin&#93; Integrate DCC live-link plugin
* &#91;Engine&#93; Improve painting performances with Sparse painting
* &#91;Export&#93; Add draft and re-export options to Sketchfab exporter
* &#91;Shelf&#93; Add "flip" control for Font substances
* &#91;Shelf&#93; Add 20 new procedurals materials
* &#91;Shelf&#93; Add 40 new grunges maps (bitmap based and procedural)
* &#91;Viewport&#93; Enable brush preview collisions on other visible texture sets
* Update AMD GPU drivers minimum requirements

**Fixed:**

* Crash When computing Substances at too big resolutions
* Crash when painting heavily with particles
* &#91;Viewport&#93; Incorrect specular reflection in the 2D view with specific meshes
* &#91;UI&#93; Some unwanted actions appear into the History window

**Known Issues:**

* &#91;Layers&#93; Some anchor's references cannot be restored if broken
* Crash when using redo after an undo of a Shader change in Viewer Settings

### 3.3.3 (2017.3.3)

*(Released: December 01, 2017)*

**Fixed:**

* &#91;Steam&#93; Version checker pop-up shouldn't be visible at launch
* &#91;Export&#93; PSD files have their groups locked when opened in Photoshop CS6

### 3.3.2 (2017.3.2)

*(Released: November 20, 2017)*

**Added:**

* &#91;UI&#93; Improve new version dialog and add changelog
* &#91;UI&#93; Indicate if maintenance is expired in new version dialog
* &#91;License&#93; Update license system to handle Maintenance dates
* &#91;Export&#93; Rename Adobe Standard Material to Adobe Dimension

**Fixed:**

* &#91;Mac&#93; Painting leads to black squares and texture corruptions
* &#91;Engine&#93; Cache can sometimes disappear in the Viewport
* &#91;Engine&#93; Blocky artifacts appear when memory compression trigger
* &#91;Baking&#93; Strange error messages when baking specific meshes
* &#91;Export&#93; PSD are incorrectly written and are not recognized properly by Photoshop
* &#91;Layers&#93; It shouldn't be possible to copy/paste layer across multiple projects
* &#91;Substance&#93; UserData color space for Normal input is flipped in some cases
* &#91;Shelf&#93; Micro-normal in generators outputs inverted curvature
* &#91;Shelf&#93; HSL filter also affect alpha channel
* &#91;Linux&#93; Installation on Centos fails because of missing dependencies
* Installer doesn't remove all resources from previous install in certain cases

### 3.3.1 (2017.3.1)

*(Released: October 26, 2017)*

**Added:**

* &#91;Export&#93; Allow to export the mesh from a project
* &#91;Shelf&#93; Remove "Sub-Shelf" from the tabs titles
* Save post-process settings in templates
* Make the TDR message more understandable
* Improve Settings window to report errors

**Fixed:**

* Crash when deleting several sub-shelves
* Crash when switching from a level to something else during an engine computation
* &#91;Mac&#93; Crash on Intel GPU during engine computations
* &#91;Mac&#93;&#91;Viewport&#93; Bad performances when dithering is enabled
* &#91;Mac&#93; MacOS 10.13 is recognized as "Unknown version" in the log file
* &#91;Baker&#93; Baking with a cage doesn't work anymore
* &#91;Layers&#93; Ctrl + C shortcut (copy action) doesn't work anymore
* &#91;Layers&#93; Pasting layers doesn't refresh UI with anchor's references
* &#91;Anchor&#93; Duplicate or Copy/Paste Layer with References breaks links
* &#91;Export&#93; 8K export can crash or deadlock application in some cases
* &#91;Export&#93; Multiple issues in generated glTF file format
* &#91;Import&#93; Re-importing a mesh with the same filename doesn't work anymore
* &#91;Plugin&#93; Auto-save window always appear on top of everything
* &#91;UI&#93; Infinite loop when you Press "Escape" on the TDR Dialog
* &#91;UI&#93; Reset UI display a second title bar on the shelf window

### 3.3.0 (2017.3.0)

*(Released: September 28, 2017)*

**Added:**

* &#91;Export&#93; Allow to export mesh and textures for Adobe Project Felix
* &#91;Export&#93; Allow to export into glTF file format
* &#91;Engine&#93; Optimize textures size in VRAM by using block compression
* &#91;Viewport&#93; Be able to drag and drop a mesh or project in the viewport
* &#91;UI&#93; Improve warning message about TDR
* &#91;UI&#93; Log should be displayed only upon request
* &#91;UI&#93; Allow to clear the content of the log window
* &#91;UI&#93; Display warnings and errors in the status bar
* &#91;UI&#93; Display Tabs on top as in web browsers
* &#91;UI&#93; Improve "not paintable" context and messages
* &#91;UI&#93; Add a "save as copy" action in the file menu
* &#91;Layer&#93; Set default tiling setting to 1 by default
* &#91;Shelf&#93; Improved gradient filter to support 10 dynamic colors
* &#91;Shelf&#93; Add a space in the default query of the mini-shelf
* &#91;Shelf&#93; Add a "Open in explorer" action for local resources in the shelf
* &#91;Shelf&#93; Add template and shader for Adobe Material Standard (Project Felix)
* &#91;Shelf&#93; Increase max tiling to 128 in Material Layering shaders
* &#91;Shelf&#93; Added sobel curvature for micro-details of Mask Generators
* &#91;Plugin&#93; Add autosave plugin with customizable time interval
* &#91;Scripting&#93; Add a "save as copy" function

**Fixed:**

* &#91;UI&#93; Layout is broken at the first launch
* &#91;Export&#93; PSD generated at export has format errors
* &#91;Export&#93; EXR always exports 8 bits height map
* &#91;Export&#93; Crash when exporting corrupted Additional maps
* &#91;Import&#93; Hard edges are not preserved on low poly meshes in some cases
* &#91;Import&#93; Improved error messages when importing meshes with issues
* &#91;Bakers&#93; ID Map Baking fail with Match By Name enabled
* &#91;Viewport&#93; Tangent space is not synched with bakers
* &#91;Effect&#93; Moving back a layer doesn't restore an anchor's reference
* &#91;Effect&#93; Refresh issue when creating a link in between two Masks with anchors
* &#91;Effect&#93; Masks anchors above mask shouldn't be listed
* &#91;Effect&#93; Extract Alpha setting from Anchors doesn't work
* &#91;Engine&#93; Mask inverts itself after first brush stroke
* &#91;Engine&#93; Crash when switching Texture Set on specific project
* &#91;Shelf&#93; Crash when deleting a preset which is in a project
* &#91;Shelf&#93; Typo in advanced Tri-Planar filter
* &#91;Shelf&#93; MG Mask Builder AO Noise Scale doesn't work properly
* &#91;Shelf&#93; MG Mask Builder has inverted curvature parameters
* &#91;Shelf&#93; Imported alphas generate a material sphere preview instead of a flat one

### 3.2.0 (2017.2.0)

*(Released: July 27, 2017)*

**Added:**

* Anchor Points - Layer and Mask referencing system
* &#91;Layers&#93; Ability to rename Fill and Paint Effects
* &#91;Plugin&#93; Updated Substance Source plugin
* &#91;Scripting&#93; Allow to query Texture Set Resolution
* &#91;Scripting&#93; Allow to get the status of the Painting engine
* &#91;Performance&#93; Improved project loading and brush stamping optimizations

**Fixed:**

* &#91;Tool&#93; Performance issues when tweaking material parameters
* &#91;Engine&#93; Disappearing brush strokes when changing resolution (4K&gt;2K)
* &#91;3D View&#93; Tangent space is not synched with bakers
* &#91;Shelf&#93; Shelf path in the user documents isn't created automatically
* &#91;Shelf&#93; Make presets compatible with previous versions after an update
* &#91;Shader&#93; Non-PBR shader doesn't work anymore
* &#91;Bakers&#93; ID Map Baking fail with Match By Name enabled
* &#91;Sample&#93; Meet Mat sample project Texture Set names are incorrect
* Saving a project before creating a template returns write permission errors

### 3.1.0 (2017.1.0)

*(Released: June 20, 2017)*

**Added:**

* &#91;Plugin&#93; New Substance Source plugin (allow to download assets in the shelf)
* &#91;Shelf&#93; 4 New Fonts (Japanese + Simplified Chinese, Typewriter, Segment)
* &#91;Shelf&#93; 230 New Alphas (Mix of patterns, brushes and fingerprint scans)
* &#91;Shelf&#93; 50 New Procedurals (Fabric patterns of medieval and contemporary clothing)
* &#91;Shelf&#93; 2 New environment maps (Mondarrain and Villa Nova Street)
* &#91;Shelf&#93; 9 New filters (MatFx Detail Edge Wear, Clamp, HBAO, etc.)
* &#91;Shelf&#93; Improved default Panorama environment map
* &#91;Shelf&#93; New Arnold 5 export presets
* &#91;Scripting&#93; Allow to import resource into the Shelf

**Known Issues:**

* &#91;Export&#93; Editing an export preset is very slow

## Version 2

### 2.6.2

*(Released: October 20, 2017)*

<b>Added:</b>

* &#91;Texture Set&#93; Allow to delete disabled texture sets
* &#91;Shelf&#93; Allow multiple users to write inside the same shelf folder
* &#91;Scripting&#93; Be able to reload plugins folder
* &#91;Scripting&#93; Add a required minimal API version in plugin metadata to ensure compatibility
* &#91;IRay&#93; Export image dialog improvements

<b>Fixed:</b>

* &#91;Engine&#93; Disappearing strokes issue, when changing resolution (4K&gt;2K)
* &#91;Bakers&#93; ID Map Baking fail with Match By Name enabled
* &#91;Bakers&#93; Error messages are not explicit enough
* &#91;3D View&#93; Tangent space is not synched with bakers
* &#91;Tool&#93; Black artifacts when using the smudge tool
* &#91;Shader&#93; Non-PBR shader doesn't work anymore
* &#91;Shader&#93; "pbr-coated" is broken
* &#91;Shader&#93; Coating Roughness of "pbr-coated" shader has no impact anymore
* &#91;Shader&#93; Spec gloss shader doesn't match Iray and SD
* &#91;Shelf&#93; Crash when loading two files with the same name but different extensions
* &#91;Shelf&#93; Can't edit preset anymore in the shelves
* &#91;Shelf&#93; Cannot set a custom preview for assets imported in the shelf
* Resources loaded from the cache lose their usages
* Saving a project before creating a template returns write permission errors
* Incorrect project save if filename contains two periods
* Importing files with multiple dots (.) in the filename causes issues

### 2.6.1

*(Released: May 12, 2017)*

**Added:**

* &#91;TextureSet&#93; Don't allow to reassign mesh materials to nothing

**Fixed:**

* Crash when switching of TextureSet after replacing baked map
* Crash when doing "Undo and Redo" after changing layer's blending mode
* Crash or Freeze when using the "color selection" effect with big ID map
* &#91;Export&#93; Texture Sets renamed are not sorted alphabetically in the export window
* &#91;TextureSet&#93; Reset to default name doesn't check for unicity
* &#91;TextureSet&#93; Renamed texture set become disabled after reopening project
* &#91;Shelf&#93; Missing default templates content
* &#91;Shelf&#93; Non-square textures are displayed as square
* &#91;Shader&#93; Once a texture set is disabled the associated shader is destroyed
* &#91;Scripting&#93; alg.baking.setTextureSetBakingParameters() doesn't work anymore
* &#91;Scripting&#93; Typo in websocket tutorial
* &#91;Scripting&#93; Various problems in AlgWidgets
* &#91;Log&#93; Incorrect detection of available virtual memory in some cases

### 2.6.0

*(Released: April 27, 2017)*

**Added:**

* Add new sample project "Meet Mat"
* &#91;Plugin&#93; New "Resources Updater" plugin
* &#91;TextureSet&#93; Allow to rename and add a description to texture sets
* &#91;TextureSet&#93; Allow to reassign materials
* &#91;TextureSet&#93; Add a setting button in the texture set list window
* &#91;TextureSet&#93; Show "disabled" texture sets at the bottom of the list
* &#91;Substance&#93; Use additional maps at the current texture set resolution to improve performances
* &#91;Scripting&#93; Allow to update a resource used in a project (material, generator, etc.)
* &#91;Scripting&#93; Add a way to add/remove a shelf
* &#91;Scripting&#93; Allow to query info from resource in projects
* &#91;Scripting&#93; Allow to retrieve a list of available shelfs
* &#91;Scripting&#93; Improve AlgWidget thumbnail tutorial
* &#91;Export&#93; Disable/Enable bit depth based on file format support
* &#91;Log&#93; Add plugin name to print in console
* &#91;Log&#93; Remove error about hidden texture sets
* Update "Welcome Screen" with new icons and text for samples

**Fixed:**

* Crash when updating a mesh in specific projects
* &#91;Viewport&#93; Symmetry plane inner color is not visible anymore
* &#91;Viewport&#93; Some post-process effects are enabled when using the solo view
* &#91;Shaders&#93; "over\_premult" blending doesn't work properly
* &#91;Shaders&#93; Warning about alpha-test with the default shader
* &#91;Shelf&#93; Incorrect parsing of tags from Substances
* &#91;Shelf&#93; MatFX Rust Weathering doesn't work properly
* &#91;Shelf&#93; HSL filter is enabled on incorrect channels by default
* &#91;Shelf&#93; Sharpen is enabled on Height/Normal channel by default
* &#91;Export&#93; Vray export presets don't use an OpenGL normal map
* &#91;Tool&#93; Imprecision issues with clone/smudge tool create artifacts

### 2.5.3

*(Released: March 15, 2017)*

**Fixed:**

* &#91;Baker&#93; Crash when baking with specific meshes

**Known Issues:**

* &#91;Mac&#93; Particles can create texture corruption in some cases

### 2.5.2

*(Released: March 14, 2017)*

**Fixed:**

* &#91;Tool&#93; Wacom tablets don't work on Linux
* &#91;Tool&#93; Black artifacts when using the smudge tool
* &#91;Bakers&#93; Baking fail if Match By Name is used with a cage
* &#91;Bakers&#93; Ambient Occlusion broken when baking with Normal Map only
* &#91;Shelf&#93; Generic filters don't handle alpha properly (Contrast/Luminosity, Highpass, etc.)
* &#91;Viewport&#93; Performance issue when loading a project with shadows enabled
* &#91;Viewport&#93; Dithering issue in 3D View on MacOS
* &#91;Viewport&#93; Particle previews incorrectly displayed when color profile is enabled
* &#91;Iray&#93; Crash when switching project back to OpenGL if Iray failed to initialize
* &#91;IRay&#93; Glossiness is ignored when rendering SpecGloss shader/mdl
* &#91;Shader&#93; Spec/Gloss shader doesn't match Iray and SD
* &#91;Shader&#93; sRGB conversion different from linear to sRGB LUT conversion
* &#91;Shader&#93; Incorrect rendering when loading project with outdated shaders
* &#91;Shader&#93; "pbr-coated" shader doesn't work anymore
* &#91;Export&#93; Some channels are still exported even if not present in the texture set
* &#91;Layers&#93; Blending mode "normal map inverse detail" doesn't work on grayscale channels
* &#91;UI&#93; Issue on "Color selection window" with HDPI monitor and display zoom at 150%

**Known Issues:**

* &#91;Mac&#93; Particles can create texture corruption in some cases

### 2.5.1

*(Released: February 27, 2017)*

**Fixed:**

* &#91;Mac&#93; Wacom tablet input broken in 3D and 2D view
* &#91;Bakers&#93; Matching by name doesn't work anymore
* &#91;Bakers&#93; "Average Normals" setting doesn't work anymore
* &#91;Iray&#93; Incorrect rendering with missing baked normal map
* &#91;Iray&#93; Color Profiles behave differently in comparison to OpenGL renderer
* &#91;Iray&#93; Exporting render as bitmap doesn't include color profile correction
* &#91;Substance&#93; Material filters don't work anymore
* &#91;Tool&#93; Stroke opacity isn't stored in brush presets
* &#91;Tool&#93; Clone Brush UV Alignment doesn't work anymore
* &#91;Export&#93; Displacement channel should be centered in 0.5 when exporting in integer
* &#91;Template&#93; Absolute path is stored in Templates
* &#91;TextureSet&#93; Channel texture persist after removing the channel

**Known Issues:**

* &#91;Linux&#93; Wacom tablets inputs don't work in 3D and 2D view
* &#91;Mac&#93; Particles can create texture corruption in some cases
* &#91;Export&#93; In very rare case, black rectangles can appear on AMD GPUs

### 2.5.0

*(Released: February 21, 2017)*

**Added:**

* Add support for AMD Radeon Pro and AMD FirePro GPUs
* &#91;Tool&#93; Add support for stroke opacity
* &#91;Tool&#93; Add a modifier that allow to continue the last brush stroke
* &#91;Iray&#93; Update to support Pascal GPUs
* &#91;Viewport&#93; Add support for Color Profiles (LUT)
* &#91;Substance&#93; Integrate new framework (SD6 engine)
* &#91;UI&#93; Increase "recent file" size list in File menu
* &#91;Import&#93; Use category from substances to fill the prefix in the import dialog
* &#91;Bakers&#93; Allow to bake 8K textures
* &#91;Bakers&#93; Allow to bake non-square resolutions
* &#91;Bakers&#93; Improve memory consumption when baking heavy high-poly meshes
* &#91;Shelf&#93; Lock shelves (and projects) to forbid concurrent editing and avoid corruptions
* &#91;Shelf&#93; Read category and keywords from substances to use them for filtering
* &#91;Shelf&#93; Allow to exclude ressources from the result of a search query
* &#91;Shelf&#93; Improved thumbnails time computation
* &#91;Shelf&#93; Allow to embed presets in projects
* &#91;Shelf&#93; Allow to quickly collapse/expand the tree-view with SHIFT
* &#91;Shelf&#93; Allow to save thumbnails when assets are read only (local cache)
* &#91;Shelf&#93; New content : new filters (transform, mirror, tri-planar, etc.)
* &#91;Shelf&#93; New content : new LUTs profiles (classic and artistic, such as Film Noir, Vintage, etc.)
* &#91;Shelf&#93; New content : 10 new Font Substances to quickly generate custom texts
* &#91;Shelf&#93; New templates : Unity 5 and Unreal Engine 4
* &#91;Shelf&#93; Improved HSL filter to be more artist friendly
* &#91;Shader&#93; Add support for specular level channel in PBR shaders
* &#91;Shader&#93; Add support for Dithering in Alpha Test shader
* &#91;Shader&#93; Add support for parallax occlusion mapping in PBR shaders
* &#91;Shader&#93; Allow to define custom UI for shader parameters
* &#91;MatLayering&#93; Create new Mask channel for material layering workflow
* &#91;Scripting&#93; Allow to write metadata in a SP project
* &#91;Scripting&#93; Allow to export with a specific export preset
* &#91;Scripting&#93; Allow to retrieve shader parameters as a JSON
* &#91;Scripting&#93; Add support for WebSocket connections
* &#91;Scripting&#93; Add the possibility to load shader instances
* &#91;Scripting&#93; Add the possibility to create a new project
* &#91;Scripting&#93; Allow to retrieve the url of the mesh imported in a project
* &#91;Scripting&#93; Allow non square baking
* &#91;Scripting&#93; Report errors when setting data via scripting API
* &#91;Substances&#93; Add user-data tag to specify normal map format

**Fixed:**

* Crash when picking color with substances
* Crash when loading a non RGBA32f image as environment map
* Crash related to painting on AMD GPUs
* &#91;Mesh&#93; OBJ import doesn't recognize materials without mtl file
* &#91;Mesh&#93; UDIM Texture set name generation can be incorrect on some meshes
* &#91;UI&#93; Undo/Redo button in Viewer Setting steal focus and stop mouse scrolling
* &#91;UI&#93; Some labels are incorrectly cropped in High-DPI
* &#91;Layer&#93; Replace mode for paint effect has an incorrect behavior on Mask
* &#91;Layer&#93; Subtract blending mode has an incorrect behavior with alpha
* &#91;Tool&#93; Brush size becomes huge in 2D View when painting on UV borders
* &#91;Tool&#93; Snapped straight line has erratic behavior with High-DPI
* &#91;Tool&#93; Stencil resolution is sometimes incorrect
* &#91;Bakers&#93; "Max Occluder Distance" values are clamped if "relative to bounding box" is "Off"
* &#91;Shader&#93; Stack and auto param channel definitions don't match
* &#91;3D View&#93; Inconsistent display of the normal channel depending of project setting
* &#91;Viewport&#93; Some normal maps have clamped values which appear as artifacts
* &#91;Viewport&#93; Post-effect are always disabled by default
* &#91;Export&#93; Normal mixing setting is incorrect if normal channel is missing
* &#91;Export&#93; Incorrect texture generation in some cases on AMD GPUs
* &#91;Export&#93; Shader parameters are not exported properly if located inside a group
* &#91;Export&#93; Editing an export preset in a custom shelf output a log error
* &#91;Shelf&#93; Tree-view filtering does not match exactly the folder name
* &#91;Shelf&#93; Renaming a shelf preset is hard to read
* &#91;Shelf&#93; Shader resource imported in the Shelf isn't preserved after relaunching
* &#91;Shelf&#93; Content : Weld tool preset is missing
* &#91;Shelf&#93; Content : Tile Generator doesn't work properly
* &#91;Shelf&#93; Content : Fixed incorrect mask on Rubber Tire Dirty smart material
* &#91;Shelf&#93; Content : Fixed incorrect group name on Leather bag material
* &#91;Iray&#93; Half of meshes are missing in Iray
* &#91;Linux&#93; Crash when dragging a resource above the 3D View
* &#91;Mac&#93; Preferences are reset at every launch on Sierra

**Known Issues:**

* &#91;Export&#93; In very rare case, black rectangles can appear on AMD GPUs
* &#91;Iray&#93; Color Profiles can behave in odd ways sometimes

### 2.4.1

*(Released: October 28, 2016)*

**Fixed:**

* Crash when creating a project with a template
* Crash when closing export dialog during an export
* &#91;Mac&#93; Errors when saving project (fail to save export preset)
* &#91;Shelf&#93; Creating a new preset will display it twice
* &#91;Shelf&#93; Presets cannot be loaded in read-only mode without admin rights

### 2.4.0

*(Released: October 27, 2016)*

**Added:**

* &#91;Shelf&#93; New interface to browse ressources (tree-view, filters and so on)
* &#91;Shelf&#93; Allow to save a search as a preset
* &#91;Shelf&#93; Allow to create a new window from a preset
* &#91;Shelf&#93; New interface for importing resources
* &#91;Shelf&#93; Don't copy default allegorithmic shelf in Documents folder
* &#91;Shelf&#93; New particles presets : Electric Circuit, Electric Lines, Rococo, Veins Small
* &#91;Shelf&#93; Improved older particles presets to be more easy to use (like "Rain")
* &#91;Shelf&#93; Add new information on resource contextual menu
* &#91;Viewport&#93; Improve performance when loading environment maps
* &#91;Viewport&#93; Add support of environment maps that are not power of two

**Fixed:**

* Crash when removing a mask
* Crash when painting after saving a preset
* Crash with environment blur on some GPUs
* Crash when assigning a wrong resource with the mini shelf
* &#91;Shelf&#93; Clean + Save remove tags and metadata for resources in the project
* &#91;Shelf&#93; importing a preset will display its ressources in the shelf
* &#91;Export&#93; Normal map generated from height channel has a low intensity
* &#91;Export&#93; Normal from mesh is not always present in final normal map
* &#91;Export&#93; Dilation with transparency can sometimes result with no transparency
* &#91;Scripting&#93; "alg.plugin\_root\_directory" can returns a truncated network path
* &#91;TextureSet&#93; Lock button is enabled when re-opening non-square projects

### 2.3.1

*(Released: October 07, 2016)*

**Added:**

* &#91;Plugin&#93;&#91;Photoshop&#93; Allow to specify which material/stack/channels to export
* &#91;Scripting&#93; Function names have some inconsistencies

**Fixed:**

* &#91;Export&#93; Alpha can be discarded in custom export presets
* &#91;Export&#93; Alpha gets incorrect gamma conversion on sRGB channels
* &#91;Export&#93; Non-square documents are exported as squared
* &#91;Export&#93; Impossible to export additional maps if one is missing
* &#91;Iray&#93; Some parameters (like emissive Intensity) have no effect
* &#91;NVIDIA&#93; Crash at Startup with NVIDIA Quadro K2200/GTX 750/760
* &#91;AMD&#93; Incorrect set of colors for thumbnails and previews
* &#91;AMD&#93; Freezes and driver failure on New File and File Open
* &#91;Log&#93; "software-version" is missing from log file

### 2.3.0

*(Released: September 15, 2016)*

**Added:**

* &#91;Plugin&#93; New "Export to Photoshop" plugin (export complete layer stack)
* &#91;Export&#93; Allow to specify the width of the padding (in pixels or infinite)
* &#91;Export&#93; Allow to set the type of background outside of the UVs
* &#91;Shelf&#93; New material layering shader to blend 10 materials
* &#91;Shelf&#93; New clay shader to view details with the height/normal channel
* &#91;Shelf&#93; New baked lighting filter with environment input
* &#91;Shelf&#93; Updated some mask generators to add non-square transformations
* &#91;Viewport&#93; Add composited normal map (normal+height+bake) to the solo mode
* &#91;Scripting&#93; Allow to export additional maps
* &#91;Scripting&#93; Allow to query available Additional maps per Texture Set
* &#91;Scripting&#93; Allow to retrieve channel format
* &#91;Scripting&#93; Add examples in the baking documentation
* &#91;Scripting&#93; Allow to query the visibility of a layer
* &#91;Scripting&#93; Allow to query layer's blending mode and opacity
* &#91;Scripting&#93; Allow to export converted maps (final normal maps, mixed AO, etc.)
* &#91;Substance&#93; Read and connect custom usages
* &#91;Shortcuts&#93; Add modifier key (SHIFT) to cycle solo mode backward
* &#91;Export&#93; Updated default export preset to disable alpha
* &#91;UI&#93; Thumbnails are now only computed if the engine is available
* &#91;UI&#93; Display a mention when thumbnails are computing

**Fixed:**

* Crash with some old projects when opening them
* Crash with corrupted texture channels cache
* Crash when blending more than 4 materials with Material Layering workflow
* &#91;UI&#93; Tool shortcuts don't work if the toolbar is hidden
* &#91;UI&#93; Iray toolbar is labeled "Untitled" in the View Menu
* &#91;UI&#93; Plugin toolbars are named "Untilted" in the View Menu
* &#91;Baker&#93; Pressing Enter while editing a bake setting launches the bake process
* &#91;Baker&#93; Incorrect ranges for some parameters
* &#91;Import&#93; Impossible to import OBJ meshes because of very big numbers
* &#91;Import&#93; Some OBJ files are imported with too many sub-objects
* &#91;Export&#93; channel background is filled with black instead of default color at export
* &#91;Tool&#93; Particles don't work properly if FOV is too low
* &#91;Tool&#93; Brush preview color is incorrect with masks in sub-stacks
* &#91;Viewport&#93; When brush goes into empty areas in 2D view it becomes gigantic
* &#91;Viewport&#93; Blank brush preview when painting Normal textures
* &#91;Scripting&#93; Incorrect documentation : "ao" listed instead of "ambientocclusion"
* &#91;Scripting&#93; Process started with subprocess() is killed when closing Painter
* &#91;Shelf&#93; Baked lighting filter use incorrect AO input
* &#91;MacOS&#93; Removed Fire Hydrant project (incompatible)
* Default project opens when loading a \*.spt file (instead of \*.spp)

**Known Issues:**

* &#91;Plugin&#93; Because of Photoshop, the height and normal channel can't be translated as-is

### 2.2.0

*(Released: July 22, 2016)*

**Added:**

* &#91;Shelf&#93; Improve search system and queries
* &#91;Shelf&#93; Add search field for mini-shelves
* &#91;Shader&#93; Allow to define step precision for sliders
* &#91;Shader&#93; Add an Undo/Redo button for shader parameters
* &#91;Shader&#93; Reloading a shader should not reset its parameters
* &#91;MatLayering&#93; Add support for Dynamic Material Layering and sub-stacks
* &#91;MatLayering&#93; Allow to import json file to setup the shader settings
* &#91;MatLayering&#93; Unlock texture samplers limit (switch to Bindless textures)
* &#91;Scripting&#93; Allow to set bakers settings and launch their computation
* &#91;Substance&#93; Use "usage" for inputs/outputs connections in addition of identifiers
* &#91;Tool&#93; Allow to select the preview channel in the viewport for the Projection Tool

**Fixed:**

* Crash during launch if substances are located in wrong folder
* Crash report sometimes doesn't work because of incorrect log file
* &#91;Iray&#93; Post effects don't refresh when Iray is paused
* &#91;Iray&#93; Auto-focus shortcut doesn't work anymore
* &#91;Iray&#93; Aperture slider behavior change depending of asset size
* &#91;Layers&#93; First material channel is not enabled by default if they are all disabled
* &#91;Shader&#93; No errors are printed if a "param auto" is incorrect

**Known Issues:**

* &#91;Mac&#93; Texture samples limit is locked at 16 (GPU driver issue)

### 2.1.1

*(Released: July 01, 2016)*

**Added:**

* &#91;License&#93; Be able to change the license file location
* &#91;Viewport&#93; Add a "B" shortcut to cycle between additional maps
* &#91;Import&#93; Allow to import FBX 2016/2017 properly
* &#91;Tool&#93; Remove checkers when using the quick mask
* &#91;Iray&#93; Add scene dimensions information
* &#91;Iray&#93; Allow to increase maximum number of samples and render time
* &#91;UI&#93; Update result immediately when using +/- button on sliders
* &#91;UI&#93; Allow greater precision for Grayscale sliders
* &#91;Export&#93; Don't export an alpha channel for textures being RGB only
* &#91;Export&#93; Update Dota 2 export preset
* &#91;Shelf&#93; New "Hexagon tiles" pattern
* &#91;Shelf&#93; New "Weld" tool
* &#91;Shelf&#93; Updated finish filters to give direction controls

**Fixed:**

* &#91;Export&#93; Impossible to export PSD files in 8bits
* &#91;Export&#93; 8K export is not available on some hardware configurations
* &#91;Export&#93; Sketchfab window is cropped
* &#91;Export&#93; Incorrect roughness map in Spec/Gloss export preset
* &#91;UI&#93; Typing in grayscale sliders doesn't work anymore
* &#91;UI&#93; Impossible to put filters into substance inputs (like Generators)
* &#91;UI&#93; Some sliders have odd behaviors
* &#91;UI&#93; DeltaTime +/- step for particles is too big
* &#91;Iray&#93; Some projects block the application when switching to Iray
* &#91;Iray&#93; Crash when detecting hardware
* &#91;Tool&#93; Brush preview color is incorrect in Mask mode
* &#91;Tool&#93; Material picker can be used with incompatible tools
* &#91;Tool&#93; Projection preview don't switch to Diffuse with Spec/Gloss workflow
* &#91;Shelf&#93; Changing default shader breaks smart mats/smart masks previews
* &#91;Shelf&#93; Some smart materials have incorrect names
* &#91;Shelf&#93; Additional alpha shapes are corrupted and won't load
* &#91;Viewport&#93; Switching to "Additional map" mode display "other" first
* &#91;Viewport&#93; Viewport switch back to "other" when an additional map doesn't exist
* &#91;Crash&#93;&#91;Linux&#93; Crash report doesn't work on Ubuntu (Steam)
* &#91;Crash&#93;&#91;Linux&#93; Web URL links don't work on Ubuntu (Steam)
* &#91;Crash&#93;&#91;Windows&#93; Remove "crashwatcher" when Substance painter doesn't run anymore
* &#91;Crash&#93;&#91;Mac&#93; Crash report system doesn't work properly
* &#91;Crash&#93; Importing a mesh while already importing a mesh lead to a crash
* Texture set picking shortcut reset to nothing after a relaunch

### 2.1.0

*(Released: June 02, 2016)*

**Added:**

* &#91;UDIM&#93; Import UDIM Tiles from a mesh as Texture Sets
* &#91;Linux&#93; Added support for CentOS 6.6 and Ubuntu 12.4
* &#91;Export&#93; Add 8K resolution (experimental)
* &#91;Export&#93; Allow to choose the bit depth during the export
* &#91;Baker&#93; Allow to bake multiple texture sets at once
* Support high resolution monitors (High DPI scaling)
* &#91;Scripting&#93; Set custom resolution and padding per texture at export
* &#91;Viewport&#93; Allow to switch between texture set by clicking on the mesh (via Ctrl+Alt+Click)
* &#91;Viewport&#93; Go where the mouse cursor is when zooming with the mouse wheel
* &#91;UI&#93; Update default background color and environment map display
* &#91;UI&#93; Add tooltips with original names for User channels
* &#91;UI&#93; Change background color for channels that can't be renamed
* &#91;Tool&#93; Remove checkers when using the quick mask
* &#91;Shader&#93; Allow to define groups for shader parameters and materials/masks
* &#91;Engine&#93; Optimization of small size stamping
* &#91;Stencil&#93; Add "W" as shortcut to temporarily toggle the mask
* &#91;Shelf&#93; Add a cross button to clear the search field
* &#91;Shelf&#93; Load Alpha with a single click
* &#91;Shelf&#93; New export preset : Vray UDIM, Arnold UDIM, Spec/Gloss from Metal/Rough
* &#91;Shelf&#93; New alphas : geometric shapes, veins and signs
* Add name and version in the properties of Substance Painter executable

**Fixed:**

* &#91;Substance&#93; Impossible to use the normal channel and additional map at the same time
* &#91;Iray&#93; MDL refraction and absorption setting don't work
* &#91;Iray&#93; Original scene scale is not preserved
* &#91;Shelf&#93; Specular/Glossiness template use an incorrect shader
* &#91;Export&#93; Default export preset doesn't export some maps (like AO)
* &#91;Viewport&#93; Pivot point doesn't update when clicking outside the UVs in the 2D View
* &#91;UI&#93; Slider values are rounded
* &#91;UI&#93; Sometimes when editing sliders values there is a very small free space
* &#91;New Project&#93; Template dropdown list is not correctly updated (from 1.x to 2.x)
* &#91;Scripting&#93; Fixed "hover" behavior on custom buttons
* &#91;Mac&#93; Undoing on an empty project locks the camera

**Known Issues:**

* Crash report is not available on Ubuntu
* Some url buttons might not work, take a look at our FAQ for a workaround

### 2.0.5

*(Released: April 29, 2016)*

**Added:**

* &#91;Shelf&#93; Added/Updated non-pbr template, shader and export preset
* &#91;Shelf&#93; Updated UE4 export preset to include Ambient Occlusion

**Fixed:**

* Crash when opening and saving some projects with corrupted ressources
* &#91;Viewport&#93; Wireframe appears broken in 2D view
* &#91;Shelf&#93; Improved performances of some studio environment maps
* &#91;Shelf&#93; Some studio environment maps are duplicated
* &#91;Shelf&#93; Missing "Baked Lighting Material"
* &#91;Shelf&#93; Missing "Grayscale conversion" generator

### 2.0.4

*(Released: April 26, 2016)*

**Added:**

* Improve mesh collisions and optimize wireframe rendering
* Improve performances and memory management with big projects
* Improve slider precision and stepping
* &#91;UI&#93; Update engine only when validating a slider (not when entering a value)
* &#91;UI&#93; Move Iray switch to a dedicated button in the main toolbar (and change its shortcut)
* &#91;Tool&#93; Add setting for clone tool source location behavior
* &#91;Shader&#93; Allow to read mesh vertex colors in custom shaders
* &#91;Scripting&#93; Allow to retrieve the list of texture sets, channels and layers
* &#91;Scripting&#93; Add helper functions (url to path, get export path from project)
* &#91;Mac&#93; Detect Mac Os "El Capitan" version in log file

**Fixed:**

* Crash after second export to Substance Share
* Crash when copying a layer between texture sets with Quick mask data.
* Some projects have a very long updater that consume a lot of memory
* &#91;Tool&#93; Crash when selecting a particle preset with clone/smudge tool
* &#91;Baker&#93; Loading FBX files takes too much time for heavy meshes
* &#91;Viewport&#93; Stretched environment map on some computers
* &#91;Viewport&#93; Wrong gamma conversion of the alpha of the brush
* &#91;Export&#93; Alpha is stored as transparency instead of a separate channel with Tiff files.
* &#91;Export&#93; Normal channel is always exported as being OpenGL
* &#91;Iray&#93; Missing slider names for Iray settings
* &#91;Iray&#93; Render is done at a wrong resolution on Retina/High DPI
* &#91;Iray&#93; Crash when resizing interface in Iray mode
* &#91;Iray&#93; Huge performance slowdown when rendering at some low resolutions
* &#91;Iray&#93; Pause doesn't work (Iray still compute in the background)
* Normal channel has sometimes black square artifacts
* Normal channel is inverted by grayscale filters
* Normal channel doesn't blend properly if the stack has some alpha
* Project is edited on disk when opening a project even if it wasn't saved yet
* Reimporting a mesh on some projects gives very bad GPU performances
* Brush orientation is incorrect when not touching a mesh
* Substance Share logo is missing in Welcome Screen

### 2.0.2

*(Released: March 25, 2016)*

**Added:**

* &#91;Iray&#93; Update Spec/Gloss template and shader to be compatible with Iray
* &#91;Export&#93; Be able to Export screenshots to ArtStation
* &#91;Scripting&#93; Support execution from plugin directory
* &#91;Scripting&#93; Allow to "Save As"
* &#91;UI&#93; Allow to double click on a slider to edit its value
* Move Vela sample to Substance Share
* New sample project : Sphere Preview
* Warn users about shell extension conflict

**Fixed:**

* Installer override installation of Substance Painter 1.x
* &#91;UI&#93; Channels list layout is broken with filters
* &#91;UI&#93; Shader parameters are not displayed
* &#91;UI&#93; Resizing the layer window crops incorrectly the content
* &#91;Tool&#93; Opacity channel isn't always used properly
* &#91;Tool&#93; Smudge/Clone don't work with Symmetry
* &#91;Tool&#93; Brush preview opacity is incorrect with some channels
* &#91;Iray&#93; Crash when using Iray while it hasn't been created yet
* &#91;Iray&#93; Can't load iray settings data from project
* &#91;Iray&#93; Iray doesn't take care of settings modification after been paused
* &#91;Shelf&#93; Importing a Material to the shelf doesn't work
* Stencil doesn't work with Normal channel
* Crash when Painting on some projects
* Crash when Painting with particles on some projects
* Crash with Pixel processor during some computations

### 2.0.0

*(Released: March 16, 2016)*

**Added:**

* Shortcut to Substance Store in the main toolbar
* Iray renderer with view mode and screenshot export
* Support for "Smart Masks" creation and usage
* Support for Specular/Glossines PBR workflow (with new diffuse channel)
* Chaining Substances (plug substances into substance image inputs)
* Scripting support with custom plugins
* Improve Height to Normal conversion by using a Sobel filter
* Switch Stencil/Projection preview resolution to 2K
* Add normal channel by default for new projects
* Read user data tag from output node to enable/disable channels of a substance by default
* Expose Normal/AO blending in TextureSet settings
* &#91;Tool&#93; New Smudge tool for blending and spreading colors
* &#91;Tool&#93; New Clone tool for copying part of textures
* &#91;Tool&#93; Allow to select channels for Smudge, Clone and Eraser tool
* &#91;Layer&#93; Add Substance name for Fill effect name
* &#91;Layer&#93; Allow to export mask to clipboard
* &#91;Viewport&#93; Switch between perspective and orthographic mode
* &#91;Viewport&#93; Allow to control Field of View in perspective mode
* &#91;Viewport&#93; Allow to set Depth of Field distance with CTRL+Middle click
* &#91;Viewport&#93; Allow to drag and drop environment maps in the 3D View.
* &#91;Viewport&#93; Improved feedback when the engine is doing strong computations
* &#91;Export&#93; Allow to export shader parameters in a json file
* &#91;UI&#93; Update interface with new icons, colors and layout
* &#91;UI&#93; Add assets names to the mini shelves
* &#91;UI&#93; Collapse "Channels mapping" by default
* &#91;Shader&#93; Choose a custom color for shader texture parameters
* &#91;Shelf&#93; Ask where to import files when drag and dropping resources
* &#91;Shelf&#93; New Preview sphere for Smart Materials and Generators
* &#91;Shelf&#93; Add Specular Glossiness shader
* &#91;Shelf&#93; New Hard Surface shapes
* &#91;Shelf&#93; New Alphas textures and shapes
* &#91;Shelf&#93; New Skin textures
* &#91;Shelf&#93; New Scan-based materials and smart-materials
* &#91;Shelf&#93; New smart materials and spec/gloss support of old ones
* &#91;Shelf&#93; New Finish filters for metallic surface simulation
* &#91;Shelf&#93; New powerful mask generator "Mask Editor"
* &#91;Shelf&#93; Reworked and cleaned old materials
* New "Vela" sample project

**Fixed:**

* &#91;Settings&#93; Camera rotation and zoom speed are overridden by the project
* &#91;Viewport&#93; Precision issue on default normal texture leads to incorrect reflections
* &#91;Viewport&#93; Vignette is enabled by default
* &#91;Viewport&#93; Artifacts appear at the environment map borders (Nvidia GPUs)
* &#91;Viewport&#93; Thumbnail in projection/stencil mode is very long to load
* &#91;Baker&#93; Store baked textures in 16bits integer instead of 32bits
* &#91;Layer&#93; Outdated substances are displayed incorrectly in the stack
* Default color and bit-depth for some channels are incorrect (ex : Specular, Glossiness)
* Fixed eraser behavior to disable blending in passthrough mode

**Known Issues:**

* Symmetry doesn't work with Smudge and Clone tool
* ArtStation export is missing

## Version 1

### 1.7.3

*(Released: March 01, 2016)*

**Added:**

* &#91;Export&#93; Add an option to disable padding
* &#91;Shelf&#93; Support sub-shelf hierarchy inside a shelf folder

**Fixed:**

* Crash when saving over previously Read Only file
* Crash when opening a second project
* Crash when loading some thumbnails (shelf, layers or tooltips)
* Disabling "Preserve strokes positions on mesh" does not work
* &#91;Export&#93; Upscale of bitmaps is done with nearest filtering
* &#91;Shelf&#93; Discovery of resources is very slow
* &#91;Shelf&#93; Blur filters are not 16 bits compatible
* &#91;Tool&#93; Symmetry doesn't work if you load an old tool preset
* Color dialog for Specular channel doesn't do a color space conversion

### 1.7.2

*(Released: January 13, 2016)*

**Added:**

* &#91;Layers&#93; Allow to specify default tilling for fill layers

**Fixed:**

* &#91;Export&#93; Sketchfab export doesn't work anymore
* &#91;Layer&#93; Bilinear filtering is applied even on Fill without any transformation
* &#91;Tool&#93; Poor performances using substance with image inputs in projection mode
* &#91;Tool&#93; Material picker is broken

### 1.7.1

*(Released: December 18, 2015)*

**Fixed:**

* Crash when switching texture set
* Slow performances when painting

### 1.7.0

*(Released: December 17, 2015)*

**Added:**

* &#91;Performances&#93; Compute layers content and their thumbnails at the same time
* &#91;Export&#93; Save export path as relative when next to the project
* &#91;Layers&#93; Added new blending mode : subtract and add/sub
* &#91;Layers&#93; New Bilinear HQ filtering for fill layers
* &#91;Shader&#93; Set a default shader for thumbnail generation in the preferences.
* &#91;Shader&#93; Allow to specify a shader per texture set
* &#91;Shader&#93; Allow to sample textures from the shelf
* &#91;Tool&#93; New "wrap" brush behavior for painting
* &#91;Tool&#93; Improved filtering and reduced aliasing while painting
* &#91;Tool&#93; Improved sub-pixels painting quality
* &#91;Tool&#93; Removed "basic" display for brush settings and improved the frame open/close icon
* &#91;Menu&#93; Add effect icons in the right-click menu
* Template creation from Projects
* &#91;Shelf&#93; New templates : PBR, Dota 2
* &#91;Shelf&#93; New export preset : Dota 2
* &#91;Shelf&#93; New shaders : Dota 2, PBR Car paint, PBR Coated, PBR Velvet
* &#91;Shelf&#93; New material : Steel rust and wear, Stylized lighting
* &#91;Shelf&#93; New filters : Blur directional, Stylized lighting
* &#91;Shelf&#93; New brush : default soft and default hard with a new alpha for a better hardness control
* &#91;Shelf&#93; New generators : 3D Distance and Light
* &#91;Shelf&#93; Updated brushes with wrap projection and backface culling (enabled by default)
* &#91;Shelf&#93; Updated White noise with pixel processor version for faster computation

**Fixed:**

* &#91;Welcome screen&#93; Tutorials link send to old videos
* &#91;Channels&#93; Saying "no" to fill layer creation with AO still create the layer
* &#91;Channels&#93; UserX channels names do not propagate in the interface
* &#91;Viewport&#93; Mask entry is empty in the list of the solo channels
* &#91;Share&#93; Exporting an alpha to Share from SP creates an unreadable .image file
* &#91;License&#93; Fix activation fro usernames with non ASCII characters
* &#91;Shader&#93; Color parameter dialog disappear when picking a color
* &#91;Shelf&#93; Thumbnails are not unloaded from memory when unused
* &#91;Shelf&#93; Fixed gradient filter
* &#91;Tool&#93; Symmetry doesn't work with stencil/projection
* &#91;Tool&#93; Incorrect name when creating new brush preset
* Preserve stroke setting stays disabled even when reimporting a mesh
* Driver reset (TDR) when computing particles with a big size.

### 1.6.1

*(Released: November 09, 2015)*

**Fixed:**

* Crash when opening project if 2D view is visible
* Crash when creating new export preset if current shelf doesn't exist
* &#91;Tool&#93; Material picker icon can stay displayed
* &#91;Tool&#93; Material picker hide mouse cursor when painting at the same time
* &#91;Shelf&#93; Metadatas are written on the disk after each exit

### 1.6.0

*(Released: October 29, 2015)*

**Added:**

* Official support for Windows 10
* &#91;Substance&#93; Collapse substance parameters groups by default
* &#91;Substance&#93; Add new framework (Improve Pixel Processor performances)
* &#91;Viewport&#93; Allow to deactivate the symmetry plane display while in symmetry mode.
* &#91;Viewport&#93; Improve shadows rendering and performances
* &#91;Viewport&#93; Pause shadow computation when painting
* &#91;Viewport&#93; Improve wireframe rendering performances
* &#91;Engine&#93; Improve Vram memory management to reduce its footprint
* &#91;Engine&#93; Improve texture refresh on AMD GPUs for better performances
* &#91;Engine&#93; Disable Threaded Optimization setting on NVIDIA GPUs for better performances
* &#91;Effect&#93; Add a tag to request "padded" image input
* &#91;Layer&#93; Increase precision of UV offset/scale in fill
* &#91;Layer&#93; Make the scale slider exponential in fill
* &#91;Layer&#93; Allow to drag and drop Materials directly in the layer stack.
* &#91;Layer&#93; Allow to drag and drop filters directly in the layer stack
* &#91;Layer&#93; Adjust the mask brush color to the newly created mask color
* &#91;Shader&#93; Expose multiple texcoords
* &#91;Shader&#93; Expose gamma/tonemapping function to allow custom functions
* &#91;Bakers&#93; Change default Position baker settings for TriPlanar usage
* &#91;Tool&#93; Rename "Geometry Decal" as "Polygon Fill"
* &#91;Shelf&#93; Update generators to support TriPlanar : MG Metal edge wear, MG Mask builder, MG Fiber glass, MG Dirt
* &#91;Shelf&#93; Update materials with new settings and removed unused materials
* &#91;Shelf&#93; 22 New smart materials (Plastic, Iron, Fabric, Steel and more)
* &#91;Shelf&#93; Update Sharpen, Blur and Warp filters with padded image input to avoid seams
* &#91;Shelf&#93; Improve Warp settings for easier usage
* &#91;Shelf&#93; 2 New procedural noises : 3D Perlin noise and 3D Worley noise

**Fixed:**

* &#91;Engine&#93; Vram amount detection for dedicated GPU is incorrect on Mac
* &#91;Engine&#93; Textures turn to darker version in the viewport
* &#91;Engine&#93; Poor performances when painting below multiple layers
* &#91;Engine&#93; Computed layers when opening project differ from cached version
* &#91;Substance&#93; Wrong results in 4K on Mac
* &#91;Substance&#93; Parameters are in the wrong order
* &#91;Shader&#93; Toon and Pixelated shaders are totally black
* &#91;Shader&#93; Parameters disappear after changing env-map
* &#91;Shelf&#93; Crash when putting png files in generator folder
* &#91;Shelf&#93; Thumbnails are generated with low roughness
* &#91;Tool&#93; Crash when using a bitmap in the brush alpha on windows
* &#91;Export&#93; Additional map export preset now export a RGB map for Position

### 1.5.7

*(Released: September 24, 2015)*

**Fixed:**

* Crash report doesn't work anymore

### 1.5.6

*(Released: September 21, 2015)*

**Added:**

* &#91;Shelf&#93; Improve thumbnail rendering quality (use 1K textures)

**Fixed:**

* &#91;Share&#93; Impossible to sign with another account
* &#91;Shelf&#93; Thumbnails are too heavy on the disk
* &#91;Shelf&#93; Smart materials are very slow to load
* &#91;Windows&#93; Fix license service install
* &#91;Channels&#93; Transmissive map is created as G8 by default

### 1.5.5

*(Released: September 15, 2015)*

**Added:**

* &#91;Shelf&#93; Export assets to Substance Share
* &#91;Shelf&#93; Add new sphere preview for Materials
* &#91;Shelf&#93; Use the env map "Glazed patio" for generating thumbnails
* &#91;Shelf&#93; Increase thumbnail size resolution to 512x512 pixels
* &#91;3D View&#93; Expose environment rotation value
* &#91;Windows&#93; Sign the application

**Fixed:**

* &#91;Bakers&#93; Wrong results when baking maps at the same time
* &#91;3D View&#93; The env map is displayed when no project is open
* &#91;Layers&#93; Mask Generators don't work on layer content
* &#91;Layers&#93; You can paint on hidden layers
* &#91;Shelf&#93; Dirt\_5 and Dirt\_6 noise are identical
* &#91;Shelf&#93; Some mask generators are pixelated or at low quality
* &#91;Tool&#93; Incorrect gizmo rotation on certain angles.
* &#91;Tool&#93; Too many channels cause the channel buttons to be cropped out
* &#91;Tool&#93; Invert mask shortcut for Quick mask doesn't work
* &#91;Export&#93; Sketchfab: cancel button not correctly taken into account
* &#91;Licence&#93; Activation failed when license cannot be copied
* Framerate limiter doesn't work on the UI anymore

### 1.5.0

*(Released: August 20, 2015)*

<b>Added:</b>

* &#91;Shader&#93; Add line number in Shader compiling error messages
* &#91;Shelf&#93; Improve thumbnails previews quality
* &#91;Shelf&#93; Automate thumbnail generation for Smart Materials
* &#91;Tool&#93; Shortcut to control hardness setting in the substance
* &#91;Tool&#93; Use grayscale widget for geometry decal when over a mask
* &#91;Tool&#93; Shortcut to invert paint color while painting on a grayscale map
* &#91;Viewport&#93; Allow to display the wireframe and change its color
* &#91;Viewport&#93; Blur the environment background
* &#91;Controls&#93; Add rotation to brush mouse shorcuts
* &#91;Export&#93; Export to Sketchfab
* &#91;Export&#93; Create export presets for renderers
* &#91;Export&#93; Add converted map Reflection, F0 and 1/IOR
* &#91;UI&#93; Add Welcome screen
* &#91;UI&#93; Update default layout
* &#91;UI&#93; Add missing tooltips and rename some menu entry
* &#91;Layers&#93; Export currently selected mask as bitmap
* &#91;Layers&#93; Add "invert mask" action in the right-click menu

<b>Fixed:</b>

* &#91;Project&#93; If the meshes pivot's are different in the FBX, the meshes get exploded upon import
* &#91;Substance&#93; Substances used in projection tools are locked in 256\*256
* &#91;Layers&#93; Crash when using clear mask
* &#91;Export&#93; Incorrect gamma conversion on very dark textures
* &#91;Export&#93; Position map can only be used in export presets as a grayscale map
* &#91;Tool&#93; Geometry decal start color is black when used on a mask
* &#91;Tool&#93; Rotation shortcut doesn't work if there is no hardness in the alpha

### 1.4.2

*(Released: July 15, 2015)*

**Fixed:**

* &#91;Tool&#93; Crash when using geometry decal with quick mask
* Updating project from 1.4.0 to 1.4.1 consume all the computer memory
* Old project format import incorrectly
* Custom shelves parse the entire hierarchy and duplicate assets everywhere

### 1.4.1

*(Released: June 23, 2015)*

**Added:**

* &#91;Viewport&#93; Allow to dock panels side by side
* &#91;Effect&#93; Add a background and a ruler for the level effect
* &#91;Effect&#93; Add a Paint effect that allow to work over other effect

**Fixed:**

* &#91;Shelf&#93; Thumbnail generation is broken if no project is open
* &#91;Shelf&#93; Material preset preview fail to generate
* &#91;Shelf&#93; Material previews are generated on a mesh with inverted normals
* &#91;Shelf&#93; Thumbnails always recompute because of incorrect hash function
* &#91;Shelf&#93; Clicking on a substance material doesn't connect additional maps
* &#91;Tool&#93; Incorrect value sampled with Material picker
* &#91;Tool&#93; Color picker pick viewport cursor color
* &#91;2D View&#93; Very low framerate/performances
* &#91;Export&#93; Crash when opening the export window with too recent export presets.
* &#91;Export&#93; Height channel to Normal map is converted to the wrong space
* &#91;Mac&#93; BaseColor from substance effects is displayed as Linear
* &#91;Mac&#93; Straight lines widget is incorrectly drawn on Retina
* Straight lines can stay enabled even with the shortcut released.
* Straight lines guizmo disappear after rotating the environment map
* Ambient occlusion outputs from substances are not plugged to the AO channel automatically
* Fix license copy issue on windows with special character in username

### 1.4.0

*(Released: June 10, 2015)*

**Added:**

* &#91;Export&#93; Add additional maps in the list of the available input maps
* &#91;Shelf&#93; Use sbsar materials as material presets
* &#91;Shelf&#93; Allow to use custom Library paths
* &#91;Shelf&#93; Change the minimum size
* &#91;Shelf&#93; New content : 20 new smart materials
* &#91;Shelf&#93; New content : new procedural substance (weave, mesh)
* &#91;Shelf&#93; Updated Blur filter
* Draw straight lines using a modifier key
* Add Ambient Occlusion channel and rework AO/Normal behavior in layer stack
* Read default color from Image Input defined in Substance user data
* Allow to export the log from the help menu

**Fixed:**

* &#91;Baker&#93;&#91;Mac&#93; Crash with Normal from mesh baker
* &#91;Baker&#93; Crash if there is no UVs in the cage file
* &#91;Baker&#93; Matching by names doesn't work with OBJs exported from zBrush
* &#91;Baker&#93; Baking with a cage overwrites bake if using multiple texture sets and overlapping UVs
* &#91;Baker&#93; Specific OBJ files result in black textures
* &#91;Shelf&#93; Can't read resources if set to read-only
* &#91;Shelf&#93; Asset files are being written Painter if they have been used in the project.
* &#91;Shelf&#93; Reloading substances also update the layer
* &#91;Export&#93; Tiff exports 32 bits images that can't be read properly by Photoshop or game engines
* &#91;Export&#93; Default channels preset always export as RGB
* &#91;Material&#93; Diffuse channel override BaseColor mapping with substances
* &#91;3D View&#93; Incorrect Diffuse lighting with specific environement maps
* &#91;Tool&#93; Unable to rotate a brush to a specific angle
* Viewport gets focus when hovered on while typing in a text field
* Crash with presets too recent for the current version of the shelf
* Crash after replacing mesh
* Crash when reloading a substance with different number of inputs
* FBX meshes from Cinema4D import with incorrect material names

### 1.3.5

*(Released: May 29, 2015)*

**Added:**

* &#91;License&#93; Activation problem when there is an already existing license file
* &#91;Mac&#93; Crash when loading specific FBX files
* &#91;Mac&#93;&#91;3D View&#93; Incorrect reflection for integrated GPU
* &#91;3D View&#93; Quick Mask font is broken
* &#91;3D View&#93; Material picker makes the viewport totally black
* Crash after opening projects created in 1.3.3
* Material preview is empty when using shaders with alpha
* Painting stop working on specific meshes
* Performances decrease a lot with specific OBJ meshes
* User channels are not mapped when using effects
* Temporary folders are not cleaned on startup

**Fixed:**

* Computation time improvements on project extremely long to load
* Change the "GPU Troubleshooting" window to be more understandable
* &#91;Layers&#93; Save the status of the the ratio lock for Fill layers and make it "On" by default
* &#91;Bakers&#93; Matching by name now use suffix as separator

### 1.3.4

*(Released: April 27, 2015)*

**Added:**

* &#91;Mac&#93; Crash with Mac OS X Yosemite (10.10)
* &#91;Mac&#93; Impossible to quit fullscreen mode
* &#91;Bakers&#93; Baking match by name option doesn't work
* &#91;Bakers&#93; Mikk tangent space used in SP doesn't work with UE4
* &#91;Bakers&#93; ID baker can't bake material ID colors
* &#91;2D View&#93; Wireframe doesn't appear when using the Geometry decal tool
* &#91;Tool&#93; Brush alpha channel is displayed as checker instead of transparency with materials
* &#91;Tool&#93; Crash with Geometry Decal
* &#91;Layers&#93; Material slot is collapsed by default on Fill layer
* &#91;Export&#93; Crash when exporting at higher size than texture set resolution
* Specular channel is not recognized in filters.
* Clean + save doesn't strip the resources from the spp archive properly
* Don't store low-poly transformation in high-poly assbin file
* FBX file is imported with too many texture sets

**Fixed:**

* Effects: Levels Clamp should be on by default to mimic "classic" levels
* Layers: Change the minimum and maximum tilling in Fill action
* Layers: Save and Restore the stack status
* Bakers: AO Baker take the normal map into account if no HP is specified
* Bakers: Added tooltips and additional information in the baking window
* Create a backup file when saving a project

### 1.3.3

*(Released: April 01, 2015)*

**Added:**

* Add software version and project name in the title bar
* Sanitize TextureSet names and Smart material names
* Update Substance engine to V5
* &#91;Shelf&#93; Add new environment maps : Corsica beach, studio 05, Tornoco studio and more
* &#91;Shelf&#93; Update MG Mask Builder with new parameters
* &#91;Shelf&#93; Update and calibrate old environment maps

**Fixed:**

* Crash when opening the export window
* Impossible to drag'n'drop in UI widget when undocked
* "Check for updates" is not working
* &#91;Layers&#93; Don't select the mask when doing ALT+click on it
* &#91;Tool&#93; Tri-planar doesn't work with Normal channel
* &#91;3D View&#93; Diffuse lighting from env map is incorrect
* &#91;3D View&#93; Exposure computation is different from Designer
* &#91;3D View&#93; Shadows should not be visible on 100% metallic surface
* &#91;3D View&#93; Mesh with mirrored UVs has flipped tangent/binomals
* &#91;3D View&#93; Shadows produce incorrect results on certain meshes
* &#91;Bakers&#93; Remove ".alg\_meta" folder created by assbin files
* &#91;Bakers&#93; Crash when baking if Painter recompute a TextureSet at the same time
* &#91;Mac&#93; White Box UI Glitch when launching the application

### 1.3.2

*(Released: March 06, 2015)*

**Fixed:**

* &#91;3D View&#93; Fail to reload an env map saved with the project

### 1.3.1

*(Released: March 05, 2015)*

**Added:**

* &#91;Bakers&#93; Add a cached version of high-poly meshes to accelerate the computation
* &#91;Bakers&#93; Add a warning icon if no high-poly mesh is loaded
* &#91;Bakers&#93; If no high-poly mesh is loaded, use the project mesh instead

**Fixed:**

* &#91;Bakers&#93; Pressing "enter" when editing the value of a slider close the window
* &#91;Bakers&#93; Enabling/Disabling a baker will also trigger the button
* &#91;Bakers&#93; Impossible to bake if you use the "all/none" button
* &#91;Bakers&#93; The sorting of the baker buttons is not in the correct order
* &#91;Bakers&#93; Checkbox are ignored and all the bakers are always processed
* &#91;Bakers&#93; Fixed progress bar progress

### 1.3.0

*(Released: March 04, 2015)*

**Added:**

* &#91;Bakers&#93;&#91;3D View&#93; Use Mikkt tangent space computation if no tangents/binormals are found
* &#91;Bakers&#93; Added new bakers : Normal, ID, Occlusion, Curvature, Thickness, Position
* &#91;Effects&#93; Effect stack is now inverted and displayed from top to bottom (like layers)
* &#91;Effects&#93; Add new icons on the effect stack
* &#91;Effects&#93; Add blending mode between fill actions in effect stack
* &#91;Effects&#93; Rename effects (substance effect = filter, etc.)
* Add a "lock" file during the save process
* &#91;Effects&#93; Add Fill action in effect stack
* Added new resource : Smart Materials
* &#91;Layers&#93; Allow to reorder layer effects
* &#91;Tool&#93; Add Tri-Planar projection
* &#91;3D View&#93; Add support for shadows
* &#91;3D View&#93; Ability to set required OpenGL states into custom shaders
* &#91;3D View&#93; Support for alpha via new shaders
* &#91;3D View&#93; Shaders are now versioned and fully saved into a project
* &#91;3D View&#93; Warn user if the shader doesn't compile anymore

**Fixed:**

* &#91;Layers&#93; fix drop under a collapsed folder
* &#91;Shelf&#93; Fix content filtering in mini-shelves
* &#91;Shelf&#93; Rename categories and reorganize tabs

### 1.2.1

*(Released: February 12, 2015)*

**Added:**

* \*.spp files can now be opened through a double click in the explorer
* &#91;Export&#93; New "$project" tag for export presets
* &#91;Export&#93; Add map list (with nomenclature) below each texture set
* &#91;Export&#93; Add a button All/None to select the texture sets
* &#91;Export&#93; Empty maps are discarded during export

**Fixed:**

* &#91;Export&#93; Unity5 presets have inverted maps
* &#91;Export&#93; Adding a forward slash in a preset name will create a corrupted folder
* &#91;Export&#93; Height channel exported in 32bits formats is incorrectly clamped
* &#91;Export&#93; Texture set list is not sorted like in the project
* &#91;Tool&#93; Backface culling doesn't work anymore
* Save doesn't work with special characters in the path

### 1.2.0

*(Released: January 28, 2015)*

**Added:**

* New Normal channel allowing to paint normal map data and combine the results
* &#91;Export&#93; New export window with the ability to create custom packing and set custom names
* The project file format is now a single file instead of folders
* &#91;Export&#93; Support different Normal formats (DirectX, OpenGL)
* &#91;Export&#93; Create a temporary "lock" file during export
* &#91;Layers&#93; Shift+LeftMouse click can be used to toggle a mask
* &#91;Parameters&#93; Expose the color space at the bottom of an image input
* &#91;Shelf&#93; Effect "MG Mask Builder" has now new settings
* &#91;3D View&#93; Ambient Occlusion map now occlude the diffuse contribution, not the specular

**Fixed:**

* Projection material/Stencil preview doesn't show properly in the viewport
* &#91;3D View&#93; Shortcut tooltip not displayed when using "S" (stencil) shortcut
* &#91;Shelf&#93; Effect "MatFx Skin Scale" has now better performances at low resolution
* &#91;Export&#93; Textures from export are just upscaled when specifying a larger document size

### 1.1.2

*(Released: January 15, 2015)*

**Added:**

* Added: New Translate, Rotate and Scale settings in the Fill layer
* Enhanced filtering for Brushes and Fill layers
* The trial version is now fully featured (can export) but limited in time.

**Fixed:**

* Impossible to import OBJ meshes with very small precisions
* Issue when activating a license on Windows 7 and 8
* Crash during a "Save As" of a project
* Crash when deleting the last channel of a texture set
* Crash when deleting a layer in a specific context

### 1.1.1

*(Released: December 25, 2014)*

**Added:**

* &#91;Layer&#93; Select the layer on top when opening a project/switching texture set
* Improved "Save" and "Save as" speed with new compression algorithm
* Display en error when opening a project too recent for Painter

**Fixed:**

* &#91;Tool&#93; Geometry decal produce memory corruptions
* &#91;Brush&#93; Impossible to manually enter float values below 1 for the brush size
* &#91;Layer&#93; Creating a color selection effect doesn't add it in the layer stack
* &#91;Layer&#93; Moving the mouse over the layers makes Painter to flick in the taskbar
* &#91;Layer&#93; Adding a bitmap as a mask can lead to a crash
* GUI for the solo mode with the Height channel is incorrect
* "Save project" can fail and corrupt a project
* Crash when opening a project after loading another one with an outdated shader

### 1.1.0

*(Released: December 16, 2014)*

**Added:**

* &#91;Effect&#93; New Material ID mask creator
* New doted white/black line for the brush gizmo
* New angle follow parameter
* New backface culling parameter
* New Lazy mouse parameter
* &#91;Layers&#93; Support for multiple selections and management
* &#91;Layers&#93; Copy and paste from one texture set to one another
* &#91;Export&#93; Adobe Photoshop's PSD format
* &#91;Shelf&#93; New tool : fur, metal stitches and zipper
* &#91;Shelf&#93; New brush : mold, pencil, sharp line and stitch
* &#91;Shelf&#93; New alpha : Gaussian noise, sharp line, mold, pen, splash, stitch, zipper
* Painting performances improved by only updating parts of the textures needed

**Fixed:**

* &#91;Shelf&#93; Impossible to load a substance with graph having identical labels
* &#91;Layers&#93; Pass Through blending mode doesn't work with masks
* &#91;Stencil&#93; Scale is broken in 2D view
* Issues and crash on Mac OS Yosemite

### 1.0.2

*(Released: November 09, 2014)*

**Added:**

* Improved performances in material preview with substances
* Improved performances with brush stroke preview when updating document
* Improved performances in viewport with lower update rate for non working area
* &#91;Post Effects&#93; Improved UI to manage settings
* &#91;Post Effects&#93; Reset to default values
* Substance effects and layers operations in right-click menu
* Support for pre-multiplied Input/Output in substances

**Fixed:**

* &#91;3D View&#93; Custom shader parameters are separated by a large space
* &#91;Export&#93; Missing sRGB conversion for Unity4 preset
* Possible Crash when loading fbx meshes
* Crash sometimes when loading simple obj meshes
* Computing bar stays blocked to 100% at loading
* Reloading a substance puts it in every category
* DirectX/OpenGL switch broken

### 1.0.1

*(Released: October 27, 2014)*

**Added:**

* &#91;Tool&#93; Improved Material parameters usage
* New shortcut to the uservoice website in the Help menu
* Various performances improvements in the engine

**Fixed:**

* Parameters values are limited to 2 decimals for Particles
* Substance loaded from cache are not displayed in the UI as outdated
* Crash when loading a mesh from a network url
* Painter is now recognized as signed on Mac OS X

### 1.0.0

*(Released: October 15, 2014)*

**Added:**

* Custom Shader Support
* 4k resolution support
* Sample character projects
* Display progress bar for long computation times
* &#91;Export&#93; Add a dilation pass before diffusion postprocess
* Command line arguments in SP for simple operations
* New Materials and Effects
* Tool preview (separated real time material preview and stroke testing area)
* Do not create a default document when Painter starts
* &#91;Tool&#93; Add the possibility to manually edit a grayscale value
* Various improvements for the Stencils (Snap, Reset)
* Particles are now subtools of the Painting brush, Eraser and Projection tools
* &#91;3D View&#93; Use baked AO in the viewport render
* Split the stencils controls between the 2D &amp; 3D view
* Small thumb size tweaking in the library
* Search fields are specific to each window
* UI tweaking

**Fixed:**

* &#91;Susbtance&#93; Switch does not work
* &#91;Color Dialog&#93; Hue gradient not refreshed
* Impossible to update a mesh if the filename is identical
* Tool is not visible in views when too small
* Decal tool on Retina display doesn't work properly
* &#91;Substance&#93; Int1 are displayed as float1
* &#91;Substance&#93; basecolor input/output are not recognized
* &#91;Substance&#93; filters can't be reloaded
* &#91;Tool&#93; grayscale widget is always collapsed

## Beta

### 0.12.1-beta

*(Released: September 18, 2014)*

**Added:**

* Unity 5 Export Preset

**Fixed:**

* PBR Shader, rendering quality should improve a lot
* Focus function is broken and meshes are cropped by default

### 0.12.0-beta

*(Released: September 17, 2014)*

**Added:**

* Eye dropper tool
* "Preserve stroke position" option added to mesh reimport for when the bounding box changes.
* Normal map for Cymourai default mesh
* Improve tool view interface (colors are wip)
* Move the menu "Help-&gt;Settings" to "Edit-&gt;Settings"
* Save the export path in the "Export all channels" window
* New levels GUI with histogram display
* Better asset management (Drag &amp; Drop, Reload resources, Delete unused)
* Switch from "diffuse" to "basecolor"
* Sliders editing adjustments - Allow dots in addition to commas
* Fill layer: increase maximum tiling value
* Default environment map

**Fixed:**

* Bad reflection artifacts on extreme angles
* Broken specular/gloss export
* Links in the "about" window of painter don't work
* Crash with OSX Yosemite
* Mesh are saved triangulated
* The color shortcut of the Tool window send to emitter instead of grayscale
* Color picker stays open when switching from layer to mask
* Can't save material from a fill layer
* Enable resizing of the three regions of the shelf

### 0.11.0-beta

*(Released: September 04, 2014)*

**Added:**

* Add a splitter between the 3D and 2D views
* Use a gradient background in the 2D/3D views
* Interface for the Levels histogram
* Merge shelf and library
* No save action required when creating or updating a preset
* Import assets in the shelf through Drag and Drop

**Fixed:**

* The name of buttons is displayed over in the main toolbar

### 0.10.2-beta

*(Released: August 28, 2014)*

**Fixed:**

* Export all channels produces wrong results

### 0.10.1-beta

*(Released: August 26, 2014)*

**Fixed:**

* Shader give black result with low roughness
* GPU check: handle 'Quadro' cards, detect all devices and adapt user message accordingly
* Most substance materials are capped at 256 in Beta 9
* Height is clamped when exported as bitmap
* The brush preview is different from the projection overlay on Mac
* Using Geometry tool to create mask doesn't show in viewports
* Quick mask is broken
* Fix blending issue on old mac pro

### 0.10.0-beta

*(Released: August 07, 2014)*

**Added:**

* Stencil masks

**Fixed:**

* Quadro cards support
* Shader give black result with low roughness
* Substance materials are capped at 256
* Normal map export deletes the green channel

### 0.9.0-beta

*(Released: July 17, 2014)*

**Added:**

* Yebis 2 post Processing
* New project wizard allows you to import input maps (AO, Curvature, etc.)
* Automatically plug input maps (AO, Curvature,etc.) to Substance Effects
* Scale control over Materials applied to Fill Layers

### 0.8.2-beta

*(Released: July 11, 2014)*

**Fixed:**

* Hue Slider defaults to White
* Project reset if Material name contains special characters
* Material name change on a single material object should not invalidate project.
* UVs are messed up after saving project and reopen

### 0.8.1-beta

*(Released: July 04, 2014)*

**Fixed:**

* Multiple GPU crashes
* Crash when exporting channels

### 0.8.0-beta

*(Released: June 28, 2014)*

**Added:**

* Multi-Material - You can now paint on multiple materials in the same document
* Symmetry painting
* All blending modes are now available

**Fixed:**

* Multiple GPU crashes
* Project reset if Material name contains special characters
* UVs are messed up after saving project and reopen with multiple UVs

### 0.7.0-beta

*(Released: June 18, 2014)*

**Added:**

* Layer Effects
* New Substance Stencil materials
* Clear mask
* Allow to Copy/Paste layer/mask
* Allwo to Duplicate Layer
* Change tool when editing layer mask
* Substances are now GPU powered

**Fixed:**

* Height map painting does not paint negative values.
* Material Picker display should not take the sampled normal map into account
* Particles determinism broken
* Stencil matrix in 2D view
* Ngons in obj files
* Various crashes

### 0.6.0-beta

*(Released: June 04, 2014)*

**Added:**

* New export option to export a Specular map from a composite of the roughness and metallic channels

**Fixed:**

* Windows Vista compatibility
* Height map won't paint negative values

### 0.5.0-beta

*(Released: May 07, 2014)*

**Added:**

* 3D/2D view switches
* UV chunk selection tool
* Tool changes automatically when painting on masks.
* Substances resolution depends on the document's

**Fixed:**

* Crash at launch
* Crash with ASCII meshes
* Fixed Stencil matrix in 2D view
* Crash with Eraser

### 0.4.0-beta

*(Released: April 17, 2014)*

**Added:**

* Seamless 2D View
* Bitmap layer masks
* Environment exposure control
* Fill Layers now use the Tools windows to set their properties
* Materials can be applied to Fill Layers
* Added more stencils in the stencil library
* Particles presets updated for faster computation
* PBR shader optimization and quality improvement for lower quality settings

**Fixed:**

* Layers thumbnails are linked to the currently selected channel
* Lots of crashes

### 0.3.0-beta

*(Released: April 04, 2014)*

**Added:**

* Allow negative values in the color selector for height map painting
* Show preview of the picked material/color
* Add shortcuts for the Tools in the Toolbar (1,2,3,4)
* Switch Normal format (OpenGL vs DirectX) globally on a project
* New Project wizard
* Spacing slider is no longer clamped
* Updated Sliders Style
* Make Color picker non modal
* Selecting a material into the library set the tool type accordingly

**Fixed:**

* Fixed: Import mesh path is not preserved
* Fixed: Wrong textures generation
* Fixed: Crash on startup

### 0.2.0-beta

*(Released: March 17, 2014)*

**Added:**

* Material Eyedropper (P shortcut)
* Thumbnails under the 3d tool preview
* Licensing system for standalone versions
* &#91; and &#93; shortcuts for Brush Size
* Padding on exported maps
* Updated Tool Window Style
* Updated Sliders Style
* Updated Default HDR environment

**Fixed:**

* Stencil: change flow value in the 3D View stops at 52
* Infinite loop in engine when adding 0-pressure keys to stroke is fixed
* Tool: angle jitter does not return values above +/- 90%
* 3D View display change when a layer mask is selected
* Inverted zoom

### 0.1.0-beta

*(Released: March 02, 2014)*

**Added:**

* New Library management
* New Brushes and Particles content
* 3D Brush Preview
* Updated Tool Window Style
* Updated Sliders Style
* Updated Cache Performances

**Fixed:**

* Camera Controls
* Brush Rotation
