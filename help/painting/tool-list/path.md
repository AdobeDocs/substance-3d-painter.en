---
breadcrumb-title: ''
description: Use the Path tool in Substance 3D Painter to create and edit paths for precise texture painting and stroke placement.
title: Path tool overview
user-guide-description: ''
user-guide-title: ''
---

# Path tool overview

![Image showing the path tool used on a shoe](../../assets/v90_banner_path.jpg)

The **Path tools** allows you to define a curve with points on the surface of your mesh. Once the curve is created, the different Path tools allow you to create different effects along the curve.

## Creating a path

Paths can be created on paint layers and paint effects. There are two ways to access the Path tool:

* **Via the interface**: navigate to the tool's toolbar on the left-side and click the third icon from the top.
* **Via a keyboard shortcut**: by default the tool doesn't have any assigned. This can be changed in the Settings menu by editing the "Select paint along path tool" shortcut.

Once the tool is selected, points can be placed by clicking on the surface of the 3D model within the 3D viewport. At least two points (or vertices) are needed to create a path.

![Gif showing the selection of the path tool and the creation of points](../../assets/path_create_points.gif)

The Path tool has different modes, which can be similar to the other paint tools available in the application:

* Paint along path: Draw a regular brush stroke along a defined path.
* [Ribbon path](ribbon-tool.md): Draws a repeated or stretched image along a path.
* [Filled path](filled-path.md): Fill the interior of a path with a uniform color.
* Erase along path: Draw a stroke that erase/remove information along a defined path.
* Smudge along path: Draw a stroke that smudges/blurs information along a defined path.

