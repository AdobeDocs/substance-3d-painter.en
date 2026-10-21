---
breadcrumb-title: ''
description: Review all changes and updates across Substance 3D Painter versions to track feature evolution and improvements over time.
title: All Changes
user-guide-description: ''
user-guide-title: ''
hold: false
---

# All Changes

This page contains release notes for all previous releases of Substance 3D Painter, sorted from most recent to oldest.

>[!NOTE]
>
> To view known issues that may affect Painter, see the [dedicated documentation page](known-issues.md).

## Version 12

### 12.2.0

Release date: **2026/10/21**

Summary: **This update is a major release, it adds a new Cage Painting feature for baking, and makes improvements on Polygon fill functionality. For further details, see the complete release notes.**

**Added:**

* Baking, Cage painting
* &lbrack;Cage Painting&rbrack; Create basic Cage Paint UI
* &lbrack;Cage Painting&rbrack; New cage Visualization options
* &lbrack;Cage Painting&rbrack; Editable Select / Fill Tool
* &lbrack;Cage Painting&rbrack; Show Blend Mode in toolbar
* &lbrack;Cage Painting&rbrack; HDR slider UI Changes
* &lbrack;Cage Painting&rbrack; Visualization shader
* &lbrack;Cage Painting&rbrack; Reset Stack options
* Polygon Fill tool improvements
* &lbrack;Polygon Fill&rbrack; Add polygon patch
* &lbrack;Polygon Fill&rbrack; Add polygon loop
* &lbrack;Polygon Fill&rbrack; Symmetry support with Loop/Patch
* &lbrack;Polygon Fill&rbrack; Symmetry edge preview
* &lbrack;Polygon Fill&rbrack; Remove Triangles with Loops and Partial Loops
* &lbrack;Polygon Fill&rbrack; Wireframe visible for active Texture Set only
* &lbrack;Polygon fill&rbrack; Red edge highlight on non-clickable triangles
* &lbrack;Polygon fill&rbrack; Don't disable the fill mode options
* &lbrack;Polygon Fill&rbrack; Allow to set all channel properties with Polygon Fill
* &lbrack;Polygon Fill&rbrack; Resume previous stroke works with Polygon Fill
* &lbrack;Polygon fill&rbrack; Show forbidden cursor on non-active Texture Sets
* &lbrack;Polygon Fill&rbrack; ALT instant preview
* &lbrack;Polygon Fill&rbrack; Shortcut for temporary switch to Polyloop (SHIFT+A)
* &lbrack;Viewport&rbrack; Show Texture Set / UV Tile selection highlight
* &lbrack;Viewport&rbrack; Add support for Order Independent Transparency in real-time viewport
* &lbrack;Display Settings&rbrack; Re-organize display settings into new groups
* &lbrack;Tool&rbrack; Add support for additive blending with brush strokes
* &lbrack;Tool&rbrack; Add support for additive blending with Polygon Fill
* &lbrack;USD&rbrack; Exported USD with opacity map renders all transparent in Arnold
* &lbrack;Nvidia&rbrack; Add warning about latest Nvidia drivers (616.56 to 617.14)
* Add new "mesh_uv_neighbor" engine map input
* Update bakers to version 3.23.0
* Update Substance engine to version 9.6.1

**Fixed:**

* &lbrack;Baking&rbrack; Ambient Occlusion Ignore backface by mesh name doesn't work
* &lbrack;Baking&rbrack; &lbrack;AMD&rbrack; Device lost when baking with heavy high poly meshes
* &lbrack;Performances&rbrack; Painter hogs VRAM usage
* &lbrack;Viewport&rbrack; Missing textures when opening projects on HDPI screens
* &lbrack;Tool&rbrack; Blending mode is grayed out when painting in a mask
* Temporary folders not deleted after export on network
* &lbrack;USD&rbrack; Exported USD geometry is split along the UV borders
* &lbrack;USD&rbrack; Freeze when loading malformed USDz

### 12.1.5

Release date: **2026/09/15**

Summary: **Minor release**

**Fixed:**

* Export image from shelf to a network does not work anymore
* &lbrack;Generator&rbrack; Setting “use texture” to false does not disable the use of the texture input
* Viewport freeze when saving while editing 3d projection
* Material layering resolution is too low

### 12.1.4

Release date: **2026/09/04**

Summary: **Minor release**

**Fixed:**

* &lbrack;Crash&rbrack; Crash when importing or exporting files whose filenames contain non-ASCII characters

### 12.1.3

Release date: **2026/08/26**

Summary: **Minor release**

**Added:**

* Update Substance engine to version 9.4.6

**Fixed:**

* &lbrack;Grayscale picker&rbrack; Picker stays open after changing tool
* &lbrack;Skew Baking&rbrack; Skew correction breaks when painting and undoing
* &lbrack;Projection Tool&rbrack; Viewport interaction is blocked by projection tool
* &lbrack;Dynamic Stroke&rbrack; Missing Dynamic Stroke parameters in brush properties
* Export to a network does not work anymore

### 12.1.2

Release date: **2026/08/03**

Summary: **Minor release**

**Fixed:**

* &lbrack;Crash&rbrack; Some Substances can lead to a crash when rendered
* &lbrack;Crash&rbrack; Reimport mesh while in baking mode
* &lbrack;Crash&rbrack; Failure to initialize graphics display can lead to a crash
* &lbrack;Crash&rbrack; Exporting textures can crash in some cases while updating the log
* &lbrack;Crash&rbrack; Crash in baking mode in some cases when loading/updating the environment map
* &lbrack;Baking&rbrack; Relaunching bake after modifying high poly file can lead to a freeze
* &lbrack;Send to Photoshop&rbrack; Fails to export layer's mask
* &lbrack;Engine&rbrack; Anchor point result doesn't render between a mask and a color channel

### 12.1.1

Release date: **2026/07/09**

Summary: Minor release

Added:

* &lbrack;Skew Baking&rbrack; Expose Skew Base Normal Mode: mesh or per-triangle
* &lbrack;Properties&rbrack; Make uniform colors always reset to their channel's default value
* &lbrack;OpenPBR&rbrack; Regroup channels by categories in Export Textures window for output templates creation
* Update Substance engine to version 9.4.5

Fixed:

* &lbrack;Project&rbrack; Opening and saving some projects can take longer than usual
* &lbrack;Crash&rbrack; Reload several meshes can lead to a crash
* &lbrack;Crash&rbrack; Deleting a channel while in mask view mode leads to a crash
* &lbrack;Crash&rbrack; Some Substances can lead to a crash when rendered
* &lbrack;Paint Skew&rbrack; Selected tool in paint skew stays selected after switching to Painting Mode
* &lbrack;Baking Common Settings&rbrack; Cage Distance settings don't update cage wireframe and shader visualization
* &lbrack;Engine&rbrack; UV padding "3D Space Neighbor" mode doesn't work well on thin triangles
* &lbrack;Engine&rbrack; Anchor point result doesn't render between a mask and a color channel

### 12.1.0

Release date: **2026/06/23**

Summary: **This update is a major release, it contains bakers improvements with New baking default UI state, painting skew map, auto rebake, new option for Auto UV unwrap for hardsurface meshes and OpenPBR. For further details, see the complete release notes.**

**Added**:

* &lbrack;Skew baking&rbrack; Skew Painting Tools
* &lbrack;Skew Baking&rbrack; Add Skew Preview shader and Skew Direction Vector visuals when painting skew map
* &lbrack;Skew Baking&rbrack; Add Edge Protection option
* &lbrack;Skew baking&rbrack; Auto rebake
* &lbrack;Skew Baking&rbrack; Rework Mesh map List UI
* &lbrack;Skew Baking&rbrack; Split Mesh Map / Common Baking settings + Move Common Settings out of mesh map list basecolor or mask only
* &lbrack;Skew Baking&rbrack; Change viewport toolbar buttons
* &lbrack;Skew Baking&rbrack; Show Symmetry toggle for brush in top toolbar
* &lbrack;Skew Baking&rbrack; Rename Options in mesh map List Sync menu
* &lbrack;Skew Baking&rbrack; Update Sync and Checked state dialogs
* &lbrack;Skew Baking&rbrack; Create Grayscale color picker variant
* &lbrack;Skew Baking&rbrack; Update baking mode icon
* &lbrack;Auto Unwrap&rbrack; Integrate Hard Surface option
* &lbrack;OpenPBR&rbrack; Add support for OpenPBR 1.1
* &lbrack;OpenPBR&rbrack; Make OpenPBR the default workflow and shader
* &lbrack;OpenPBR&rbrack; Import OpenPBR materials and textures via USD
* &lbrack;OpenPBR&rbrack; Export OpenPBR materials and textures via USD
* &lbrack;OpenPBR&rbrack; Update Export Textures window to show OpenPBR naming convention
* &lbrack;OpenPBR&rbrack; Add documentation about changes to support OpenPBR
* &lbrack;OpenPBR&rbrack;&lbrack;Iray&rbrack; Add new MDL to support OpenPBR 1.1 in Iray
* Several minor improvements to USD exports
* &lbrack;UI&rbrack; Add warning in the viewport when trying to paint on another Texture Set
* &lbrack;Flatten&rbrack; Allow to flatten all instanced layers across Texture Sets
* &lbrack;Texture Set settings&rbrack; Allow to select several channels at once via new window
* &lbrack;History&rbrack; Update "value" Undo entry wording to reflect parameter name
* &lbrack;Layer stack&rbrack; Make fill effects in masks default to white (1.0)
* &lbrack;Substance&rbrack; Add new "mesh_hard_edges_triangle" engine map input
* &lbrack;Substance&rbrack; Add new "mesh_hard_edges" engine map input
* &lbrack;Shader&rbrack; Prevent shader instances to share the same names
* &lbrack;Shader&rbrack; Use the shader from the project template when importing a USD or GLTF file
* Update Adobe Color Engine to version 7.0
* Upgrade minimum MacOSX version to 13.0 (Ventura)
* &lbrack;Content&rbrack; New project templates for OpenPBR
* &lbrack;Content&rbrack; Update sample projects to use the new OpenPBR shader
* &lbrack;Python&rbrack; Expand Geometry Mask API to allow inclusion and exclusion modes like in UI

**Fixed**:

* &lbrack;Crash&rbrack;&lbrack;Mesh Maps Settings&rbrack; Apply settings to other texture sets
* &lbrack;Crash&rbrack; When baking curvature from map without world space normal
* &lbrack;Crash&rbrack;&lbrack;Baking&rbrack; Baking with custom cage enabled but no file selected crashes
* &lbrack;Crash&rbrack; Cancelling AO baking
* &lbrack;Auto-Cage&rbrack; Infinite load when high poly file path is invalid
* &lbrack;Linux&rbrack;&lbrack;Windows&rbrack; Color picker can sometimes be fully black or not appear
* &lbrack;Polygon Fill Tool&rbrack; The tool does not work with non-PBR
* &lbrack;&lbrack;Paint&rbrack; Deleting base color channel does not delete previously painted color
* &lbrack;USD&rbrack; Shader instances are not all correctly detected
* &lbrack;Substance&rbrack; Only the first usage of an input/output node is taken into account
* &lbrack;Shader&rbrack; Ambient Occlusion is applied twice with Texture Sets using different mixing methods
* &lbrack;Engine&rbrack; Normal textures with empty blue channel (black) can lead to wrong blend results
* &lbrack;GLTF Import&rbrack; Alpha blending is enabled on every texture sets
* &lbrack;GLTF Export&rbrack; Alpha blending is always enabled at export
* &lbrack;Export&rbrack; Double sided geometry is always disabled when importing a GLTF file
* &lbrack;Javascript&rbrack; Modification of shaders settings don't contribute to undo history
* &lbrack;Samples&rbrack; Subsurface scattering is not enabled in Display Settings for Meet Mat

### 12.0.3

Release date: **2026/05/05**

Summary: **Minor release**

**Added:**

* Update bakers to version 3.22.2
* Update Substance engine to version 9.4.3
* &lbrack;Python&rbrack; Save a smart material into a specific location

**Fixed:**

* &lbrack;Ubuntu&rbrack; Crash when selecting material
* &lbrack;Mac&rbrack; Recurrent pop-up appears to ask access to other apps data
* &lbrack;Baking&rbrack; Artifacts can appear on curvature map
* &lbrack;Baking&rbrack; Baking is slower in some cases
* &lbrack;Warp to geometry&rbrack; Warp to geometry gets disabled in some cases
* &lbrack;UV Tile&rbrack; Anchor point's extracted alpha ignored by other tiles
* &lbrack;Python&rbrack;&lbrack;Mac&rbrack; Exceptions in Python console with SSL
* &lbrack;Python&rbrack; Painter crash on exit with leftover Qt widgets

### 12.0.2

Release date: **2026/04/07**

Summary: **Minor release**

**Added:**

* &lbrack;Color management&rbrack; Add new OCIO to specify the default color space of color picker
* &lbrack;Python&rbrack; Expose auto-unwrap settings in Python API

**Fixed:**

* &lbrack;Crash&rbrack; Saving with insufficient disk space can crash or corrupt projects
* &lbrack;Crash&rbrack; &lbrack;Ribbon&rbrack; Using ribbon can cause crashes for some projects
* &lbrack;Crash&rbrack; &lbrack;Baking&rbrack; crash when .assbin file can't be written in folder
* &lbrack;Import&rbrack; OBJ meshes from Stager can fail at project creation
* &lbrack;Import&rbrack; OBJ has missing face in some cases
* &lbrack;Import&rbrack; USD mesh with no material assigned can crash at import
* &lbrack;Filled Path&rbrack; Not affected by symmetry
* &lbrack;Stencil&rbrack; Preview has lower resolution than painted result
* &lbrack;UI&rbrack; 'uv island' is still mentioned in ID map color source tooltip
* &lbrack;Display&rbrack; Shadows appear inverted
* &lbrack;Viewport&rbrack; Warp projection transform remains after switching to baking mode
* &lbrack;Warp&rbrack; Grid disappears when scale is set to 0 on Z axis with Warp to geometry enabled
* &lbrack;Python&rbrack; Unexpected error when adding a channel with scoped modification

### 12.0.1

Release date: **2026/03/18**

Summary: **Minor release**

**Fixed:**

* &lbrack;Crash&rbrack;&lbrack;Freeze&rbrack; Export from specific projects

### 12.0.0

Release date: **2026/03/09**Summary: **This is a major release. This release contains the features flatten layers, warp on geometry, new post effects, improvement to the new project window and other improvements.**

**Added**:

* &lbrack;Flatten Layers&rbrack; Flatten layers inside the layer stack
* &lbrack;Flatten Layers&rbrack; Export flattened layers to disk
* &lbrack;Warp to geometry&rbrack; Add new auto-warping functionality to Warp projections
* &lbrack;Post-effects&rbrack; Replace post effects with addition of new ones
* &lbrack;Post-effects&rbrack; Update tone mapper
* &lbrack;Post-effects&rbrack; Add new usage for Post-effects assets
* &lbrack;Content&rbrack;&lbrack;Post-effects&rbrack; Integrate default post-effects assets in library
* &lbrack;New Project&rbrack; Improve UI for Project Creation
* &lbrack;New project&rbrack; Changes to reimport mesh functionality
* &lbrack;New project&rbrack; Allow for \*.geo.usd files to be opened
* &lbrack;Project Configuration&rbrack; Improve UI for Project Configuration
* Update USD library to version 25.05
* Update Substance Engine to version 9.3.4
* Raise minimum drivers to 25.3.1/25.Q2 for AMD GPUs
* Update Qt to 6.8.6
* &lbrack;Scripting&rbrack; Update JavaScript API to version 1.1.20
* Update Python to 3.13

**Fixed:**

* &lbrack;Crash&rbrack; Changing a material channel output in a mask can crash
* &lbrack;Import&rbrack; EXR textures are forced into sRGB instead of linear when importing USD files
* &lbrack;UV Tiles&rbrack; Image sequence with a single image also fills other UV Tiles
* &lbrack;Baking&rbrack; AO is different between CPU and GPU baking
* &lbrack;Color Management&rbrack;&lbrack;MacOS&rbrack; Viewport BaseColor does not match colorpicker
* &lbrack;USD&rbrack; Uniform values are not imported in some cases

## Version 11

### 11.1.3

Release date: **2026/02/12**Summary: **Minor release**

**Fixed**:

* &lbrack;Paint&rbrack; Stencil and symmetry do not work in some cases
* &lbrack;Path&rbrack; No update when changing smudge stroke opacity slider
* &lbrack;Project&rbrack; Unable to paint on some geometry
* &lbrack;Ribbon&rbrack; Instantiated path disappears when changing Texture Set resolution
* &lbrack;UI&rbrack; Color picker can shrink and disappear in some cases

### 11.1.2

Release date: **2026/01/13**Summary: **Minor release**

**Added**:

* &lbrack;Baking&rbrack; Improve baking time for UV Tiles project with asynchronous saving
* &lbrack;Shaders&rbrack; Mention in Shader API changelog changes following Vulkan migration
* Update OpenEXR to version 3.4.4

**Fixed**:

* &lbrack;Crash&rbrack; Crash during startup on Nvidia GTX 10xx series
* &lbrack;Crash&rbrack; Using the color picker on different Texture Sets can result in a crash when quitting the application
* &lbrack;Performance&rbrack; Performance issue when painting in project with many layers
* &lbrack;Performance&rbrack; Lag when painting with graphic tablet pen
* &lbrack;UI&rbrack; Camera settings stay disabled in render mode (Iray)
* &lbrack;Ribbon&rbrack; Path can overlap itself unexpectedly after a corner in some cases
* &lbrack;Ribbon&rbrack; Performance issue with UV Tiles
* &lbrack;Substance&rbrack;&lbrack;UI&rbrack; Image inputs disappears when collapsed
* &lbrack;Substance&rbrack;&lbrack;UI&rbrack; Nested groups can remain even if Visible If hides them
* &lbrack;Baking&rbrack;&lbrack;UI&rbrack; Unable to set Curvature Sampling Radius beyond 0.01
* &lbrack;Baking&rbrack;&lbrack;UI&rbrack; Unable to set Max Occluder Distance beyond 1
* &lbrack;Baking&rbrack; AO setting "Self Occlusion" is ignored with several Texture Set and Low as High baking
* &lbrack;Baking&rbrack; ID map does not bake vertex colors from FBX in Low as High mode
* &lbrack;Content&rbrack; Highpass filter results in washed out colors in color managed channels

### 11.1.1

Release date: **2025/12/09**Summary: **Minor release**

**Added**:

* &lbrack;Performance&rbrack; Improve UV Tiles performance when computing partial textures
* &lbrack;Bakers&rbrack; Update to version 3.15.4

**Fixed**:

* &lbrack;Crash&rbrack;&lbrack;MacOS&rbrack; Saving project from previous version always crash
* &lbrack;Crash&rbrack; Closing a project can sometimes result in a crash
* &lbrack;Project&rbrack; Error "members count mismatch" when opening project made in previous version
* &lbrack;Baking&rbrack; UV Tiles are not combined with previous bake results if present
* &lbrack;Baking&rbrack; Device lost even with raytracing disabled on Nvidia GTX 10XX series
* &lbrack;Baking&rbrack; AO with normal has artefacts at edges because no padding
* &lbrack;Baking&rbrack; AO setting "Self Occlusion" is ignored with several Texture Sets and "match by name" on
* &lbrack;Baking&rbrack; ID Map is fully black if any high-poly meshes are missing vertex colors
* &lbrack;Ribbon&rbrack; Tooltip for Alpha blending mode mentions Screen blend mode instead of Linear Dodge
* &lbrack;Path&rbrack; Tangents create unexpected loop when point is moved closely to the path ends
* &lbrack;Tool&rbrack; Material preview does not work when projection is used in a mask
* &lbrack;Engine&rbrack; Painting small strokes can result in blocky artifacts
* &lbrack;Shader&rbrack; Undoing shader instance creation does not remove it properly
* &lbrack;Export&rbrack; Alpha mode for GLTF export is always set to MASK
* &lbrack;Python&rbrack; Unexpected error when editing layer stack outside of scoped modification block

**Known Issues**:

* &lbrack;Ribbon&rbrack; Performance issue with UV Tiles
* &lbrack;Ribbon&rbrack; Path can overlap itself unexpectedly after a corner in some cases
* &lbrack;Crash&rbrack;&lbrack;Ribbon&rbrack; Creating very long texts in Ribbon can crash
* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Regression&rbrack;&lbrack;UI&rbrack; Right-click Menu is too small on HD screens
* &lbrack;Crash&rbrack;&lbrack;Python&rbrack; USD export triggered by TextureStateEvent
* &lbrack;Engine&rbrack; Painting with Clone tool in normal channel shift colors incorrectly
* &lbrack;Python&rbrack; Ghost widget appears deleted by script still functioning

### 11.1.0

Release date: **2025/11/18**Summary: **This update is a major release, it contains the new Ribbon tool with dedicated new content, symmetry support for fill layers, physical size parameter for displacement, improved performance through the updated bakers, full Vulkan support for Windows and Linux and other improvements.**

**Added**:

* New ribbon tool
* &lbrack;Tool&rbrack; Add new Ribbon tool to make seamless paths
* &lbrack;Ribbon&rbrack; Add Ribbon preset shortcuts in Properties window
* &lbrack;Ribbon&rbrack; Allow to change the opacity of the Ribbon per vertex on the path
* &lbrack;Ribbon&rbrack; Allow to change the size of the Ribbon per vertex on the path
* &lbrack;Ribbon&rbrack; Remove begin/end defined in a Substance when paths are closed
* &lbrack;Ribbon&rbrack; Remove Path/Material preview in properties window for Paint/Eraser/Smudge path tools
* &lbrack;Ribbon&rbrack; Add blending modes for the alpha and some channels when self-overlapping
* Fill symmetry
* &lbrack;Fill&rbrack; Add support for symmetry on fill layers and effects
* &lbrack;Fill&rbrack;&lbrack;UI&rbrack; Expose symmetry settings in properties window for fill layer and effects
* &lbrack;Fill&rbrack; Rework symmetry settings UI in both viewport menu and properties window
* &lbrack;Fill&rbrack; Properly reorient normal textures when projecting in warp mode
* Physical size displacement
* &lbrack;Displacement&rbrack; Use physical size as displacement unit
* Performance improvement
* &lbrack;Performance&rbrack; Improve rendering of small brush strokes on big triangles
* &lbrack;Performance&rbrack; Improve Shader compilation time
* &lbrack;Performance&rbrack; Full Vulkan support for Windows and Linux
* &lbrack;Performance&rbrack; Updated bakers with faster GPU rendering and support of AMD raytracing
* &lbrack;UI&rbrack; Re-organize tools properties into groups and collapse some by default
* &lbrack;Engine&rbrack; Update Substance Engine to version 9.2.5
* &lbrack;Substance&rbrack; Expose resolution override for Substance resources in Tools and Fills
* &lbrack;Export&rbrack; Update Mesh Maps export preset to export grayscale textures
* Python
* &lbrack;Baking&rbrack;&lbrack;Python&rbrack; Indicate in changelog breaking changes following bakers update
* &lbrack;Python&rbrack; Expose fill symmetry settings in Python
* Content and new content
* &lbrack;Content&rbrack; Add 75 new tool presets for the Ribbon tool
* &lbrack;Content&rbrack; Update gradient builder resource to be compatible with Ribbon

**Fixed**:

* &lbrack;Crash&rbrack; Loading another project while path snapping is enabled can crash
* &lbrack;Crash&rbrack; Right click in Path panel with info from another session in clipboard can crash
* &lbrack;UI&rbrack; Interface scrolls up in tool properties when creating a path
* &lbrack;UI&rbrack; Mouse cursor disappear when path viewport visualization is hidden
* &lbrack;Path&rbrack; Copy/pasting different Tool properties in Path panel lead to unstable properties
* &lbrack;Tool&rbrack; Eraser and Smudge tool presets do not always update channel selection
* &lbrack;Tool&rbrack; Painted value is gray but UI shows white after loading colored tool preset in mask
* &lbrack;Tool&rbrack; Preset created from mask retains channels values loaded from another preset
* &lbrack;Substance&rbrack; Normal color space override defined in graph is not taken into account
* &lbrack;Content&rbrack; Default brush shape resource uses an outdated Substance

**Known Issues**:

* Shader instance history not tracked properly
* &lbrack;Ribbon&rbrack; Performance issue with UV Tiles
* &lbrack;Ribbon&rbrack; Path can overlap itself unexpectedly after a corner in some cases
* &lbrack;Ribbon&rbrack; Tangents create unwanted loop when point is moved closely to the path ends
* &lbrack;Crash&rbrack;&lbrack;Ribbon&rbrack; Creating very long texts in Ribbon can crash
* &lbrack;Tool&rbrack; Material preview does not work when projection is used in a mask
* &lbrack;Baking&rbrack; AO setting "Self Occlusion" is ignored with several Texture Sets and "match by name" enabled
* &lbrack;Baking&rbrack; AO with normal has artifacts at edges because of missing padding
* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Regression&rbrack;&lbrack;UI&rbrack; Right-click Menu is too small on HD screens
* &lbrack;Crash&rbrack;&lbrack;Python&rbrack; USD export triggered by TextureStateEvent
* &lbrack;Engine&rbrack; Painting with Clone tool in normal channel shift colors incorrectly
* &lbrack;Python&rbrack; Ghost widget appears deleted by script still functioning

### 11.0.3

Release date: **2025/08/05**Summary: **Minor release**

**Added**:

* &lbrack;Substance 3D Assets&rbrack; Add a notification dot to the 3D Assets panel
* &lbrack;VFX Platform 2025&rbrack; Add ACES 2.0 config in color management settings
* &lbrack;VFX Platform 2025&rbrack; Update OCIO to version 2.4.2
* Update Iray to version 2024.10
* &lbrack;Engine&rbrack; Update to Substance Engine v.9.2.3
* &lbrack;Nvidia&rbrack; Raise Nvidia minimum drivers version to 572.60 (Win) and 570.169 (Linux)

**Fixed**:

* &lbrack;Python&rbrack; Scoped Modification does not appear in History window

**Known Issues**:

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Regression&rbrack;&lbrack;UI&rbrack; Right-click Menu is too small on HD screens
* &lbrack;Crash&rbrack;&lbrack;Python&rbrack; USD export triggered by TextureStateEvent
* &lbrack;Engine&rbrack; Painting with Clone tool in normal channel shift colors incorrectly
* &lbrack;Python&rbrack; Ghost widget appears deleted by script still functioning

### 11.0.2

Release date: **2025/06/10**Summary: **Minor release**

**Added**:

* &lbrack;Mac&rbrack; Add warning about specific operating system version leading to artifacts
* &lbrack;Auto-update&rbrack; Minor UX improvements to Assets error log
* &lbrack;Auto-unwrap&rbrack; Update to version 1.3.2 with seaming improvements
* &lbrack;USD&rbrack;&lbrack;FBX&rbrack; Add support for multiple UV sets with sparse data
* &lbrack;Export&rbrack; Meshes exported as FBX are missing their additional UV sets if any were present at import

**Fixed**:

* &lbrack;MacOS&rbrack;&lbrack;Linux&rbrack; Crash when saving on network drive
* &lbrack;Win&rbrack;&lbrack;Tablet&rbrack; Flickering when panning
* &lbrack;SpaceMouse&rbrack; Issue when working with Path Tool
* &lbrack;Auto-cage&rbrack; Cannot bake after a mesh reload
* &lbrack;Auto-update&rbrack; Image sequence is not reloaded when first tile is missing
* &lbrack;Path&rbrack; Custom tangent can affect other tangent
* &lbrack;Path&rbrack; Path does not appear on Texture Set if the first point is on another Texture Set
* &lbrack;UI&rbrack; Some menus are always disabled after opening a project (ex: symmetry)
* &lbrack;Properties&rbrack; Cannot use/load tool presets with Filled path tool
* &lbrack;USD&rbrack; Multiple UV sets are not recognized in custom shader when using USD files
* &lbrack;USD&rbrack; Cameras with the same names are overridden
* &lbrack;Export&rbrack; Send to Photoshop results in incorrect color space for both color and grayscale results
* &lbrack;Export&rbrack; Grayscale channels with alpha are exported as color instead of grayscale with PNG format
* &lbrack;Export&rbrack; Exporting grayscale channel as PSD result in invalid/truncated file
* &lbrack;Content&rbrack; Warp filter in multi-directional mode does not work
* &lbrack;Python&rbrack; Cannot allocate list error when crawling layer stack nodes

**Known Issues**:

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Regression&rbrack;&lbrack;UI&rbrack; Right-click Menu is too small on HD screens
* &lbrack;Crash&rbrack;&lbrack;Python&rbrack; USD export triggered by TextureStateEvent
* &lbrack;Engine&rbrack; Painting with Clone tool in normal channel shift colors incorrectly
* &lbrack;Python&rbrack; Ghost widget appears deleted by script still functioning

### 11.0.1

Release date: **2025/04/10**Summary: **Minor release**

Note: **Linux CCD version will be delayed until April 29**

**Added:**

* Update to Qt 6.5.8
* &lbrack;Substance&rbrack; Add log message for filters when several image inputs share the same usage
* &lbrack;Nvidia&rbrack; Add warning about latest Nvidia drivers (572.47)

**Fixed:**

* &lbrack;Crash&rbrack; When drag and dropping an sbsar with an usage in a single channel slots
* &lbrack;Crash&rbrack;&lbrack;Path&rbrack; Change path type option is not grayed out when not clicking on specific path
* &lbrack;Fill Path&rbrack; Should not be able to select substance material
* &lbrack;Engine&rbrack; Artifacts along brush strokes
* &lbrack;Engine&rbrack; Paths can be broken with specific settings
* Issue with drop down for eye dropper color space
* &lbrack;Auto-update&rbrack; &lbrack;Python&rbrack; Wrong error message when using ResourceID without version
* &lbrack;Shader&rbrack; Crash when opening some projects

**Known Issues:**

* &lbrack;SpaceMouse&rbrack; Issue when working with Path Tool
* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Regression&rbrack;&lbrack;UI&rbrack; Right-click Menu is too small on HD screens
* &lbrack;Crash&rbrack;&lbrack;Python&rbrack; USD export triggered by TextureStateEvent
* &lbrack;Engine&rbrack; Painting with Clone tool in normal channel shift colors incorrectly
* &lbrack;Python&rbrack; Ghost widget appears deleted by script still functioning

### 11.0.0

Release date: **2025/03/11**Summary: **Major release, new Auto-update feature, Filled path tool and other path improvements, as well as new filters and an experimental Auto-cage generation for baking**

**Added**:

* Auto Update
* &lbrack;Auto-update&rbrack; Auto-update modified assets in the Assets panel
* &lbrack;Auto-update&rbrack; Auto-update modified assets across the project
* &lbrack;Auto-update&rbrack; Keep auto-update off by default
* &lbrack;Auto-update&rbrack; Make update optional if resource parameters do not match (.sbsar, .glsl, .ai, .svg)
* &lbrack;Auto-update&rbrack; Add environment variable to disable auto-update feature
* &lbrack;Auto-update&rbrack;&lbrack;SBSAR&rbrack; Make update optional if resource parameters do not match
* Filled Path
* &lbrack;Path&rbrack;&lbrack;Fill&rbrack; Add new tool to create filled paths
* Path improvements
* &lbrack;Path&rbrack; Create path which snaps to polygons
* &lbrack;Path&rbrack; Allow to switch Path types
* &lbrack;Path&rbrack; Allow to copy paste path vertex data between content and mask
* &lbrack;Path&rbrack; Allow to constrain angle when creating a new point
* &lbrack;Path&rbrack; Allow to constraint point creation to a line
* &lbrack;Path&rbrack; Close shape with a single click
* &lbrack;Path&rbrack; Display path information
* &lbrack;Path&rbrack; Allow to scale and rotate path vertices
* &lbrack;Path&rbrack;&lbrack;UX&rbrack; Make transformation gizmos easier to access
* &lbrack;Path&rbrack; Add path preview
* &lbrack;Path&rbrack; Disable Path preview with Shift + P
* &lbrack;Path&rbrack; Improve tangent edition from side view
* &lbrack;Path&rbrack; Allow to focus on a 3D path
* &lbrack;Path&rbrack; Vertices should retain selection status when toggling UI off and on again
* &lbrack;Path&rbrack; Allow to delete Path using Backspace
* &lbrack;Path&rbrack; Keep path list open if user expands it
* &lbrack;Path&rbrack;&lbrack;Layer Stack&rbrack; Correctly rename duplicates on copy/paste
* &lbrack;Path&rbrack; UI and tooltip improvements
* Performance
* &lbrack;Performance&rbrack; Improve viewport performance when using high tessellation level
* &lbrack;Performance&rbrack; Enable only the first channel on new fill layers/effects
* &lbrack;Performance&rbrack; Parallelize brush stroke computation
* Baking
* &lbrack;Baking&rbrack; Add new fully automatic cage generation option for baking with high-poly meshes (Experimental)
* Content
* &lbrack;Content&rbrack; Add 6 new filters: stylization, quantize, anisotropic kuwahara, bevel smooth, directional distance, grayscale conversion
* &lbrack;Content&rbrack; Update Noises and Grunges to latest version from Designer (with new 2D Voronoi)
* &lbrack;Content&rbrack; Add 3 new texture generators (Tile Random, Triangle Grid, Scratches Generator)
* &lbrack;Content&rbrack; Rename Unreal Engine template and export presets
* Python
* &lbrack;Shelf&rbrack;&lbrack;Python&rbrack; Save smart material or smart mask to disk from Python
* &lbrack;Python&rbrack; Add baking auto-cage to Python API
* &lbrack;Python&rbrack; Allow to edit Texture Sets/UV Tiles names and descriptions
* &lbrack;Python&rbrack; Share resolution settings on Vector & Font sources
* &lbrack;Auto-update&rbrack;&lbrack;Python&rbrack; Expose project auto-update functionalities in Python
* Misc
* &lbrack;Export&rbrack; Make Send to options easier to access with a new panel
* &lbrack;Nvidia&rbrack; Add warning about latest Nvidia drivers (572.16)
* Angle snapping should be affected by Object/World space selection
* &lbrack;Texture Set list&rbrack; Allow to add custom name to UV Tiles and use them at export
* Mac
* &lbrack;Mac&rbrack; Use Metal instead of OpenGL for graphics rendering
* &lbrack;Mac&rbrack; Drop Mac Intel support

**Fixed**:

* &lbrack;Crash&rbrack; Delete image input
* Cannot add smart mat through layer stack button
* &lbrack;Python&rbrack; Effects on GroupLayerNode cannot be found

**Known Issues**:

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Regression&rbrack;&lbrack;UI&rbrack; Right-click Menu is too small on HD screens
* &lbrack;Crash&rbrack;&lbrack;Python&rbrack; USD export triggered by TextureStateEvent
* &lbrack;MacOS Intel&rbrack; Crash when importing some presets
* &lbrack;Engine&rbrack; Painting with Clone tool in normal channel shift colors incorrectly
* &lbrack;Python&rbrack; Ghost widget appears deleted by script still functioning
* &lbrack;RedHat&rbrack; Color picker issues

