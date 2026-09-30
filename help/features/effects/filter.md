---
title: Filters
description: Learn how to use filter effects in Substance 3D Painter to apply image processing filters and texture adjustments.
---

# Filters

Filter Effects are substances that transform the contents of a layer or mask. With the Passthrough blend mode, a layer can modify the results of the layer stack; using a filter on a layer with the Passthrough blend mode thus allows you to use filters to modify the layer stack as a whole.

## How can I apply a filter?

Depending of the filter type, a filter effect has to be created on the content or the mask of a layer. There are two ways to apply a filter:

* The manual approach requires multiple steps to set up the filter but provides direct control over each step of the process.
* The drag-and-drop approach allows you to add a filter quickly and automatically sets the blend mode to passthrough on all channels.

### Manually add a Filter

In the following example a blur filter is applied on the content of a layer, but it is more commonly used for applying Filters to Masks :

**1. Add a filter effect**

Start by selecting either the content of a layer or the layer mask then click on the **Effect button** (or right click to open the context menu). Select the option " **Add filter** " in the list.

![](../../assets/filters/filter-add-manually.gif)

**2. Select the filter in the properties window**

In the **Properties panel**, no filter has been selected yet. Click the Filter selection button to open the mini-shelf and select the desired filter, here we choose the **Blur filter**.
![](../../assets/filters/filter-select.gif)

>[!NOTE]
>
> When manually applying a filter, remember that you may need use the passthrough blend mode if you want the filter to affect the contents of the layers beneath it.

## Drag-and-Drop a Filter from the Shelf

This method is only intended for filters that should apply to the whole Layerstack. It will automatically set all Channel [Blending modes](../../interface/layer-stack/blending-modes.md) . It does not work for applying filters to a mask.

**1. Open the Filters area of the Shelf**

In the Shelf, click the "Filters" section to the left.

![](../../assets/shelf-filters.gif)

**2. Drag-and-Drop the Filter**

Select the filter you want to use in the shelf. Drag and Drop it into your layerstack, ensuring it is placed at the correct location (avoid dropping it into unwanted groups for example).

![](../../assets/filter-dragdrop.gif)

Note, in the above example, that the dropped filter already has a Passthrough Blending mode. This is true for all channels of the document.

## Add new filters to Painter

If you have new filters to bring into Painter, you can add them just like you would add standard resources - just drag-and-drop the SBSAR file onto the **Assets Panel** and you will be able to manage the import of your new filters.

## Create your own filters

All filters are Substances, which can be created with Substance 3D Designer. Substance 3D Designer provides templates for Substance 3D Painter to help you get started quickly.

For more information see this page : [Creating custom effects](../../content/creating-custom-effects/creating-custom-effects.md)

## Default filters in Painter

### Standard

* [Blur](filters/standard/blur.md)
* [Blur Directional](filters/standard/blur-directional.md)
* [Blur Slope](filters/standard/blur-slope.md)
* [Clamp](filters/standard/clamp.md)
* [Color Balance](filters/standard/color-balance.md)
* [Color Correct](filters/standard/color-correct.md)
* [Contrast Luminosity](filters/standard/contrast-luminosity.md)
* [Drop Shadow](filters/standard/drop-shadow.md)
* [Fill Area Color](filters/standard/fill-area-color.md)
* [Fill Area Mask](filters/standard/fill-area-mask.md)
* [FXAA (Anti-Aliasing)](filters/standard/fxaa-anti-aliasing.md)
* [Glow](filters/standard/glow.md)
* [Gradient](filters/standard/gradient.md)
* [Gradient Dynamic](filters/standard/gradient-dynamic.md)
* [Grayscale Conversion](filters/standard/grayscale-conversion.md)
* [Highpass](filters/standard/highpass.md)
* [Histogram Scan](filters/standard/histogram-scan.md)
* [Histogram Shift](filters/standard/histogram-shift.md)
* [HSL Perceptive](filters/standard/hsl-perceptive.md)
* [Invert](filters/standard/invert.md)
* [Mirror](filters/standard/mirror.md)
* [Pixelate](filters/standard/pixelate.md)
* [Posterize](filters/standard/posterize.md)
* [Sharpen](filters/standard/sharpen.md)
* [Smoothstep](filters/standard/smoothstep.md)
* [Threshold](filters/standard/threshold.md)
* [Transform](filters/standard/transform.md)
* [Warp](filters/standard/warp.md)

### Finishes

* [MatFinish Brushed Linear](filters/finishes/matfinish-brushed-linear.md)
* [MatFinish Galvanized](filters/finishes/matfinish-galvanized.md)
* [MatFinish Grainy](filters/finishes/matfinish-grainy.md)
* [MatFinish Grinded](filters/finishes/matfinish-grinded.md)
* [MatFinish Hammered](filters/finishes/matfinish-hammered.md)
* [MatFinish Perforated Circles](filters/finishes/matfinish-perforated-circles.md)
* [MatFinish Powder Coated](filters/finishes/matfinish-powder-coated.md)
* [MatFinish Raw](filters/finishes/matfinish-raw.md)
* [MatFinish Rough](filters/finishes/matfinish-rough.md)

### MatFX

* [MatFX Comic Book](filters/matfx/matfx-comic-book.md)
* [MatFX Detail Edge Wear](filters/matfx/matfx-detail-edge-wear.md)
* [MatFX Edge Damages](filters/matfx/matfx-edge-damages.md)
* [MatFX HBAO](filters/matfx/matfx-hbao.md)
* [MatFX Oil Paint](filters/matfx/matfx-oil-paint.md)
* [MatFX Peeling Paint](filters/matfx/matfx-peeling-paint.md)
* [MatFX Rust Weathering](filters/matfx/matfx-rust-weathering.md)
* [MatFX Shut Line](filters/matfx/matfx-shut-line.md)
* [MatFX Watercolor](filters/matfx/matfx-watercolor.md)
* [MatFX Water Drops](filters/matfx/matfx-water-drops.md)

### Lighting

* [Baked Lighting Environment](filters/lighting/baked-lighting-environment.md)
* [Baked Lighting Stylized](filters/lighting/baked-lighting-stylized.md)

### Advanced

* [Anisotropic Kuwahara](filters/advanced/anisotropic-kuwahara.md)
* [Bevel](filters/advanced/bevel.md)
* [Bevel Smooth](filters/advanced/bevel-smooth.md)
* [Color Match](filters/advanced/color-match.md)
* [Directional Distance](filters/advanced/directional-distance.md)
* [Gradient Curve](filters/advanced/gradient-curve.md)
* [Height Adjust](filters/advanced/height-adjustments.md)
* [Height To Normal](filters/advanced/height-to-normal.md)
* [Mask Outline](filters/advanced/mask-outline.md)
* [PBR Validate](filters/advanced/pbr-validate.md)
* [Quantize](filters/advanced/quantize.md)
* [Stylization](filters/advanced/stylization.md)
* [Tri-Planar Advanced](filters/advanced/tri-planar-advanced-filter.md)