![Screenshot of the tool's toolbar showing the different path tool modes](../../assets/PathTools.png)

For example, here is the path tool in **Smudge** mode affecting other painting information:

![Gif showing a path tool in smudge mode](../../assets/v90_path_smudge.gif)

>[!NOTE]
>
> The **Path tools** only works in 3D space on the surface of the geometry. Creating a path in UV space or as a screen space projection is currently not supported.

### Editing a path

Path points (or vertices) adhere automatically to the surface of the mesh. They can be moved and adjusted at any time. It is possible to add new vertices to an existing path by clicking anywhere along the line.

* Pressing **Escape** or **Enter** will exit path edition.
* Once exited, clicking on a blank surface of the mesh will begin a new path.
* Hovering and clicking on an existing path will select it, allowing to continue or edit that path. Paths can also be re-selected via the **Paths** panel (see below).

![Gif showing the addition of new points and move of existing points on a path](../../assets/path_edit_move_points.gif)

Some properties are specific to a path as a whole. This is the case for options found in the **Properties** window. Just like with a regular stroke (see the [Paint tool documentation](paint-brush.md)), it is possible to define the following properties for a path:

* **Brush**
* **Alpha**
* **Material**

The **brush** section contains additional options which are only available with the Path tool:

| **Setting** | **Description** |
| --- | --- |
| **Projection depth** | Determines how close the path needs to be to the mesh surface for the brush stamps to appear. To see this visual feedback directly in the viewport, it is possible to enable **Normals** in the **Path display settings** (see below). |
| **Up axis** | The axis used to orient brush stamps when **Follow path** is off.   In some context, it makes more sense to have all the stamps aligned along a global axis/direcction and not along the path. For example with rivets on a metallic surface. |

Other properties are defined per points (vertices) on the path, such as the pressure. To edit a specific point, simply click on it (or use the rectangular selection). Then use the contextual toolbar to edit the selected points values.

![Gif showing the edition of pressure per vertex](../../assets/path_point_pressure_example.gif)

### Controlling tangents

There can be times where a smooth path is not ideal, either because it doesn't follow the best the 3D model surface or because it doesn't fit a specific look. To solve those issues, it is possible to modify the tangents of a given vertex. The tangents are the directions of a point that control how the path bend.

To switch between smooth or linear/broken tangents, simply double click on a vertex (or use the dedicated button in the contextual toolbar):

![Gid showing how to control tangents on a path](../../assets/path_break_tangents.gif)

To control more precisely the orientation of the tangents, use the Custom tangents button in the contextual toolbar to override them manually:

![Gid showing how to control tangents on a path](../../assets/path_control_tangents.gif)

Use the **ALT** keyboard shortcut to break the tangents while moving if the point wasn't already.

Use the **CTRL** keyboard shorcut to scale both tangents at the same time.

>[!NOTE]
>
> The tangent controls are defined along the plan that align with the normal of the given point in the path. This means that tangents cannot bend in some directions.

### Contextual toolbar

![Screenshot of the contextual toolbar in path mode](../../assets/path_contextual_toolbar_overview.png)

The **contextual toolbar** when the **Path** tool is selected provides several settings that allow to control the currently selected path:

<table>
  <tr>
    <th><strong>Parameter</strong></th>
    <th><strong>Description</strong></th>
  </tr>
  <tr>
    <td><strong>Show / hide viewport interface</strong><br><img src="../../assets/path_contextual_toolbar_showhide.png" alt="Path tool show hide icon"/></td>
    <td>If enabled, the paths and vertices overlay will be visible in the viewport.</td>
  </tr>
  <tr>
    <td><strong>Display settings</strong><br><img src="../../assets/path_contextual_toolbar_display.png" alt="Paht display settings icon"/></td>
    <td>Control the look of the path visual feedback in the viewport:<br><ul><li><strong>Handle size</strong>: control how big the path's points look like.</li><li><strong>Path width</strong>: control the thickness of the path line.<br></li><li><strong>Path color</strong>: control the color of the path line.<br></li><li><strong>Unselected path color</strong>: control the color of the non-active paths.<br></li><li><strong>Normals</strong>: If enabled, show the projection direction on eahc points of a path.<br></li><li><strong>Tangents</strong>: If enabled, show the curve direction of the control points of the path.<br></li><li><strong>Path direction</strong>: If enabled, show a little arrow at the end of the path to indicate its painting direction. This is useful to know how stamps within the stroke will be oriented.</li></ul><br><img src="../../assets/path_contextual_toolbar_display_settings.png" alt="Screenshot of the path display settings panel"/></td>
  </tr>
  <tr>
    <td><strong>Reverse path direction</strong><br><img src="../../assets/path_contextual_toolbar_direction.png" alt="Icon of reverse path direction"/></td>
    <td>Flip the direction of the current path. The direction defines the general orientation used to paint the stamps within the stroke. Inverting the path can help to re-orient the pattern drawn.</td>
  </tr>
  <tr>
    <td><strong>Toggle corner / smooth</strong><br><img src="../../assets/path_contextual_toolbar_smoothcorner.png" alt="Icon of toggle smooth corner"/></td>
    <td>Break or align the tangent of the currently selected vertices, allowing to switch between a smooth or linear curve.<br><img src="../../assets/path_smooth_corner_demo.png" alt="Screenshot of a path with both a smooth and linear path "/><br><strong>Note:</strong> Switch between the corner / smooth behavior can also be done by double-clicking on a point directly on the path.</td>
  </tr>
  <tr>
    <td><strong>Custom tangents</strong><br><img src="../../assets/path_icon_custom_tangents.png" alt="Paht tool icon for custom tangents"/></td>
    <td>If enabled, allow to manually control the tangents of a given point on the path.<br><img src="../../assets/paht_cutom_tangents_demo.png" alt="Image showing custom path tangents"/></td>
  </tr>
  <tr>
    <td><strong>Open / close path</strong><br><img src="../../assets/path_contextual_toolbar_close.png" alt="Icon of open close path"/></td>
    <td>Open or close the current path. To close a path, one of the two end points of the current path need to be selected first.<br><img src="../../assets/v90_path_open_close.gif" alt="Gif showing a path being open then closed"/></td>
  </tr>
  <tr>
    <td><strong>Delete vertex</strong><br><img src="../../assets/path_contextual_toolbar_delete.png" alt="Icon of delete path vertex"/></td>
    <td>Remove the currently selected vertices on a path.</td>
  </tr>
  <tr>
    <td><strong>Symmetry</strong><br><img src="../../assets/path_contextual_toolbar_symmetry.png" alt="Icon of symmetry feature"/></td>
    <td>Enable or disable symmetry for the current path. See the <a href="../symmetry/symmetry.md">symmetry documentation</a> for more information.<br><img src="../../assets/v90_path_symmetry.gif" alt="Gif showing a path being drawn in symmetry"/></td>
  </tr>
  <tr>
    <td><strong>Hide / ignore excluded geometry</strong><br><img src="../../assets/path_contextual_toolbar_exclude.png" alt="Icon of geometry mask exclude feature"/></td>
    <td>If enabled, make the current path paint through the hidden geometry. See the <a href="../../interface/layer-stack/geometry-mask.md">Geometry mask documentation</a> for more information.</td>
  </tr>
</table>

### Paths panel

![Path panel](../../assets/path_panel_visibility.png)

>[!NOTE]
>
> The panel is hidden when the current tool is not the Path tool or if a fill layer/folder is selected.

Inside the viewport is the **Paths** panel where are listed all the paths of the currently selected paint layer / effect. It provides an easy way to select and manage paths.

With this panel, it is possible to:

* Double-click on a path to **rename** it.
* **Delete** a path by selecting it and then pressing the delete key.
* **Copy**/**Paste**/**Duplicate** a path with the dedicated keyboard shortcuts.
* **Show** or **hide** a path with the eye icon (which control if the path is applied to the texturing).

For convenience, it is also possible to right-click on a path to open the contextual menu which offers the same actions:

![Path panel right click menu](../../assets/path_panel_rightclick_menu_copy_properties.png)

The right-click menu also open actions to copy the properties or position of a path onto another path. This allows to easily share or synchronize features across different paths:

![Gif showing how to copy and paste path properties](../../assets/path_copy_paste_properties.gif)![Gif showing how to copy and paste path positions](../../assets/path_copy_paste_vertices.gif)

>[!NOTE]
>
> Copy and pasting properties only work when paths are based on the same painting tool. For example it is not possible to share properties between a path using smudge settings and another using brush settings.

## Tool presets

![A screenshot of the presets section of the properties panel when a path tool is selected](../../assets/path_presets.png){width="400px"}

When a path tool is selected, a Presets section is available at the top of the Properties panel. From here you can quickly access presets for the various path tools.

### Favorite path presets

The Favorites option in the Presets section only holds presets that you've favorited for even faster access. To start adding favorites, select Favorites, then "Show compatible presets in assets" for a full list of available path presets.

To favorite a preset, right-click the preset in the Assets panel or in the Presets section of the Properties panel, then select "Add to favorites".

You can also remove presets from the favorites list. Right-click a Favorited preset, then select "Remove from favorites".

![A screenshot of the presets section of the properties panel when a path tool is selected. The Favorites option is selected, and the "Show compatible presets in Assets" button is highlighted.](../../assets/ShowCompatiblePresets.png){width="400px"}

### Create path presets

Like other tools, presets can be create to quickly restore brush settings / configurations. To do so, simply right-click in the **Properties** window and choose **Create tool preset.** This newly created preset will automatically switch to the Path tool when selected in the **Assets** window.