## Version 10

### 10.1.2

Release date: **2024/12/3**Summary: **Minor release, bug fixes**

**Fixed**:

* &lbrack;Crash&rbrack; Delete image input
* Cannot add smart mat through layer stack button
* &lbrack;Python&rbrack; Effects on GroupLayerNode cannot be found

**Known Issues**:

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Regression&rbrack;&lbrack;UI&rbrack; Right-click Menu is too small on HD screens
* &lbrack;Crash&rbrack;&lbrack;Python&rbrack; USD export triggered by TextureStateEvent
* &lbrack;MacOS Intel&rbrack; Crash when importing some presets
* &lbrack;Engine&rbrack; Painting with Clone tool in normal channel shift colors incorrectly
* &lbrack;Python&rbrack; Ghost widget appears deleted by script still functioning
* &lbrack;RedHat&rbrack; Color picker issues

### 10.1.1

Release date: **2024/11/5**Summary: **Minor release, bug fixes**

**Added**:

* &lbrack;Project&rbrack; Keep current project open until new project selection is validated
* &lbrack;Auto-unwrap&rbrack; Texel density allows to better split UV islands into UDIMs
* &lbrack;Baking&rbrack; Fix ambiguous copy in contextual menu of Mesh Maps
* &lbrack;Warp&rbrack; Remove scaling in viewport for Z (depth) axis
* &lbrack;Import/Export&rbrack; Remove support of unused image file formats
* Update Substance Engine to 9.1.4

**Fixed**:

* &lbrack;Crash&rbrack; After relocating resource in Assets and saving project
* &lbrack;Crash&rbrack; Issues with aiserver library
* &lbrack;Crash&rbrack; Illustrator server crash in some rare cases
* &lbrack;Crash&rbrack; When exiting application in some rare cases
* Cannot send crash reports on some machines
* &lbrack;Baking&rbrack; Vertex color is not read properly
* &lbrack;UI&rbrack; Location of windows and What's New on startup is shifted
* &lbrack;Assimp&rbrack; Maya's StandardSurface not recognized in ID baking
* &lbrack;Python&rbrack; Missing SSL lib outputs an error
* &lbrack;Python&rbrack;&lbrack;Win&rbrack; Error when calling QColorConstants.Transparent
* &lbrack;Python&rbrack; Layers thumbnails created via Python do not refresh until clicking inside the layer stack
* &lbrack;Shader&rbrack; Broken link in Shader API changelog
* &lbrack;3D Assets&rbrack; Use OS proxy settings when accessing 3D Assets

**Known Issues**:

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Regression&rbrack;&lbrack;UI&rbrack; Right-click menu is too small on HD screens
* &lbrack;Crash&rbrack;&lbrack;Python&rbrack; USD export triggered by TextureStateEvent
* &lbrack;MacOS Intel&rbrack; Crash when importing some presets
* &lbrack;Engine&rbrack; Painting with Clone tool in normal channel shift colors incorrectly
* &lbrack;Python&rbrack; Widget that seems deleted via script still working
* &lbrack;RedHat&rbrack; Color picker issues

### 10.1.0

Release date: **2024/09/17**Summary: **Major release, new content: Fill area mask/color filter, embroidery decal filter and six generic Substance filters, import USD with material and shader properties, performance improvement, VFX platform 2024 compliant and migration to Linux RedHat**

**Added**:

* &lbrack;Content&rbrack; Add new Fill area mask/color filter
* &lbrack;Content&rbrack; Add new Embroidery decal filter
* &lbrack;Content&rbrack; Add 6 new generic Substance filters (FXAA, pixelate, highpass, posterize, smoothstep, threshold)
* &lbrack;USD&rbrack; Export USD layer with a defined ASM material
* &lbrack;USD&rbrack; Import USD with material and shader properties
* &lbrack;Performance&rbrack; Enable optimized layer stack thumbnails by default
* &lbrack;Performance&rbrack; Reduce project file opening time and memory consumption (data decoding)
* VFX platform 2024 compliant
* &lbrack;VFX Platform 2024&rbrack; Update to Python 3.11
* &lbrack;VFX Platform 2024&rbrack; Update to OpenEXR 3.2
* &lbrack;VFX Platform 2024&rbrack; &lbrack;USD&rbrack; Update OpenSubdiv 3.6.0
* &lbrack;VFX Platform 2024&rbrack;&lbrack;Color Management&rbrack; Update to OCIO 2.3.2
* &lbrack;Linux&rbrack; Migration to Linux RedHat
* &lbrack;Linux&rbrack; Update Nvidia driver min version to 535.171.04
* &lbrack;Import&rbrack; Add an option to flip normal map when importing a GLTF mesh
* &lbrack;UI&rbrack; Use operating system default value for drag event detection distance
* &lbrack;Substance Engine&rbrack; Add call strip function to remove the symbols from the executable
* &lbrack;Splash screen&rbrack; Update to new splash screen format
* Update Substance Engine to version 9.1.3
* &lbrack;Python&rbrack; Show link to examples in the layer stack documentation menu
* &lbrack;JavaScript&rbrack; Move Javascript plugins into javascript/plugins subfolder

**Fixed**:

* &lbrack;Illustrator&rbrack; Crash exporting a UV Tile with .ai graphic in specific cases
* &lbrack;Dynamic Strokes&rbrack;&lbrack;Path&rbrack; Random per stroke does not work on a path
* &lbrack;UI&rbrack;&lbrack;Properties&rbrack; Lock is enabled when tiling is non-uniform
* Debug TXT file is created when double clicking on Painter project
* &lbrack;USD&rbrack;&lbrack;Export&rbrack; Some textures may be missing
* &lbrack;ASM&rbrack; Scattering Color channel ignores metallic
* &lbrack;Content&rbrack; Blur filter doesn't work in "working" color space
* &lbrack;Content&rbrack; Height Adjust filter also modifies the alpha of the layer

**Known Issues**:

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Win&rbrack;&lbrack;Crash&rbrack; &lbrack;ACE&rbrack; Not using sRGB ICE color space for display transform
* &lbrack;Regression&rbrack;&lbrack;UI&rbrack; Right-click Menu is too small on HD screens
* &lbrack;Crash&rbrack;&lbrack;Python&rbrack; USD export triggered by TextureStateEvent
* &lbrack;MacOS Intel&rbrack; Crash when importing some presets
* &lbrack;Crash&rbrack; Relocate resource and save project
* &lbrack;Engine&rbrack; Painting with Clone tool in normal channel shift colors incorrectly
* &lbrack;Python&rbrack; Ghost widget appears deleted by script still functioning
* &lbrack;RedHat&rbrack; Color picker issues

### 10.0.1

Release date: **2024/06/11**Summary: **Minor release, bug fixes**

**Added:**

* &lbrack;Library&rbrack; Convert Substance fonts into regular font files
* &lbrack;Illustrator&rbrack;&lbrack;SVG&rbrack; Give thumbnails in scope selection a light gray background
* &lbrack;Python&rbrack; Add function on bitmap source to list available color spaces

**Fixed**:

* &lbrack;Layer Stack&rbrack; Folder always closed when moved in or out of other folders
* &lbrack;Save&rbrack; Project file is lost when "save as copy" or autosave fails in specific cases
* &lbrack;Import&rbrack; Assets with same name but different extensions are overridden
* &lbrack;Properties&rbrack; Settings missing when using anchor point in image inputs
* &lbrack;Illustrator&rbrack; Cannot import Illustrator files after server crash without restarting Painter
* &lbrack;Python&rbrack; Instance parent cannot be set with type "properties"
* &lbrack;Python&rbrack; Setting the high poly as a baking parameter does not load the high poly
* &lbrack;Python&rbrack; Error message for set_color_space() is too generic
* &lbrack;Python&rbrack; Reference sources allow to create cycles

**Known Issues**:

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Regression&rbrack;&lbrack;UI&rbrack; Right-click Menu is too small on HD screens
* &lbrack;Crash&rbrack;&lbrack;Python&rbrack; USD export triggered by TextureStateEvent
* &lbrack;MacOS Intel&rbrack; Crash when importing some presets
* &lbrack;Illustrator&rbrack; Crash exporting a UV Tile with .ai graphic in specific cases
* &lbrack;Dynamic Strokes&rbrack;&lbrack;Path&rbrack; Random per stroke does not work on a path

### 10.0.0

Release date: **2024/05/16**Summary: **Major release, edition of the layer stack with Python API, read native Illustrator files, integration of 3D Assets and new text resource**

**Added**:

* &lbrack;Illustrator&rbrack; Use Illustrator files with art boards in Painter
* &lbrack;Illustrator&rbrack;&lbrack;SVG&rbrack; Add previews in scope selection
* &lbrack;Substance 3D Assets&rbrack; Browse, select and download 3D Assets directly in Painter
* &lbrack;Substance 3D Assets&rbrack;&lbrack;UI&rbrack; New panel
* &lbrack;Substance 3D Assets&rbrack; Support environment maps and materials
* &lbrack;Substance 3D Assets&rbrack; Allow to reload and navigate and open location folder in new Substance 3D Assets panel
* &lbrack;Substance 3D Assets&rbrack; Addition of a download manager
* &lbrack;Text Resource&rbrack; Allow to use embeddable fonts
* &lbrack;Text Resource&rbrack; Allow to render a font/text on a mesh
* &lbrack;Text Resource&rbrack; Display fonts from user and other shared paths in Assets panel with a new category
* &lbrack;Text Resource&rbrack;&lbrack;Properties&rbrack; Add support for advanced font properties
* &lbrack;Text Resource&rbrack; Allow to search/view fonts in mini-shelves
* &lbrack;Text Resource&rbrack; Add error message/dialog when importing an incompatible font
* Miscellaneous
* &lbrack;Fill projection&rbrack; Improve Scale manipulator behavior when using small values
* &lbrack;Manipulators&rbrack; Add new precise mode when pressing CTRL shortcut
* &lbrack;Manipulators&rbrack; Improve surface manipulator stability when translating
* &lbrack;Export&rbrack; Add colorspace name in SBSAR outputs
* &lbrack;Performance&rbrack; Improve library discovery time of assets on disk
* &lbrack;Substance&rbrack; Update to Substance engine version 9.1.2
* &lbrack;Drag and Drop&rbrack; Align decal rotation to camera when dropping in viewport
* &lbrack;Python&rbrack; Edition of the layer stack
* &lbrack;Python&rbrack; Allow to select layer, effect, mask, geo mask in UI
* &lbrack;Python&rbrack; Allow to get/set layer blending modes
* &lbrack;Python&rbrack; Allow to get/set fill layer projection settings
* &lbrack;Python&rbrack; Allow to query Substance material color from a fill layer
* &lbrack;Python&rbrack; Allow to query and set uniform colors and resources in layers and effects
* &lbrack;Python&rbrack; Allow to create and edit text resources in layer stack
* &lbrack;Python&rbrack; Allow to edit active channels on layers and effects
* &lbrack;Python&rbrack; Allow to batch actions to have a single undo/redo
* &lbrack;Python&rbrack; Allow to load/edit vectorial source parameters
* &lbrack;Python&rbrack; Allow to edit layer and effects color properties with color management
* &lbrack;Python&rbrack; Allow to query and create instanced layers
* &lbrack;Python&rbrack; Allow to add color selection effect
* &lbrack;Python&rbrack; Allow to control bitmap image color management
* &lbrack;Python&rbrack; Allow to pause/unpause engine
* &lbrack;Python&rbrack; Allow to navigate to siblings and parent nodes
* &lbrack;Python&rbrack; Allow to create filter/generator effect
* &lbrack;Python&rbrack; Allow to add level effect
* &lbrack;Python&rbrack; Allow to add smart mask on a layer
* &lbrack;Python&rbrack; Allow to create/edit anchor points
* &lbrack;Python&rbrack; Allow to get/Set mask on layers
* &lbrack;Python&rbrack; Allow to create compare mask effect
* &lbrack;Python&rbrack; Allow to query and use presets from Substance resources
* &lbrack;Python&rbrack; Allow to list presets and their values via internal_properties function for Substance resources
* &lbrack;Python&rbrack; Allow to list predefined export presets
* &lbrack;Python&rbrack; Allow to list export presets available in the library
* &lbrack;Python&rbrack; Allow to retrieve the content of export presets

**Fixed**:

* &lbrack;Crash&rbrack; Undoing "Remove shader instance" with Ctrl-Z
* &lbrack;Crash&rbrack; Create a layer on empty stack if last selection was an effect
* &lbrack;SVG&rbrack; Issue with custom cropped area value
* &lbrack;Auto-Unwrap&rbrack; Recomputing only the packing without any change to UV orientation results in crash
* &lbrack;Drag and drop&rbrack; Lag due to external resources are preloaded multiple times
* &lbrack;UI&rbrack; Drag and drop resource thumbnail can hide warning message in layer stack
* &lbrack;Performance&rbrack; Masked UV tiles are still computed
* &lbrack;USD&rbrack; Wrong highlight for scope selection
* &lbrack;Resource&rbrack; Bitmap image gets corrupted after painting in normal channel and saving project
* &lbrack;USD&rbrack; Support left-handed vertex mesh ordering
* &lbrack;Substance&rbrack; Reset to default always go back to zero for angle widget
* &lbrack;Engine&rbrack; Painting with an SVG in a stencil doesn't work
* &lbrack;Engine&rbrack; Normal map brush strokes break after an undo
* &lbrack;Content&rbrack; Graphic to Material filter has incorrect alpha blending and color space
* &lbrack;Content&rbrack; Blending modes on Tile Generator are not working
* &lbrack;Content&rbrack; Histogram scan filter produces banding in some cases
* &lbrack;Content&rbrack; Baked lighting stylized does not take painted height into account
* &lbrack;Python&rbrack; Unexpected error when retrieving instanced layer information after shader change
* &lbrack;Save&rbrack; Project file is lost when "save as" fails in specific cases

**Known Issues**:

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Crash&rbrack;&lbrack;Linux&rbrack;&lbrack;AMD&rbrack; Dragging and dropping resources in layer stack on Wayland OS
* &lbrack;Regression&rbrack;&lbrack;UI&rbrack; Right Click Menu is too small on HD screens
* &lbrack;Crash&rbrack;&lbrack;Python&rbrack; USD export triggered by TextureStateEvent
* &lbrack;Save&rbrack; Spp project file is lost when "save as copy" fails in specific cases
* &lbrack;MacOS Intel&rbrack; Crash when importing some presets
* &lbrack;Illustrator&rbrack; Cannot import Ai files after server crash without restarting Painter
* &lbrack;Import&rbrack; Assets with same name but different extensions are overridden

## Version 9

### 9.1.2

Release date: **2024/01/30**Summary: **Minor release, bug fixes**

**Added**:

* &lbrack;Performance&rbrack; Improve first fill layer creation time in new projects
* &lbrack;Performance&rbrack; Reduce loading time of heavy environment maps
* &lbrack;Substance&rbrack; Allow to save/close projects even when thumbnails are generating

**Fixed**:

* Save fails on previous version projects when viewport is modified
* &lbrack;Crash&rbrack; Reimporting mesh when using custom AO and color management
* &lbrack;Fill projection&rbrack; Clicking on Scale manipulator gives "not paintable" message
* &lbrack;Brush&rbrack; Painting with UV alignment causes artefacts
* &lbrack;Layer stack&rbrack; Renaming layer is slow when stack is very long
* &lbrack;Layer Stack&rbrack; Incorrect error message when using incompatible filter in mask
* &lbrack;Layer stack&rbrack; Selection switches back to top layer after deletion
* &lbrack;Export&rbrack; Generated normal texture is always in 3D Space Neighbor padding mode
* &lbrack;Export&rbrack; Texture alpha is not generated with 2D View export preset
* &lbrack;Export&rbrack; SBSAR export has incorrect usages with converted maps
* &lbrack;Shader&rbrack; Shader API changelog is not up to date with latest ASM changes

**Known Issues**:

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Crash&rbrack;&lbrack;Linux&rbrack;&lbrack;AMD&rbrack; Dragging and dropping resources in layer stack on Wayland OS
* &lbrack;Regression&rbrack;&lbrack;UI&rbrack; Right Click Menu is too small on HD screens
* &lbrack;Crash&rbrack;&lbrack;Python&rbrack; USD export triggered by TextureStateEvent

### 9.1.1

Release date: **2023/12/05**Summary: **Minor release, bug fixes and send to After Effects functionality**

**Added:**

* &lbrack;Interop&rbrack; Allow to send a textured mesh to After Effects (Ae 24.1)

**Fixed:**

* &lbrack;Fill&rbrack; UV set to UV set projection does not read more than 2 UV sets
* &lbrack;Crash&rbrack; Using 16K environment map
* &lbrack;Crash&rbrack; Exr used as image input
* &lbrack;Crash&rbrack; Copy and pasting Paths across projects
* &lbrack;QoL&rbrack; Drag and drop of Alpha resource in decal mode creates UV projection in mask
* &lbrack;Path&rbrack; Copying path vertices also rename target path when reopening project
* &lbrack;Linux&rbrack; Color picking can be broken with multiple screens
* &lbrack;Auto Unwrap&rbrack; UI issue for texel density control
* &lbrack;Color Management&rbrack; UI feedback is sensible to case but engine is not
* &lbrack;Color Management&rbrack; Incorrect color space selection in mask with user data override

**Known Issues:**

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Crash&rbrack;&lbrack;Linux&rbrack; with Linux Wayland on AMD when drag and dropping resource in the Layer Stack
* &lbrack;Crash&rbrack;&lbrack;Mac&rbrack; Changing Anisotropic filtering value on Monterey OS
* &lbrack;Regression&rbrack;&lbrack;UI&rbrack; Right Click Menu is too small on hd screen
* &lbrack;Python&rbrack; Crash exporting USD triggered by TextureStateEvent

### 9.1.0

Release date: **2023/11/07**Summary: **Major release introducing SVG and transparency support, as well as drag and drop and path tool improvements**

**Added:**

* &lbrack;SVG&rbrack; Allow to import vectorial files (SVG)
* &lbrack;SVG&rbrack;&lbrack;UI&rbrack; Add support for SVG-specific properties
* &lbrack;SVG&rbrack; Add an option to easily preserve original image proportions
* &lbrack;SVG&rbrack; Allow to automatically use alpha of SVG with transparency
* &lbrack;Interop&rbrack; Allow to send a textured mesh to After Effects (Ae 24.1 beta)
* &lbrack;Interop&rbrack; Add settings for Send to After Effects
* &lbrack;QoL&rbrack;&lbrack;Assets&rbrack;&lbrack;UI&rbrack; Auto-import asset when drag and dropping into UI slot
* &lbrack;QoL&rbrack; Allow to drag and drop external assets into the layer stack
* &lbrack;QoL&rbrack;&lbrack;Layer Stack&rbrack; Drag and drop textures from Assets Panel into the Layer Stack
* &lbrack;QoL&rbrack;&lbrack;Viewport&rbrack; Allow to drag and drop generator, filters on the mesh
* &lbrack;QoL&rbrack;&lbrack;Viewport&rbrack; Allow to drop external assets onto the mesh
* &lbrack;QoL&rbrack;&lbrack;Projection&rbrack; Add new UV set to UV set projection mode
* &lbrack;QoL&rbrack; Drag and drop Smart Masks as new layers in viewport and Layer Stack
* &lbrack;QoL&rbrack; Add selector for Generators with multiple outputs when used in mask
* &lbrack;QoL&rbrack; Allow to drag and drop single channel images over a fill effect
* &lbrack;QoL&rbrack;&lbrack;Layer stack&rbrack; Use CTRL/ALT modifiers with drag and drop to specify where/how to create effects/layer
* &lbrack;Path&rbrack; Toggle paths visibility individually in path panel
* &lbrack;Path&rbrack; Allow to use transformation manipulators for path points
* &lbrack;Path&rbrack; Allow to control tangents per vertex manually
* &lbrack;Path&rbrack; Copy/paste path properties
* &lbrack;Path&rbrack; Introduce an empty shortcut for break tangent button
* &lbrack;Shader&rbrack; Add support for Opacity & Translucency in ASM shader
* &lbrack;Shader&rbrack; Add support for Absorption color channel with ASM shader
* &lbrack;Shader&rbrack; Improve ASM shader parameters tooltips
* &lbrack;Shader&rbrack; Change Translucency channel default color to black
* &lbrack;Display settings&rbrack; Enable Temporal Anti-Aliasing by default
* &lbrack;Display settings&rbrack; Enable Sub-surface scattering setting by default
* &lbrack;Substance&rbrack; Add support for ColorSpace property from graph input/output
* &lbrack;Substance&rbrack; Update Substance engine to version 9.0.3
* &lbrack;UI&rbrack; Make contextual toolbar button accessible even if the app window is small
* &lbrack;Auto Unwrap&rbrack; Control UV Tiles number with Texel Density
* &lbrack;Baking&rbrack; Deactivate GPU raytracing on AMD GPUs by default
* &lbrack;Performance&rbrack; Apply lossless compression on 16bit images to reduce project footprint
* &lbrack;Python&rbrack; Allow to manipulate the default Camera in 3D View
* &lbrack;Python&rbrack; Expose the ability to export mesh via scripting
* &lbrack;Content&rbrack;&lbrack;Samples&rbrack; Add new sample project "French Restaurant Table"
* &lbrack;Content&rbrack; Update Substance logo alpha to new version
* &lbrack;Content&rbrack; Add three SVG focused material filters (Custom Sticker, Custom Spray and Graphic to Material)

**Fixed:**

* &lbrack;Crash&rbrack; Changing manipulator size when not using symmetry tool
* &lbrack;Crash&rbrack; &lbrack;Layer stack&rbrack; Creating layer when nothing is selected
* &lbrack;Project&rbrack; Mesh maps can be corrupted after a removing unused resources
* &lbrack;Project&rbrack; Resource corruption after re-importing or re-baking image
* &lbrack;Assets&rbrack; Reloading an asset removes it from Favorites
* &lbrack;Import&rbrack; Can not import resources when there is "No result found" in asset panel
* &lbrack;UI&rbrack; Contextual toolbar arrow does not appear in some cases
* &lbrack;Substance&rbrack; Side by side button for boolean values is not supported
* &lbrack;Level&rbrack; Wrong channel label when used in mask
* &lbrack;Export&rbrack;&lbrack;glTF&rbrack; glTF/GLB files exported from Painter do not have a physical size unit
* &lbrack;Content&rbrack; Blur filter intensity is clamped to 16
* &lbrack;Content&rbrack; Color Match filter "target color" image input is not visible

**Known issues:**

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Crash&rbrack;&lbrack;Linux&rbrack; with Linux Wayland on AMD when drag and dropping resource in the Layer Stack
* &lbrack;Crash&rbrack;&lbrack;Mac&rbrack; Changing Anisotropic filtering value on Monterey OS
* &lbrack;Crash&rbrack; Exr used as image input
* &lbrack;Crash&rbrack; Using 16K environment map
* &lbrack;Auto Unwrap&rbrack; UI issue for texel density control
* &lbrack;Regression&rbrack;&lbrack;UI&rbrack; Right Click Menu is too small on hd screen
* &lbrack;Python&rbrack; Crash exporting USD triggered by TextureStateEvent
* &lbrack;QoL&rbrack; Drag and drop of Alpha resource in decal mode creates UV projection in mask

### 9.0.1

Release date: **2023/09/19**Summary: **Minor bugfix release with several improvements**

**Added:**

* &lbrack;Import&rbrack; Set default import location in import window
* &lbrack;Baking Mode&rbrack; Allow to reset parameters to their default values
* &lbrack;Baking&rbrack; Set baking to paint resolution when creating a project
* &lbrack;Symmetry&rbrack; Unbind symmetry-specific manipulator from shortcut Q
* &lbrack;Menu&rbrack; Add "show log" option in help menu
* &lbrack;Viewport&rbrack; Improve shadow rendering speed
* &lbrack;Substance&rbrack; Update engine to version 9.0.1
* &lbrack;Color Management&rbrack; OCIO config file can have any extension type
* &lbrack;Assets&rbrack; Sbsar resource with 'decal' usage should be auto-set to warp projection
* &lbrack;Path&rbrack; Display a message when trying to interact with the Path tool while UI and Gizmos are hidden

**Fixed:**

* &lbrack;Crash&rbrack; Alt + Drag on Path panel
* &lbrack;Import Resources&rbrack; Random crash when removing resources to import
* Crash when importing a compressed GLB file
* Issue while painting on meshes sharing UVs
* Mesh flash black when recomputing or loading cache
* &lbrack;Properties&rbrack; Right-click menu to reset parameters doesn't appear on dropdowns
* &lbrack;Level&rbrack; Input sliders locked by previous level
* &lbrack;AMD&rbrack;&lbrack;Sparse&rbrack; SVT option if activated generates artefacts
* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack; Crash when double clicking on vertices
* &lbrack;Path&rbrack; UI and path visible in baking mode
* &lbrack;AMD&rbrack; Texture lost when playing with visibility
* &lbrack;Sparse&rbrack; Resolution too low when turning around the mesh

**Known Issues:**

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors

### 9.0.0

Release date: **2023/06/20**Summary: **Major release with Paint along path allowing 3D Curves, new base materials and cleaning of legacy materials and new presets for 3D Curves**

**Added:**

* &lbrack;Path&rbrack; Add new Paint along Path tool
* &lbrack;Path&rbrack; Add an empty shortcut for the path tool
* &lbrack;Path&rbrack; Allow to add new points to an existing path
* &lbrack;Path&rbrack; Add shortcut to exit current path creation
* &lbrack;Path&rbrack; Allow to edit brush properties for paths
* &lbrack;Path&rbrack; Adjust tangents automatically when placing a point
* &lbrack;Path&rbrack; Recompute tangents when a point is moved
* &lbrack;Path&rbrack; Snap newly created points to the surface of a mesh
* &lbrack;Path&rbrack; Allow to edit pressure per vertex
* &lbrack;Path&rbrack; Adjust newly created point's pressure from neighboring points
* &lbrack;Path&rbrack; Allow to convert points to smooth/corner (tangent break)
* &lbrack;Path&rbrack; Allow to move a newly added point immediately
* &lbrack;Path&rbrack; Allow to remove points from existing path
* &lbrack;Path&rbrack; Allow to reverse the direction of a path
* &lbrack;Path&rbrack; Allow to select a path in the viewport
* &lbrack;Path&rbrack; Allow to select path points with marquee selection
* &lbrack;Path&rbrack; Introduce CTRL-A shortcuts to select all points of a path
* &lbrack;Path&rbrack; Allow to close path
* &lbrack;Path&rbrack; Allow to specify path up axis in Properties
* &lbrack;Path&rbrack; Add a vertex control menu to the contextual toolbar
* &lbrack;Path&rbrack; Introduce paint/erase/smudge modes to the path tool
* &lbrack;Path&rbrack; Create visual feedback for paths in the viewport
* &lbrack;Path&rbrack; Add a visual indicator for path direction
* &lbrack;Path&rbrack; Add line thickness to path display settings
* &lbrack;Path&rbrack; Allow to hide paths UI
* &lbrack;Path&rbrack; Add Path panel to list paths of currently selected layer
* &lbrack;Path&rbrack; Add visual feedback when hovering over a path in the Path panel
* &lbrack;Path&rbrack; Display path panel whenever the Path tool is selected
* &lbrack;Path&rbrack; Allow to rename, delete, copy, cut, duplicate path in Path panel
* &lbrack;Path&rbrack; Display message when trying to interact in the 2D viewport with the Path tool
* &lbrack;Library&rbrack; Integrate new content (path tools and base materials)
* &lbrack;Dynamic Strokes&rbrack; Add distance property for dynamic strokes
* &lbrack;Dynamic Strokes&rbrack; Add size and spacing properties to dynamic strokes
* &lbrack;Dynamic Strokes&rbrack; Add start/middle/end property for dynamic strokes
* &lbrack;Python&rbrack;&lbrack;USD&rbrack; Expose project configuration parameters for the USD format
* &lbrack;Python&rbrack;&lbrack;USD&rbrack; Expose project creation parameters for the USD format
* &lbrack;Export&rbrack;&lbrack;USD&rbrack; Add project path information inside exported USD file
* &lbrack;GLTF&rbrack; Update textures in library when reloading a GLTF file
* &lbrack;Shader&rbrack; Reduce seam artifacts for UV islands with different orientation
* &lbrack;Engine&rbrack; Update to Substance engine version 9.0

**Fixed:**

* &lbrack;Import&rbrack; Some GLB with textures do not get textures in Painter
* &lbrack;AMD&rbrack; Artefacts on borders for all 3D projection fills
* &lbrack;Engine&rbrack; Textures break when toggling layer visibility
* &lbrack;Engine&rbrack; Textures are empty in some places when changing blending mode
* &lbrack;Engine&rbrack; Texture/Projection is empty warp mode in some cases
* &lbrack;Iray&rbrack; Iteration reset to 0 when saving render
* &lbrack;Log&rbrack; USD error message when doing File &gt; New

**Known Issues:**

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Layer Stack&rbrack; Input source not saved per layer

## Version 8

### 8.3.1

Release date: **2023/04/27**

**Added:**

* &lbrack;Baking Mode&rbrack; Add (empty) shortcut to show/hide the viewport visualization
* &lbrack;Baking Mode&rbrack; Always show Low Poly when using "Hide baking meshes" button
* &lbrack;Baking Mode&rbrack; Show suffix for Matching By Name based on current Texture Set
* &lbrack;Import&rbrack; Add support for GLTF binary files (glb)
* &lbrack;Texture Set list&rbrack; Add menu to select or create shader instances
* &lbrack;Texture Set list&rbrack; Allow to quickly change Texture Set and UV Tile resolution
* &lbrack;Physical Size&rbrack; Improve manipulator behavior when using physical size in UV projection
* &lbrack;UI&rbrack; Bring back 'Save as' to main File menu
* &lbrack;UI&rbrack; Save view selection (2D only, 3D only, both) in UI layout
* &lbrack;USD&rbrack; Less vague error message at project creation with unsupported USD shapes
* &lbrack;Python&rbrack; Add baking events to follow Baking progress
* &lbrack;Python&rbrack; Allow to cancel a bake
* &lbrack;Python&rbrack; Expose 'Based on output template' for File Type and Bitdepth in export
* &lbrack;Python&rbrack; Expose refresh time for TextureStateEvent.Update

**Fixed:**

* &lbrack;Crash&rbrack; Rare crash when closing a project
* &lbrack;Crash&rbrack; &lbrack;Baking&rbrack; Activate mesh map sync with Height or curvature on specific project
* &lbrack;Crash&rbrack;&lbrack;Scripting&rbrack; Crash when adding a material after shader instance creation
* &lbrack;Baking Mode&rbrack; AO intensity in neutral material has no effect
* &lbrack;Baking Mode&rbrack; Crash when switching to baking mode before model is loaded
* &lbrack;Baking Mode&rbrack; Missing error message in Baking Process tab
* &lbrack;Baking Mode&rbrack; Neutral material settings have no effect after re-importing a mesh
* &lbrack;Baking Mode&rbrack; Viewport separator is saved globally and not per mode
* &lbrack;Baking Mode&rbrack; Visualisation issue: average normal doesn't change the cage surface
* &lbrack;Color Management&rbrack; Auto detect color space setting is disabled when OCIO env var is present
* &lbrack;Content&rbrack; Mask Outline filter has artefact with height input
* &lbrack;Content&rbrack; Slope blur filter intensity slider is clamped at 1.0
* &lbrack;Interop&rbrack; Unable to create project with GLTF from Sampler
* &lbrack;Layer Stack&rbrack; Projection tiling value is not updated correctly with manipulator
* &lbrack;Linux&rbrack; Offset between graphic tablet pen and cursor with HDPI higher than 100%
* &lbrack;Python&rbrack; Crash when re-importing a mesh after creating a project
* &lbrack;Substance&rbrack; 3D noises are broken after re-importing a mesh
* &lbrack;UV Tiles&rbrack; Offset for UV projection is clamped to 1
* &lbrack;Viewport&rbrack; Straight lines visual feedback is not visible anymore
* &lbrack;WhatsNew&rbrack; Incorrect line return on feature titles

**Known Issues:**

* &lbrack;Import&rbrack; Some GLB with textures do not get textures in Painter

### 8.3.0

*(Released: January 10, 2023*)Summary: **Major release with new baking mode, new import and export of USD files, and physical size support for UV projection**

**Added:**

* &lbrack;Baking Mode&rbrack; New baking mode dedicated to baking process

* &lbrack;Baking Mode&rbrack; Set shortcut to switch to baking mode to F8

* &lbrack;Baking Mode&rbrack; Add Start and Cancel baking button in the viewport

* &lbrack;Baking Mode&rbrack; Add baking selection in Texture Set list

* &lbrack;Baking Mode&rbrack; Add new Mesh Map Bakers window to select bakers

* &lbrack;Baking Mode&rbrack; Add new Mesh Map Settings window to edit baking settings

* &lbrack;Baking Mode&rbrack; Add new Baking Log window to follow baking process

* &lbrack;Baking Mode&rbrack; Add baking parameters and undo actions to history window

* &lbrack;Baking Mode&rbrack; Add breadcrumbs in Mesh Map Settings

* &lbrack;Baking Mode&rbrack; Add mesh maps thumbnails in the Mesh Map Bakers window

* &lbrack;Baking Mode&rbrack; Add visualization settings collapsible menu in 3D viewport

* &lbrack;Baking Mode&rbrack; Add visualization setting to show/hide the high-poly mesh

* &lbrack;Baking Mode&rbrack; Add visualization setting to show/hide the cage mesh and wireframe

* &lbrack;Baking Mode&rbrack; Add visualization setting to show/hide the low-poly mesh

* &lbrack;Baking Mode&rbrack; Add visualization setting to show hard edges without UV seams as errors

* &lbrack;Baking Mode&rbrack; Inform in viewport about mesh and bake errors if Baking Log is not visible

* &lbrack;Baking Mode&rbrack; Add action to synchronize baker settings across all Texture Sets

  In the Mesh Map Bakers window, each baker (as well as the common settings) can be synced across Texture Sets by clicking on the link icon next to their name. This action will open a window which allows to select which Texture Sets will share the same parameters.

* &lbrack;Baking Mode&rbrack; Add actions to copy and paste baker settings

  In the Mesh Map Bakers window are available actions to copy and past each baker settings across Texture Sets either via the dedicated menu at the top of the window or the right-click contextual menu.

* &lbrack;Baking Mode&rbrack; Add button in Baking Log to jump from error to the right settings

  When a baker fails or a mesh doesn't load properly, an error message appears in the Baking Log. A button next to the message allows to change the Mesh Map Bakers and Mesh Map Settings window to show the related settings. This help isolate more easily the source of an issue to be able to fix it.

