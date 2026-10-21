---
breadcrumb-title: ""
description: Use the Polygon Fill tool in Substance 3D Painter to fill selected polygons with paint for efficient texture painting.
title: Polygon fill
user-guide-description: ""
user-guide-title: ""
---

# Polygon Fill

![](../../assets/v12-2/v12_banner_polygonfill.jpg)

The **Polygon Fill** tool fills polygons with material channel values or grayscale mask values. It can be used on paint layers, effects and masks to quickly fill regions of the mesh.

This tool is more of a painting tool than a selection tool: this is why after it has been used, it can only be erased via the eraser tool or by filling over it.

The tool can be accessed from the tool toolbar:

![](../../assets/v12-2/doc_polygonfill_toolbar.png)

## Settings

Below is the list of settings available with the **Polygon Fill** tool via the **Properties** window.

### Selection mode

![](../../assets/v12-2/doc_polygonfill_selection_mode.png)

The selection mode controls how triangles and quads of the mesh geometry are selected.

| **Mode** | **Description** |
|---|---|
| ![](../../assets/v12-2/v12_polyfill_icon_marquee.png) **Rectangular marquee fill** | Draw a rectangular selection by clicking and dragging. **Fill mode** defines what geometry is filled, while **Hit-test** defines which polygons are included. <br data-preserve-html="true"> ![](../../assets/v12-2/doc_polygon_fill_rectangle.gif) |
| ![](../../assets/v12-2/v12_polyfill_icon_loop.png)  **Polygon loop fill** | Fill a complete loop of quads with a single click. Dragging selects multiple loops. <br data-preserve-html="true"> ![](../../assets/v12-2/v12_polygon_fill_loop_mode.gif) |
| ![](../../assets/v12-2/v12_polyfill_icon_partial_loop.png) **Partial polygon loop fill** | Fill a portion of a loop by clicking and dragging. The selection can extend along secondary loops to form a patch of polygons. <br data-preserve-html="true"> ![](../../assets/v12-2/v12_polygon_fill_quad_mode.gif) |

### Fill mode

![](../../assets/v12-2/doc_polygonfill_fill_mode.png)

The fill mode, which can only be used with the **Rectangular marquee fill** mode, controls which parts of the geometry are selected.

| **Mode** | **Description** |
|---|---|
| ![](../../assets/v12-2/v12_polyfill_icon_triangle.png) **Triangle fill** | Fill individual mesh triangles. |
| ![](../../assets/v12-2/v12_polyfill_icon_polygon.png) **Polygon fill** | Fill entire polygons. On a mesh triangulated before import, the result is the same as **Triangle fill**. |
| ![](../../assets/v12-2/v12_polyfill_icon_mesh.png) **Mesh fill** | Fill every polygon connected to the one clicked. |
| ![](../../assets/v12-2/v12_polyfill_icon_uv_chunk.png) **UV chunk fill** | Fill polygons connected in UV space. The fill stops at UV borders. |

### Hit-test

![](../../assets/v12-2/doc_polygonfill_hittest.png)

The hit-test settings control how triangles and quads get selected by the **Rectangular marquee fill** mode.

| **Mode** | **Description** |
|---|---|
| ![](../../assets/v12-2/v12_polyfill_icon_intersection.png) **Intersection** | (default) A polygon is filled if any part of its geometry is inside or intersects the selection area. |
| ![](../../assets/v12-2/v12_polyfill_icon_contained_center.png) **Contained center** | A polygon is filled only if its center point lies inside the selection area. |
| **Visible polygons only** | If enabled, filling only affect polygons visible from the current camera view. Occluded and back-facing polygons are ignored. If disabled, polygons can be filled through the mesh. |

### Blending

![](../../assets/v12-2/v12_polyfill_blending.png)

These settings control how the fill result is mixed with the underlying pixels.

| **Parameter** | **Description** |
|---|---|
| Blending Mode | Control how the fill is blended with existing pixel values. In **Material** mode, the blending mode applies to all channels enabled in the **Material** section. |
| Opacity | Control the opacity of the fill. |

>[!NOTE]
>
> The tool supports the same blending modes available in the layer stack. For more information, see the [blending modes documentation page](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/interface/layer-stack/blending-modes).

### Material

![](../../assets/v12-2/v12_polygonfill_material.png)

The material section controls which channels can be enabled to be painted on by the tool.

## Shortcuts

The Polygon fill tool can be used effectively with the help of specific keyboard shortcuts:

|**Shortcut**|**Description**|
|---|---|
| **Alt** | With the **Polygon loop fill** and **Partial polygon loop fill**, this shortcut extends the selection on the other side of the initial click while dragging. <br data-preserve-html="true"> ![](../../assets/v12-2/doc_polygon_fill_alt.gif) |
| **Shift** | With the **Partial polygon loop fill**, this shortcut fills only the primary loop, ignoring the secondary loops. Example of toggling **Shift**: <br data-preserve-html="true"> ![](../../assets/v12-2/v12_polyfill_partial_loop_400px_15fps.gif) |
| **Shift + A** | This shortcut temporarily switches to **Polygon loop fill** from any other selection mode. If the shortcut is released before the mouse button, the selection continues until the mouse button is released. |
| **A** | If this shortcut is pressed while dragging, the current result is combined with the previous result. This works across blending modes and opacities: <br data-preserve-html="true"> ![](../../assets/v12-2/v12_polygon_fill_resume_a_shortcut.gif) |

## Limitations

Some limitations apply to the tool:

* **Polygon loop fill** and **Partial polygon loop fill** work on quads only, so triangles and n-gons can't be filled with these modes.
* **Radial symmetry** support is also limited and may be unreliable. To use symmetry prefer to use the mirror mode instead. See the [symmetry documentation page](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/painting/symmetry/symmetry) for more information.
* The tool fills geometry from the **active Texture Set** only. The wireframe is displayed for that Texture Set and updates when the active Texture Set changes.