* &lbrack;Baking Mode&rbrack; Add menus to manage Texture Sets and Baker selections

  In both the "Texture Set list" and "Mesh Map Bakers" window have been added a little action menu to help copy, invert selections.

* &lbrack;Baking Mode&rbrack; Split baker selection list per Texture Set

* &lbrack;Baking Mode&rbrack; Split common settings per Texture Set

* &lbrack;Baking mode&rbrack; Load high-poly and cage meshes without freezing the interface

* &lbrack;Baking Mode&rbrack; Use the viewport progress bar to show mesh loading

* &lbrack;Baking Mode&rbrack; Add mesh loading state in Baking Log

* &lbrack;Baking Mode&rbrack; Allow to turn around mesh in viewport during baking

* &lbrack;Baking Mode&rbrack; Set baking order based on current mesh viewport visibility

* &lbrack;Baking Mode&rbrack; Display implicit baking cage in viewport

  When not using a custom cage mesh file, an automatic cage mesh will be generated and displayed in the viewport. Its size will we based on the Max Frontal Distance parameter from the baking common settings. The cage mesh is used to indicate how far the matching between the low and high poly will go.

* &lbrack;Baking Mode&rbrack; Show matching list of mesh names for Matching By Name in Baking Log

* &lbrack;Baking Mode&rbrack; Use neutral material to display 3D model in viewport

* &lbrack;Baking Mode&rbrack; Disable engine computation while in baking mode

* &lbrack;Baking Mode&rbrack; Display a warning when quitting the app while a bake is in progress

* &lbrack;Bakers&rbrack; Update anti-aliasing setting labels

  The anti-aliasing setting values have been renamed to "Supersampling" and with an explicit multiplier number to clarify their behavior.

* &lbrack;Bakers&rbrack; Update bakers to version 2.5.7.

* &lbrack;USD&rbrack; Import and export Universal Scene Description (USD) files

* &lbrack;USD&rbrack; Add USD options to the New Project window when selecting a USD file

* &lbrack;USD&rbrack; Add new Scope and Variants selection window

  When importing a USD file, clicking on the change button in the New Project or Project Configuration window allow to select which part and variants of a USD file to import.

* &lbrack;USD&rbrack; Add subdivision levels option

  When creating a new project with a USD mesh file that contains subdivisions, it is possible to select the level of subdivisions using a slider. The project will be created with the subdivided mesh. The level can be modifier via Project Configuration.

* &lbrack;USD&rbrack; Import USD skinned meshes at specific frame

  When creating a new project with a USD mesh file that contains animation, it is possible to select the frame using a slider which reflects the embedded timeline sequence. The frame can be modifier via Project Configuration.

* &lbrack;USD&rbrack;&lbrack;Export&rbrack; Add an option to export USD files

  New Export USD check box added to Export textures window. When it is checked, it allows to export USD files as well as texture maps using any template.

* &lbrack;USD&rbrack;&lbrack;Export&rbrack; Add USD file format to mesh export

* &lbrack;USD&rbrack; Rename the existing "USD PBR Metal Roughness" export preset to be more explicit

  The USD export template previously known as 'USD PBR Metal Roughness' is still accessible via Export textures &gt; Output template &gt; USDz (Apple AR).

* &lbrack;Auto Unwrap&rbrack; Add Lock orientation for packing

  New option for auto-unwrap settings which allows to preserve the orientation of existing UV islands when using the packing feature. It can be accessed via New project &gt; Auto-unwrap options &gt; UV island orientation.

* &lbrack;Physical Size&rbrack; Add setting to automatically use Physical Size in fill effect/layer

  A new option to automatically switch to physical size scale when using a material with embedded physical size has been added. It can be enabled per project via New project or via Edit &gt; Project configuration &gt; Physical size &gt; Switch fill layer scaling to Physical size when assigning materials.

* &lbrack;Physical Size&rbrack; Expose physical size for UV projection

  Physical size scaling is now available for UV projections - it enable auto-resizing for a material based on the physical size of a mesh. It can be selected via Scale &gt; Physical size in the Fill layer or effect Properties window.

* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Allow to query the application version

* &lbrack;Scripting&rbrack;&lbrack;JavaScript&rbrack; Update API to match new baking parameters

* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Baking module: edit baking parameters

* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Baking module: launch/cancel baking

* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Baking module: select curvature method

* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Baking module: selection of bakers/uv tiles

* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Baking module: synchronize baker settings across all Texture Sets

* &lbrack;SVT&rbrack; Enable sparse hardware support on AMD GPUs

  Hardware acceleration for the Sparse Virtual Textures system can now be enabled with AMD GPUs. This setting is automatically enabled in the general preferences.

* &lbrack;Projection&rbrack; Rename Cylindrical projection parameters

  The parameter "Cylinder Cap Culling" has been renamed to "Backface Culling" to better represent its action. The associated tooltip as been adjusted accordingly.

* &lbrack;Project&rbrack; Save application version in project and retrieve it via scripting

  Since version 8.2, the version of the application is now stored inside the spp file when saving. This version number can be retrieved with the function last_saved_substance_painter_version() in the project module of the Python API. For project made before 8.2, the returned value will be null.

* &lbrack;Import&rbrack; Improve general import time of 3D models

  We improved the general import time of meshes. For example reducing the waiting time when loading high-poly meshes for baking. This optimization applies in particular to the loading of OBJ files.

**Fixed:**

* &lbrack;Crash&rbrack; Changing channels on filter with specific stack

* &lbrack;Mac&rbrack;&lbrack;M1&rbrack; Crash when creating a fill layer and leaving the layer stack

  This issue can be fixed by updating to Mac OS 13 (Ventura).

* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Crash when using ui.add_dock_widget() with wrong type

* &lbrack;Baking&rbrack; Incomplete error message in log when a bake fails

* &lbrack;Baking&rbrack; Memory is not freed when baking is finished

* &lbrack;Engine&rbrack; Texture cache doesn't update when changing effect visibility

* &lbrack;Export&rbrack; 2D View exports randomly uniform map

* &lbrack;Project&rbrack; Memory allocation error when saving project with big mesh

* &lbrack;Viewport&rbrack; TAA causes artifacts when painting in some cases

**Known Issues:**

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Layer Stack&rbrack; Input source not saved per layer

### 8.2.0

*(Released: October 06, 2022*)Summary: **Major release with new onboarding panels (new welcome panel and what's new panel), export to SBSAR, effects for folder, several improvements for quality of life and bug fixes.**

**Added:**

* &lbrack;Onboarding&rbrack; Onboarding panel to welcome new users

  Added a new Welcome screen when new CC users open Painter for the very first time.

* &lbrack;Onboarding&rbrack; What's new panel to improve new features discoverability

  Added a new What's New screen which displays main new features. It is shown automatically the very first time Painter is opened after a major update, and can be accessed again via Help &gt; What's new.

* &lbrack;Onboarding&rbrack; Rename old Welcome to "Home screen"

  Old Welcome screen renamed Home screen to avoid confusion with the new Welcome screen.

* &lbrack;UI&rbrack; Resolve scaling issues for high-DPI screens

  Improved Painter UI adaptation on high definition screens with custom display scaling.

* &lbrack;UI&rbrack; Avoid persistent error messages in the UI

  Error messages from previous projects are now removed from the bottom status bar.

* &lbrack;UI&rbrack; Rework save menu

  Additional save options are now grouped in a sub-menu and some are renamed for consistency.

* &lbrack;UI&rbrack; Save and Export/Share UI layouts

  Inside the Window menu are new actions to save the UI layout into files and to reload them. The Painting and Rendering layouts are saved separately. Various functions have been added to "substance_painter.ui" to save, reset and load UI layouts as well.

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

* &lbrack;Assets panel&rbrack; "Pin" favorite assets to appear on top of asset panel

  Added a new right-click option to library assets that allows to pin them as favorites to the top of the panel. You can also view all your favorite assets via Saved Searches.

* &lbrack;Assets panel&rbrack; Delete, reload and rename assets

  Added right-click menu options to delete, reload and rename assets in the user library. They are deleted directly from their library location on disk and reloaded from original location. Assets that are part of a package like .abr or .sbsar cannot be edited individually.

* &lbrack;Color Selection&rbrack; Add blending modes to Color Selection effect

* &lbrack;Layer Stack&rbrack; Add blending mode and opacity on filters

* &lbrack;Layer stack&rbrack; Allow tiling values bigger than 128 for fill layer/effects

* &lbrack;Layer stack&rbrack; Cylinder caps for cylindrical projection in fill layer/effect

  Cylindrical projection in Fill layer properties now has the option to remove cylinder caps.

* &lbrack;Log&rbrack; Show an error message if mesh part are in negative space when trying to create a UV Tile project

  Added a clearer error message when failing to create a UV Tile project because UV parts are found in negative spaces.

* &lbrack;Project&rbrack; Indicate version in error message "data too recent" when opening a project

  When opening a project that is too recent for the application, the error message will now indicate the version of the project to make it easier to identify the right application version.

* &lbrack;Viewport&rbrack; Allow to light the mesh from underneath

  Added a new Environment Alignment parameter in Display Settings &gt; Camera &gt; Environment settings to align the environment map lighting to the camera when set to "Local".

* &lbrack;Viewport&rbrack; View R, G, B and Alpha in viewport (solo display mode)

  Under Display Settings &gt; Viewport Settings &gt; Channel display there is a new Color channels setting that allows to only display the R, G, B or Alpha component of a channel when in single display mode.

* &lbrack;Shader&rbrack; Allow to set User channels as RGBA in Material Layering shaders

  When setting the Texture Set channels configuration inside a shader for material layering, it is now possible to specify the format of the channel to deviate from the default value. This allows notably to request color user channels instead of grayscale only.

* &lbrack;Export&rbrack; Allow to export textures as SBSAR

  When exporting textures via the File &gt; Export Textures window the SBSAR (Substance Archive) file format can be chosen to regroup them together. The content of the SBSAR is driven by the output template used. The SBSAR file format can also be set in the export presets. When using hybrid configuration (SBSAR + Other format) textures that target an SBSAR are grouped together while the rest is exported alongside.

* &lbrack;Export&rbrack; Expose 16bit option for EXR file format

  When exporting EXR texture files, it is now possible to chose 16f bit (Half-Float) or 32f bit (Float) in the Export Textures window (both for export settings and export presets). Old projects and old export presets will default to 16f bit to reflect the old behavior.

* &lbrack;Python&rbrack; Add event to know when Texture Sets are modified

  The new "substance_painter.event.TextureStateEvent" allows to know when a Texture Set has been modified either because of a paint stroke, a new channel added or a channel removed.

* &lbrack;Python&rbrack; Allow to get and set Mesh Map resources in Texture Set settings

  New functions have been added in "substance_painter.project" module to get and set mesh maps resources. These functions can be used to update the mesh maps referenced by the Texture Set settings.

* &lbrack;Plugins&rbrack; Remove option to get other JS plugins

  Removed the option to get JavaScript plugins since they were hosted on the deprecated Share website.

* &lbrack;Content&rbrack; Add new Roblox template and export preset

  A new Roblox "Material Variant" and "Surface Appearance" project template and export preset have been added to make it easier to export PBR textures to Roblox. The template can be accessed via the File &gt; New project window.

* Update Substance Engine to last version (8.6.3)

* &lbrack;Steam&rbrack; Optimized build for Apple Silicon chipset (Apple M1 / M2)

**Fixed:**

* Crash when using 16k exr

* &lbrack;Crash&rbrack; Ctrl Z After deleting a shader instance

* &lbrack;Iray&rbrack; IoR is blocked to 1 for some shaders

* &lbrack;Win&rbrack;&lbrack;Baking&rbrack; Some high-poly fail to load

* &lbrack;Color Management&rbrack; Incorrect color space name in UI with filters

* &lbrack;Python&rbrack; Resource objects returned by import function don't have a type

  When importing a Substance package in Python the function was returning the package instead of its graph(s). The resource module now provides functions and parameters to retrieve the graph(s) of a Substance package.

**Known Issues:**

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Layer Stack&rbrack; Input source not saved per layer
* &lbrack;Painting&rbrack; Temporal anti aliasing causes artifacts when painting in some cases
* &lbrack;Export&rbrack; 2D View exports randomly uniform map

### 8.1.3

*(Released: August 25, 2022*)Summary: **Minor bugfix release**

**Added:**

* Update to Iray SDK 1.6

**Fixed:**

* &lbrack;Shader&rbrack; Crash with old faulty shader
* &lbrack;Material Layering&rbrack; Materials can disappear when reopening a project

**Known Issues:**

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Layer Stack&rbrack; Input source not saved per layer
* &lbrack;Crash&rbrack; Ctrl Z After deleting a shader instance
* &lbrack;Iray&rbrack; IoR is blocked to 1 for some shaderss

### 8.1.2

*(Released: July 19, 2022*)Summary: **Minor bugfix release**

**Added:**

* &lbrack;Auto Unwrap&rbrack; New option "Optimize for organic meshes" to select the segmentation algorithm
* &lbrack;Physical Size&rbrack; Expose unit options in New Project and Project Configuration
* &lbrack;Color Management&rbrack; Use monitor Display by default when using ACE
* &lbrack;Color Management&rbrack;&lbrack;Python&rbrack; Take into account ACE env-var preset file when creating project
* &lbrack;Color Management&rbrack; Reset Color Management settings in New Project window when the configuration changes
* &lbrack;Color Management&rbrack; Disable OCIO settings access when env-var is present
* &lbrack;Color Management&rbrack; Safely update ACE settings when a parameter does not exist anymore
* Update Substance Engine to version 8.6.0
* &lbrack;Export&rbrack; Add new GLTF export preset with Displacement support
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Retrieve resource information (including custom metadata)
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Add function to query list of mesh names per Texture Set
* &lbrack;Content&rbrack; Add new Blender template and export preset

**Fixed:**

* &lbrack;MacOS&rbrack; Crash when launching Iray in some cases
* &lbrack;Thumbnails&rbrack; Shelf thumbnails do not load properly
* Multiple UV channels are ignored
* &lbrack;Auto Unwrap&rbrack; Unnecessary computation when splitting long islands
* &lbrack;Auto Unwrap&rbrack; Option avoid elongated islands not taken into account
* &lbrack;Auto Unwrap&rbrack; Loss of extra data (vertex colors) when repacking UVs
* &lbrack;UI&rbrack; Horizontal scrollbar in properties window when Color Management is enabled
* &lbrack;Color Management&rbrack; OCIO configs are missing substance_3d_painter_standard_srgb role
* &lbrack;Generator&rbrack; Wrong usage of User data "disabled"
* &lbrack;Color Management&rbrack; Color Space "Not Compatible" dropdown should not be clickable
* &lbrack;Color Management&rbrack;&lbrack;Shader&rbrack; sRGB override define doesn't work anymore
* &lbrack;Generator&rbrack; Wrong usage of User data "disable"
* &lbrack;Layer stack&rbrack; Broken previews with UV Tiles projects
* &lbrack;Shader&rbrack; API documentation is not fully up to date with Bent Normals
* &lbrack;Export&rbrack;&lbrack;Interoperability&rbrack; Cannot send to Stager with special characters
* &lbrack;Content&rbrack; Some brush presets thumbnails are empty or too dark

**Known Issues:**

* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors
* &lbrack;Layer Stack&rbrack; Input source are not saved per layer
* &lbrack;Crash&rbrack; Ctrl Z After deleting a shader instance
* &lbrack;Iray&rbrack; IoR is blocked to 1 for some shaders
* &lbrack;Shader&rbrack; Crash with old faulty shader

### 8.1.1

*(Released: June 28, 2022*)Summary: **Minor release hotfix**

**Added:**

* &lbrack;Layer Stack&rbrack; Alt click on mask does not deselect effects anymore

**Fixed:**

* &lbrack;Crash&rbrack; Opening old project saved in solo view mode
* &lbrack;Crash&rbrack; Delete a Generator in properties
* &lbrack;Texture Set Settings&rbrack; Normal/Ambient Occlusion mixing and height to normal methods are broken
* &lbrack;Export&rbrack; Export textures using diffusion padding renders black maps

**Known Issues:**

* &lbrack;MacOS&rbrack; Crash when launching Iray on Monterey
* &lbrack;Preview Thumbnail&rbrack; Simplified thumbnails are not updated when an anchor is used
* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors

### 8.1.0

*(Released: June 07, 2022*)Summary: **Major release with ICC support, material scaling based on physical size data, new bakers, color eye dropper improvements, and a range of additional content**

**Added:**

* &lbrack;Color Management&rbrack; Add support for ICC profiles with Adobe Color Engine (ACE)
* &lbrack;Color Management&rbrack; Add support for "Adobe 98 RGB" as working color space for ICC
* &lbrack;Color Management&rbrack; Allow to configure ACE/ICC settings via a configuration file
* &lbrack;Color Management&rbrack; Allow to input linear color values in Color Picker with Legacy mode
* &lbrack;Color Management&rbrack; Allow to specify the color profile used for picking color outside the UI
* &lbrack;Color Management&rbrack; Remember the last Display value chosen in the viewport
* &lbrack;Color Management&rbrack;&lbrack;Substance&rbrack; Make generators/filters work properly with Color Management
* &lbrack;Color Management&rbrack;&lbrack;Substance&rbrack; Add new colorspace override keywords $working and $standardsrgb
* &lbrack;Physical Size&rbrack;&lbrack;Engine&rbrack; Extract physical size info from mesh
* &lbrack;Physical Size&rbrack;&lbrack;Engine&rbrack; Physical size computation
* &lbrack;Physical Size&rbrack; Expose options to use physical size in the UI
* &lbrack;Physical Size&rbrack; Add visual helpers in the viewport
* &lbrack;Baking&rbrack; Add Height baker
* &lbrack;Baking&rbrack; Add Bent Normals baker
* &lbrack;Baking&rbrack; Add Opacity baker
* &lbrack;Eye Dropper&rbrack; New color eye dropper preview next to the mouse and color managed
* &lbrack;Eye Dropper&rbrack; Color picker panel reappears at its last position when reopened
* &lbrack;Eye Dropper&rbrack; A new icon for the Material Picker
* &lbrack;Eye Dropper&rbrack; Color manage the channel preview of the color picker
* &lbrack;Eye Dropper&rbrack; Add click-to-select functionality to the eyedropper
* &lbrack;Eye Dropper&rbrack; Material picker no longer activates non-active channels
* &lbrack;Eye dropper&rbrack; Allow to use eyedropper with a shortcut
* &lbrack;Eye dropper&rbrack; Eyedropper picks up the relevant channel, when applicable
* &lbrack;Eye dropper&rbrack; Entering the color picker mode deactivates all shortcuts
* &lbrack;Eye dropper&rbrack; Remove auto selection of the hex field
* &lbrack;Eye dropper&rbrack; Don't close the panel when using the material picker
* &lbrack;Eye dropper&rbrack; New disabled state when channel is unavailable to pick
* &lbrack;Export&rbrack; Add tangent attribute to glTF export
* Update Substance Engine to v8.4
* Update Auto Unwrap to 0.9.0
* Update to Qt 5.15.8
* Update to Python 3.9
* &lbrack;Shader&rbrack; Add support for Bent Normals shading
* &lbrack;MacOS&rbrack; Support of 3DConnexion SpaceMouse
* &lbrack;Python&rbrack; Document the Python version used in the API
* &lbrack;Content&rbrack; Add 6 new 3D noises with 105 presets
* &lbrack;Content&rbrack; 20 new grunge maps and 2 cloth folds patterns
* &lbrack;Content&rbrack; Update "Mesh maps" export preset to use new bakers
* &lbrack;Content&rbrack; Blur Slope and warp filter depends on texture set resolution
* &lbrack;Content&rbrack; Update sample projects to use the 3 new bakers

**Fixed:**

* &lbrack;glTF&rbrack; Cannot open glTF with special character
* &lbrack;Engine&rbrack; Artefacts with anisotropy and SVT disabled
* &lbrack;MacOS&rbrack;&lbrack;M1&rbrack; Smart materials are not displayed correctly
* &lbrack;Mesh Processing&rbrack; Cannot import meshes from Modeler
* &lbrack;UI&rbrack; Horizontal scrollbar in new project window with Color Management enabled
* &lbrack;Color Management&rbrack; Working space value missing in color picker with some OCIO configs
* &lbrack;Color Management&rbrack; Brush preview in the viewport is not color managed
* &lbrack;SpaceMouse&rbrack; Pivot is not updated immediately with focus change and sometimes out of the model
* &lbrack;Export&rbrack;&lbrack;USD&rbrack; Exported USD files have a wrong structure
* &lbrack;USD&rbrack; Ambient Occlusion issue when exporting
* &lbrack;Content&rbrack; Update thumbnail's mesh to match Preview Sphere sample project

**Known Issues:**

* Export textures using diffusion padding renders black maps
* Normal/Ambient Occlusion mixing is broken
* &lbrack;MacOS&rbrack; Crash when launching Iray in some rare cases
* &lbrack;Preview Thumbnail&rbrack; Simplified thumbnails aren't updated when an anchor is used
* &lbrack;Color Management&rbrack; HDR color space conversions with ACE on Linux produce clamped colors

## Version 7

### 7.4.3

*(Released: April 11, 2022*)Summary: **Bugfix with support of 3Dconnexion SpaceMouse in 2D Viewport**

**Added:**

* &lbrack;SpaceMouse&rbrack; Support of 3DConnexion SpaceMouse in 2D Viewport

**Fixed:**

* &lbrack;Color Picker&rbrack; Cannot write in hexadecimal field
* &lbrack;Color Management&rbrack; Resources used in projection mode are not color managed in the overlay
* &lbrack;Color Management&rbrack; Errors are not reported in log
* &lbrack;SpaceMouse&rbrack; Remove generic error message if user does not have a SpaceMouse
* &lbrack;SpaceMouse&rbrack; When loading a project, pivot point is always hidden
* &lbrack;Bakers&rbrack; "Average normals" setting has no effect in UV Tile projects
* &lbrack;UV Tile&rbrack; Inactive uv tiles overlays disappear when reloading mesh with different tiles
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Remote scripting is broken
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Several channels cannot be queried from API and it raises an error
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Crash when using ProjectEditionEntered event
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Crash when calling get_active_stack()

**Known Issues:**

* 3Dconnexion SpaceMouse not supported on MacOS
* &lbrack;UI&rbrack; Horizontal scroll bar with color management appearing in some cases in new project window
* &lbrack;Mac M1&rbrack; Smart materials are not displayed correctlys

### 7.4.2

*(Released: March 08, 2022*)Summary: **Bugfix with support of 3Dconnexion SpaceMouse and color management (OCIO) improvements**

**Added:**

* &lbrack;SpaceMouse&rbrack;&lbrack;Windows&rbrack; Support of the 3Dconnexion SpaceMouse in the 3D Viewport for navigation
* &lbrack;SpaceMouse&rbrack;&lbrack;Windows&rbrack; Basic shortcuts/keys for Pro and Enterprise SpaceMouse models in the 3D Viewport
* &lbrack;SpaceMouse&rbrack;&lbrack;Windows&rbrack; Dedicated rotation center icon in the 3D Viewport
* &lbrack;Color Management&rbrack; Use roles from OCIO configuration to change default settings
* &lbrack;Color Management&rbrack; Color manage the properties window for color widgets
* &lbrack;Color Management&rbrack; Color manage the properties window for material preview
* &lbrack;Color Management&rbrack; Color manage swatches in color picker
* &lbrack;Color Management&rbrack; Add a setting to define the standard sRGB color space
* &lbrack;Color Management&rbrack; Add the Standard sRGB color space from OCIO config in color picker Display selector list
* &lbrack;Color Management&rbrack; Improvements for color space override menu
* &lbrack;Color Management&rbrack; Allow to override the environment map color space in Display Settings
* &lbrack;Color Management&rbrack; Draw color picker gradients based on current Display
* &lbrack;Color Management&rbrack; Clamp HDR values by default in color editor
* &lbrack;Color Management&rbrack; Use passthrough (no color space) for filters in Legacy mode
* &lbrack;Color Management&rbrack; Limit gradients display in color editor to match &lbrack;0-1&rbrack; range
* &lbrack;Color Management&rbrack; Hide Display selector in color picker in Legacy mode
* &lbrack;Color Management&rbrack; Make color picker hexadecimal field always in sRGB color space
* &lbrack;Color Management&rbrack; Disable color picker Display dropdown for data channels
* &lbrack;Optimization&rbrack; Warp grid recomputes only covered UV tiles
* &lbrack;Export&rbrack; Allow to export UV Tile projects for Sketchfab, USD and glTF
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Allow to change tonemapping function

**Fixed:**

* &lbrack;Sketchfab&rbrack; Updating existing model ends up creating new model
* &lbrack;Sketchfab&rbrack; Crash when searching for previously updated model
* Crash when exporting to USD
* Crash when creating a new shader instance in Geometry Mask or when geometry is hidden
* &lbrack;Import Asset Window&rbrack; Crash when changing the type of imported resources
* Normal mesh maps are inverted when used in layer stack
* &lbrack;Substance&rbrack; User data blending mode is not taken into account
* &lbrack;Color Management&rbrack; Bitmaps with color space in filename are imported as UV Tile sequences
* &lbrack;Color Management&rbrack; Color managed outputs of Substance graph are in wrong color space
* &lbrack;Color Management&rbrack; Polygon Fill tool displays the wrong color
* &lbrack;Color Management&rbrack; ACES tonemapper is applied to channels in solo mode
* &lbrack;Color Management&rbrack; Tool preview sphere lighting is not color managed
* &lbrack;Color management&rbrack;&lbrack;Export&rbrack; Converted maps applies an incorrect conversion
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack;&lbrack;Color Management&rbrack; Projects created with template & OCIO environment variable are in Legacy mode
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Cannot use the JavaScript evaluate function on startup
* &lbrack;3D Adobe Offer&rbrack; Can not launch Painter when using regional settings with languages not supported by default

**Known Issues:**

* 3Dconnexion SpaceMouse not supported on MacOS
* &lbrack;UI&rbrack; Horizontal scroll bar with color management appearing in some cases in new project window
* &lbrack;Bakers&rbrack; "Average normals" setting has no effect in UV Tile projects
* &lbrack;Mac M1&rbrack; Smart materials are not displayed correctly
* &lbrack;Color Management&rbrack; Resources used in projection mode are not color managed in the overlay
* &lbrack;Color Picker&rbrack; Cannot write in hexadecimal field

### 7.4.1

*(Released: December 14, 2021*)Summary: **Bugfix with color management improvements**

**Added:**

* &lbrack;Color Management&rbrack; Use data role in exported filenames
* &lbrack;Color Management&rbrack; Expand the section Color Management, by default, when OCIO is selected in new project and project settings windows
* &lbrack;Color Management&rbrack; Add ACES tonemapper in legacy mode
* &lbrack;Color Management&rbrack; Adjust default configuration settings
* &lbrack;Color Management&rbrack;&lbrack;Export&rbrack; Fill $colorSpace in filenames for data channels
* &lbrack;Export&rbrack; Export UV Tile project to Stager
* &lbrack;Interoperability&rbrack; Not available for Steam and Substance editions
* &lbrack;Interoperability&rbrack; Allow to send a UV Tile project to Stager

**Fixed:**

* &lbrack;MacOS&rbrack;&lbrack;Crash&rbrack; Painter does not start with Catalina
* &lbrack;Color Management&rbrack;&lbrack;Crash&rbrack; Random crash when playing with data type/color management on user channel
* &lbrack;Color management&rbrack; Resources used as grayscale in mask display color space new menu
* &lbrack;Color Management&rbrack; User channel is darker in the viewport in legacy mode + solo view
* &lbrack;Color Management&rbrack; Env map is always linear when used in iRay
* &lbrack;Color Management&rbrack; Color picker does not pick the right value for data channel in legacy mode
* &lbrack;Color management&rbrack; Color picker is broken inside of a Substance in legacy mode
* &lbrack;Color management&rbrack; Switching between solo channel views in the viewport does display with the right color space when using the dropdown menu
* &lbrack;Color Management&rbrack; Export applies the wrong conversion on color managed user channels in legacy mode
* Strokes made in solo view mask are not shown when switching back to material view
* &lbrack;Export&rbrack; Converted maps are not exported as color managed channels
* &lbrack;Texture Set&rbrack; Tooltip with original name is missing on renamed user channels
* &lbrack;Steam&rbrack; Files missing when checking file integrity with Steam

**Known Issues:**

* &lbrack;Mac M1&rbrack; Smart materials are not displayed correctly

### 7.4.0

*(Released: November 24, 2021*)Summary: **Major release. Introduction of the 1st version of color management, undock 2D or 3D view, new option for auto UV unwrapping for avoiding elongated islands, call JavaScript functions from Python API and new content**

**Added:**

* &lbrack;Color Management&rbrack; Support of Color Management OpenColorIO version 2
* &lbrack;Color Management&rbrack; Add color management settings to project settings
* &lbrack;Color Management&rbrack; Warning window about Color Management configuration changes when opening a project
* &lbrack;Color Management&rbrack; Display an error message if an invalid OCIO config file is selected
* &lbrack;Color Management&rbrack; Allow to override configuration with OCIO environment variable
* &lbrack;Color Management&rbrack; Multiple OCIO configurations integrated by default with the application
* &lbrack;Color Management&rbrack; Extract color space name from imported bitmap filename
* &lbrack;Color Management&rbrack; Allow to override the color space with one color space from the configuration in Properties window
* &lbrack;Color Management&rbrack; Add color management options in Texture Set Settings
* &lbrack;Color Management&rbrack;&lbrack;Viewport&rbrack; Allow to color manage 2D and 3D views separately
* &lbrack;Color Management&rbrack; Load and convert environment map to the working color space
* &lbrack;Color Management&rbrack; Adjust color picker and editor with current color space
* &lbrack;Color Management&rbrack; Allow to select the display transform color space in the viewport with a new dropdown menu
* &lbrack;Color Management&rbrack; Apply display transform with Iray rendering results
* &lbrack;Color Management&rbrack; Export textures with different color spaces
* &lbrack;Color Management&rbrack;&lbrack;Python&rbrack; Apply color management settings from Environment variable (OCIO) to new projects
* &lbrack;Viewport&rbrack; Allow to undock the 2D or 3D viewport
* &lbrack;Auto Unwrap&rbrack; New option to avoid elongated islands
* &lbrack;Scripting Python&rbrack; Call JavaScript functions from Python API
* &lbrack;New Project Window&rbrack; Make the imported maps section collapsible
* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack; Allow to hide normals as an option in the Warp settings
* &lbrack;Content&rbrack; 11 new grunge maps
* &lbrack;Content&rbrack; 8 new tool presets (zipper, tightening cord, glitter)
* &lbrack;Content&rbrack; 8 new materials (scar, pocket, ...)
* &lbrack;Content&rbrack; 1 new generator (inflate shrinkwarp)

**Known Issues:**

* &lbrack;Mac M1&rbrack; Smart materials are not displayed correctly
* &lbrack;Color Management&rbrack;&lbrack;Crash&rbrack; Random crash when playing with data type/color management on user channel
* &lbrack;Color Management&rbrack; Color picker does not pick the right value for data channel in legacy mode
* &lbrack;Color management&rbrack;&lbrack;Iray&rbrack; Saving the render in EXR or TIFF while Color Management is activated in the viewport will always save in linear
* &lbrack;Color management&rbrack; Resources used as grayscale in mask display the wrong Color Space menu
* &lbrack;Color Management&rbrack;&lbrack;Iray&rbrack; Env map is always linear when used in Iray
* &lbrack;Color Management&rbrack;&lbrack;Export&rbrack; Converted maps are not exported as a color managed channels
* &lbrack;Color Management&rbrack;&lbrack;Export&rbrack; Export ignores if user channel is color managed or not with legacy mode

### 7.3.1

*(Released: November 24, 2021*)Summary: **Bugfix**

**Added:**

* &lbrack;Projection&rbrack; Scaling should only work in Object Space

**Fixed:**

* &lbrack;Mac M1&rbrack; Material layering not working
* &lbrack;Mac M1&rbrack;&lbrack;Projection&rbrack; Warp does not work
* Micro details are not displayed properly
* &lbrack;Projection&rbrack;&lbrack;Crash&rbrack; Switching to warp mode with a layer created with a previous version
* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack; Flip does not work when transformation is set to world space
* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack; Split option remains selected after splitting is done
* &lbrack;Projection&rbrack;&lbrack;UV&rbrack; Pivot point is reset when flipping projection
* &lbrack;Filter&rbrack; Bake Lighting environment is changing when reloading or changing a parameter
* &lbrack;Interoperability&rbrack; Not available for Steam and Substance editions
* &lbrack;Interoperability&rbrack; The "Browse 3D assets in Marketplace" button should always open CCD in the Stock & Marketplace 3D tab

**Known Issues:**

* &lbrack;Mac M1&rbrack; Smart materials are not displayed correctly

### 7.3.0

*(Released: October 13, 2021*)Summary: **Major release. It contains a new 3D warp projection, a new cylindrical projection, improvements of the color picker, new functions in Python API and bug fixes**

**Added:**

* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack; Expose 3D warp as a new projection mode
* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack; Allow decal mode for Alphas, Textures and Procedurals with drag and drop in the viewport
* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack; Use warp projection with decal shortcut (ALT)
* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack;&lbrack;Toolbar&rbrack; Transform warp as whole or per vertices
* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack;&lbrack;Toolbar&rbrack; Add grid points with split warp cross wise, horizontally or vertically options
* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack;&lbrack;Toolbar&rbrack; Dedicated menu for reset actions
* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack;&lbrack;Toolbar&rbrack; Option to automatically adjust tangents when moving points
* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack;&lbrack;Toolbar&rbrack; Dedicated menu for grid edition (size, reset, color and handle size)
* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack; New keyboard shortcut to switch whole-vertices warp edition mode (SHIFT+V)
* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack; Click+Ctrl allows to switch between surface tool and other tools
* &lbrack;Projection&rbrack;&lbrack;Cylindrical&rbrack; Expose the cylindrical projection mode
* &lbrack;Projection&rbrack;&lbrack;Toolbar&rbrack; Group manipulator settings (size, grid steps, angle steps)
* &lbrack;Color Picker&rbrack; New color picker UI
* &lbrack;Color Picker&rbrack; Use sRGB values in color picker widgets
* &lbrack;Color Picker&rbrack; Allow to save and delete color swatches
* &lbrack;Color Picker&rbrack; Eyedropper accessible from color and normal slots
* &lbrack;Color Picker&rbrack; Allow to edit dynamic color between 0 and 255 values
* &lbrack;Color Picker&rbrack; Make HSV/RGB state common across the app
* &lbrack;Color Picker&rbrack; Color Picker window is semi persistent
* &lbrack;Color Picker&rbrack; Pressing Esc closes the color picker window
* Performance improvement for UI interaction and while painting
* &lbrack;Engine&rbrack; Update to new Substance engine version (8.3.0)
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Allow to reload the mesh of the current project
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Allow to update resources in projects
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Allow to set and query the resolution of UV Tiles
* &lbrack;Interoperability&rbrack; Not available for Steam and Substance editions
* &lbrack;Interoperability&rbrack; Receive multiple resources from Bridge

**Fixed:**

* Color picker does not display the right color
* &lbrack;Baking&rbrack; Texture set list are not ordered correctly
* &lbrack;FBX import&rbrack; 3ds Max group pivot transformations are not taken into account
* &lbrack;Substance Engine&rbrack; Crash with import of corrupted SBSAR
* &lbrack;MacOS&rbrack; Project configuration option in different languages is not present
* Autosaves can freeze Painter during long processes

**Known Issues:**

* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack; Split option remains selected after splitting is done
* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack; Flip does not work when transformation is set to world space
* &lbrack;Projection&rbrack;&lbrack;Warp&rbrack; Artifact lines between patches in some rare cases
* &lbrack;Projection&rbrack;&lbrack;UV&rbrack; Pivot point is reset when flipping projection
* &lbrack;Mac M1&rbrack; Smart materials are not displayed correctly
* &lbrack;M1&rbrack;&lbrack;Regression&rbrack; Material layering not working

### 7.2.3

*(Released: August 24, 2021*)Summary: **Minor release, bugfix**

**Added:**

* &lbrack;Libraries&rbrack; Add a way to exclude unwanted files from being crawled

**Fixed:**

* &lbrack;Win&rbrack; Multi screens and sleep issues
* &lbrack;MacOS&rbrack;&lbrack;Crash&rbrack; Switching shader when using effects
* &lbrack;Viewport&rbrack; Full preview mode no longer shows brush cursor without alpha
* &lbrack;UI&rbrack; Angle widget turns the wrong way
* &lbrack;Layer Stack&rbrack; Many sub folders create very long freeze
* &lbrack;Iray&rbrack; Different views in Iray and OpenGL: Visible if not working
* &lbrack;Iray&rbrack; Index of refraction not taken into account and does not appear in mdl properties
* &lbrack;JavaScript&rbrack; ShowExportDialog() never returns true
* Can't read mtl from Adobe Stock

### 7.2.2

*(Released: July 27, 2021*)Summary: **Minor release, bugfix**

**Added:**

* Upgrade AMD driver requirements version

**Fixed:**

* &lbrack;Mac M1&rbrack; Wrong Memory detection
* &lbrack;Export&rbrack; Very long paths are not displayed properly

**Known Issues:**

* &lbrack;Content&rbrack; Outdated shaders of the samples

### 7.2.1

*(Released: July 02, 2021*)Summary: **Minor release, Hotfix**

**Added:**

* &lbrack;Interop&rbrack; Add tooltip to inform that sending UV Tile projects to Stager is not yet supported
* &lbrack;Plugin&rbrack;&lbrack;UI&rbrack; Update of the Livelink icon

**Fixed:**

* &lbrack;Nvidia&rbrack; Driver version starting with 30 are considered outdated
* &lbrack;Libraries&rbrack; Asset panel state is not saved unless a project is open
* &lbrack;Libraries&rbrack; New saved search retains keyword from old saved search
* &lbrack;Bakers&rbrack;&lbrack;UVTiles&rbrack; ID maps per meshID also take UV Tiles in consideration
* &lbrack;Export&rbrack; gLTF files do not import vertex color
* &lbrack;Iray&rbrack; Some tooltips missing
* &lbrack;Interop&rbrack; Send to Stager is not always disabled when Stager is not detected
* &lbrack;Resource Updater&rbrack; Photoshop brush maker cannot be updated
* &lbrack;Content&rbrack; Fiber glass edge wear generator is broken

### 7.2.0

*(Released: June 23, 2021*)Summary: **Major release, it provides an update to the asset panel, a new shader with access to new channels and parameters, an overall refresh of the UI, some much-requested performance improvements, expanded language support, and more!**

**Added:**

* &lbrack;Libraries&rbrack; New Asset panel to replace the shelf
* &lbrack;Libraries&rbrack;&lbrack;UI&rbrack; New Asset panel layout
* &lbrack;Libraries&rbrack;&lbrack;UI&rbrack; Change default Asset panel orientation and UI
* &lbrack;Libraries&rbrack;&lbrack;UI&rbrack; Introduce a list view option to library
* &lbrack;Libraries&rbrack;&lbrack;UI&rbrack; New breadcrumbs navigation in the Asset panel
* &lbrack;Libraries&rbrack;&lbrack;UI&rbrack; Select "All libraries" when selecting a saved search
* &lbrack;Libraries&rbrack;&lbrack;UI&rbrack; Select "All libraries" when all folders are deselected
* &lbrack;Libraries&rbrack;&lbrack;UI&rbrack; New tag for particle brushes
* &lbrack;Libraries&rbrack;&lbrack;UI&rbrack; Replaced "shelf" by "All libraries" across the app
* &lbrack;Libraries&rbrack;&lbrack;UI&rbrack; Allow to hide empty folders
* &lbrack;Libraries&rbrack;&lbrack;UI&rbrack; Default user library should be visible even if empty
* &lbrack;Libraries&rbrack;&lbrack;UI&rbrack; New filtering method via asset type icons
* &lbrack;Libraries&rbrack; Shortcut "CTRL" to select multiple asset types
* &lbrack;Libraries&rbrack; New environment variable to control the asset preview memory budget
* &lbrack;Libraries&rbrack;&lbrack;Content&rbrack; New environment maps
* &lbrack;Libraries&rbrack;&lbrack;Content&rbrack;&lbrack;UI&rbrack; Render displacement on default materials
* &lbrack;Libraries&rbrack;&lbrack;Content&rbrack; Set Adobe Standard Material (ASM) shader as default for previews generation
* &lbrack;Libraries&rbrack;&lbrack;Content&rbrack;&lbrack;ASM&rbrack; New Project Templates for new ASM shader
* &lbrack;Libraries&rbrack;&lbrack;Thumbnail&rbrack; Use new Studio 6 environment map
* &lbrack;Libraries&rbrack;&lbrack;Thumbnail&rbrack; Read thumbnail in resource instead of generating it
* &lbrack;Libraries&rbrack;&lbrack;Thumbnail&rbrack; Add displacement to thumbnail generation
* &lbrack;Texture Set Settings&rbrack;
* &lbrack;Texture Set Settings&rbrack;&lbrack;UI&rbrack; Expose new height to normal conversion method
* &lbrack;Texture Set Settings&rbrack;&lbrack;UI&rbrack; Rework of the channels' UI organization
* &lbrack;Texture Set Settings&rbrack; User Channels limit raised to 16 channels
* &lbrack;Texture Set Settings&rbrack;&lbrack;UI&rbrack; Indicate which channels are compatible with currently selected shader
* &lbrack;Shader&rbrack;&lbrack;ASM&rbrack; New Adobe Standard Material shader
* &lbrack;Shader&rbrack;&lbrack;ASM&rbrack; Added support for Anisotropy, Clear Coat, Subsurface Scattering, Specular Edge Color, and Sheen
* &lbrack;Shader&rbrack;&lbrack;ASM&rbrack; Change default channels' color values
* &lbrack;Shader&rbrack;&lbrack;ASM&rbrack;&lbrack;Export&rbrack; Updated export template Adobe Dimension to Adobe Substance 3D Stager
* &lbrack;Shader&rbrack;&lbrack;ASM&rbrack; Added labels and tooltips for shader and MDL parameters
* &lbrack;Shader&rbrack;&lbrack;ASM&rbrack; Make the Scatter Color visible in 2D View even if SSS is not supported
* &lbrack;Shader&rbrack;&lbrack;ASM&rbrack;&lbrack;Iray&rbrack; Support ASM shader in Iray with new MDL
* &lbrack;Shader&rbrack;&lbrack;ASM&rbrack;&lbrack;Iray&rbrack; Updated Subsurface Scattering in legacy PBR spec gloss & coated
* &lbrack;Shader&rbrack;&lbrack;ASM&rbrack;&lbrack;Content&rbrack; Changed the default SSS type for samples
* &lbrack;Shader&rbrack;&lbrack;ASM&rbrack; Added documentation for ASM API
* &lbrack;Shader&rbrack;&lbrack;ASM&rbrack; Optimize shaders to ignore unused channels
* &lbrack;Shader&rbrack; Expose new Texture Set channels
* &lbrack;Shader&rbrack; Improved Subsurface Scattering
* &lbrack;Shader&rbrack; Hided new shader parameters for some shaders
* &lbrack;Shader&rbrack; Visible if for shader parameters
* &lbrack;Performance&rbrack;
* &lbrack;Libraries&rbrack; Resource preview loading time and calculation performance improvements
* &lbrack;Engine&rbrack; Painting performance improvements
* &lbrack;Auto Unwrap&rbrack;
* &lbrack;Auto Unwrap&rbrack; Packing performance improvements
* &lbrack;Auto Unwrap&rbrack; Auto unwrap compatible with UV Tile workflow
* &lbrack;Auto-Unwrap&rbrack; New option to position UVs according to mesh orientation
* &lbrack;Other&rbrack;
* &lbrack;Settings&rbrack; Changed default zoom direction
* &lbrack;UI&rbrack; Overall refresh of the UI
* &lbrack;UI&rbrack; Rework of the Help Menu
* &lbrack;UI&rbrack; Replace invert icon
* &lbrack;UI&rbrack;&lbrack;Plugin&rbrack; Replace icon for the plugin dcc link
* &lbrack;UI&rbrack;&lbrack;AMD&rbrack; Update minimum required version and popup message
* &lbrack;Layer Stack&rbrack; Create new layer inside selected empty folder
* Update Python Documentation
* &lbrack;Branding&rbrack;
* &lbrack;Branding&rbrack;&lbrack;UI&rbrack; Updated application name to Adobe Substance 3D Painter
* &lbrack;Branding&rbrack;&lbrack;UI&rbrack; Updated standalone version to 'Substance edition'
* &lbrack;Branding&rbrack;&lbrack;UI&rbrack; Updated application executable name, installation path, package and icons
* &lbrack;Branding&rbrack;&lbrack;UI&rbrack; Renamed default library and path
* &lbrack;Branding&rbrack;&lbrack;UI&rbrack; Updated About Window
* &lbrack;Branding&rbrack;&lbrack;UI&rbrack; Updated Welcome screen
* &lbrack;Branding&rbrack;&lbrack;UI&rbrack; Removed year-based version number
* &lbrack;Localization&rbrack; New translations in German, French, and Simplified Chinese
* &lbrack;Interoperability&rbrack; Not available for Steam and Substance editions
* &lbrack;Interoperability&rbrack; Interoperability with Adobe Ecosystem: Designer, Sampler, Stager, and Bridge
* &lbrack;Interoperability&rbrack;&lbrack;UI&rbrack; Receive and update asset from Designer
* &lbrack;Interoperability&rbrack;&lbrack;UI&rbrack; Receive asset from Sampler
* &lbrack;Interoperability&rbrack;&lbrack;UI&rbrack; Send asset to Stager
* &lbrack;Interoperability&rbrack;&lbrack;UI&rbrack; Show in Adobe Bridge
* &lbrack;Interoperability&rbrack;&lbrack;UI&rbrack; Allow to quickly access Adobe 3D Assets
* &lbrack;Interoperability&rbrack; New usage tags of sbsar
* &lbrack;Interoperability&rbrack; Handle received asset types
* &lbrack;Interoperability&rbrack; Asset received from Adobe Substance 3D Designer or Adobe Substance 3D Sampler are stored in user's default chosen library
* &lbrack;Interoperability&rbrack;&lbrack;UI&rbrack; New icon in left toolbar to send to Stager or Photoshop

**Fixed:**

* &lbrack;Tablet&rbrack; Low performance when Painting with pressure
* &lbrack;Tablet&rbrack; Issue on tablets with slider controls
* &lbrack;Crash&rbrack; Name mismatch between Texture Set list and Exporter
* &lbrack;Crash&rbrack;&lbrack;Libraries&rbrack; Double click on a sub-library
* &lbrack;Libraries&rbrack; Issue when Crawling library directories
* &lbrack;Libraries&rbrack; Force preview generation command line does not work as expected
* &lbrack;Libraries&rbrack;&lbrack;Content&rbrack; Baked Light Environment filter is black by default
* &lbrack;Linux&rbrack;&lbrack;MacOS&rbrack;&lbrack;Export Mesh&rbrack; Cannot import glTF created on Linux/MacOS
* &lbrack;Linux&rbrack; Dragging and dropping a file into the Asset panel can lead to a crash
* &lbrack;Auto-Unwrap&rbrack; Auto-Unwrap is available even if a mesh has not been selected for reloading
* &lbrack;Particles&rbrack; Wrong particle behavior with gravity
* &lbrack;Layer Stack&rbrack; Level histogram can only use Luminance with some channels
* &lbrack;Geometry Mask&rbrack; Right-click menu on a folder when editing the geometry mask does not work
* &lbrack;Projection&rbrack; Seam with spherical projection & bilinear filtering
* &lbrack;UV Tiles&rbrack; Export mask to file only exports tile 0, 0
* &lbrack;Export Mesh&rbrack; FBX mesh export is empty
* &lbrack;Iray&rbrack; Normal map is not taken into account in new projects when rendering
* &lbrack;Save&rbrack; Save issues on shared drives
* &lbrack;Baking&rbrack; Rebaking a mesh with modified parameters displays a warning
* &lbrack;Baking&rbrack;&lbrack;Regression&rbrack; Incorrect result when high poly meshes' global bounding box does not include the scene origin
* &lbrack;Python&rbrack; Custom user libraries are not taken into consideration

**Known Issues:**

* &lbrack;Libraries&rbrack; Saved searches not saved if no project opened
* &lbrack;NVIDIA&rbrack; Message for outdated driver even if the driver is up to date

### 7.1.1 (2021.1.1)

*(Released: March 23, 2021*)Summary: **Minor release, Bugfix with possibility to enter hexadecimal values in the color picker**

**Added:**

* &lbrack;Log&rbrack; Warn users about incompatible AMD GPU drivers
* &lbrack;Color Picker&rbrack; Allow to type hexadecimal values

**Fixed:**

* &lbrack;Baker&rbrack; Drop in performance
* &lbrack;Geometry mask&rbrack; Alt click on mesh name can lead to a crash
* &lbrack;Engine&rbrack; Painting does not refresh the entire view when necessary
* &lbrack;Layer stack&rbrack; Selection is stuck after changing shader
* &lbrack;MacOS&rbrack;&lbrack;Color picker&rbrack; Color is slightly different than the one picked
* &lbrack;Export&rbrack; Using PSD file format does not generate one file per UV Tile
* &lbrack;Scripting&rbrack;&lbrack;Javascript&rbrack; alg.mapexport.getPathsExportDocumentMaps() doesn't return all the values
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Disabled plugins are enabled again when reopening Painter

### 7.1.0 (2021.1.0)

*(Released: January 28, 2021*)Summary: **Major release, new Geometry Mask which allows to select and paint parts of the geometry, copy/paste effects in the layer stack, improvement of UV Tile workflow, update of Iray, Bakers, Substance Engine and new content**

**Added:**

* New geometry mask and paint selected parts of the geometry
* &lbrack;Geometry Mask&rbrack; Allow to paint selected parts of geometry by mesh names
* &lbrack;Geometry Mask&rbrack; Rectangular selection in both viewports
* &lbrack;Geometry Mask&rbrack; Allow to hide/ignore excluded geometry on any layer
* &lbrack;Geometry Mask&rbrack;&lbrack;Properties&rbrack; Quick selection for checkboxes with click and drag
* &lbrack;Geometry Mask&rbrack;&lbrack;Properties&rbrack;&lbrack;UI&rbrack; Include/Exclude all with a dropdown in Properties window
* &lbrack;Geometry Mask&rbrack;&lbrack;Properties&rbrack; Allow to quickly select one item in a list with ALT+LEFT CLICK
* &lbrack;Geometry Mask&rbrack;&lbrack;Properties&rbrack; Overlay in viewports when hovering Mesh names/UV Tiles in Properties window
* &lbrack;Geometry Mask&rbrack;&lbrack;Layer Stack&rbrack; Add Copy/Paste options to the geometry mask
* &lbrack;Geometry Mask&rbrack; New icon for Hide/ignore excluded geometry button
* &lbrack;Geometry Mask&rbrack; New tooltip for Hide/ignore excluded geometry
* &lbrack;Geometry Mask&rbrack; Keyboard shortcut ALT+H to toggle on/off "hide ignore excluded geometry" button
* &lbrack;UV Tiles&rbrack;&lbrack;Layer Stack&rbrack; New Fill layer sphere preview thumbnail for UV Tiles and simplified mode
* &lbrack;UV Tiles&rbrack;&lbrack;Layer Stack&rbrack; Allow to easily exit the UV Tile mask
* &lbrack;UV Tiles&rbrack;&lbrack;Texture Set List&rbrack; Allow to give a description per UV Tile
* &lbrack;UV Tiles&rbrack;&lbrack;Texture Set Settings&rbrack;&lbrack;UI&rbrack; Two new section titles in the dropdown menu to change UV Tile resolution
* &lbrack;UV Tiles&rbrack;&lbrack;Viewport&rbrack; Exit UV Tile Mask when dragging a material into the viewport
* &lbrack;Layer Stack&rbrack; Add Copy/Paste options for effects
* &lbrack;Layer Stack&rbrack; Allow to copy/paste effects from one Texture Set to another
* &lbrack;Layer Stack&rbrack; Allow multi-selection of effects
* &lbrack;Layer Stack&rbrack; Add copy/paste options as shortcuts for layer effects
* &lbrack;Layer Stack&rbrack; Automatically switch between mask and content when dragging effects to another layer
* &lbrack;Layer Stack&rbrack; Automatically create a mask when pasting a mask from another layer
* &lbrack;Layer Stack&rbrack; Add move effect actions inside the effects' contextual right click menu
* &lbrack;Layer Stack&rbrack; Allow to drag and drop effects from one layer to another
* &lbrack;Layer Stack&rbrack; Dragging items onto a folder places them on the top of the folder
* Update Iray to version 2020.1.0
* &lbrack;Bakers&rbrack; Update Bakers to version 2.5.4
* &lbrack;Bakers&rbrack; Display individual UV Tiles in the baking progress window
* &lbrack;Bakers&rbrack;&lbrack;UI&rbrack; Allow to quickly bake the current Texture Set with a new button
* &lbrack;Bakers&rbrack; Allow user to quickly select one of the bakers with ALT+LEFT CLICK
* Update Substance Engine to version 8.0.8
* &lbrack;Substance Engine&rbrack; Support Default Color in new .sbsar files
* &lbrack;Auto Unwrap&rbrack; Performance improvement
* &lbrack;Export&rbrack; Add visual feedback to indicate which UV Tile's resolution differs from project's default
* &lbrack;Export&rbrack; Add scene size factor into exported shader json file
* &lbrack;Language&rbrack; Add Japanese translation
* &lbrack;UI&rbrack; Update About window with versioning of internal dependencies
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Allow to manage Shelf resources
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Allow to know when a project is ready for baking and exporting
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Allow to know when a Shelf has finished crawling resources on disk
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Allow to query the list of UV tiles per Texture Sets
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Allow to assign custom preview to Shelf resources
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Allow to manage custom shelves
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Add a method index in each submodule in the documentation
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; New style for the documentation
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Improvement of resources and Shelf documentation
* &lbrack;Content&rbrack; Three new tool presets to make stitches
* &lbrack;Shelf&rbrack; Temporarily remove "Export to Substance Share" while transitioning to the new Substance Share platform

**Fixed:**

* Crash when using monitors with different resolutions
* Crash in Substance Engine with some rare projects
* Viewport refresh fails with Hide/Ignore Excluded Geometry when switching layers
* &lbrack;2D View&rbrack; 2D Viewport can be missing on some projects
* &lbrack;Baking&rbrack; "Match by mesh name" ignores parts of the object
* &lbrack;Layer Stack&rbrack; Clicking on a layer effect opens folder
* &lbrack;Geometry Mask&rbrack; UV Tile is still counted in mask even when reimporting the mesh without it
* &lbrack;Geometry Mask&rbrack; Right click menu in the viewport does not provide the correct tools
* &lbrack;Engine&rbrack; Heavy lags on particular projects
* &lbrack;Scripting&rbrack; High latency with remote JSON POST requests on Windows
* &lbrack;Linux&rbrack; Vram amount is not detected properly with specific integrated GPUs
* &lbrack;Auto Unwrap&rbrack; Crashes or long unwrap on some projects

## Version 6

### 6.2.2 (2020.2.2)

*(Released: September 28, 2020*)Summary: **Minor release, Bugfix with some functions in Python API**

**Added:**

* &lbrack;Performance&rbrack; Do not compute all UV Tiles when using the color ID selection
* &lbrack;Bakers&rbrack;&lbrack;UI&rbrack; Display Texture Set descriptions
* &lbrack;Bakers&rbrack; Allow to save bake settings
* &lbrack;Bakers&rbrack; Add collapse all/expand all options to the Selection tab
* &lbrack;Texture Set List&rbrack; Hide description when empty
* &lbrack;UV Tiles&rbrack;&lbrack;Texture Set List&rbrack; Clicking on UV Tile should expand/collapse list
* &lbrack;Export&rbrack;&lbrack;UI&rbrack; Allow to resize the Texture Set List panel horizontally
* &lbrack;Export&rbrack;&lbrack;UI&rbrack; Consistent tooltip text for both UV Tiles and Texture Set workflow with unselected textures
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Allow to use export presets to export textures
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Add a changelog in documentation
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Allow to query all the available channels on a given stack
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Console UI improvements

**Fixed:**

* &lbrack;AMD&rbrack; Incorrect detection of outdated driver version
* Crash when reimporting a mesh with different UV Tiles layout in some cases
* Crash when using particles with UDIMs on very heavy meshes
* &lbrack;UV Tiles&rbrack; Crash when exporting a mesh with displacement information in some cases
* &lbrack;Export&rbrack;&lbrack;Crash&rbrack; Exporting 2D view in psd format can cause a crash
* Importing images as sequences when creating a project does not work
* Engine stuck in an endless loop
* &lbrack;Shortcut&rbrack; Camera rotates always in snap mode when changing snap mode shortcuts
* Meshes are always auto-unwrapped when re-imported even if option is off
* &lbrack;Texture Set List&rbrack; Description text field is sometimes not fully visible during edition
* &lbrack;Texture Set List&rbrack; Dropdown menu to hide/unhide Texture Sets is not fully visible
* &lbrack;Texture Set List&rbrack; Clicking on eye icon should not enter the "Edit Texture Set name"
* &lbrack;Texture Set Settings&rbrack; Removing a Channel also removes the Channel below
* &lbrack;Export&rbrack; Include all and Reset all does not take UV Tiles into consideration
* &lbrack;Bakers&rbrack; Deselected bakers appear during the baking process
* Resolution update is not taken into account for baked maps used as input
* &lbrack;UV Tiles&rbrack;&lbrack;Viewport&rbrack; 3D Viewport freeze when adding Smart Material after folder with UV Tile mask selected
* &lbrack;UV Tiles&rbrack;&lbrack;Viewport&rbrack; Wireframe is still visible for hidden tiles with paint through mode
* &lbrack;Export&rbrack;&lbrack;Sketchfab&rbrack; Issues with "plus" subscription type
* &lbrack;Sketchfab&rbrack; "This asset is private" checkbox is not displayed after switching account
* &lbrack;Export&rbrack;&lbrack;Content&rbrack; "Wiggly" brush presets can lead to performance issues
* &lbrack;Plugin Photoshop&rbrack; Message in log: not compatible with UV Tile workflow
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; PYTHONPATH env var prevents the application from starting
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Typo in Python documentation

### 6.2.1 (2020.2.1)

*(Released: July 29, 2020*)Summary: **Minor release, Hotfix**

**Added:**

* Add environment variable "SUBSTANCE_PAINTER_VRAM_BUDGET" to override GPU VRam amount
* &lbrack;UV Tiles&rbrack;&lbrack;Performance&rbrack; Do not compute all UV tiles when using the Polygon Fill tool

**Fixed:**

* &lbrack;Iray&rbrack; Save render returns an error results in a black image
* &lbrack;Linux&rbrack; Crash after the splash screen on CentOS 7.3
* &lbrack;Linux&rbrack; Vram amount is not detected properly with specific configurations
* &lbrack;Crash&rbrack; Opening a project with duplicated texture set's name
* &lbrack;Engine&rbrack; Cache invalidation issue when modifying a mask
* &lbrack;Texture Set List&rbrack; Wrong font effect when Texture Set is deactivated

**Known Issues:**

* &lbrack;Texture Set List&rbrack; Cannot hide description
* &lbrack;Texture Set List&rbrack; UI issues
* &lbrack;Iray&rbrack; PSD render does not open
* &lbrack;Plugin Photoshop&rbrack; Not compatible with UV Tiles workflow

### 6.2.0 (2020.2.0)

*(Released: July 23, 2020*)Summary: **Major release with new UV Tiles workflow, paint across UV Tiles and performance improvement**

**Added:**

* UV Tiles (UDIMs)
* &lbrack;UV Tiles&rbrack; Paint across UV tiles
* &lbrack;UV Tiles&rbrack; Allow to choose between new and legacy workflow for UV Tiles
* &lbrack;UV Tiles&rbrack; Import UDIMs/UV Tile image sequences as a resource
* &lbrack;UV Tiles&rbrack; Add list of UV Tiles per Texture Set in Texture Set List window
* &lbrack;UV Tiles&rbrack; Allow to edit the resolution of multiple UV Tiles at once in Texture Set Settings
* &lbrack;UV Tiles&rbrack;&lbrack;2D View&rbrack; Display UV Tiles as a grid
* &lbrack;UV Tiles&rbrack;&lbrack;2D View&rbrack; New viewport button to display or hide UV Tiles information
* &lbrack;UV Tiles&rbrack; Switch painting tool to single channel by default for UV Tile projects
* &lbrack;UV Tiles&rbrack; New button in contextual toolbar to ignore masked UV Tiles while painting
* &lbrack;UV Tiles&rbrack;&lbrack;Layer Stack&rbrack; New layer stack icons to improve performance
* &lbrack;UV Tiles&rbrack;&lbrack;Layer Stack&rbrack; Improve Paint and Fill icons in the toolbar
* &lbrack;UV Tile Mask&rbrack;&lbrack;2D View&rbrack; Allow to include or exclude multiple UV Tiles at once (left click, CTRL+left click)
* &lbrack;UV Tile Mask&rbrack; New UV Tile mask to include, exclude tiles per layer with a new icon
* &lbrack;UV Tile Mask&rbrack;&lbrack;Layer Stack&rbrack; Display the number of UV Tiles in the UV Tiles mask icon when not all are included
* &lbrack;UV Tile Mask&rbrack;&lbrack;2D/3D View&rbrack; Add hover effect to visualize UV Tiles under the cursor
* &lbrack;UV Tiles&rbrack;&lbrack;Bakers&rbrack; Allow to select and bake specific UV Tiles
* &lbrack;UV Tiles&rbrack;&lbrack;Bakers&rbrack; Add selection options for Texture Sets/UV Tiles
* &lbrack;UV Tiles&rbrack;&lbrack;Bakers&rbrack; Right click menu option to select UV Tiles within a Texture Set
* &lbrack;UV Tiles&rbrack;&lbrack;Bakers&rbrack; Allow quick selection in the Texture Set/UV Tiles by dragging
* &lbrack;UV Tiles&rbrack;&lbrack;Bakers&rbrack; Replace "All" and "None" buttons in Mesh Maps by more explicit selection options
* &lbrack;UV Tiles&rbrack;&lbrack;Bakers&rbrack; Display number of textures to be baked
* &lbrack;UV Tiles&rbrack;&lbrack;Export&rbrack; Allow to select and export specific UV Tiles
* &lbrack;UV Tiles&rbrack;&lbrack;Export&rbrack; Allow quick selection of UV Tiles by dragging
* &lbrack;UV Tiles&rbrack;&lbrack;Export&rbrack; Add dropdown menu options for UV Tiles
* &lbrack;UV Tiles&rbrack;&lbrack;Export&rbrack; Make some export presets unavailable if they do not work with UV Tiles (Adobe Dimension, Sketchfab, glTF, USD)
* &lbrack;UV Tiles&rbrack;&lbrack;Content&rbrack; Update export presets to use the new $udim tag
* &lbrack;UV Tiles&rbrack; Improve error reporting when importing meshes with overlapping UV islands
* &lbrack;UV Tiles&rbrack; UV Tiles compatible in Iray
* &lbrack;UV Tiles&rbrack;&lbrack;Scripting&rbrack; Add UV Tile export documentation to Python doc
* Performance
* &lbrack;Performance&rbrack; New button in contextual toolbar to pause engine computation when working (SHIFT+ESC)
* &lbrack;Performance&rbrack; Faster project opening by delaying Texture Set cache computation
* &lbrack;Performance&rbrack; Don't wait for mesh maps to load when opening project
* &lbrack;Performance&rbrack;&lbrack;2D/3D View&rbrack; Don't compute Mask channel in viewport when it is not used
* &lbrack;Performance&rbrack; Do not block the application when loading mesh maps displayed in the viewports
* &lbrack;Performance&rbrack; Improve incremental save speed when saving a project
* &lbrack;Performance&rbrack;&lbrack;Bakers&rbrack; Change default dilation settings to improve saving time and project size
* &lbrack;Performance&rbrack;&lbrack;Bakers&rbrack; Switch to grayscale on specific Bakers to improve saving time and project size
* &lbrack;Performance&rbrack;&lbrack;Export&rbrack; Improve engine performance to export textures faster
* &lbrack;Performance&rbrack;&lbrack;Export&rbrack; Improve responsiveness when opening the export dialog with a lot of Texture Sets
* &lbrack;Performance&rbrack;&lbrack;Export&rbrack; Improve performance when switching to tab "List of Exports"
* &lbrack;Performance&rbrack;&lbrack;Iray&rbrack; Reduce Iray startup time
* Other
* &lbrack;Bakers&rbrack; Add selection options for Texture Sets
* Move shader instance management to Texture Set Settings
* &lbrack;2D/3D View&rbrack; Add message at bottom of the viewport to indicate which mask type is edited
* &lbrack;Layer Stack&rbrack; New option in settings to switch between legacy and new thumbnails
* &lbrack;Layer Stack&rbrack; Add visual feedback to indicate loading state of the thumbnails
* &lbrack;Proj&rbrack; New projection mode "Fill (Match Per UV-Tile)" to load image sequences
* &lbrack;Proj&rbrack; Change fill layers projection mode to "Fill (Match Per UV-Tile)" in specific cases
* &lbrack;Content&rbrack; Optimize Charcoal brush presets to improve performance
* Update Iray to version 2020.0.0
* &lbrack;Export&rbrack; Disable List of Exports tab when nothing is selected
* Auto Unwrap
* &lbrack;Auto Unwrap&rbrack; Improve success rate of the automatic unwrap process
* &lbrack;Auto Unwrap&rbrack; Improved parameterization to increase speed and stability

**Fixed:**

* &lbrack;Alembic&rbrack; Facesets are ignored when importing files
* &lbrack;Alembic&rbrack; Infinite loading time with specific files
* &lbrack;Import&rbrack; Incorrect UDIM image sequence is imported when only the file extension differs
* &lbrack;Crash&rbrack; Trying to open project locked by another process leads to a crash
* &lbrack;Projection&rbrack; Artefacts on duplicated mesh when using triplanar projection
* &lbrack;Export&rbrack; Emissive channel is not exported with USD format
* &lbrack;Content&rbrack; Smart Material "Charcoal" contains paint strokes

**Known Issues:**

* &lbrack;Texture Set List&rbrack; Cannot hide description
* &lbrack;Texture Set List&rbrack; UI issues

### 6.1.3 (2020.1.3)

*(Released: June 16, 2020*)Summary: **Bugfix**

**Added:**

* &lbrack;Export&rbrack; Add displacement settings in Shader parameters json file

**Fixed:**

* &lbrack;Crash&rbrack;&lbrack;Engine&rbrack; Crash when trying to erase and replace existing channels
* &lbrack;Crash&rbrack; Changing shader after painting a mask in material layering
* &lbrack;Crash&rbrack;&lbrack;Engine&rbrack; Crashes with some heavy projects
* &lbrack;Bakers&rbrack; Matching By Name doesn't work with OBJs exported from zBrush
* &lbrack;Displacement&rbrack;&lbrack;SVT&rbrack; Textures are not displayed at project opening when displacement is on
* &lbrack;Export&rbrack; Some textures are exported uniform gray
* &lbrack;Export&rbrack; Disabled Texture Sets should not be exported for Dimension and Sketchfab export presets
* &lbrack;Scripting&rbrack;&lbrack;JavaScript&rbrack; Crash while using the JavaScript API to access the export config in the onProjectOpened event
* &lbrack;Scripting&rbrack;&lbrack;Javascript&rbrack; onExportFinished() is not called after an export

### 6.1.2 (2020.1.2)

*(Released: May 28, 2020*)Summary: **Bugfix with Substance Engine and Bakers update**

**Added:**

* &lbrack;Bakers&rbrack; Update to the most recent version
* &lbrack;Bakers&rbrack; New Sampling method in Ambient Occlusion, Curvature, Thickness bakers
* Update to the most recent version of Substance Engine
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Allow creation of ResourceID for project resources
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Allow querying channel information
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; Add dryrun and callback functions to simulate texture export

**Fixed:**

* &lbrack;Bakers&rbrack; Incorrect normals in World Space Normals baker using a tangent Normal map in specific cases
* &lbrack;Bakers&rbrack; Error baking Ambient Occlusion with Optix when no high poly
* &lbrack;Dynamic Strokes&rbrack; Lag when loading specific Texture Set
* &lbrack;Export&rbrack; Should not export the disabled texture sets for USD, glTF
* &lbrack;Scripting&rbrack;&lbrack;JavaScript&rbrack; Cannot edit new Curvature baker settings
* &lbrack;Scripting&rbrack;&lbrack;JavaScript&rbrack; alg.texturesets.addChannel() does not return an error in some cases
* &lbrack;Scripting&rbrack;&lbrack;JavaScript&rbrack; Typo in Javascript API documentation for setProjectExportOptions()
* &lbrack;Scripting&rbrack;&lbrack;JavaScript&rbrack; Always exports all texture sets
* &lbrack;Scripting&rbrack;&lbrack;Python&rbrack; sys.executable returns a path to python.exe instead of Substance Painter
* Texture cache not compatible across Mac OS and Windows/Linux
* &lbrack;Livelink UE4&rbrack; Only last material is used for all texture sets in a combined mesh

**Known Issues:**

* &lbrack;Export&rbrack;&lbrack;Dimension&rbrack;&lbrack;Skecthfab&rbrack; Should not export the disabled texture sets
* &lbrack;Crash&rbrack; Change shader after having painted a mask in material layering

### 6.1.1 (2020.1.1)

*(Released: May 05, 2020*)Summary: **Hotfix**

**Added:**

* &lbrack;Export&rbrack; Overridden state visual feedback on TextureSet

**Fixed:**

* &lbrack;Export&rbrack; Exporter window size too large on special resolution monitor and can not be resized
* &lbrack;Export&rbrack; Options are not saved after export
* &lbrack;Export&rbrack; Crash or cannot export with "from cache" export preset
* &lbrack;Export&rbrack; Cancelling export generates an unexpected additional empty map
* &lbrack;Export&rbrack; Fix virtual export preset settings
* &lbrack;Python&rbrack; PYTHONPATH env var is not taken into account
* &lbrack;Python&rbrack;&lbrack;Export&rbrack; Cancelling export via Python returns an exception error
* &lbrack;Python&rbrack;&lbrack;Export&rbrack; export_project_textures incorrect result with psd file format
* &lbrack;Bakers&rbrack; Crash on Linux with GPU raytracing

**Known Issues:**

* &lbrack;JavaScript&rbrack; Cannot edit new Curvature baker settings
* &lbrack;JavaScript&rbrack;&lbrack;Export&rbrack; Always exports all texture sets
* &lbrack;Export&rbrack;&lbrack;USD&rbrack; Should not export the disabled texture sets
* &lbrack;Crash&rbrack; Change shader after having painted a mask in material layering

### 6.1.0 (2020.1.0)

*(Released: April 22, 2020*)Summary: **Major release with New texture and mesh exporter (with displacement and tessellation), updated UV unwrapping with more controls, new bakers, new scripting python API, better UX for decal projection and new content**

**Added:**

* New texture and mesh exporter
* &lbrack;Export&rbrack; New exporter interface
* &lbrack;Export&rbrack;&lbrack;Export tab&rbrack; Allow selection of which maps channels are exported per Texture Set
* &lbrack;Export&rbrack;&lbrack;Export tab&rbrack; Allow modification of the Texture Set size for all Texture Sets in one action
* &lbrack;Export&rbrack;&lbrack;Export tab&rbrack; Allow a different template per Texture Set (except for USD, glTF, Sketchfab and Dimension)
* &lbrack;Export&rbrack;&lbrack;Export tab&rbrack; Quick activation and deactivation of maps and Texture Sets
* &lbrack;Export&rbrack;&lbrack;Export tab&rbrack; Export resolution 8192x8192 no longer experimental
* &lbrack;Export&rbrack;&lbrack;Export tab&rbrack; Allow modification of the file format and bit depth per map
* &lbrack;Export&rbrack;&lbrack;Export tab&rbrack; Allow reset to the default parameters' values
* &lbrack;Export&rbrack;&lbrack;Export tab&rbrack; Allow settings to be saved without exporting
* &lbrack;Export&rbrack;&lbrack;Output templates tab&rbrack; Rename "Configuration" tab to "Output templates" tab
* &lbrack;Export&rbrack;&lbrack;Output templates tab&rbrack; Allow definition of file format and bit depth per preset map
* &lbrack;Export&rbrack;&lbrack;List of exports tab&rbrack; New preview tab to summarize and view export process
* &lbrack;Import/Export Mesh&rbrack; Import/Export time performance optimization
* &lbrack;Export Mesh&rbrack; Export mesh in FBX
* &lbrack;Export Mesh&rbrack; Export mesh with displacement and tessellation
* &lbrack;Export Mesh&rbrack;&lbrack;UI&rbrack; New settings for recomputing normal vertex, apply triangulation
* &lbrack;Export Mesh&rbrack; Export original mesh topology with new UVs generated by auto unwrapping
* Updated auto UV unwrapping with more controls
* &lbrack;UV Unwrapping&rbrack;&lbrack;UI&rbrack; Add setting to activate auto UV unwrapping in new project window
* &lbrack;UV Unwrapping&rbrack;&lbrack;UI&rbrack; New Options to control the unwrapping steps (seams, unwrapping, packing)
* &lbrack;UV Unwrapping&rbrack;&lbrack;UI&rbrack; Allow conservation of existing unwrapping seams/unwrapping/packing
* &lbrack;UV Unwrapping&rbrack;&lbrack;UI&rbrack; New Options to fully recompute unwrapping steps
* &lbrack;UV Unwrapping&rbrack;&lbrack;UI&rbrack; New Option to control the margin size (none, small, medium and large)
* New Bakers
* &lbrack;Bakers&rbrack; Replace old Curvature by new Curvature from mesh
* &lbrack;Bakers&rbrack; Add match by name option to ignore backface in "Ambient Occlusion" baker
* &lbrack;Bakers&rbrack; Add ground plane option in "Ambient Occlusion" baker
* New scripting Python API (3.7.6)
* &lbrack;Python&rbrack;&lbrack;UI&rbrack; New scripting menu for Python
* &lbrack;Python&rbrack;&lbrack;UI&rbrack; New Python documentation in Help menu
* &lbrack;Python&rbrack; Expose Substance Painter python modules: substance_painter, alg, display, project.setting, project, texturesets, ui
* &lbrack;Python&rbrack; Expose new "substance_painter" Python module
* &lbrack;Python&rbrack; Expose new Python sub-module: alg, display, log, project, resource, texturesets, ui
* &lbrack;Python&rbrack; Listener for project changes
* &lbrack;Python&rbrack; New examples in Python documentation
* &lbrack;JavaScript&rbrack;&lbrack;UI&rbrack; Plugins menu replaced by JavaScript
* &lbrack;Viewport&rbrack; Allow creation of a decal projection by "drag/dropping + ALT" a resource from the shelf
* New Content
* &lbrack;Content&rbrack; 5 new decal materials from Substance Source
* &lbrack;Content&rbrack; Add new project templates and export presets for Maxwell renderer
* &lbrack;Content&rbrack; Add project template for Keyshot 9 export
* &lbrack;Content&rbrack; Update Keyshot 9 export preset to support displacement and emissive
* &lbrack;Content&rbrack;&lbrack;Exporter&rbrack; Update of all export presets to match latest versions of game engines and renderers
* &lbrack;Content&rbrack;&lbrack;Exporter&rbrack; Update export presets files to use new format and dithering settings
* &lbrack;Content&rbrack; New templates and shaders to support VRay material (VRayMtl)
* &lbrack;Layer Stack&rbrack; Allow deletion of layer effects using trash icon or keyboard shortcut Delete
* Remove plugin Substance Source (use launcher with "send to" functionality)
* &lbrack;Windows&rbrack; Do not display TDR warning on high-end GPUs

**Fixed:**

* Translation issues in new project file dialog
* &lbrack;Bakers&rbrack; Setting "Save preprocessed scene file" does not work anymore
* &lbrack;Planar Projection&rbrack; Projection does not work on meshes with repeating UVs
* &lbrack;Decal&rbrack; Difference of behavior in normal channel when using different fill layer projection modes
* &lbrack;Smudge&rbrack;&lbrack;Clone&rbrack; Artifact may appear when painting in mask
* &lbrack;Engine&rbrack; Crash with specific layer content
* &lbrack;Engine&rbrack; Random crash when painting in some cases
* &lbrack;Anchor point&rbrack; Reference to an empty mask always returns white
* &lbrack;Export&rbrack; Layer not taken into account in some particular stack configurations
* &lbrack;Export mesh&rbrack; Cannot export with path containing special characters
* &lbrack;Export Mesh&rbrack; Cannot read glTF files when exported from Linux or MacOS
* &lbrack;Import mesh&rbrack; Re-importing DAE, PLY or glTF does not work as intended

**Known Issues:**

* &lbrack;Scripting&rbrack;&lbrack;JavaScript&rbrack; Cannot edit new Curvature baker settings
* &lbrack;Bakers&rbrack; Crash on Linux with GPU raytracing
* &lbrack;Export&rbrack;&lbrack;USD&rbrack; Should not export the disabled texture sets
* &lbrack;Crash&rbrack; Change shader after having painted a mask in material layering

## Version 5

### 5.3.3 (2019.3.3)

*(Released: February 06, 2020*)Summary: **Bugfix with upgrade to Iray 2019.3**

**Added:**

* Upgrade to Iray 2019.3
* &lbrack;Log&rbrack; Indicate outdated bios for Ryzen CPU leading to crash during baking
* &lbrack;ABR&rbrack; Extract ABR alphas to shelf

**Fixed:**

* &lbrack;Baker&rbrack; Baking fail if High-poly mesh does not have UVs
* &lbrack;Linux&rbrack; Custom mouse shortcuts are not saved
* &lbrack;Brush&rbrack; Outline disappears with some alpha shapes
* &lbrack;Tablet&rbrack; Bad detection when moving sliders
* &lbrack;Shortcuts&rbrack; Can not set up any shortcut with "Ctrl+Alt+MouseClick"
* &lbrack;Shelf&rbrack; Can not see resource tooltip when using a pen tablet
* &lbrack;2D View&rbrack;&lbrack;Export&rbrack; 2D View preset does not take into account the normal information
* Freeze when painting in UV alignment with certain brushes
* Painting under a filter creates artifact on the ongoing stroke
* &lbrack;Viewport&rbrack; Incorrect texture cache in viewport after re-importing a mesh
* &lbrack;Crash&rbrack; Error when saving after exporting to Photoshop
* &lbrack;Crash&rbrack; Writing special symbols in prefix when importing resources
* &lbrack;Crash&rbrack; Click on the reference in Anchor Point Properties
* &lbrack;Anchor Points&rbrack; Channel does not update when there is a filter between Anchor point and reference
* Iray url link in Help menu does not work

**Known Issues:**

* &lbrack;UV Unwrapping&rbrack; Processing high poly meshes can take a long time
* &lbrack;UV Unwrapping&rbrack; Vertices at the exact same coordinates are merged
* &lbrack;UV Unwrapping&rbrack; UV Generation may fail on some mesh parts in some rare cases
* &lbrack;UV Unwrapping&rbrack; Non uniform or highly distorted texel ratio in a single UV island in some cases
* &lbrack;UV Unwrapping&rbrack; Non uniform texel ratio between Texture Sets
* &lbrack;UV Unwrapping&rbrack; UV island generated can be very elongated and do not fit into UV space in some cases
* &lbrack;UV Unwrapping&rbrack; Degenerated faces or non-triangular mesh faces with small or overlaping edges may not get UV unwrapped

### 5.3.2 (2019.3.2)

*(Released: January 21, 2020*)Summary: **Bugfix**

**Fixed:**

* Opening a project that was saved in solo channel mode does not display the mesh
* Viewport is not always updated when painting under layer using clone tool

**Known Issues:**

* &lbrack;Bakers&rbrack; Crash related to multi-threading on Ryzen CPUs
* &lbrack;UV Unwrapping&rbrack; Processing high poly meshes can take a long time
* &lbrack;UV Unwrapping&rbrack; Vertices at the exact same coordinates are merged
* &lbrack;UV Unwrapping&rbrack; UV Generation may fail on some mesh parts in some rare cases
* &lbrack;UV Unwrapping&rbrack; Non uniform or highly distorted texel ratio in a single UV island in some cases
* &lbrack;UV Unwrapping&rbrack; Non uniform texel ratio between Texture Sets
* &lbrack;UV Unwrapping&rbrack; UV island generated can be very elongated and do not fit into UV space in some cases
* &lbrack;UV Unwrapping&rbrack; Degenerated faces or non-triangular mesh faces with small or overlaping edges may not get UV unwrapped

### 5.3.1 (2019.3.1)

*(Released: December 20, 2019*)Summary: **Hotfix**

**Fixed:**

* Crash when working on meshes with specific UV projections
* &lbrack;ABR&rbrack; Crash when switching between Photoshop presets
* &lbrack;Linux&rbrack; Cannot start Substance Painter on CentOS 7.4 because of libGLX dependency issue
* &lbrack;Bakers&rbrack; Crash when baking after using File &gt; Clean
* &lbrack;Bakers&rbrack; Baking progress dialog freeze after cancel
* &lbrack;Bakers&rbrack; Baking mesh after exporting textures does not work
* &lbrack;Bakers&rbrack; Using "Match By Name" results with black Mesh Maps
* &lbrack;Bakers&rbrack; Cage is not taken into account
* &lbrack;Shelf&rbrack; Importing PSD files leads to broken images
* &lbrack;Sample&rbrack; "Mat" sample project has broken cameras and incorrect export preset

**Known Issues:**

* &lbrack;Bakers&rbrack; Crash related to multi-threading on Ryzen CPUs
* &lbrack;UV Unwrapping&rbrack; Processing high poly meshes can take a long time
* &lbrack;UV Unwrapping&rbrack; Vertices at the exact same coordinates are merged
* &lbrack;UV Unwrapping&rbrack; UV Generation may fail on some mesh parts in some rare cases
* &lbrack;UV Unwrapping&rbrack; Non uniform or highly distorted texel ratio in a single UV island in some cases
* &lbrack;UV Unwrapping&rbrack; Non uniform texel ratio between Texture Sets
* &lbrack;UV Unwrapping&rbrack; UV island generated can be very elongated and do not fit into UV space in some cases
* &lbrack;UV Unwrapping&rbrack; Degenerated faces or non-triangular mesh faces with small or overlaping edges may not get UV unwrapped

### 5.3.0 (2019.3.0)

*(Released: December 17, 2019*)Summary: **Major release with improvment of handpainting user experience, working with tablets, automatic UV unwrapping in beta (0.3.0) and diverse new content for handpainting**

**Added:**

* Integrate Automatic UV unwrapping 0.3.0 version in Substance Painter
* &lbrack;UV unwrapping&rbrack; Automatic UV unwrapping in Substance Painter when No UVs present or partial UVs
* &lbrack;UV unwrapping&rbrack; One Global setting to activate and deactivate it
* &lbrack;UV unwrapping&rbrack; Version reported in log file
* &lbrack;UV unwrapping&rbrack;&lbrack;UI&rbrack; Indicate UV Unwrapping progress
* &lbrack;UI&rbrack; New settings in contextual toolbar to select the brush preview: Full preview, Brush outline and Crosshair
* &lbrack;Tool&rbrack; New advanced blending mode in alpha section: Lighten (Maximum) in addition to Normal
* &lbrack;Layer Stack&rbrack; Gamma correction option per layer for alpha or mask (right click menu)
* &lbrack;Layer Stack&rbrack;&lbrack;UI&rbrack; Add 'i' icon when a layer alpha is gamma corrected
* &lbrack;Tablet&rbrack;&lbrack;Tool&rbrack; Expose minimum pressure for size and flow
* &lbrack;Tablet&rbrack;&lbrack;UI&rbrack; New setting in contextual toolbar to select the curve pressure: linear, easy-in, easy-in-out
* &lbrack;Tablet&rbrack;&lbrack;UX&rbrack; Add Ctrl+Alt+click to scroll
* Import Photoshop brush presets (ABR format)
* &lbrack;ABR&rbrack; Support Shape parameters
* &lbrack;ABR&rbrack; Support Shape dynamics parameters
* &lbrack;ABR&rbrack; Support Transfer parameters
* &lbrack;ABR&rbrack; Support Scattering parameters
* &lbrack;ABR&rbrack;&lbrack;Dynamic strokes&rbrack; Support Roundness and Flip
* &lbrack;ABR&rbrack;&lbrack;Shelf&rbrack; Expose the brush folder structure in the Filter Editor
* &lbrack;ABR&rbrack;&lbrack;Shelf&rbrack; Add Photoshop icon in thumbnails
* &lbrack;ABR&rbrack;&lbrack;Shelf&rbrack; Add list of unsupported parameters in the ABR detailed thumbnail
* &lbrack;Tool&rbrack;&lbrack;Dynamic Strokes&rbrack; New dynamic stroke setting to control how many random seed to generate
* &lbrack;Tool&rbrack;&lbrack;UI&rbrack; Add new distribution and axis settings for Scattering jitter
* &lbrack;Shortcut&rbrack; Add Ctrl+Shift+B to open the Baking window
* &lbrack;UI&rbrack;&lbrack;Menu&rbrack; Add entry in 'Edit' menu to open Baking window
* &lbrack;UI&rbrack;&lbrack;Settings&rbrack; Improvement alignment of the shortcuts list
* &lbrack;UI&rbrack; Replace pressure controls (size and flow) icons by on/off buttons
* &lbrack;Viewport&rbrack; Allow to focus 2D and 3D viewport separately
* Update to QT 5.12.5
* &lbrack;UI&rbrack; Indicate mesh loading progress
* &lbrack;Substance&rbrack; Add support for non-clamped and soft range with sliders
* &lbrack;Substance&rbrack; Increase Substance parameters precision up to 6 decimals
* &lbrack;Substance&rbrack; Take into account the step defined by a parameter
* &lbrack;Substance&rbrack; Optimize Dynamic Stroke generation with support of conditions in userdata
* &lbrack;Substance&rbrack; Allow to designate a graph output as a mask for all channels via userdata
* &lbrack;Content&rbrack; Update 'Mat' sample project with displacement friendly topology, new ID map and new cameras
* &lbrack;Content&rbrack; Integrate 3 new filters (MatFx): Comic Book, Watercolor, Oil Paint (inspired by Emrecan Cubukcu work)
* &lbrack;Content&rbrack; Integrate 102 Photoshop brush presets from Kyle T. Webster's packs
* &lbrack;Content&rbrack; Integrate 18 new brush presets: Paint Roller Arrow, Paint Roller Warning text, Charcoal Fine and more
* &lbrack;Content&rbrack; Integrate 9 new alphas: Brush Maker Paint Roller, Brush Maker Photoshop, Brush patterns and more
* &lbrack;Content&rbrack; Integrate 2 new tool presets: Gouache Dense and Gouache Faded
* &lbrack;Content&rbrack; Integrate 1 new generator : UV checker (highlight UV islands and seams)
* &lbrack;Content&rbrack; Integrate 2 new export preset: Keyshot 9+ and Spark AR Studio
* &lbrack;Content&rbrack; Integrate 1 new project template : Spark AR Studio (Facebook)

**Fixed:**

* &lbrack;Tablet&rbrack; Undoing stylus strokes (Ctrl+Z) lags more than undoing mouse strokes
* &lbrack;Tablet&rbrack; Start and end pressure not taken into account when drawing a straight line
* &lbrack;Tablet&rbrack; First stamp is drawn twice when using a straight line
* &lbrack;Tablet&rbrack; Improve support for Huion tablet shortcuts
* &lbrack;Tablet&rbrack; Improve support for Huion pen buttons
* &lbrack;Tablet&rbrack; Offset between the brush preview and the drawn stamp
* &lbrack;Tablet&rbrack; Shortcuts to modify brushes with pen lead to low performance in rare cases
* &lbrack;Tablet&rbrack; Lag when painting on a specific layer
* Blurry textures may occur in rare cases when switching viewport
* &lbrack;UI&rbrack;&lbrack;Substance&rbrack; Image inputs are not always displayed
* Clean does not remove presets from shelf which have been imported in a project
* &lbrack;Tool&rbrack;&lbrack;Dynamic Stroke&rbrack; Performance issue when tweaking Stamp Cycle Count
* Refresh issues while painting in 3D/2D viewport mode in rare cases
* Painting one very long stroke can lead to a freeze
* &lbrack;Tool&rbrack; Performance issue when painting with specific dynamic strokes
* &lbrack;UI&rbrack; Contextual toolbar still display brush properties when selecting a folder
* Symmetry axis values do not reset
* Import of EXR textures with floating point values are fully black
* Alt+click on a channel to isolate does not work for filter and generator
* &lbrack;Export&rbrack; Specific project crashes at export
* &lbrack;Substance&rbrack; Incorrect default value on dropdown if parameter is hidden by Visible If
* &lbrack;Shader&rbrack; Channels defined via Material Layering are not sorted the same way in the UI
* &lbrack;Shelf&rbrack; Presets metadata are not saved on disk

**Known Issues:**

* &lbrack;UV Unwrapping&rbrack; Processing high poly meshes can take a long time
* &lbrack;UV Unwrapping&rbrack; Vertices at the exact same coordinates are merged
* &lbrack;UV Unwrapping&rbrack; UV Generation may fail on some mesh parts in some rare cases
* &lbrack;UV Unwrapping&rbrack; Non uniform or highly distorted texel ratio in a single UV island in some cases
* &lbrack;UV Unwrapping&rbrack; Non uniform texel ratio between Texture Sets
* &lbrack;UV Unwrapping&rbrack; UV island generated can be very elongated and do not fit into UV space in some cases
* &lbrack;UV Unwrapping&rbrack; Degenerated faces or non-triangular mesh faces with small or overlaping edges may not get UV unwrapped
* Meetmat sample has some issues with imported cameras

### 5.2.3 (2019.2.3)

*(Released: October 23, 2019*)Summary: **Bugfix release**

**Added:**

* &lbrack;Texture Set List&rbrack; Add button to quickly enable/disable focus mode
* &lbrack;Log&rbrack; Add Windows 10 version number in the log file
* Update to latest version of Substance Engine
* &lbrack;MacOS&rbrack; Notarized the software to follow new MacOS Catalina distribution requirements

**Fixed:**

* &lbrack;Plugin&rbrack; Plugin Source does not work
* &lbrack;MacOS&rbrack;&lbrack;Shader&rbrack; Mac OS 10.14.5 and AMD: material layering does not work as intended

**Known Issues:**

* Alembic files with subdivisions cannot be imported
* Rare crashes when importing some Alembic files
* UI temporarily unresponsive when baking with DXR on Pascal GPUs

### 5.2.2 (2019.2.2)

*(Released: September 20, 2019*)Summary: **Bugfix release**

**Fixed:**

* Import resource by scripting can lead to a crash
* &lbrack;Plugin&rbrack; Downloading material from source can lead to a crash

**Known Issues:**

* Alembic files with subdivisions cannot be imported
* Rare crashes when importing some Alembic files
* UI temporarily unresponsive when baking with DXR on Pascal GPUs

### 5.2.1 (2019.2.1)

*(Released: September 17, 2019*)Summary: **Bugfix release**

**Fixed:**

* &lbrack;Mac&rbrack;&lbrack;USD&rbrack; Exported USDZ files from MacOS cannot be opened
* &lbrack;Texture Set&rbrack; Not possible to isolate a texture set with the ALT modifier
* &lbrack;Shelf&rbrack; Presets, Smart Materials and Smart Masks are always modified when exiting application
* &lbrack;Layer Stack&rbrack; Cannot select effect after deleting another effect
* Flickering when using a slider inside the tool properties panel
* Crash when exporting presets to shelf
* Crash when exporting a preset with insufficient space
* Crash when creating a preset with insufficient space

**Known Issues:**

* Alembic files with subdivisions cannot be imported
* Rare crashes when importing some Alembic files
* UI temporarily unresponsive when baking with DXR on Pascal GPUs

### 5.2.0 (2019.2.0)

*(Released: July 25, 2019*)Summary: **Major release with updates of the bakers in terms of performance and a new previsualization mode + new content**

**Added:**

* &lbrack;Bakers&rbrack; Added support for GPU Raytracing with DXR and OptiX (Ambient Occlusion, Thickness)
* &lbrack;Bakers&rbrack; Optimizations and accelerations for CPU Raytracing
* &lbrack;Bakers&rbrack;&lbrack;Vis mode&rbrack;&lbrack;UI&rbrack; New baking visualization mode in viewport
* &lbrack;Bakers&rbrack;&lbrack;Preferences&rbrack;&lbrack;UI&rbrack; New baking option for enabling-disabling GPU Raytracing
* &lbrack;Bakers&rbrack;&lbrack;UI&rbrack; Rework of the progress bar dialog
* &lbrack;Bakers&rbrack; Improvement of warning and error messages
* &lbrack;Bakers&rbrack; Allow more responsive cancelling of baking process
* &lbrack;Bakers&rbrack; Reopen bake window after clicking cancel
* &lbrack;Proj&rbrack;&lbrack;UX&rbrack; Usability improvement of rotation manipulator
* &lbrack;Settings&rbrack; Option to improve performance by reducing viewport resolution for HDPI screens
* &lbrack;Scripting&rbrack; Change texture set resolution
* &lbrack;Scripting&rbrack; Get selected texture set
* &lbrack;Scripting&rbrack; Allow the user to select a texture set
* &lbrack;Scripting&rbrack; Function to know when texture set selection has been changed
* &lbrack;Shelf&rbrack; Added 40 new smart materials
* &lbrack;Shelf&rbrack; Added 20 new smart masks

**Fixed:**

* &lbrack;Layer stack&rbrack; Freeze of UI when multi-selecting layers
* &lbrack;Layer stack&rbrack; Grouping lots of layers freezes the UI for longer than usual
* &lbrack;Layer stack&rbrack; A layer and an effect can be both selected at the same time in some cases
* Substance graphs used inside painting tools are not generated at the right resolution
* &lbrack;Baker&rbrack; "Bake All Texture Sets" button is not disabled when no bakers are selected
* &lbrack;MacOS&rbrack; Deactivate the warning message about tessellation
* Projection tool has no preview when used with a mask
* Crashes and corrupted projects when trying to save with insufficient disk space
* &lbrack;Shelf&rbrack; Crash when importing a resource on disk via shelf with insufficient space
* &lbrack;Shelf&rbrack; Crash when restoring session preset
* &lbrack;Shelf&rbrack; Importing a preset with a name that ends with a space leads to a crash
* &lbrack;Shelf&rbrack; Importing a resource with a prefix that ends with an empty space leads to a crash

**Known Issues:**

* Alembic files with subdivisions cannot be imported
* Rare crashes when importing some Alembic files
* UI temporarily unresponsive when baking with DXR on Pascal GPUs

### 5.1.3 (2019.1.3)

*(Released: July 01, 2019*)Summary: **Bugfix with 2 new features**

**Added:**

* Allow to specify the VRam budget with a command line (e.g. --vram-budget 4096)
* &lbrack;QML&rbrack; Expose wrapMode and elide properties of QML buttons and checkboxes

**Fixed:**

* "Follow path" does not work all the time
* Channel mapping doesn't work with SBSAR used in single channel slots
* &lbrack;Layer Stack&rbrack; Low performance when scrolling with hidden layers
* &lbrack;TextureSet&rbrack; Crash when clicking between masks
* &lbrack;SVT&rbrack; Displacement in not displayed properly and flickers in some cases
* &lbrack;Alembic&rbrack; Crash with mesh using point normals instead of vertex normals
* &lbrack;Alembic&rbrack;&lbrack;Log&rbrack; Report error in Log if Alembic file is not supported during import

**Known Issues:**

* Alembic files with subdivisions cannot be imported
* Rare crashes when importing some Alembic files

### 5.1.2 (2019.1.2)

*(Released: May 21, 2019*)Summary: **Hotfix**

**Fixed:**

* Crash when selecting two resources with an image input

### 5.1.1 (2019.1.1)

*(Released: May 20, 2019*)Summary: **Hotfix**

**Added:**

* Update to latest version of Substance Engine with last release of Substance Designer 2019.1

**Fixed:**

* &lbrack;Substance&rbrack; Visible If is not taken into account for Input Images
* &lbrack;SVT&rbrack;&lbrack;Engine&rbrack; Changing texture set resolution leads to a crash in some cases
* &lbrack;Engine&rbrack; Random black textures appear in some cases
* &lbrack;Layer Stack&rbrack;&lbrack;UI&rbrack; Toggling a mask with SHIFT can select multiple layers at the same time
* &lbrack;Layer Stack&rbrack; Opacity has no effect on Paint effect with Pass-Through blending mode
* &lbrack;Layer Stack&rbrack; Height To Normal filter input doesn't update properly with eraser brush stroke
* &lbrack;LayersStack&rbrack; Crash when undoing the drop of a smart mask
* Wireframe flickering with shadows and temporal anti aliasing activated
* &lbrack;Displacement&rbrack; Lag on AMD with some heavy meshes
* &lbrack;Windows&rbrack; Crash when opening some projects via the file explorer
* &lbrack;Histogram&rbrack; Crash when removing mask with anchor point in some cases
* Crash in preview generation in some rare cases
* &lbrack;Crash&rbrack; Can not reopen a project using too many clone and smudge tools
* No mesh displayed in material mode after saving in some cases
* &lbrack;Scripting&rbrack; alg.mapexport.documentStructure() returns incorrect values for folders

**Known Issues:**

* Double clicking texture set name will select it before entering renaming mode

### 5.1.0 (2019.1.0)

*(Released: April 23, 2019*)Summary: **Dynamic Stroke with dedicated new content, Displacement and Tessellation in real-time and Iray, Compare Mask effect, Radial symmetry, Planar and Spherical projection**

**Added:**

* &lbrack;Tool&rbrack; Dynamic stroke: Substance variation alongside a brush stroke
* &lbrack;Dynamic stroke&rbrack; Expose new stamp index parameter with options
* &lbrack;Dynamic stroke&rbrack; Take into account $time parameter
* &lbrack;Dynamic stroke&rbrack; Generate new $randomseed parameter per stroke and per stamp
* &lbrack;Dynamic stroke&rbrack; Start a dynamic stroke index from a random number
* &lbrack;Dynamic stroke&rbrack;&lbrack;Shelf&rbrack; Help finding a dynamic stroke resource with dedicated new icon
* Displacement and tessellation in real-time viewport
* Displacement and tessellation in Iray
* &lbrack;Shader settings&rbrack;&lbrack;UI&rbrack; New tab for controlling displacement and tessellation
* &lbrack;Layer stack&rbrack; New CompareMask effect: generate a mask by comparing two channels
* &lbrack;Layer stack&rbrack;&lbrack;UI&rbrack; New entry in right-click menu "Add mask with height combination" to insert a CompareMask effect
* &lbrack;Symmetry&rbrack; New symmetry mode: radial painting
* &lbrack;Symmetry settings&rbrack; Expand both sections "Settings" and "Display"
* &lbrack;Symmetry settings&rbrack;&lbrack;UI&rbrack; Preview for radial painting
* Expose two new projection modes: planar and spherical
* &lbrack;Proj&rbrack; New shape crop mode for all projections
* &lbrack;Proj&rbrack; Planar mode with new manipulator: Surface tool
* &lbrack;Proj&rbrack;&lbrack;Shortcut&rbrack; Shortcut SHIFT+W for Surface tool
* &lbrack;Proj&rbrack; Planar projection masking with depth culling and backface culling
* &lbrack;Manipulator&rbrack; Improvment of rotation manipulator on all three axes for triplanar
* &lbrack;Tool&rbrack;&lbrack;UX&rbrack; Alt-clicking on a channel focuses that channel (enables it or disables all others)
* &lbrack;Engine&rbrack; Update to latest version of Substance Engine
* &lbrack;Texture set&rbrack; Multiple selection and change resolution
* &lbrack;Texture set&rbrack; Quick activation and deactivation of the texture sets
* &lbrack;Texture set&rbrack; Combine solo and all options into a new menu
* &lbrack;Texture set&rbrack;&lbrack;Layer stack&rbrack; New icon for activation and deactivation
* &lbrack;Layer stack&rbrack;&lbrack;UX&rbrack; Insert effects above those already selected
* &lbrack;Layer stack&rbrack;&lbrack;UI&rbrack; Rework layer stack view selection style
* &lbrack;Layer Stack&rbrack; Blending mode for instanced layers is now in Pass Through mode by default
* &lbrack;Export&rbrack; Option to activate and deactivate dithering
* &lbrack;Plugin&rbrack; Support precision modifier for sliders (SHIFT)
* &lbrack;Plugin&rbrack;&lbrack;UI&rbrack; New icon for autosave
* &lbrack;Scripting&rbrack; List the contents of a folder
* &lbrack;Scripting&rbrack; Allow deletion of files
* &lbrack;Scripting&rbrack; Read all stack information including used resources
* &lbrack;Content&rbrack;&lbrack;Dynamic stroke&rbrack; New tools and brush presets
* &lbrack;Content&rbrack;&lbrack;Dynamic stroke&rbrack; Two new procedural gradients: Gradient Hue and Gradient Builder
* &lbrack;Content&rbrack; 11 new Filters: MatFx Peeling Paint, MatFx Water Drops and more
* &lbrack;Content&rbrack; 7 new generators: Auto Stitcher, UV Random Color, UV Texel Density and more
* &lbrack;Content&rbrack; 93 new alphas: new texts, arrows and various other shapes
* &lbrack;Content&rbrack; 2 new procedurals: Gradient Hue, Gradient Builder and more
* &lbrack;Content&rbrack; 21 new Tool and Brush presets for Dynamic Strokes : Pebbles, Footprints, Spray and more
* &lbrack;Content&rbrack; 2 New HDRis: Canopus Ground and Autumn Forest
* &lbrack;Content&rbrack; Update content with random seed curation in shelf
* &lbrack;Content&rbrack; New icon with exposed random seed parameter in shelf

**Fixed:**

* &lbrack;Layers stack&rbrack; Layer stack keeps dragging forever
* &lbrack;Mac&rbrack; "Show in Finder" can lead to freezing
* &lbrack;Scripting&rbrack; Settings saved via Custom UI are lost if shader file is moved
* &lbrack;Scripting&rbrack; API version number is incorrect and not up to date
* &lbrack;Effect&rbrack; Histogram content is not displayed correctly
* &lbrack;Effect&rbrack; Histogram effect does not update in some cases
* &lbrack;Shelf&rbrack; Stitches are not properly aligned on material "Plastic Fabric Pyramid"

**Known Issues:**

* Double clicking texture set name will select it before entering renaming mode
* &lbrack;Layer Stack&rbrack;&lbrack;UI&rbrack; Toggling a mask with SHIFT can select multiple layers at the same time

## Version 4

### 4.3.3 (2018.3.3)

*(Released: March 07, 2019*)Summary: **bugfix**

**Added:**

* &lbrack;Content&rbrack; Integrate new project template: "PBR - Metallic Roughness Alpha-blend"
* Linux Dynamic library search order changed to prioritize libraries in the installation directory ahead of what is installed on the system

**Fixed:**

* Mesh sometimes disappears from the 3D viewport (press F to reset camera)
* Update Substance Painter Sketchfab uploader with the new Sketchfab license types
* &lbrack;Import&rbrack;&lbrack;glTF&rbrack; Wrong handling input texture modulation as defined in glTF files
* &lbrack;Import&rbrack;&lbrack;glTF&rbrack; Ground plane is incorrectly displayed with glTF import in some cases
* &lbrack;Export&rbrack;&lbrack;USD&rbrack; Opacity does not work in Arkit
* &lbrack;Export&rbrack;&lbrack;USD&rbrack; USDz export crashes in some cases
* &lbrack;Export&rbrack;&lbrack;USD&rbrack; Export to USD without saving leads to crash
* &lbrack;Export&rbrack;&lbrack;USD&rbrack; Incorrect tiling mode for textures, subdivision mode for meshes and output types for shaders
* &lbrack;Export&rbrack;&lbrack;USD&rbrack; Sparse exports of only some texture sets with all geometry
* &lbrack;Instance&rbrack; Crash when trying to delete a broken instance layer
* &lbrack;Regression&rbrack;&lbrack;Export&rbrack; Some maps not exported in the chosen bit depth
* &lbrack;Linux&rbrack; Issue with library libtbb.so.2

**Known Issues:**

* Computation freeze in some cases on AMD VEGA GPUs
* Huion tablet issue with shortcuts on Windows OS

### 4.3.2 (2018.3.2)

*(Released: January 24, 2019*)Summary: **Hotfix with new features (USDZ export and Texture filtering in viewport)**

**Added:**

* &lbrack;Export&rbrack; Allow export to USDZ
* &lbrack;Viewport&rbrack; Allow to control the texture quality in the Display Settings
* &lbrack;Viewport&rbrack; Added mip bias setting in Display Settings
* &lbrack;Viewport&rbrack; Added anisotropic filtering in Display Settings
* &lbrack;plugins&rbrack; Update official plugins to use the style of Substance Painter 2018
* &lbrack;License&rbrack; Install license by default in a user folder

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
* &lbrack;Scripting&rbrack; File path creation not forced when saving a project
* &lbrack;Scripting&rbrack; Callback "onProjectAboutToSave()" doesn't work anymore
* Forum links broken in report bug window

**Known Issues:**

* Computation freeze in some cases on AMD VEGA GPUs
* Huion tablet issue with shortcuts on Windows OS

### 4.3.1 (2018.3.1)

*(Released: December 06, 2018*)Summary: **Hotfix**

**Added:**

* &lbrack;Symmetry&rbrack;&lbrack;Viewport&rbrack; Symmetry painting in the 2D view is back and now features a clone brush preview fixed

**Fixed:**

* &lbrack;Export&rbrack; 2D view export outputs a black texture in some cases
* &lbrack;Iray&rbrack; Normal information becomes incorrect in Iray after instancing a material layer
* Non square texture sets can lead in some cases to crash
* &lbrack;Undo&rbrack; Several Ctrl+Z can randomly lead in few cases to crash
* &lbrack;QML&rbrack; AlgScrollView can create a warning in the log in some cases (binding loops)

**Known Issues:**

* Computation freeze in some cases on AMD VEGA GPUs
* Huion tablet issue with shortcuts on Windows OS
* Anti-aliasing and shadows when active together may give unexpected results

### 4.3.0 (2018.3.0)

*(Released: November 20, 2018*)Summary: **Viewport upgrades, proper 2D view export, new UI helpers, an enhanced symmetry tool, new content and a huge boost in performance**

**Added:**

* &lbrack;Anti-aliasing&rbrack;&lbrack;Viewport&rbrack; New temporal anti-aliasing filtering for 3D viewport (via Display Settings)
* &lbrack;Export&rbrack; Export the content of the 2D viewport as a single texture
* &lbrack;Export&rbrack;&lbrack;Dithering&rbrack; Expose dithering at export
* &lbrack;Layer stack&rbrack; Colors on layers and folders
* &lbrack;Layer stack&rbrack; Quick activation and deactivation of multiple layers and effects
* &lbrack;Layer stack&rbrack; Easier navigation for blending modes with up down keys and mouse scroll
* &lbrack;Proj&rbrack;&lbrack;UI&rbrack; Additional rotation manipulator on all three axis for triplanar
* &lbrack;Proj&rbrack;&lbrack;Shorcuts&rbrack; - and + to change the UV projection manipulator size
* &lbrack;Shader&rbrack; Control coated layer parameters with channels in the PBR-coated shader
* &lbrack;Substance&rbrack; Expose new mesh-based texture inputs for filters and generators
* &lbrack;Symmetry&rbrack;&lbrack;Viewport&rbrack;&lbrack;UI&rbrack; Control symmetry offset with manipulators
* &lbrack;Symmetry&rbrack;&lbrack;Contextual toolbar&rbrack;&lbrack;UI&rbrack; New symmetry panel with options
* &lbrack;Symmetry&rbrack; New symmetry line intersection mode
* &lbrack;Symmetry&rbrack; New symmetry clone cursor
* &lbrack;Symmetry&rbrack;&lbrack;Shortcuts&rbrack; Q to hide and -, + to change size and shift to snap
* &lbrack;Log&rbrack; Improve error messages when unable to export textures
* &lbrack;Scripting&rbrack; Allow to change or update the resources in Display Settings
* &lbrack;Scripting&rbrack; Allow to create or remove channels in Texture Sets
* &lbrack;Content&rbrack;&lbrack;Shaders&rbrack; Add support for anisotropy with a dedicated shader (pbr-metal-rough-anisotropy-angle)
* &lbrack;Content&rbrack; Update of the preview sphere with anisotropy and modified angle
* &lbrack;Content&rbrack; Updated matFx shutline
* &lbrack;Content&rbrack; New Texturing.XYZ seamless face scan
* &lbrack;Content&rbrack; New anisotropic procedurals
* &lbrack;Content&rbrack; New filter: baked lighting environment
* &lbrack;Content&rbrack; New environment map: studio automotive neutral
* &lbrack;Content&rbrack; New project template: PBR - metallic roughness Anisotropy angle (with anisotropy channels)
* &lbrack;Content&rbrack; New project template: PBR - metallic roughness Coated
* &lbrack;SVT&rbrack;&lbrack;Engine&rbrack; Sparse Virtual Textures (SVT)
* &lbrack;SVT&rbrack;&lbrack;Preferences&rbrack;&lbrack;UI&rbrack; SVT hardware support acceleration option
* &lbrack;SVT&rbrack;&lbrack;Log&rbrack; Additional information for Sparse Virtual Texturing feature (e.g. size disk)
* &lbrack;SVT&rbrack;&lbrack;UI&rbrack; Message window at start if size on disk too low for the cache
* &lbrack;SVT&rbrack;&lbrack;Preferences&rbrack;&lbrack;UI&rbrack; Substance Painter global cache location
* &lbrack;SVT&rbrack; New environment variable to specify the path of the cache of Substance Painter
* &lbrack;SVT&rbrack; New environment variable to activate the SVT hardware support acceleration
* &lbrack;SVT&rbrack; Detect sparse support by hardware
* &lbrack;SVT&rbrack;&lbrack;Hardware Sparse&rbrack; Raise minimum driver version for Nvidia GPU
* &lbrack;SVT&rbrack;&lbrack;Shader&rbrack;&lbrack;Viewport&rbrack;&lbrack;UI&rbrack; Warn user if artefacts present with Sparse Virtual Texturing at project opening

**Fixed:**

* &lbrack;Color Picker&rbrack; Painting cursor appearing when trying to pick a color
* Crash by Selecting or Unselecting layers in a specific order can lead to crash
* Crash when pasting as an instance a layer with a mask
* &lbrack;User Channel&rbrack;&lbrack;Regression&rbrack; Crash when renaming user channel
* &lbrack;User Channel&rbrack; Grayed brush preview
* &lbrack;Alembic&rbrack; Only one texture set from several materials after import
* &lbrack;Engine&rbrack; Exported texture differs from viewport for brush stamps
* &lbrack;Engine&rbrack; Invert with a level effect does not fully affect a texture
* Material picker is applying a brush stroke while picking
* Switching resolution to 128x128px leads to a crash
* Mesh map links are not updated properly when rebaking or instancing layers
* &lbrack;Substance&rbrack; UserData ColorSpace does not work on Baked Mesh Normal requested as input
* MDL association mismatch when using multiple shaders instances
* &lbrack;Symmetry&rbrack;&lbrack;Fill Layer&rbrack; Symmetry plane and its manipulator active in Fill Layer
* &lbrack;Viewport&rbrack; Pivot point for translation not always updated after clicking
* &lbrack;UI&rbrack; Fixed icons and removal of placeholders for HDPI monitors

**Known Issues:**

* Computation freeze in some cases on AMD VEGA GPUs
* Huion tablet issue with shortcuts on Windows OS
* Anti-aliasing and shadows when active together may give unexpected results

### 4.2.3 (2018.2.3)

*(Released: September 25, 2018)*

**Fixed:**

* &lbrack;2D View&rbrack; 2D View is broken with some meshes when creating a new project
* &lbrack;Crash&rbrack; Switching from UV projection to tri-planar projection leads to a crash
* &lbrack;RayCollider&rbrack; Multiple crashes due to "RayCollider"
* &lbrack;Tool&rbrack; Switching layers lose the modified brush properties
* Brush settings are reseted when switching to the eraser

**Known Issues:**

* Computation freeze on AMD VEGA GPUs
* Huion tablet issue with shortcuts on Windows OS

### 4.2.2 (2018.2.2)

*(Released: September 11, 2018*)Summary: **Hotfix with content update, new scripting functionalities and being able to disable the auto update**

**Added:**

* &lbrack;Content&rbrack;&lbrack;Shelf&rbrack; Add a Skin shelf preset
* &lbrack;Content&rbrack;&lbrack;shelf&rbrack; Conversion of 19 skin normals into materials for subsurface scattering
* &lbrack;Scripting&rbrack; Create a project template from an open project
* &lbrack;Scripting&rbrack; Get/Set export settings of an opened project
* &lbrack;Updates&rbrack; Be able to disable the auto update pop-up from settings and environment variable
* &lbrack;Updates&rbrack; Have a not display until next version on the maintenance outdated pop-up

**Fixed:**

* &lbrack;Camera&rbrack; Wrong zoom by switching from orthographic to perspective
* &lbrack;Display&rbrack; Some maps are displayed in linear instead of sRGB
* &lbrack;Viewports&rbrack; Mesh focus does not behave properly
* &lbrack;2D View&rbrack; Project with broken camera has disappearing UVs Shells
* &lbrack;SSS&rbrack;&lbrack;Tooltip&rbrack; subsurface scattering tooltips appear in the log
* Some projects cannot be opened in 2018.2 and error message can't save a null substance package
* &lbrack;Mask&rbrack; Paint tool color can be stuck in some cases when working in a mask
* &lbrack;Material&rbrack; Maps not appearing in specific situations
* &lbrack;Proj&rbrack;&lbrack;Tools&rbrack; Manipulator active with a generator
* &lbrack;Substance&rbrack; Missing Substance groups of parameters
* &lbrack;Scripting&rbrack; Incorrect software name in documentation
* &lbrack;UDIMs&rbrack; No information in log about UVs shells on multiple UVs tiles

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

*(Released: August 02, 2018*)Summary: **Summer release, subsurface scattering Support, projection and fill improvements, camera import and selection, Alembic and glTF support, drag and drop on ID map, improved Substance format support and new content**

**Added:**

* &lbrack;SSS&rbrack;&lbrack;Viewport&rbrack;&lbrack;Iray&rbrack; Generic subsurface scattering
* &lbrack;SSS&rbrack; Sync MDL and subsurface scattering parameters
* &lbrack;SSS&rbrack; Added a new grayscale channel named Scattering
* &lbrack;SSS&rbrack;&lbrack;Shader Settings&rbrack; Scattering type parameter for subsurface scattering (skin or translucent)
* &lbrack;SSS&rbrack;&lbrack;Shader Settings&rbrack; Scattering scale parameter for subsurface scattering
* &lbrack;SSS&rbrack;&lbrack;Shader Settings&rbrack; Scattering color parameter for subsurface scattering
* &lbrack;SSS&rbrack;&lbrack;Display Settings&rbrack; Scattering Sample count for subsurface scattering
* &lbrack;Shader&rbrack;&lbrack;Iray&rbrack; Integrate subsurface scattering MDL for Iray
* &lbrack;Shader&rbrack; Shader update via the resource updater
* &lbrack;Shader&rbrack; Update change log API and documentation
* &lbrack;Tool Properties&rbrack;&lbrack;Proj&rbrack; New parameters for the triplanar projection
* &lbrack;Viewport&rbrack;&lbrack;Proj&rbrack; Control Fill Layer properties in 3D view directly with manipulators (triplanar projection)
* &lbrack;Shortcuts&rbrack;&lbrack;Proj&rbrack; New shortcuts Q, W, E, R, T for triplanar projection manipulators
* &lbrack;Viewport&rbrack;&lbrack;Proj&rbrack; Control Fill Layer properties in 2D view directly with manipulators (UV projection)
* &lbrack;Shortcuts&rbrack;&lbrack;Proj&rbrack; New shortcut Q for UV projection manipulators
* &lbrack;Contextual Toolbar&rbrack;&lbrack;Proj&rbrack; Control triplanar projection manipulators
* &lbrack;Contextual Toolbar&rbrack;&lbrack;Proj&rbrack; Control UV projection manipulators
* &lbrack;Tool Properties&rbrack; Disable texture tiling with projection and Stencil tool
* &lbrack;Stencil&rbrack; Use non-squared images with the projection tool/stencil
* &lbrack;Stencil&rbrack; Allow control of tiling mode in Properties window
* &lbrack;Stencil&rbrack; Zoom is not centered on a non-tiling stencil
* &lbrack;Cameras&rbrack; Import cameras from Maya, Max, Blender, Modo, DAE
* &lbrack;Cameras&rbrack;&lbrack;Viewport&rbrack; Select and control imported cameras in viewport
* &lbrack;Cameras&rbrack;&lbrack;Iray&rbrack; Select and control imported cameras in Iray
* &lbrack;Cameras&rbrack;&lbrack;UI&rbrack;&lbrack;New project&rbrack;&lbrack;Project configuration&rbrack; Import cameras is checked by default
* &lbrack;Cameras&rbrack;&lbrack;Shortcuts&rbrack; Add shortcuts to switch between cameras
* &lbrack;Cameras&rbrack;&lbrack;Viewport&rbrack; Add frame in viewport
* &lbrack;Cameras&rbrack;&lbrack;Viewport Settings&rbrack; Control of frame opacity
* &lbrack;Cameras&rbrack;&lbrack;Camera Settings&rbrack; Maximum focal length at 500mm
* &lbrack;Cameras&rbrack;&lbrack;Camera Settings&rbrack; Expose ratio
* &lbrack;Cameras&rbrack;&lbrack;Camera Settings&rbrack; Add a lock option
* &lbrack;Cameras&rbrack;&lbrack;Camera Settings&rbrack; Add a restore option
* &lbrack;Cameras&rbrack;&lbrack;Camera Settings&rbrack; Add focus distance attribute
* &lbrack;glTF&rbrack; Import of a glTF file
* &lbrack;glTF&rbrack; Import ambient occlusion map
* &lbrack;Alembic&rbrack; Import Alembic 1 frame with static geometry
* &lbrack;Shelf&rbrack; Drag and drop materials directly onto the mesh using ID maps with a modifier (CTRL/Command)
* &lbrack;Layer Stack&rbrack; Automatic ID mask creation with drag and drop of materials on mesh with ID maps
* &lbrack;Layer Stack&rbrack; Automatic scroll of layers with drag and drop across the layer stack
* &lbrack;UI&rbrack;&lbrack;Tool Properties&rbrack; Expose Substance's preset
* &lbrack;UI&rbrack;&lbrack;Help menu&rbrack; Improvement of the Help menu
* &lbrack;UI&rbrack;&lbrack;New Project&rbrack;&lbrack;Project Configuration&rbrack; Reorganization of the window
* &lbrack;UI&rbrack;&lbrack;New Project&rbrack;&lbrack;Project Configuration&rbrack; Replace Mesh term by File
* &lbrack;UI&rbrack;&lbrack;Substance&rbrack; Display Substance attributes in UI
* &lbrack;Shortcuts&rbrack; F4 switches between 2D and 3D view
* &lbrack;Shortcuts&rbrack; New shortcuts for toggle stencil N and quick mask U
* &lbrack;Substance integration&rbrack; Take into account 'visible if' statements in the Substance parameters
* &lbrack;Viewport&rbrack; Shadows not forced to be computed after camera move
* &lbrack;Content&rbrack; Update MeetMat with imported cameras
* &lbrack;Content&rbrack; Add a sample with subsurface scattering enabled - JadeToad
* &lbrack;Content&rbrack; Add a new PBR project template with subsurface scattering enabled
* &lbrack;Content&rbrack; Updated export presets to add new Scattering channel
* &lbrack;Content&rbrack;&lbrack;Shelf&rbrack; Added subsurface scattering support for: pbr-metal-rough, pbr-metal-rough-alpha-test, pbr-coated, pbr-spec-gloss
* &lbrack;Content&rbrack;&lbrack;Shelf&rbrack; Added Scattering channel to 5 smart materials (marbles and skins)
* &lbrack;Content&rbrack;&lbrack;Shelf&rbrack; 1 new jade Material
* &lbrack;Content&rbrack;&lbrack;Shelf&rbrack; 1 new wax Material

**Fixed:**

* &lbrack;CMD&rbrack; Different results using same command line with different versions
* &lbrack;TDR&rbrack; If TdrLevel is set up you don't have any errors in your log
* &lbrack;Baker&rbrack; Ambient occlusion map is flipped
* &lbrack;ID Map&rbrack; Crashing when picking outside of 0-1 range
* &lbrack;Iray&rbrack; Crash when switching texture sets and going back to Paint mode
* &lbrack;Viewport&rbrack; Sync drop areas between viewports for drag and drop
* &lbrack;Engine&rbrack; Moire artifact when tiling fill layers or painting small brush
* &lbrack;License&rbrack; License service bad software version check
* &lbrack;License&rbrack; Rework the way we handle authentication
* &lbrack;API&rbrack; Call the onNewProjectCreated scripting API event even when creating with a template
* &lbrack;Shader&rbrack; Compiled shader is not loaded from cache when shader file doesn't compile
* &lbrack;Shelf&rbrack; Exporting HDR file from the shelf will output a file with clamped values
* &lbrack;Export&rbrack; EXR export clamps RGB color values between 0-1
* &lbrack;Content&rbrack; Procedural noise 3D Perlin Noise Fractal is pixelated

**Known Issues:**

* Computation freeze on AMD VEGA GPUs
* Huion tablet issue with shortcuts on Windows OS

### 4.1.3 (2018.1.3)

*(Released: June 28, 2018)*

**Added:**

* &lbrack;Preferences&rbrack; Propose to save project when Painter restarts

**Fixed:**

* &lbrack;Plugin&rbrack; Search Substance Source does not work
* &lbrack;Smart Materials&rbrack; Importing Smart Materials leads to a crash in some cases
* &lbrack;Smart Materials&rbrack; Deleting Smart Materials leads to a crash in some cases
* &lbrack;Save&rbrack; Saving leads to a crash in some rare cases
* &lbrack;Shelf&rbrack; Invert does not work on Cells 2 and Cells 3
* &lbrack;Shelf&rbrack; Typo in some Alphas
* &lbrack;Shelf&rbrack; Some substance materials do not render properly

**Known Issues:**

* Computation freeze on AMD VEGA GPUs

### 4.1.2 (2018.1.2)

*(Released: June 12, 2018*)Summary: **Improved Baking Speed, Improved Save System, Updated Sliders, Updated Plugin API, Chinese Translation, Improved Padding now Optional**

**Added:**

* &lbrack;Bakers&rbrack; Performance improvement with new baker version
* Force display dialog with incompatible GPU
* &lbrack;Save&rbrack; Expose new compact project functionality (full/compact save mode)
* &lbrack;Save&rbrack; Inform user in case of saving error
* &lbrack;Clean&rbrack; Next save in full/compact mode
* &lbrack;Sliders&rbrack; Improvement of the precision of the color/grayscale bars and sliders
* &lbrack;Sliders&rbrack; Addition of Up/Down arrow controls
* &lbrack;Sliders&rbrack; Same detection zone for color and grayscale bar sliders
* &lbrack;Plugin&rbrack; Autosave always in incremental mode
* &lbrack;Plugin&rbrack; Option to switch plugins to new interface style
* &lbrack;Language&rbrack; Add Chinese translation
* &lbrack;Padding&rbrack; Option to switch between UV and 3D space neighbor padding per Texture Set in Texture Set Settings
* &lbrack;Script&rbrack; Expose save mode: full/compact or incremental
* &lbrack;Script&rbrack; Update scripting/QML documentation
* &lbrack;Log&rbrack; Indicate save mode in log (full/compact or incremental)

**Fixed:**

* &lbrack;Tool&rbrack; Channel slot transforms into a material slot on single-channel fills
* Crash when loading a mesh (FBX) with some faces not assigned by a material
* Crash in Iray with NVIDIA GRID 5.2 on virtual machine
* Crash when undoing a material preset deletion
* Crash when loading some projects
* &lbrack;Command line&rbrack; New command line for UDIMs meshes split-by-udim
* &lbrack;Toolbar&rbrack; Shrinking of the toolbar
* &lbrack;Instancing&rbrack; Cannot instantiate bitmaps across multiple texture sets
* &lbrack;Viewport&rbrack; Refresh is not complete when painting on mesh with tiled UVs
* &lbrack;Iray&rbrack; Normal Map is applied twice for dielectrics
* &lbrack;Shelf&rbrack; Typos in some Substance parameters (alphas, procedurals and matfx)
* &lbrack;Shelf&rbrack; Typo for the bitmap "Authorized Personnel Only"
* &lbrack;Script&rbrack; Function alg.shaders.materials() does not work anymore

**Known Issues:**

* Computation freeze on AMD VEGA GPUs

### 4.1.1 (2018.1.1)

*(Released: April 03, 2018)*

**Fixed:**

* &lbrack;Tablet&rbrack; Issue when changing default interaction choices
* &lbrack;Bakers&rbrack; Crash with Assimp library
* &lbrack;Bakers&rbrack; Regression on performance with A.O. map
* &lbrack;Iray&rbrack; Lens Distortion is not applied to the Alpha channel
* &lbrack;Drivers&rbrack; Update of minimum drivers requirements
* &lbrack;3Dview&rbrack; Normals not correctly generated on UDIM meshes without normals information
* &lbrack;Intel&rbrack; Crash with Substance Painter 2018.1.0
* &lbrack;Intel&rbrack;&lbrack;Viewport&rbrack; Issue with padding (black artefacts)

**Known Issues:**

* Computation freeze on AMD VEGA GPUs

### 4.1.0 (2018.1.0)

*(Released: March 15, 2018)*

**Added:**

* New overall style (icons, color, behavior)
* New default layout
* &lbrack;Tablet&rbrack; User experience enhancement while painting
* &lbrack;Main menu&rbrack; Sort native items in views and toolbars first
* &lbrack;Main menu&rbrack; Move quick mask actions in viewport section
* &lbrack;Main menu&rbrack; Move right-click actions into viewport section
* &lbrack;Main menu&rbrack; Rename "View" menu as "Window"
* &lbrack;Quick menu&rbrack; New tool properties by right click in viewport
* &lbrack;Dock widget&rbrack; New dock toolbar for quick reduce/recall
* &lbrack;Display settings&rbrack; Camera and viewer settings window merged
* &lbrack;Layer stack&rbrack; Contextual right click menu
* &lbrack;Layer stack&rbrack; Drag and drop to move any effect within the same layer
* &lbrack;Toolbar&rbrack; Reorganization of toolbar and new contextual toolbar
* &lbrack;Tools toolbar&rbrack; Split clone tool into two separate tools
* &lbrack;Tools properties&rbrack; Lighter background grayscale value in the preview
* &lbrack;Tools properties&rbrack; Organization in tabs (fill and tools)
* &lbrack;Tool&rbrack; Painting result matches the stencil
* &lbrack;Viewport&rbrack; New cursor for fill layer
* &lbrack;Viewport&rbrack; Smoother navigation and painting (higher frame rate)
* &lbrack;Viewport&rbrack; Material/Channel/Map selection combobox in viewport
* &lbrack;Viewport&rbrack; Reduce flickering while rotating (shadow on)
* &lbrack;Shelf&rbrack; Display materials by default when opening Painter
* &lbrack;Shelf&rbrack; Loading time improvement of Substance textures and materials (2 to 6 times faster)
* &lbrack;Shelf&rbrack; Reorganize materials folders to fit Substance Source structure
* &lbrack;Shelf&rbrack; Drag and drop materials directly on the mesh in the viewport
* &lbrack;Shelf&rbrack; New 3D Noises (Perlin, Perlin Fractal, Simplex and Worley)
* &lbrack;Shelf&rbrack; New 3D Linear Gradient mask generator using mesh position
* &lbrack;Shelf&rbrack; Updated base Noises to support non square expansion
* &lbrack;Shelf&rbrack; Added new template and export preset for Lens Studio (Snap application)
* &lbrack;Shelf&rbrack; Updated Smart Materials and Smart Masks to use latest version of the Mask Editor (micro details)
* &lbrack;Shelf&rbrack; New sample project "TilingMaterial" to create seamless tiling materials
* &lbrack;Shelf&rbrack; New brush presets (Calligraphy, Wet, Hatching and so on)
* &lbrack;Sliders&rbrack; New sliders and grayscale/color bars style and behavior
* &lbrack;Bakers&rbrack; Allow use of full scene bounding box to compute the position map
* &lbrack;Shader&rbrack; Remove height force parameter from the default shader parameters
* &lbrack;Engine&rbrack; Substance engine updated
* &lbrack;Engine&rbrack; No or less discontinuities across UV chunks
* &lbrack;Plugins&rbrack; Import materials downloaded from Substance Source more quickly
* &lbrack;Plugins&rbrack; Update all plugins to match new overall style
* &lbrack;Preferences&rbrack; Preview background color changes automatically
* &lbrack;Clean&rbrack; Reduced risk of project corruption
* &lbrack;Open&rbrack; Opening project time improvement
* &lbrack;New project&rbrack; New project - mesh update time improvement
* &lbrack;Save&rbrack; Saving Project time improvement
* &lbrack;Log&rbrack; License type reported in log
* &lbrack;TextureSet&rbrack; Rename "Bake Textures" button as "Bake Mesh Maps"
* Rename "Additional maps" as "Mesh maps"

**Fixed:**

* &lbrack;Viewport&rbrack; Bad performances with meshes containing a lot of sub-objects
* &lbrack;Tools properties&rbrack; Channel disabled when dragging and dropping an image into the material slot
* &lbrack;Tools properties&rbrack; Brush preview is broken with smudge and clone tools
* &lbrack;Texture set&rbrack; Channels order is wrong when using templates
* &lbrack;Shelf&rbrack; Missing icon for Grayscale Conversion generator
* &lbrack;Shelf&rbrack; Sign Circle Number alpha is broken (missing font)
* Incorrect detection of integrated GPUs at launch
* &lbrack;Crash&rbrack; Drag-and-droping an imported ressource named with a # character
* &lbrack;Engine&rbrack; Vram detection issue on integrated GPU
* &lbrack;Engine&rbrack; Fixed numerous crashes in Substance Engine Linker
* &lbrack;Engine&rbrack; Square artefacts when changing resolution
* &lbrack;Post Effects&rbrack; Interface resize is slow when post effects are on
* &lbrack;Bakers&rbrack; Scene unit is not correctly respected for Ray Distance values
* &lbrack;Bakers&rbrack; AO from Mesh Occluder distance is clamped to 1 no matter the input value
* &lbrack;Bakers&rbrack; Match by name ignores some meshes with specific names
* &lbrack;Bakers&rbrack; Color from mesh Polygroup and Submesh ID setting always return a black image
* &lbrack;Bakers&rbrack; ID Baking fails with binary FBX meshes from Blender
* &lbrack;Shader&rbrack; Noise in the 2D View with dota-2 and non-pbr-spec-gloss
* &lbrack;Linux&rbrack; Only one CPU thread is used when baking
* &lbrack;MacOS&rbrack; Crash with brush cursor moving over the viewport

**Known Issues:**

* Computation freeze on AMD VEGA GPUs
* Distorsion post process not taken into account while exporting in IRay (alpha)

## Version 3

### 3.4.2 (2017.4.2)

*(Released: January 24, 2018)*

**Added:**

* &lbrack;Export&rbrack; Get the status of an export with step progress
* &lbrack;Export&rbrack; Allow cancelling an export
* &lbrack;Export&rbrack; Export textures to Sketchfab without loosing normal map quality
* &lbrack;Export&rbrack; Export in glTF binary format (glb)
* &lbrack;Export&rbrack; Allow resizing columns in configuration tab of the export window
* &lbrack;Shader&rbrack; Add a changelog for the shader API
* &lbrack;Scripting&rbrack; Add Before and After callback functions when exporting textures
* &lbrack;Iray&rbrack; Upgrade to SDK 2017.1 (support of Volta GPUs)

**Fixed:**

* Crash when quitting the application before the main window is displayed
* &lbrack;MAC&rbrack; Crash when loading grayscale maps with IRAY
* &lbrack;MAC&rbrack; VRAM detection is not correct with the new High Sierra OS
* &lbrack;Plugin&rbrack; Downloading assets from Substance Source does not work anymore
* &lbrack;Scripting&rbrack; Incorrect minimum plugin version detection
* &lbrack;Export&rbrack; Fail to save export preset after exporting textures
* &lbrack;Instancing&rbrack; Issue on generators instantiated in a TextureSet with no Additional Maps
* &lbrack;Viewport&rbrack; Dithering does not work with resolution above 4k
* &lbrack;Viewport&rbrack; 2D View material display is covered with noise
* &lbrack;Shelf&rbrack; Improve loading time for shelf presets
* &lbrack;Engine&rbrack; Incorrect blending when painting under color selection

### 3.4.1 (2017.4.1)

*(Released: December 15, 2017)*

**Added:**

* &lbrack;Scripting&rbrack; Export mesh through the scripting API
* &lbrack;Import&rbrack; Disable import of unsupported mesh file format (allow only obj, fbx, dae, ply)
* &lbrack;Log&rbrack; Indicate more precisely the TDR issue in the log file

**Fixed:**

* Crash if application is closed before resources crawling has finished
* Crash when opening projects with Smudge/Clone tool
* Crash when using redo after an undo of a Shader change in Viewer Settings
* &lbrack;Engine&rbrack; Texturing differs between Painter 2017.2 and 2017.4
* &lbrack;Viewport&rbrack; Picking on an ID map from an instance samples the wrong color
* &lbrack;Export&rbrack; Crash when exporting an invalid normal or occlusion texture
* &lbrack;Export&rbrack; PSD files have their groups locked when opened in Photoshop CS6
* &lbrack;Plugin&rbrack; Photoshop plugin ignores channel selection and always export everything
* &lbrack;Layers&rbrack; Anchors break when copy/pasted across Texture Sets
* &lbrack;Layers&rbrack; Some anchor's references cannot be restored if broken
* &lbrack;Shader&rbrack; pbr-coated secondary roughness parameter is broken
* &lbrack;Steam&rbrack; Version checker pop-up shouldn't be visible at launch

**Known Issues:**

* &lbrack;AMD&rbrack; Crashes/Freezes when trying to paint on a mesh. Can be fixed with a GPU Driver update.

### 3.4.0 (2017.4.0)

*(Released: November 23, 2017)*

**Added:**

* &lbrack;Instancing&rbrack; Allow to instantiate parameters across layers
* &lbrack;Instancing&rbrack; Allow to jump between a source layer and an instance
* &lbrack;Instancing&rbrack; Add a "instantiate across texture sets" action
* &lbrack;Instancing&rbrack; Indicate in the layer stack re-entrant instances (cycles)
* &lbrack;Instancing&rbrack; Delete instances when a source is removed
* &lbrack;Instancing&rbrack; Don't allow Anchor's references from outside an instanced folder
* &lbrack;UI&rbrack; Move the Undo Stack into its own window named "History"
* &lbrack;Plugin&rbrack; Integrate DCC live-link plugin
* &lbrack;Engine&rbrack; Improve painting performances with Sparse painting
* &lbrack;Export&rbrack; Add draft and re-export options to Sketchfab exporter
* &lbrack;Shelf&rbrack; Add "flip" control for Font substances
* &lbrack;Shelf&rbrack; Add 20 new procedurals materials
* &lbrack;Shelf&rbrack; Add 40 new grunges maps (bitmap based and procedural)
* &lbrack;Viewport&rbrack; Enable brush preview collisions on other visible texture sets
* Update AMD GPU drivers minimum requirements

**Fixed:**

* Crash When computing Substances at too big resolutions
* Crash when painting heavily with particles
* &lbrack;Viewport&rbrack; Incorrect specular reflection in the 2D view with specific meshes
* &lbrack;UI&rbrack; Some unwanted actions appear into the History window

**Known Issues:**

* &lbrack;Layers&rbrack; Some anchor's references cannot be restored if broken
* Crash when using redo after an undo of a Shader change in Viewer Settings

### 3.3.3 (2017.3.3)

*(Released: December 01, 2017)*

**Fixed:**

* &lbrack;Steam&rbrack; Version checker pop-up shouldn't be visible at launch
* &lbrack;Export&rbrack; PSD files have their groups locked when opened in Photoshop CS6

### 3.3.2 (2017.3.2)

*(Released: November 20, 2017)*

**Added:**

* &lbrack;UI&rbrack; Improve new version dialog and add changelog
* &lbrack;UI&rbrack; Indicate if maintenance is expired in new version dialog
* &lbrack;License&rbrack; Update license system to handle Maintenance dates
* &lbrack;Export&rbrack; Rename Adobe Standard Material to Adobe Dimension

**Fixed:**

* &lbrack;Mac&rbrack; Painting leads to black squares and texture corruptions
* &lbrack;Engine&rbrack; Cache can sometimes disappear in the Viewport
* &lbrack;Engine&rbrack; Blocky artifacts appear when memory compression trigger
* &lbrack;Baking&rbrack; Strange error messages when baking specific meshes
* &lbrack;Export&rbrack; PSD are incorrectly written and are not recognized properly by Photoshop
* &lbrack;Layers&rbrack; It shouldn't be possible to copy/paste layer across multiple projects
* &lbrack;Substance&rbrack; UserData color space for Normal input is flipped in some cases
* &lbrack;Shelf&rbrack; Micro-normal in generators outputs inverted curvature
* &lbrack;Shelf&rbrack; HSL filter also affect alpha channel
* &lbrack;Linux&rbrack; Installation on Centos fails because of missing dependencies
* Installer doesn't remove all resources from previous install in certain cases

### 3.3.1 (2017.3.1)

*(Released: October 26, 2017)*

**Added:**

* &lbrack;Export&rbrack; Allow to export the mesh from a project
* &lbrack;Shelf&rbrack; Remove "Sub-Shelf" from the tabs titles
* Save post-process settings in templates
* Make the TDR message more understandable
* Improve Settings window to report errors

**Fixed:**

* Crash when deleting several sub-shelves
* Crash when switching from a level to something else during an engine computation
* &lbrack;Mac&rbrack; Crash on Intel GPU during engine computations
* &lbrack;Mac&rbrack;&lbrack;Viewport&rbrack; Bad performances when dithering is enabled
* &lbrack;Mac&rbrack; MacOS 10.13 is recognized as "Unknown version" in the log file
* &lbrack;Baker&rbrack; Baking with a cage doesn't work anymore
* &lbrack;Layers&rbrack; Ctrl + C shortcut (copy action) doesn't work anymore
* &lbrack;Layers&rbrack; Pasting layers doesn't refresh UI with anchor's references
* &lbrack;Anchor&rbrack; Duplicate or Copy/Paste Layer with References breaks links
* &lbrack;Export&rbrack; 8K export can crash or deadlock application in some cases
* &lbrack;Export&rbrack; Multiple issues in generated glTF file format
* &lbrack;Import&rbrack; Re-importing a mesh with the same filename doesn't work anymore
* &lbrack;Plugin&rbrack; Auto-save window always appear on top of everything
* &lbrack;UI&rbrack; Infinite loop when you Press "Escape" on the TDR Dialog
* &lbrack;UI&rbrack; Reset UI display a second title bar on the shelf window

### 3.3.0 (2017.3.0)

*(Released: September 28, 2017)*

**Added:**

* &lbrack;Export&rbrack; Allow to export mesh and textures for Adobe Project Felix
* &lbrack;Export&rbrack; Allow to export into glTF file format
* &lbrack;Engine&rbrack; Optimize textures size in VRAM by using block compression
* &lbrack;Viewport&rbrack; Be able to drag and drop a mesh or project in the viewport
* &lbrack;UI&rbrack; Improve warning message about TDR
* &lbrack;UI&rbrack; Log should be displayed only upon request
* &lbrack;UI&rbrack; Allow to clear the content of the log window
* &lbrack;UI&rbrack; Display warnings and errors in the status bar
* &lbrack;UI&rbrack; Display Tabs on top as in web browsers
* &lbrack;UI&rbrack; Improve "not paintable" context and messages
* &lbrack;UI&rbrack; Add a "save as copy" action in the file menu
* &lbrack;Layer&rbrack; Set default tiling setting to 1 by default
* &lbrack;Shelf&rbrack; Improved gradient filter to support 10 dynamic colors
* &lbrack;Shelf&rbrack; Add a space in the default query of the mini-shelf
* &lbrack;Shelf&rbrack; Add a "Open in explorer" action for local resources in the shelf
* &lbrack;Shelf&rbrack; Add template and shader for Adobe Material Standard (Project Felix)
* &lbrack;Shelf&rbrack; Increase max tiling to 128 in Material Layering shaders
* &lbrack;Shelf&rbrack; Added sobel curvature for micro-details of Mask Generators
* &lbrack;Plugin&rbrack; Add autosave plugin with customizable time interval
* &lbrack;Scripting&rbrack; Add a "save as copy" function

**Fixed:**

* &lbrack;UI&rbrack; Layout is broken at the first launch
* &lbrack;Export&rbrack; PSD generated at export has format errors
* &lbrack;Export&rbrack; EXR always exports 8 bits height map
* &lbrack;Export&rbrack; Crash when exporting corrupted Additional maps
* &lbrack;Import&rbrack; Hard edges are not preserved on low poly meshes in some cases
* &lbrack;Import&rbrack; Improved error messages when importing meshes with issues
* &lbrack;Bakers&rbrack; ID Map Baking fail with Match By Name enabled
* &lbrack;Viewport&rbrack; Tangent space is not synched with bakers
* &lbrack;Effect&rbrack; Moving back a layer doesn't restore an anchor's reference
* &lbrack;Effect&rbrack; Refresh issue when creating a link in between two Masks with anchors
* &lbrack;Effect&rbrack; Masks anchors above mask shouldn't be listed
* &lbrack;Effect&rbrack; Extract Alpha setting from Anchors doesn't work
* &lbrack;Engine&rbrack; Mask inverts itself after first brush stroke
* &lbrack;Engine&rbrack; Crash when switching Texture Set on specific project
* &lbrack;Shelf&rbrack; Crash when deleting a preset which is in a project
* &lbrack;Shelf&rbrack; Typo in advanced Tri-Planar filter
* &lbrack;Shelf&rbrack; MG Mask Builder AO Noise Scale doesn't work properly
* &lbrack;Shelf&rbrack; MG Mask Builder has inverted curvature parameters
* &lbrack;Shelf&rbrack; Imported alphas generate a material sphere preview instead of a flat one

### 3.2.0 (2017.2.0)

*(Released: July 27, 2017)*

**Added:**

* Anchor Points - Layer and Mask referencing system
* &lbrack;Layers&rbrack; Ability to rename Fill and Paint Effects
* &lbrack;Plugin&rbrack; Updated Substance Source plugin
* &lbrack;Scripting&rbrack; Allow to query Texture Set Resolution
* &lbrack;Scripting&rbrack; Allow to get the status of the Painting engine
* &lbrack;Performance&rbrack; Improved project loading and brush stamping optimizations

**Fixed:**

* &lbrack;Tool&rbrack; Performance issues when tweaking material parameters
* &lbrack;Engine&rbrack; Disappearing brush strokes when changing resolution (4K&gt;2K)
* &lbrack;3D View&rbrack; Tangent space is not synched with bakers
* &lbrack;Shelf&rbrack; Shelf path in the user documents isn't created automatically
* &lbrack;Shelf&rbrack; Make presets compatible with previous versions after an update
* &lbrack;Shader&rbrack; Non-PBR shader doesn't work anymore
* &lbrack;Bakers&rbrack; ID Map Baking fail with Match By Name enabled
* &lbrack;Sample&rbrack; Meet Mat sample project Texture Set names are incorrect
* Saving a project before creating a template returns write permission errors

### 3.1.0 (2017.1.0)

*(Released: June 20, 2017)*

**Added:**

* &lbrack;Plugin&rbrack; New Substance Source plugin (allow to download assets in the shelf)
* &lbrack;Shelf&rbrack; 4 New Fonts (Japanese + Simplified Chinese, Typewriter, Segment)
* &lbrack;Shelf&rbrack; 230 New Alphas (Mix of patterns, brushes and fingerprint scans)
* &lbrack;Shelf&rbrack; 50 New Procedurals (Fabric patterns of medieval and contemporary clothing)
* &lbrack;Shelf&rbrack; 2 New environment maps (Mondarrain and Villa Nova Street)
* &lbrack;Shelf&rbrack; 9 New filters (MatFx Detail Edge Wear, Clamp, HBAO, etc.)
* &lbrack;Shelf&rbrack; Improved default Panorama environment map
* &lbrack;Shelf&rbrack; New Arnold 5 export presets
* &lbrack;Scripting&rbrack; Allow to import resource into the Shelf

**Known Issues:**

* &lbrack;Export&rbrack; Editing an export preset is very slow

## Version 2

### 2.6.2

*(Released: October 20, 2017)*

**Added:**

* &lbrack;Texture Set&rbrack; Allow to delete disabled texture sets
* &lbrack;Shelf&rbrack; Allow multiple users to write inside the same shelf folder
* &lbrack;Scripting&rbrack; Be able to reload plugins folder
* &lbrack;Scripting&rbrack; Add a required minimal API version in plugin metadata to ensure compatibility
* &lbrack;IRay&rbrack; Export image dialog improvements

**Fixed:**

* &lbrack;Engine&rbrack; Disappearing strokes issue, when changing resolution (4K&gt;2K)
* &lbrack;Bakers&rbrack; ID Map Baking fail with Match By Name enabled
* &lbrack;Bakers&rbrack; Error messages are not explicit enough
* &lbrack;3D View&rbrack; Tangent space is not synched with bakers
* &lbrack;Tool&rbrack; Black artifacts when using the smudge tool
* &lbrack;Shader&rbrack; Non-PBR shader doesn't work anymore
* &lbrack;Shader&rbrack; "pbr-coated" is broken
* &lbrack;Shader&rbrack; Coating Roughness of "pbr-coated" shader has no impact anymore
* &lbrack;Shader&rbrack; Spec gloss shader doesn't match Iray and SD
* &lbrack;Shelf&rbrack; Crash when loading two files with the same name but different extensions
* &lbrack;Shelf&rbrack; Can't edit preset anymore in the shelves
* &lbrack;Shelf&rbrack; Cannot set a custom preview for assets imported in the shelf
* Resources loaded from the cache lose their usages
* Saving a project before creating a template returns write permission errors
* Incorrect project save if filename contains two periods
* Importing files with multiple dots (.) in the filename causes issues

### 2.6.1

*(Released: May 12, 2017)*

**Added:**

* &lbrack;TextureSet&rbrack; Don't allow to reassign mesh materials to nothing

**Fixed:**

* Crash when switching of TextureSet after replacing baked map
* Crash when doing "Undo and Redo" after changing layer's blending mode
* Crash or Freeze when using the "color selection" effect with big ID map
* &lbrack;Export&rbrack; Texture Sets renamed are not sorted alphabetically in the export window
* &lbrack;TextureSet&rbrack; Reset to default name doesn't check for unicity
* &lbrack;TextureSet&rbrack; Renamed texture set become disabled after reopening project
* &lbrack;Shelf&rbrack; Missing default templates content
* &lbrack;Shelf&rbrack; Non-square textures are displayed as square
* &lbrack;Shader&rbrack; Once a texture set is disabled the associated shader is destroyed
* &lbrack;Scripting&rbrack; alg.baking.setTextureSetBakingParameters() doesn't work anymore
* &lbrack;Scripting&rbrack; Typo in websocket tutorial
* &lbrack;Scripting&rbrack; Various problems in AlgWidgets
* &lbrack;Log&rbrack; Incorrect detection of available virtual memory in some cases

### 2.6.0

*(Released: April 27, 2017)*

**Added:**

* Add new sample project "Meet Mat"
* &lbrack;Plugin&rbrack; New "Resources Updater" plugin
* &lbrack;TextureSet&rbrack; Allow to rename and add a description to texture sets
* &lbrack;TextureSet&rbrack; Allow to reassign materials
* &lbrack;TextureSet&rbrack; Add a setting button in the texture set list window
* &lbrack;TextureSet&rbrack; Show "disabled" texture sets at the bottom of the list
* &lbrack;Substance&rbrack; Use additional maps at the current texture set resolution to improve performances
* &lbrack;Scripting&rbrack; Allow to update a resource used in a project (material, generator, etc.)
* &lbrack;Scripting&rbrack; Add a way to add/remove a shelf
* &lbrack;Scripting&rbrack; Allow to query info from resource in projects
* &lbrack;Scripting&rbrack; Allow to retrieve a list of available shelfs
* &lbrack;Scripting&rbrack; Improve AlgWidget thumbnail tutorial
* &lbrack;Export&rbrack; Disable/Enable bit depth based on file format support
* &lbrack;Log&rbrack; Add plugin name to print in console
* &lbrack;Log&rbrack; Remove error about hidden texture sets
* Update "Welcome Screen" with new icons and text for samples

**Fixed:**

* Crash when updating a mesh in specific projects
* &lbrack;Viewport&rbrack; Symmetry plane inner color is not visible anymore
* &lbrack;Viewport&rbrack; Some post-process effects are enabled when using the solo view
* &lbrack;Shaders&rbrack; "over_premult" blending doesn't work properly
* &lbrack;Shaders&rbrack; Warning about alpha-test with the default shader
* &lbrack;Shelf&rbrack; Incorrect parsing of tags from Substances
* &lbrack;Shelf&rbrack; MatFX Rust Weathering doesn't work properly
* &lbrack;Shelf&rbrack; HSL filter is enabled on incorrect channels by default
* &lbrack;Shelf&rbrack; Sharpen is enabled on Height/Normal channel by default
* &lbrack;Export&rbrack; Vray export presets don't use an OpenGL normal map
* &lbrack;Tool&rbrack; Imprecision issues with clone/smudge tool create artifacts

### 2.5.3

*(Released: March 15, 2017)*

**Fixed:**

* &lbrack;Baker&rbrack; Crash when baking with specific meshes

**Known Issues:**

* &lbrack;Mac&rbrack; Particles can create texture corruption in some cases

### 2.5.2

*(Released: March 14, 2017)*

**Fixed:**

* &lbrack;Tool&rbrack; Wacom tablets don't work on Linux
* &lbrack;Tool&rbrack; Black artifacts when using the smudge tool
* &lbrack;Bakers&rbrack; Baking fail if Match By Name is used with a cage
* &lbrack;Bakers&rbrack; Ambient Occlusion broken when baking with Normal Map only
* &lbrack;Shelf&rbrack; Generic filters don't handle alpha properly (Contrast/Luminosity, Highpass, etc.)
* &lbrack;Viewport&rbrack; Performance issue when loading a project with shadows enabled
* &lbrack;Viewport&rbrack; Dithering issue in 3D View on MacOS
* &lbrack;Viewport&rbrack; Particle previews incorrectly displayed when color profile is enabled
* &lbrack;Iray&rbrack; Crash when switching project back to OpenGL if Iray failed to initialize
* &lbrack;IRay&rbrack; Glossiness is ignored when rendering SpecGloss shader/mdl
* &lbrack;Shader&rbrack; Spec/Gloss shader doesn't match Iray and SD
* &lbrack;Shader&rbrack; sRGB conversion different from linear to sRGB LUT conversion
* &lbrack;Shader&rbrack; Incorrect rendering when loading project with outdated shaders
* &lbrack;Shader&rbrack; "pbr-coated" shader doesn't work anymore
* &lbrack;Export&rbrack; Some channels are still exported even if not present in the texture set
* &lbrack;Layers&rbrack; Blending mode "normal map inverse detail" doesn't work on grayscale channels
* &lbrack;UI&rbrack; Issue on "Color selection window" with HDPI monitor and display zoom at 150%

**Known Issues:**

* &lbrack;Mac&rbrack; Particles can create texture corruption in some cases

### 2.5.1

*(Released: February 27, 2017)*

**Fixed:**

* &lbrack;Mac&rbrack; Wacom tablet input broken in 3D and 2D view
* &lbrack;Bakers&rbrack; Matching by name doesn't work anymore
* &lbrack;Bakers&rbrack; "Average Normals" setting doesn't work anymore
* &lbrack;Iray&rbrack; Incorrect rendering with missing baked normal map
* &lbrack;Iray&rbrack; Color Profiles behave differently in comparison to OpenGL renderer
* &lbrack;Iray&rbrack; Exporting render as bitmap doesn't include color profile correction
* &lbrack;Substance&rbrack; Material filters don't work anymore
* &lbrack;Tool&rbrack; Stroke opacity isn't stored in brush presets
* &lbrack;Tool&rbrack; Clone Brush UV Alignment doesn't work anymore
* &lbrack;Export&rbrack; Displacement channel should be centered in 0.5 when exporting in integer
* &lbrack;Template&rbrack; Absolute path is stored in Templates
* &lbrack;TextureSet&rbrack; Channel texture persist after removing the channel

**Known Issues:**

* &lbrack;Linux&rbrack; Wacom tablets inputs don't work in 3D and 2D view
* &lbrack;Mac&rbrack; Particles can create texture corruption in some cases
* &lbrack;Export&rbrack; In very rare case, black rectangles can appear on AMD GPUs

### 2.5.0

*(Released: February 21, 2017)*

**Added:**

* Add support for AMD Radeon Pro and AMD FirePro GPUs
* &lbrack;Tool&rbrack; Add support for stroke opacity
* &lbrack;Tool&rbrack; Add a modifier that allow to continue the last brush stroke
* &lbrack;Iray&rbrack; Update to support Pascal GPUs
* &lbrack;Viewport&rbrack; Add support for Color Profiles (LUT)
* &lbrack;Substance&rbrack; Integrate new framework (SD6 engine)
* &lbrack;UI&rbrack; Increase "recent file" size list in File menu
* &lbrack;Import&rbrack; Use category from substances to fill the prefix in the import dialog
* &lbrack;Bakers&rbrack; Allow to bake 8K textures
* &lbrack;Bakers&rbrack; Allow to bake non-square resolutions
* &lbrack;Bakers&rbrack; Improve memory consumption when baking heavy high-poly meshes
* &lbrack;Shelf&rbrack; Lock shelves (and projects) to forbid concurrent editing and avoid corruptions
* &lbrack;Shelf&rbrack; Read category and keywords from substances to use them for filtering
* &lbrack;Shelf&rbrack; Allow to exclude ressources from the result of a search query
* &lbrack;Shelf&rbrack; Improved thumbnails time computation
* &lbrack;Shelf&rbrack; Allow to embed presets in projects
* &lbrack;Shelf&rbrack; Allow to quickly collapse/expand the tree-view with SHIFT
* &lbrack;Shelf&rbrack; Allow to save thumbnails when assets are read only (local cache)
* &lbrack;Shelf&rbrack; New content : new filters (transform, mirror, tri-planar, etc.)
* &lbrack;Shelf&rbrack; New content : new LUTs profiles (classic and artistic, such as Film Noir, Vintage, etc.)
* &lbrack;Shelf&rbrack; New content : 10 new Font Substances to quickly generate custom texts
* &lbrack;Shelf&rbrack; New templates : Unity 5 and Unreal Engine 4
* &lbrack;Shelf&rbrack; Improved HSL filter to be more artist friendly
* &lbrack;Shader&rbrack; Add support for specular level channel in PBR shaders
* &lbrack;Shader&rbrack; Add support for Dithering in Alpha Test shader
* &lbrack;Shader&rbrack; Add support for parallax occlusion mapping in PBR shaders
* &lbrack;Shader&rbrack; Allow to define custom UI for shader parameters
* &lbrack;MatLayering&rbrack; Create new Mask channel for material layering workflow
* &lbrack;Scripting&rbrack; Allow to write metadata in a SP project
* &lbrack;Scripting&rbrack; Allow to export with a specific export preset
* &lbrack;Scripting&rbrack; Allow to retrieve shader parameters as a JSON
* &lbrack;Scripting&rbrack; Add support for WebSocket connections
* &lbrack;Scripting&rbrack; Add the possibility to load shader instances
* &lbrack;Scripting&rbrack; Add the possibility to create a new project
* &lbrack;Scripting&rbrack; Allow to retrieve the url of the mesh imported in a project
* &lbrack;Scripting&rbrack; Allow non square baking
* &lbrack;Scripting&rbrack; Report errors when setting data via scripting API
* &lbrack;Substances&rbrack; Add user-data tag to specify normal map format

**Fixed:**

* Crash when picking color with substances
* Crash when loading a non RGBA32f image as environment map
* Crash related to painting on AMD GPUs
* &lbrack;Mesh&rbrack; OBJ import doesn't recognize materials without mtl file
* &lbrack;Mesh&rbrack; UDIM Texture set name generation can be incorrect on some meshes
* &lbrack;UI&rbrack; Undo/Redo button in Viewer Setting steal focus and stop mouse scrolling
* &lbrack;UI&rbrack; Some labels are incorrectly cropped in High-DPI
* &lbrack;Layer&rbrack; Replace mode for paint effect has an incorrect behavior on Mask
* &lbrack;Layer&rbrack; Subtract blending mode has an incorrect behavior with alpha
* &lbrack;Tool&rbrack; Brush size becomes huge in 2D View when painting on UV borders
* &lbrack;Tool&rbrack; Snapped straight line has erratic behavior with High-DPI
* &lbrack;Tool&rbrack; Stencil resolution is sometimes incorrect
* &lbrack;Bakers&rbrack; "Max Occluder Distance" values are clamped if "relative to bounding box" is "Off"
* &lbrack;Shader&rbrack; Stack and auto param channel definitions don't match
* &lbrack;3D View&rbrack; Inconsistent display of the normal channel depending of project setting
* &lbrack;Viewport&rbrack; Some normal maps have clamped values which appear as artifacts
* &lbrack;Viewport&rbrack; Post-effect are always disabled by default
* &lbrack;Export&rbrack; Normal mixing setting is incorrect if normal channel is missing
* &lbrack;Export&rbrack; Incorrect texture generation in some cases on AMD GPUs
* &lbrack;Export&rbrack; Shader parameters are not exported properly if located inside a group
* &lbrack;Export&rbrack; Editing an export preset in a custom shelf output a log error
* &lbrack;Shelf&rbrack; Tree-view filtering does not match exactly the folder name
* &lbrack;Shelf&rbrack; Renaming a shelf preset is hard to read
* &lbrack;Shelf&rbrack; Shader resource imported in the Shelf isn't preserved after relaunching
* &lbrack;Shelf&rbrack; Content : Weld tool preset is missing
* &lbrack;Shelf&rbrack; Content : Tile Generator doesn't work properly
* &lbrack;Shelf&rbrack; Content : Fixed incorrect mask on Rubber Tire Dirty smart material
* &lbrack;Shelf&rbrack; Content : Fixed incorrect group name on Leather bag material
* &lbrack;Iray&rbrack; Half of meshes are missing in Iray
* &lbrack;Linux&rbrack; Crash when dragging a resource above the 3D View
* &lbrack;Mac&rbrack; Preferences are reset at every launch on Sierra

**Known Issues:**

* &lbrack;Export&rbrack; In very rare case, black rectangles can appear on AMD GPUs
* &lbrack;Iray&rbrack; Color Profiles can behave in odd ways sometimes

### 2.4.1

*(Released: October 28, 2016)*

**Fixed:**

* Crash when creating a project with a template
* Crash when closing export dialog during an export
* &lbrack;Mac&rbrack; Errors when saving project (fail to save export preset)
* &lbrack;Shelf&rbrack; Creating a new preset will display it twice
* &lbrack;Shelf&rbrack; Presets cannot be loaded in read-only mode without admin rights

### 2.4.0

*(Released: October 27, 2016)*

**Added:**

* &lbrack;Shelf&rbrack; New interface to browse ressources (tree-view, filters and so on)
* &lbrack;Shelf&rbrack; Allow to save a search as a preset
* &lbrack;Shelf&rbrack; Allow to create a new window from a preset
* &lbrack;Shelf&rbrack; New interface for importing resources
* &lbrack;Shelf&rbrack; Don't copy default allegorithmic shelf in Documents folder
* &lbrack;Shelf&rbrack; New particles presets : Electric Circuit, Electric Lines, Rococo, Veins Small
* &lbrack;Shelf&rbrack; Improved older particles presets to be more easy to use (like "Rain")
* &lbrack;Shelf&rbrack; Add new information on resource contextual menu
* &lbrack;Viewport&rbrack; Improve performance when loading environment maps
* &lbrack;Viewport&rbrack; Add support of environment maps that are not power of two

**Fixed:**

* Crash when removing a mask
* Crash when painting after saving a preset
* Crash with environment blur on some GPUs
* Crash when assigning a wrong resource with the mini shelf
* &lbrack;Shelf&rbrack; Clean + Save remove tags and metadata for resources in the project
* &lbrack;Shelf&rbrack; importing a preset will display its ressources in the shelf
* &lbrack;Export&rbrack; Normal map generated from height channel has a low intensity
* &lbrack;Export&rbrack; Normal from mesh is not always present in final normal map
* &lbrack;Export&rbrack; Dilation with transparency can sometimes result with no transparency
* &lbrack;Scripting&rbrack; "alg.plugin_root_directory" can returns a truncated network path
* &lbrack;TextureSet&rbrack; Lock button is enabled when re-opening non-square projects

### 2.3.1

*(Released: October 07, 2016)*

**Added:**

* &lbrack;Plugin&rbrack;&lbrack;Photoshop&rbrack; Allow to specify which material/stack/channels to export
* &lbrack;Scripting&rbrack; Function names have some inconsistencies

**Fixed:**

* &lbrack;Export&rbrack; Alpha can be discarded in custom export presets
* &lbrack;Export&rbrack; Alpha gets incorrect gamma conversion on sRGB channels
* &lbrack;Export&rbrack; Non-square documents are exported as squared
* &lbrack;Export&rbrack; Impossible to export additional maps if one is missing
* &lbrack;Iray&rbrack; Some parameters (like emissive Intensity) have no effect
* &lbrack;NVIDIA&rbrack; Crash at Startup with NVIDIA Quadro K2200/GTX 750/760
* &lbrack;AMD&rbrack; Incorrect set of colors for thumbnails and previews
* &lbrack;AMD&rbrack; Freezes and driver failure on New File and File Open
* &lbrack;Log&rbrack; "software-version" is missing from log file

### 2.3.0

*(Released: September 15, 2016)*

**Added:**

* &lbrack;Plugin&rbrack; New "Export to Photoshop" plugin (export complete layer stack)
* &lbrack;Export&rbrack; Allow to specify the width of the padding (in pixels or infinite)
* &lbrack;Export&rbrack; Allow to set the type of background outside of the UVs
* &lbrack;Shelf&rbrack; New material layering shader to blend 10 materials
* &lbrack;Shelf&rbrack; New clay shader to view details with the height/normal channel
* &lbrack;Shelf&rbrack; New baked lighting filter with environment input
* &lbrack;Shelf&rbrack; Updated some mask generators to add non-square transformations
* &lbrack;Viewport&rbrack; Add composited normal map (normal+height+bake) to the solo mode
* &lbrack;Scripting&rbrack; Allow to export additional maps
* &lbrack;Scripting&rbrack; Allow to query available Additional maps per Texture Set
* &lbrack;Scripting&rbrack; Allow to retrieve channel format
* &lbrack;Scripting&rbrack; Add examples in the baking documentation
* &lbrack;Scripting&rbrack; Allow to query the visibility of a layer
* &lbrack;Scripting&rbrack; Allow to query layer's blending mode and opacity
* &lbrack;Scripting&rbrack; Allow to export converted maps (final normal maps, mixed AO, etc.)
* &lbrack;Substance&rbrack; Read and connect custom usages
* &lbrack;Shortcuts&rbrack; Add modifier key (SHIFT) to cycle solo mode backward
* &lbrack;Export&rbrack; Updated default export preset to disable alpha
* &lbrack;UI&rbrack; Thumbnails are now only computed if the engine is available
* &lbrack;UI&rbrack; Display a mention when thumbnails are computing

**Fixed:**

* Crash with some old projects when opening them
* Crash with corrupted texture channels cache
* Crash when blending more than 4 materials with Material Layering workflow
* &lbrack;UI&rbrack; Tool shortcuts don't work if the toolbar is hidden
* &lbrack;UI&rbrack; Iray toolbar is labeled "Untitled" in the View Menu
* &lbrack;UI&rbrack; Plugin toolbars are named "Untilted" in the View Menu
* &lbrack;Baker&rbrack; Pressing Enter while editing a bake setting launches the bake process
* &lbrack;Baker&rbrack; Incorrect ranges for some parameters
* &lbrack;Import&rbrack; Impossible to import OBJ meshes because of very big numbers
* &lbrack;Import&rbrack; Some OBJ files are imported with too many sub-objects
* &lbrack;Export&rbrack; channel background is filled with black instead of default color at export
* &lbrack;Tool&rbrack; Particles don't work properly if FOV is too low
* &lbrack;Tool&rbrack; Brush preview color is incorrect with masks in sub-stacks
* &lbrack;Viewport&rbrack; When brush goes into empty areas in 2D view it becomes gigantic
* &lbrack;Viewport&rbrack; Blank brush preview when painting Normal textures
* &lbrack;Scripting&rbrack; Incorrect documentation : "ao" listed instead of "ambientocclusion"
* &lbrack;Scripting&rbrack; Process started with subprocess() is killed when closing Painter
* &lbrack;Shelf&rbrack; Baked lighting filter use incorrect AO input
* &lbrack;MacOS&rbrack; Removed Fire Hydrant project (incompatible)
* Default project opens when loading a \*.spt file (instead of \*.spp)

**Known Issues:**

* &lbrack;Plugin&rbrack; Because of Photoshop, the height and normal channel can't be translated as-is

### 2.2.0

*(Released: July 22, 2016)*

**Added:**

* &lbrack;Shelf&rbrack; Improve search system and queries
* &lbrack;Shelf&rbrack; Add search field for mini-shelves
* &lbrack;Shader&rbrack; Allow to define step precision for sliders
* &lbrack;Shader&rbrack; Add an Undo/Redo button for shader parameters
* &lbrack;Shader&rbrack; Reloading a shader should not reset its parameters
* &lbrack;MatLayering&rbrack; Add support for Dynamic Material Layering and sub-stacks
* &lbrack;MatLayering&rbrack; Allow to import json file to setup the shader settings
* &lbrack;MatLayering&rbrack; Unlock texture samplers limit (switch to Bindless textures)
* &lbrack;Scripting&rbrack; Allow to set bakers settings and launch their computation
* &lbrack;Substance&rbrack; Use "usage" for inputs/outputs connections in addition of identifiers
* &lbrack;Tool&rbrack; Allow to select the preview channel in the viewport for the Projection Tool

**Fixed:**

* Crash during launch if substances are located in wrong folder
* Crash report sometimes doesn't work because of incorrect log file
* &lbrack;Iray&rbrack; Post effects don't refresh when Iray is paused
* &lbrack;Iray&rbrack; Auto-focus shortcut doesn't work anymore
* &lbrack;Iray&rbrack; Aperture slider behavior change depending of asset size
* &lbrack;Layers&rbrack; First material channel is not enabled by default if they are all disabled
* &lbrack;Shader&rbrack; No errors are printed if a "param auto" is incorrect

**Known Issues:**

* &lbrack;Mac&rbrack; Texture samples limit is locked at 16 (GPU driver issue)

### 2.1.1

*(Released: July 01, 2016)*

**Added:**

* &lbrack;License&rbrack; Be able to change the license file location
* &lbrack;Viewport&rbrack; Add a "B" shortcut to cycle between additional maps
* &lbrack;Import&rbrack; Allow to import FBX 2016/2017 properly
* &lbrack;Tool&rbrack; Remove checkers when using the quick mask
* &lbrack;Iray&rbrack; Add scene dimensions information
* &lbrack;Iray&rbrack; Allow to increase maximum number of samples and render time
* &lbrack;UI&rbrack; Update result immediately when using +/- button on sliders
* &lbrack;UI&rbrack; Allow greater precision for Grayscale sliders
* &lbrack;Export&rbrack; Don't export an alpha channel for textures being RGB only
* &lbrack;Export&rbrack; Update Dota 2 export preset
* &lbrack;Shelf&rbrack; New "Hexagon tiles" pattern
* &lbrack;Shelf&rbrack; New "Weld" tool
* &lbrack;Shelf&rbrack; Updated finish filters to give direction controls

**Fixed:**

* &lbrack;Export&rbrack; Impossible to export PSD files in 8bits
* &lbrack;Export&rbrack; 8K export is not available on some hardware configurations
* &lbrack;Export&rbrack; Sketchfab window is cropped
* &lbrack;Export&rbrack; Incorrect roughness map in Spec/Gloss export preset
* &lbrack;UI&rbrack; Typing in grayscale sliders doesn't work anymore
* &lbrack;UI&rbrack; Impossible to put filters into substance inputs (like Generators)
* &lbrack;UI&rbrack; Some sliders have odd behaviors
* &lbrack;UI&rbrack; DeltaTime +/- step for particles is too big
* &lbrack;Iray&rbrack; Some projects block the application when switching to Iray
* &lbrack;Iray&rbrack; Crash when detecting hardware
* &lbrack;Tool&rbrack; Brush preview color is incorrect in Mask mode
* &lbrack;Tool&rbrack; Material picker can be used with incompatible tools
* &lbrack;Tool&rbrack; Projection preview don't switch to Diffuse with Spec/Gloss workflow
* &lbrack;Shelf&rbrack; Changing default shader breaks smart mats/smart masks previews
* &lbrack;Shelf&rbrack; Some smart materials have incorrect names
* &lbrack;Shelf&rbrack; Additional alpha shapes are corrupted and won't load
* &lbrack;Viewport&rbrack; Switching to "Additional map" mode display "other" first
* &lbrack;Viewport&rbrack; Viewport switch back to "other" when an additional map doesn't exist
* &lbrack;Crash&rbrack;&lbrack;Linux&rbrack; Crash report doesn't work on Ubuntu (Steam)
* &lbrack;Crash&rbrack;&lbrack;Linux&rbrack; Web URL links don't work on Ubuntu (Steam)
* &lbrack;Crash&rbrack;&lbrack;Windows&rbrack; Remove "crashwatcher" when Substance painter doesn't run anymore
* &lbrack;Crash&rbrack;&lbrack;Mac&rbrack; Crash report system doesn't work properly
* &lbrack;Crash&rbrack; Importing a mesh while already importing a mesh lead to a crash
* Texture set picking shortcut reset to nothing after a relaunch

### 2.1.0

*(Released: June 02, 2016)*

**Added:**

* &lbrack;UDIM&rbrack; Import UDIM Tiles from a mesh as Texture Sets
* &lbrack;Linux&rbrack; Added support for CentOS 6.6 and Ubuntu 12.4
* &lbrack;Export&rbrack; Add 8K resolution (experimental)
* &lbrack;Export&rbrack; Allow to choose the bit depth during the export
* &lbrack;Baker&rbrack; Allow to bake multiple texture sets at once
* Support high resolution monitors (High DPI scaling)
* &lbrack;Scripting&rbrack; Set custom resolution and padding per texture at export
* &lbrack;Viewport&rbrack; Allow to switch between texture set by clicking on the mesh (via Ctrl+Alt+Click)
* &lbrack;Viewport&rbrack; Go where the mouse cursor is when zooming with the mouse wheel
* &lbrack;UI&rbrack; Update default background color and environment map display
* &lbrack;UI&rbrack; Add tooltips with original names for User channels
* &lbrack;UI&rbrack; Change background color for channels that can't be renamed
* &lbrack;Tool&rbrack; Remove checkers when using the quick mask
* &lbrack;Shader&rbrack; Allow to define groups for shader parameters and materials/masks
* &lbrack;Engine&rbrack; Optimization of small size stamping
* &lbrack;Stencil&rbrack; Add "W" as shortcut to temporarily toggle the mask
* &lbrack;Shelf&rbrack; Add a cross button to clear the search field
* &lbrack;Shelf&rbrack; Load Alpha with a single click
* &lbrack;Shelf&rbrack; New export preset : Vray UDIM, Arnold UDIM, Spec/Gloss from Metal/Rough
* &lbrack;Shelf&rbrack; New alphas : geometric shapes, veins and signs
* Add name and version in the properties of Substance Painter executable

**Fixed:**

* &lbrack;Substance&rbrack; Impossible to use the normal channel and additional map at the same time
* &lbrack;Iray&rbrack; MDL refraction and absorption setting don't work
* &lbrack;Iray&rbrack; Original scene scale is not preserved
* &lbrack;Shelf&rbrack; Specular/Glossiness template use an incorrect shader
* &lbrack;Export&rbrack; Default export preset doesn't export some maps (like AO)
* &lbrack;Viewport&rbrack; Pivot point doesn't update when clicking outside the UVs in the 2D View
* &lbrack;UI&rbrack; Slider values are rounded
* &lbrack;UI&rbrack; Sometimes when editing sliders values there is a very small free space
* &lbrack;New Project&rbrack; Template dropdown list is not correctly updated (from 1.x to 2.x)
* &lbrack;Scripting&rbrack; Fixed "hover" behavior on custom buttons
* &lbrack;Mac&rbrack; Undoing on an empty project locks the camera

**Known Issues:**

* Crash report is not available on Ubuntu
* Some url buttons might not work, take a look at our FAQ for a workaround

### 2.0.5

*(Released: April 29, 2016)*

**Added:**

* &lbrack;Shelf&rbrack; Added/Updated non-pbr template, shader and export preset
* &lbrack;Shelf&rbrack; Updated UE4 export preset to include Ambient Occlusion

**Fixed:**

* Crash when opening and saving some projects with corrupted ressources
* &lbrack;Viewport&rbrack; Wireframe appears broken in 2D view
* &lbrack;Shelf&rbrack; Improved performances of some studio environment maps
* &lbrack;Shelf&rbrack; Some studio environment maps are duplicated
* &lbrack;Shelf&rbrack; Missing "Baked Lighting Material"
* &lbrack;Shelf&rbrack; Missing "Grayscale conversion" generator

### 2.0.4

*(Released: April 26, 2016)*

**Added:**

* Improve mesh collisions and optimize wireframe rendering
* Improve performances and memory management with big projects
* Improve slider precision and stepping
* &lbrack;UI&rbrack; Update engine only when validating a slider (not when entering a value)
* &lbrack;UI&rbrack; Move Iray switch to a dedicated button in the main toolbar (and change its shortcut)
* &lbrack;Tool&rbrack; Add setting for clone tool source location behavior
* &lbrack;Shader&rbrack; Allow to read mesh vertex colors in custom shaders
* &lbrack;Scripting&rbrack; Allow to retrieve the list of texture sets, channels and layers
* &lbrack;Scripting&rbrack; Add helper functions (url to path, get export path from project)
* &lbrack;Mac&rbrack; Detect Mac Os "El Capitan" version in log file

**Fixed:**

* Crash after second export to Substance Share
* Crash when copying a layer between texture sets with Quick mask data.
* Some projects have a very long updater that consume a lot of memory
* &lbrack;Tool&rbrack; Crash when selecting a particle preset with clone/smudge tool
* &lbrack;Baker&rbrack; Loading FBX files takes too much time for heavy meshes
* &lbrack;Viewport&rbrack; Stretched environment map on some computers
* &lbrack;Viewport&rbrack; Wrong gamma conversion of the alpha of the brush
* &lbrack;Export&rbrack; Alpha is stored as transparency instead of a separate channel with Tiff files.
* &lbrack;Export&rbrack; Normal channel is always exported as being OpenGL
* &lbrack;Iray&rbrack; Missing slider names for Iray settings
* &lbrack;Iray&rbrack; Render is done at a wrong resolution on Retina/High DPI
* &lbrack;Iray&rbrack; Crash when resizing interface in Iray mode
* &lbrack;Iray&rbrack; Huge performance slowdown when rendering at some low resolutions
* &lbrack;Iray&rbrack; Pause doesn't work (Iray still compute in the background)
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

* &lbrack;Iray&rbrack; Update Spec/Gloss template and shader to be compatible with Iray
* &lbrack;Export&rbrack; Be able to Export screenshots to ArtStation
* &lbrack;Scripting&rbrack; Support execution from plugin directory
* &lbrack;Scripting&rbrack; Allow to "Save As"
* &lbrack;UI&rbrack; Allow to double click on a slider to edit its value
* Move Vela sample to Substance Share
* New sample project : Sphere Preview
* Warn users about shell extension conflict

**Fixed:**

* Installer override installation of Substance Painter 1.x
* &lbrack;UI&rbrack; Channels list layout is broken with filters
* &lbrack;UI&rbrack; Shader parameters are not displayed
* &lbrack;UI&rbrack; Resizing the layer window crops incorrectly the content
* &lbrack;Tool&rbrack; Opacity channel isn't always used properly
* &lbrack;Tool&rbrack; Smudge/Clone don't work with Symmetry
* &lbrack;Tool&rbrack; Brush preview opacity is incorrect with some channels
* &lbrack;Iray&rbrack; Crash when using Iray while it hasn't been created yet
* &lbrack;Iray&rbrack; Can't load iray settings data from project
* &lbrack;Iray&rbrack; Iray doesn't take care of settings modification after been paused
* &lbrack;Shelf&rbrack; Importing a Material to the shelf doesn't work
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
* &lbrack;Tool&rbrack; New Smudge tool for blending and spreading colors
* &lbrack;Tool&rbrack; New Clone tool for copying part of textures
* &lbrack;Tool&rbrack; Allow to select channels for Smudge, Clone and Eraser tool
* &lbrack;Layer&rbrack; Add Substance name for Fill effect name
* &lbrack;Layer&rbrack; Allow to export mask to clipboard
* &lbrack;Viewport&rbrack; Switch between perspective and orthographic mode
* &lbrack;Viewport&rbrack; Allow to control Field of View in perspective mode
* &lbrack;Viewport&rbrack; Allow to set Depth of Field distance with CTRL+Middle click
* &lbrack;Viewport&rbrack; Allow to drag and drop environment maps in the 3D View.
* &lbrack;Viewport&rbrack; Improved feedback when the engine is doing strong computations
* &lbrack;Export&rbrack; Allow to export shader parameters in a json file
* &lbrack;UI&rbrack; Update interface with new icons, colors and layout
* &lbrack;UI&rbrack; Add assets names to the mini shelves
* &lbrack;UI&rbrack; Collapse "Channels mapping" by default
* &lbrack;Shader&rbrack; Choose a custom color for shader texture parameters
* &lbrack;Shelf&rbrack; Ask where to import files when drag and dropping resources
* &lbrack;Shelf&rbrack; New Preview sphere for Smart Materials and Generators
* &lbrack;Shelf&rbrack; Add Specular Glossiness shader
* &lbrack;Shelf&rbrack; New Hard Surface shapes
* &lbrack;Shelf&rbrack; New Alphas textures and shapes
* &lbrack;Shelf&rbrack; New Skin textures
* &lbrack;Shelf&rbrack; New Scan-based materials and smart-materials
* &lbrack;Shelf&rbrack; New smart materials and spec/gloss support of old ones
* &lbrack;Shelf&rbrack; New Finish filters for metallic surface simulation
* &lbrack;Shelf&rbrack; New powerful mask generator "Mask Editor"
* &lbrack;Shelf&rbrack; Reworked and cleaned old materials
* New "Vela" sample project

**Fixed:**

* &lbrack;Settings&rbrack; Camera rotation and zoom speed are overridden by the project
* &lbrack;Viewport&rbrack; Precision issue on default normal texture leads to incorrect reflections
* &lbrack;Viewport&rbrack; Vignette is enabled by default
* &lbrack;Viewport&rbrack; Artifacts appear at the environment map borders (Nvidia GPUs)
* &lbrack;Viewport&rbrack; Thumbnail in projection/stencil mode is very long to load
* &lbrack;Baker&rbrack; Store baked textures in 16bits integer instead of 32bits
* &lbrack;Layer&rbrack; Outdated substances are displayed incorrectly in the stack
* Default color and bit-depth for some channels are incorrect (ex : Specular, Glossiness)
* Fixed eraser behavior to disable blending in passthrough mode

**Known Issues:**

* Symmetry doesn't work with Smudge and Clone tool
* ArtStation export is missing

## Version 1

### 1.7.3

*(Released: March 01, 2016)*

**Added:**

* &lbrack;Export&rbrack; Add an option to disable padding
* &lbrack;Shelf&rbrack; Support sub-shelf hierarchy inside a shelf folder

**Fixed:**

* Crash when saving over previously Read Only file
* Crash when opening a second project
* Crash when loading some thumbnails (shelf, layers or tooltips)
* Disabling "Preserve strokes positions on mesh" does not work
* &lbrack;Export&rbrack; Upscale of bitmaps is done with nearest filtering
* &lbrack;Shelf&rbrack; Discovery of resources is very slow
* &lbrack;Shelf&rbrack; Blur filters are not 16 bits compatible
* &lbrack;Tool&rbrack; Symmetry doesn't work if you load an old tool preset
* Color dialog for Specular channel doesn't do a color space conversion

### 1.7.2

*(Released: January 13, 2016)*

**Added:**

* &lbrack;Layers&rbrack; Allow to specify default tilling for fill layers

**Fixed:**

* &lbrack;Export&rbrack; Sketchfab export doesn't work anymore
* &lbrack;Layer&rbrack; Bilinear filtering is applied even on Fill without any transformation
* &lbrack;Tool&rbrack; Poor performances using substance with image inputs in projection mode
* &lbrack;Tool&rbrack; Material picker is broken

### 1.7.1

*(Released: December 18, 2015)*

**Fixed:**

* Crash when switching texture set
* Slow performances when painting

### 1.7.0

*(Released: December 17, 2015)*

**Added:**

* &lbrack;Performances&rbrack; Compute layers content and their thumbnails at the same time
* &lbrack;Export&rbrack; Save export path as relative when next to the project
* &lbrack;Layers&rbrack; Added new blending mode : subtract and add/sub
* &lbrack;Layers&rbrack; New Bilinear HQ filtering for fill layers
* &lbrack;Shader&rbrack; Set a default shader for thumbnail generation in the preferences.
* &lbrack;Shader&rbrack; Allow to specify a shader per texture set
* &lbrack;Shader&rbrack; Allow to sample textures from the shelf
* &lbrack;Tool&rbrack; New "wrap" brush behavior for painting
* &lbrack;Tool&rbrack; Improved filtering and reduced aliasing while painting
* &lbrack;Tool&rbrack; Improved sub-pixels painting quality
* &lbrack;Tool&rbrack; Removed "basic" display for brush settings and improved the frame open/close icon
* &lbrack;Menu&rbrack; Add effect icons in the right-click menu
* Template creation from Projects
* &lbrack;Shelf&rbrack; New templates : PBR, Dota 2
* &lbrack;Shelf&rbrack; New export preset : Dota 2
* &lbrack;Shelf&rbrack; New shaders : Dota 2, PBR Car paint, PBR Coated, PBR Velvet
* &lbrack;Shelf&rbrack; New material : Steel rust and wear, Stylized lighting
* &lbrack;Shelf&rbrack; New filters : Blur directional, Stylized lighting
* &lbrack;Shelf&rbrack; New brush : default soft and default hard with a new alpha for a better hardness control
* &lbrack;Shelf&rbrack; New generators : 3D Distance and Light
* &lbrack;Shelf&rbrack; Updated brushes with wrap projection and backface culling (enabled by default)
* &lbrack;Shelf&rbrack; Updated White noise with pixel processor version for faster computation

**Fixed:**

* &lbrack;Welcome screen&rbrack; Tutorials link send to old videos
* &lbrack;Channels&rbrack; Saying "no" to fill layer creation with AO still create the layer
* &lbrack;Channels&rbrack; UserX channels names do not propagate in the interface
* &lbrack;Viewport&rbrack; Mask entry is empty in the list of the solo channels
* &lbrack;Share&rbrack; Exporting an alpha to Share from SP creates an unreadable .image file
* &lbrack;License&rbrack; Fix activation fro usernames with non ASCII characters
* &lbrack;Shader&rbrack; Color parameter dialog disappear when picking a color
* &lbrack;Shelf&rbrack; Thumbnails are not unloaded from memory when unused
* &lbrack;Shelf&rbrack; Fixed gradient filter
* &lbrack;Tool&rbrack; Symmetry doesn't work with stencil/projection
* &lbrack;Tool&rbrack; Incorrect name when creating new brush preset
* Preserve stroke setting stays disabled even when reimporting a mesh
* Driver reset (TDR) when computing particles with a big size.

### 1.6.1

*(Released: November 09, 2015)*

**Fixed:**

* Crash when opening project if 2D view is visible
* Crash when creating new export preset if current shelf doesn't exist
* &lbrack;Tool&rbrack; Material picker icon can stay displayed
* &lbrack;Tool&rbrack; Material picker hide mouse cursor when painting at the same time
* &lbrack;Shelf&rbrack; Metadatas are written on the disk after each exit

### 1.6.0

*(Released: October 29, 2015)*

**Added:**

* Official support for Windows 10
* &lbrack;Substance&rbrack; Collapse substance parameters groups by default
* &lbrack;Substance&rbrack; Add new framework (Improve Pixel Processor performances)
* &lbrack;Viewport&rbrack; Allow to deactivate the symmetry plane display while in symmetry mode.
* &lbrack;Viewport&rbrack; Improve shadows rendering and performances
* &lbrack;Viewport&rbrack; Pause shadow computation when painting
* &lbrack;Viewport&rbrack; Improve wireframe rendering performances
* &lbrack;Engine&rbrack; Improve Vram memory management to reduce its footprint
* &lbrack;Engine&rbrack; Improve texture refresh on AMD GPUs for better performances
* &lbrack;Engine&rbrack; Disable Threaded Optimization setting on NVIDIA GPUs for better performances
* &lbrack;Effect&rbrack; Add a tag to request "padded" image input
* &lbrack;Layer&rbrack; Increase precision of UV offset/scale in fill
* &lbrack;Layer&rbrack; Make the scale slider exponential in fill
* &lbrack;Layer&rbrack; Allow to drag and drop Materials directly in the layer stack.
* &lbrack;Layer&rbrack; Allow to drag and drop filters directly in the layer stack
* &lbrack;Layer&rbrack; Adjust the mask brush color to the newly created mask color
* &lbrack;Shader&rbrack; Expose multiple texcoords
* &lbrack;Shader&rbrack; Expose gamma/tonemapping function to allow custom functions
* &lbrack;Bakers&rbrack; Change default Position baker settings for TriPlanar usage
* &lbrack;Tool&rbrack; Rename "Geometry Decal" as "Polygon Fill"
* &lbrack;Shelf&rbrack; Update generators to support TriPlanar : MG Metal edge wear, MG Mask builder, MG Fiber glass, MG Dirt
* &lbrack;Shelf&rbrack; Update materials with new settings and removed unused materials
* &lbrack;Shelf&rbrack; 22 New smart materials (Plastic, Iron, Fabric, Steel and more)
* &lbrack;Shelf&rbrack; Update Sharpen, Blur and Warp filters with padded image input to avoid seams
* &lbrack;Shelf&rbrack; Improve Warp settings for easier usage
* &lbrack;Shelf&rbrack; 2 New procedural noises : 3D Perlin noise and 3D Worley noise

**Fixed:**

* &lbrack;Engine&rbrack; Vram amount detection for dedicated GPU is incorrect on Mac
* &lbrack;Engine&rbrack; Textures turn to darker version in the viewport
* &lbrack;Engine&rbrack; Poor performances when painting below multiple layers
* &lbrack;Engine&rbrack; Computed layers when opening project differ from cached version
* &lbrack;Substance&rbrack; Wrong results in 4K on Mac
* &lbrack;Substance&rbrack; Parameters are in the wrong order
* &lbrack;Shader&rbrack; Toon and Pixelated shaders are totally black
* &lbrack;Shader&rbrack; Parameters disappear after changing env-map
* &lbrack;Shelf&rbrack; Crash when putting png files in generator folder
* &lbrack;Shelf&rbrack; Thumbnails are generated with low roughness
* &lbrack;Tool&rbrack; Crash when using a bitmap in the brush alpha on windows
* &lbrack;Export&rbrack; Additional map export preset now export a RGB map for Position

### 1.5.7

*(Released: September 24, 2015)*

**Fixed:**

* Crash report doesn't work anymore

### 1.5.6

*(Released: September 21, 2015)*

**Added:**

* &lbrack;Shelf&rbrack; Improve thumbnail rendering quality (use 1K textures)

**Fixed:**

* &lbrack;Share&rbrack; Impossible to sign with another account
* &lbrack;Shelf&rbrack; Thumbnails are too heavy on the disk
* &lbrack;Shelf&rbrack; Smart materials are very slow to load
* &lbrack;Windows&rbrack; Fix license service install
* &lbrack;Channels&rbrack; Transmissive map is created as G8 by default

### 1.5.5

*(Released: September 15, 2015)*

**Added:**

* &lbrack;Shelf&rbrack; Export assets to Substance Share
* &lbrack;Shelf&rbrack; Add new sphere preview for Materials
* &lbrack;Shelf&rbrack; Use the env map "Glazed patio" for generating thumbnails
* &lbrack;Shelf&rbrack; Increase thumbnail size resolution to 512x512 pixels
* &lbrack;3D View&rbrack; Expose environment rotation value
* &lbrack;Windows&rbrack; Sign the application

**Fixed:**

* &lbrack;Bakers&rbrack; Wrong results when baking maps at the same time
* &lbrack;3D View&rbrack; The env map is displayed when no project is open
* &lbrack;Layers&rbrack; Mask Generators don't work on layer content
* &lbrack;Layers&rbrack; You can paint on hidden layers
* &lbrack;Shelf&rbrack; Dirt_5 and Dirt_6 noise are identical
* &lbrack;Shelf&rbrack; Some mask generators are pixelated or at low quality
* &lbrack;Tool&rbrack; Incorrect gizmo rotation on certain angles.
* &lbrack;Tool&rbrack; Too many channels cause the channel buttons to be cropped out
* &lbrack;Tool&rbrack; Invert mask shortcut for Quick mask doesn't work
* &lbrack;Export&rbrack; Sketchfab: cancel button not correctly taken into account
* &lbrack;Licence&rbrack; Activation failed when license cannot be copied
* Framerate limiter doesn't work on the UI anymore

### 1.5.0

*(Released: August 20, 2015)*

**Added:**

* &lbrack;Shader&rbrack; Add line number in Shader compiling error messages
* &lbrack;Shelf&rbrack; Improve thumbnails previews quality
* &lbrack;Shelf&rbrack; Automate thumbnail generation for Smart Materials
* &lbrack;Tool&rbrack; Shortcut to control hardness setting in the substance
* &lbrack;Tool&rbrack; Use grayscale widget for geometry decal when over a mask
* &lbrack;Tool&rbrack; Shortcut to invert paint color while painting on a grayscale map
* &lbrack;Viewport&rbrack; Allow to display the wireframe and change its color
* &lbrack;Viewport&rbrack; Blur the environment background
* &lbrack;Controls&rbrack; Add rotation to brush mouse shorcuts
* &lbrack;Export&rbrack; Export to Sketchfab
* &lbrack;Export&rbrack; Create export presets for renderers
* &lbrack;Export&rbrack; Add converted map Reflection, F0 and 1/IOR
* &lbrack;UI&rbrack; Add Welcome screen
* &lbrack;UI&rbrack; Update default layout
* &lbrack;UI&rbrack; Add missing tooltips and rename some menu entry
* &lbrack;Layers&rbrack; Export currently selected mask as bitmap
* &lbrack;Layers&rbrack; Add "invert mask" action in the right-click menu

**Fixed:**

* &lbrack;Project&rbrack; If the meshes pivot's are different in the FBX, the meshes get exploded upon import
* &lbrack;Substance&rbrack; Substances used in projection tools are locked in 256\*256
* &lbrack;Layers&rbrack; Crash when using clear mask
* &lbrack;Export&rbrack; Incorrect gamma conversion on very dark textures
* &lbrack;Export&rbrack; Position map can only be used in export presets as a grayscale map
* &lbrack;Tool&rbrack; Geometry decal start color is black when used on a mask
* &lbrack;Tool&rbrack; Rotation shortcut doesn't work if there is no hardness in the alpha

### 1.4.2

*(Released: July 15, 2015)*

**Fixed:**

* &lbrack;Tool&rbrack; Crash when using geometry decal with quick mask
* Updating project from 1.4.0 to 1.4.1 consume all the computer memory
* Old project format import incorrectly
* Custom shelves parse the entire hierarchy and duplicate assets everywhere

### 1.4.1

*(Released: June 23, 2015)*

**Added:**

* &lbrack;Viewport&rbrack; Allow to dock panels side by side
* &lbrack;Effect&rbrack; Add a background and a ruler for the level effect
* &lbrack;Effect&rbrack; Add a Paint effect that allow to work over other effect

**Fixed:**

* &lbrack;Shelf&rbrack; Thumbnail generation is broken if no project is open
* &lbrack;Shelf&rbrack; Material preset preview fail to generate
* &lbrack;Shelf&rbrack; Material previews are generated on a mesh with inverted normals
* &lbrack;Shelf&rbrack; Thumbnails always recompute because of incorrect hash function
* &lbrack;Shelf&rbrack; Clicking on a substance material doesn't connect additional maps
* &lbrack;Tool&rbrack; Incorrect value sampled with Material picker
* &lbrack;Tool&rbrack; Color picker pick viewport cursor color
* &lbrack;2D View&rbrack; Very low framerate/performances
* &lbrack;Export&rbrack; Crash when opening the export window with too recent export presets.
* &lbrack;Export&rbrack; Height channel to Normal map is converted to the wrong space
* &lbrack;Mac&rbrack; BaseColor from substance effects is displayed as Linear
* &lbrack;Mac&rbrack; Straight lines widget is incorrectly drawn on Retina
* Straight lines can stay enabled even with the shortcut released.
* Straight lines guizmo disappear after rotating the environment map
* Ambient occlusion outputs from substances are not plugged to the AO channel automatically
* Fix license copy issue on windows with special character in username

### 1.4.0

*(Released: June 10, 2015)*

**Added:**

* &lbrack;Export&rbrack; Add additional maps in the list of the available input maps
* &lbrack;Shelf&rbrack; Use sbsar materials as material presets
* &lbrack;Shelf&rbrack; Allow to use custom Library paths
* &lbrack;Shelf&rbrack; Change the minimum size
* &lbrack;Shelf&rbrack; New content : 20 new smart materials
* &lbrack;Shelf&rbrack; New content : new procedural substance (weave, mesh)
* &lbrack;Shelf&rbrack; Updated Blur filter
* Draw straight lines using a modifier key
* Add Ambient Occlusion channel and rework AO/Normal behavior in layer stack
* Read default color from Image Input defined in Substance user data
* Allow to export the log from the help menu

**Fixed:**

* &lbrack;Baker&rbrack;&lbrack;Mac&rbrack; Crash with Normal from mesh baker
* &lbrack;Baker&rbrack; Crash if there is no UVs in the cage file
* &lbrack;Baker&rbrack; Matching by names doesn't work with OBJs exported from zBrush
* &lbrack;Baker&rbrack; Baking with a cage overwrites bake if using multiple texture sets and overlapping UVs
* &lbrack;Baker&rbrack; Specific OBJ files result in black textures
* &lbrack;Shelf&rbrack; Can't read resources if set to read-only
* &lbrack;Shelf&rbrack; Asset files are being written Painter if they have been used in the project.
* &lbrack;Shelf&rbrack; Reloading substances also update the layer
* &lbrack;Export&rbrack; Tiff exports 32 bits images that can't be read properly by Photoshop or game engines
* &lbrack;Export&rbrack; Default channels preset always export as RGB
* &lbrack;Material&rbrack; Diffuse channel override BaseColor mapping with substances
* &lbrack;3D View&rbrack; Incorrect Diffuse lighting with specific environement maps
* &lbrack;Tool&rbrack; Unable to rotate a brush to a specific angle
* Viewport gets focus when hovered on while typing in a text field
* Crash with presets too recent for the current version of the shelf
* Crash after replacing mesh
* Crash when reloading a substance with different number of inputs
* FBX meshes from Cinema4D import with incorrect material names

### 1.3.5

*(Released: May 29, 2015)*

**Added:**

* &lbrack;License&rbrack; Activation problem when there is an already existing license file
* &lbrack;Mac&rbrack; Crash when loading specific FBX files
* &lbrack;Mac&rbrack;&lbrack;3D View&rbrack; Incorrect reflection for integrated GPU
* &lbrack;3D View&rbrack; Quick Mask font is broken
* &lbrack;3D View&rbrack; Material picker makes the viewport totally black
* Crash after opening projects created in 1.3.3
* Material preview is empty when using shaders with alpha
* Painting stop working on specific meshes
* Performances decrease a lot with specific OBJ meshes
* User channels are not mapped when using effects
* Temporary folders are not cleaned on startup

**Fixed:**

* Computation time improvements on project extremely long to load
* Change the "GPU Troubleshooting" window to be more understandable
* &lbrack;Layers&rbrack; Save the status of the the ratio lock for Fill layers and make it "On" by default
* &lbrack;Bakers&rbrack; Matching by name now use suffix as separator

### 1.3.4

*(Released: April 27, 2015)*

**Added:**

* &lbrack;Mac&rbrack; Crash with Mac OS X Yosemite (10.10)
* &lbrack;Mac&rbrack; Impossible to quit fullscreen mode
* &lbrack;Bakers&rbrack; Baking match by name option doesn't work
* &lbrack;Bakers&rbrack; Mikk tangent space used in SP doesn't work with UE4
* &lbrack;Bakers&rbrack; ID baker can't bake material ID colors
* &lbrack;2D View&rbrack; Wireframe doesn't appear when using the Geometry decal tool
* &lbrack;Tool&rbrack; Brush alpha channel is displayed as checker instead of transparency with materials
* &lbrack;Tool&rbrack; Crash with Geometry Decal
* &lbrack;Layers&rbrack; Material slot is collapsed by default on Fill layer
* &lbrack;Export&rbrack; Crash when exporting at higher size than texture set resolution
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
* &lbrack;Shelf&rbrack; Add new environment maps : Corsica beach, studio 05, Tornoco studio and more
* &lbrack;Shelf&rbrack; Update MG Mask Builder with new parameters
* &lbrack;Shelf&rbrack; Update and calibrate old environment maps

**Fixed:**

* Crash when opening the export window
* Impossible to drag'n'drop in UI widget when undocked
* "Check for updates" is not working
* &lbrack;Layers&rbrack; Don't select the mask when doing ALT+click on it
* &lbrack;Tool&rbrack; Tri-planar doesn't work with Normal channel
* &lbrack;3D View&rbrack; Diffuse lighting from env map is incorrect
* &lbrack;3D View&rbrack; Exposure computation is different from Designer
* &lbrack;3D View&rbrack; Shadows should not be visible on 100% metallic surface
* &lbrack;3D View&rbrack; Mesh with mirrored UVs has flipped tangent/binomals
* &lbrack;3D View&rbrack; Shadows produce incorrect results on certain meshes
* &lbrack;Bakers&rbrack; Remove ".alg_meta" folder created by assbin files
* &lbrack;Bakers&rbrack; Crash when baking if Painter recompute a TextureSet at the same time
* &lbrack;Mac&rbrack; White Box UI Glitch when launching the application

### 1.3.2

*(Released: March 06, 2015)*

**Fixed:**

* &lbrack;3D View&rbrack; Fail to reload an env map saved with the project

### 1.3.1

*(Released: March 05, 2015)*

**Added:**

* &lbrack;Bakers&rbrack; Add a cached version of high-poly meshes to accelerate the computation
* &lbrack;Bakers&rbrack; Add a warning icon if no high-poly mesh is loaded
* &lbrack;Bakers&rbrack; If no high-poly mesh is loaded, use the project mesh instead

**Fixed:**

* &lbrack;Bakers&rbrack; Pressing "enter" when editing the value of a slider close the window
* &lbrack;Bakers&rbrack; Enabling/Disabling a baker will also trigger the button
* &lbrack;Bakers&rbrack; Impossible to bake if you use the "all/none" button
* &lbrack;Bakers&rbrack; The sorting of the baker buttons is not in the correct order
* &lbrack;Bakers&rbrack; Checkbox are ignored and all the bakers are always processed
* &lbrack;Bakers&rbrack; Fixed progress bar progress

### 1.3.0

*(Released: March 04, 2015)*

**Added:**

* &lbrack;Bakers&rbrack;&lbrack;3D View&rbrack; Use Mikkt tangent space computation if no tangents/binormals are found
* &lbrack;Bakers&rbrack; Added new bakers : Normal, ID, Occlusion, Curvature, Thickness, Position
* &lbrack;Effects&rbrack; Effect stack is now inverted and displayed from top to bottom (like layers)
* &lbrack;Effects&rbrack; Add new icons on the effect stack
* &lbrack;Effects&rbrack; Add blending mode between fill actions in effect stack
* &lbrack;Effects&rbrack; Rename effects (substance effect = filter, etc.)
* Add a "lock" file during the save process
* &lbrack;Effects&rbrack; Add Fill action in effect stack
* Added new resource : Smart Materials
* &lbrack;Layers&rbrack; Allow to reorder layer effects
* &lbrack;Tool&rbrack; Add Tri-Planar projection
* &lbrack;3D View&rbrack; Add support for shadows
* &lbrack;3D View&rbrack; Ability to set required OpenGL states into custom shaders
* &lbrack;3D View&rbrack; Support for alpha via new shaders
* &lbrack;3D View&rbrack; Shaders are now versioned and fully saved into a project
* &lbrack;3D View&rbrack; Warn user if the shader doesn't compile anymore

**Fixed:**

* &lbrack;Layers&rbrack; fix drop under a collapsed folder
* &lbrack;Shelf&rbrack; Fix content filtering in mini-shelves
* &lbrack;Shelf&rbrack; Rename categories and reorganize tabs

### 1.2.1

*(Released: February 12, 2015)*

**Added:**

* \*.spp files can now be opened through a double click in the explorer
* &lbrack;Export&rbrack; New "$project" tag for export presets
* &lbrack;Export&rbrack; Add map list (with nomenclature) below each texture set
* &lbrack;Export&rbrack; Add a button All/None to select the texture sets
* &lbrack;Export&rbrack; Empty maps are discarded during export

**Fixed:**

* &lbrack;Export&rbrack; Unity5 presets have inverted maps
* &lbrack;Export&rbrack; Adding a forward slash in a preset name will create a corrupted folder
* &lbrack;Export&rbrack; Height channel exported in 32bits formats is incorrectly clamped
* &lbrack;Export&rbrack; Texture set list is not sorted like in the project
* &lbrack;Tool&rbrack; Backface culling doesn't work anymore
* Save doesn't work with special characters in the path

### 1.2.0

*(Released: January 28, 2015)*

**Added:**

* New Normal channel allowing to paint normal map data and combine the results
* &lbrack;Export&rbrack; New export window with the ability to create custom packing and set custom names
* The project file format is now a single file instead of folders
* &lbrack;Export&rbrack; Support different Normal formats (DirectX, OpenGL)
* &lbrack;Export&rbrack; Create a temporary "lock" file during export
* &lbrack;Layers&rbrack; Shift+LeftMouse click can be used to toggle a mask
* &lbrack;Parameters&rbrack; Expose the color space at the bottom of an image input
* &lbrack;Shelf&rbrack; Effect "MG Mask Builder" has now new settings
* &lbrack;3D View&rbrack; Ambient Occlusion map now occlude the diffuse contribution, not the specular

**Fixed:**

* Projection material/Stencil preview doesn't show properly in the viewport
* &lbrack;3D View&rbrack; Shortcut tooltip not displayed when using "S" (stencil) shortcut
* &lbrack;Shelf&rbrack; Effect "MatFx Skin Scale" has now better performances at low resolution
* &lbrack;Export&rbrack; Textures from export are just upscaled when specifying a larger document size

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

* &lbrack;Layer&rbrack; Select the layer on top when opening a project/switching texture set
* Improved "Save" and "Save as" speed with new compression algorithm
* Display en error when opening a project too recent for Painter

**Fixed:**

* &lbrack;Tool&rbrack; Geometry decal produce memory corruptions
* &lbrack;Brush&rbrack; Impossible to manually enter float values below 1 for the brush size
* &lbrack;Layer&rbrack; Creating a color selection effect doesn't add it in the layer stack
* &lbrack;Layer&rbrack; Moving the mouse over the layers makes Painter to flick in the taskbar
* &lbrack;Layer&rbrack; Adding a bitmap as a mask can lead to a crash
* GUI for the solo mode with the Height channel is incorrect
* "Save project" can fail and corrupt a project
* Crash when opening a project after loading another one with an outdated shader

### 1.1.0

*(Released: December 16, 2014)*

**Added:**

* &lbrack;Effect&rbrack; New Material ID mask creator
* New doted white/black line for the brush gizmo
* New angle follow parameter
* New backface culling parameter
* New Lazy mouse parameter
* &lbrack;Layers&rbrack; Support for multiple selections and management
* &lbrack;Layers&rbrack; Copy and paste from one texture set to one another
* &lbrack;Export&rbrack; Adobe Photoshop's PSD format
* &lbrack;Shelf&rbrack; New tool : fur, metal stitches and zipper
* &lbrack;Shelf&rbrack; New brush : mold, pencil, sharp line and stitch
* &lbrack;Shelf&rbrack; New alpha : Gaussian noise, sharp line, mold, pen, splash, stitch, zipper
* Painting performances improved by only updating parts of the textures needed

**Fixed:**

* &lbrack;Shelf&rbrack; Impossible to load a substance with graph having identical labels
* &lbrack;Layers&rbrack; Pass Through blending mode doesn't work with masks
* &lbrack;Stencil&rbrack; Scale is broken in 2D view
* Issues and crash on Mac OS Yosemite

### 1.0.2

*(Released: November 09, 2014)*

**Added:**

* Improved performances in material preview with substances
* Improved performances with brush stroke preview when updating document
* Improved performances in viewport with lower update rate for non working area
* &lbrack;Post Effects&rbrack; Improved UI to manage settings
* &lbrack;Post Effects&rbrack; Reset to default values
* Substance effects and layers operations in right-click menu
* Support for pre-multiplied Input/Output in substances

**Fixed:**

* &lbrack;3D View&rbrack; Custom shader parameters are separated by a large space
* &lbrack;Export&rbrack; Missing sRGB conversion for Unity4 preset
* Possible Crash when loading fbx meshes
* Crash sometimes when loading simple obj meshes
* Computing bar stays blocked to 100% at loading
* Reloading a substance puts it in every category
* DirectX/OpenGL switch broken

### 1.0.1

*(Released: October 27, 2014)*

**Added:**

* &lbrack;Tool&rbrack; Improved Material parameters usage
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
* &lbrack;Export&rbrack; Add a dilation pass before diffusion postprocess
* Command line arguments in SP for simple operations
* New Materials and Effects
* Tool preview (separated real time material preview and stroke testing area)
* Do not create a default document when Painter starts
* &lbrack;Tool&rbrack; Add the possibility to manually edit a grayscale value
* Various improvements for the Stencils (Snap, Reset)
* Particles are now subtools of the Painting brush, Eraser and Projection tools
* &lbrack;3D View&rbrack; Use baked AO in the viewport render
* Split the stencils controls between the 2D & 3D view
* Small thumb size tweaking in the library
* Search fields are specific to each window
* UI tweaking

**Fixed:**

* &lbrack;Susbtance&rbrack; Switch does not work
* &lbrack;Color Dialog&rbrack; Hue gradient not refreshed
* Impossible to update a mesh if the filename is identical
* Tool is not visible in views when too small
* Decal tool on Retina display doesn't work properly
* &lbrack;Substance&rbrack; Int1 are displayed as float1
* &lbrack;Substance&rbrack; basecolor input/output are not recognized
* &lbrack;Substance&rbrack; filters can't be reloaded
* &lbrack;Tool&rbrack; grayscale widget is always collapsed

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
* Better asset management (Drag & Drop, Reload resources, Delete unused)
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
* &lbrack; and &rbrack; shortcuts for Brush Size
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
