---
title: "Changelog - Shader API"
description: ""
helpx_description: "Painter > Scripting and development > API Reference > Shader API > Changelog - Shader API"
---

# Changelog - Shader API

## Changelog

## 2018.3.2

* [lib-sparse.glsl](../libraries-shader-api/lib-sparse-shader-api/lib-sparse-shader-api.md): Sampling functions uses texture derivatives instead simple mipmap level. It's a requirement for the support of anisotropy sampling. Sampling functions signatures are not modified.
* [lib-pom.glsl](../libraries-shader-api/lib-pom-shader-api/lib-pom-shader-api.md): the *getParallaxOffset* function signature has changed in order to uses texture derivatives

## 2018.3.0

* Add a new [lib-pbr-aniso.glsl](../libraries-shader-api/lib-pbr-aniso-shader-api/lib-pbr-aniso-shader-api.md) library to help visualizing anisotropic specular highlight
* Add a new [lib-sparse.glsl](../libraries-shader-api/lib-sparse-shader-api/lib-sparse-shader-api.md) library to help channel sampling by taking care of mipmaps availability
* Update shader libraries interfaces to take care of this safe sampling
* **Deprecation**: The previous functions based on the vec2 texture coordinates and the texture sampler have been deprecated (please use new signatures)
* [lib-pom.glsl](../libraries-shader-api/lib-pom-shader-api/lib-pom-shader-api.md): Add a *applyParallaxOffset* function to simplify to use of parallax occlusion effect
* [lib-random.glsl](../libraries-shader-api/lib-random-shader-api/lib-random-shader-api.md): Add a Blue Noise random value generator and temporal alternatives
* [lib-sampler.glsl](../libraries-shader-api/lib-sampler-shader-api/lib-sampler-shader-api.md): Split all channel sampling helpers to have both value interpretation and sampling helpers

## 2018.2.0

* **Surface shader API change**: the *shade* function signature has changed, see [surface-shader.glsl](../shaders-shader-api/surface-shader-shader-api/surface-shader-shader-api.md)
* The *shadeShadow* function is no longer used and can safely be removed from custom surface shaders
* Add Subsurface Scattering support, see [surface-shader.glsl](../shaders-shader-api/surface-shader-shader-api/surface-shader-shader-api.md) and [lib-sss.glsl](../libraries-shader-api/lib-sss-shader-api/lib-sss-shader-api.md) for details
* [lib-pbr.glsl](../libraries-shader-api/lib-pbr-shader-api/lib-pbr-shader-api.md): the *pbrComputeBRDF* function has been removed. See [pbr-metal-rough.glsl](../shaders-shader-api/pbr-metal-rough-shader/pbr-metal-rough-shader-api.md) example to know how to use the library now
* New engine parameters have been added: *texture\_blue\_noise*, *aspect\_ratio*, *camera\_vp\_matrix\_inverse*, *environment\_exposure*, *environment\_rotation*, *fovy*, *main\_light* and *screen\_size*. See [all-engine-params.glsl](../parameters-shader-api/all-engine-params-shader/all-engine-params-shader-api.md) for details
* Add the *description* metadata to provide tooltips for custom shader parameters

## 2017.4.2

* Fix missing shaders in documentation samples (pixelated and toon shaders)
* Fix dithering for high resolution
  * [lib-bayer.glsl](../libraries-shader-api/lib-bayer-shader-api/lib-bayer-shader-api.md): **bayerMatrix8()** return valid values for coords &gt; 4k

## 2017.4.1

* Fix pbr-coated shader
  * [lib-vectors.glsl](../libraries-shader-api/lib-vectors-shader-api/lib-vectors-shader-api.md): **tangentSpaceToWorldSpace()** and **worldSpaceToTangentSpace()** outputs are now normalized

## 2017.4.0

* Incorrect specular reflection in the 2D view for certain meshes

## 2017.3.1

* Cheaper dithering

## 2017.2.0

* Remove interpolated tbn normalization to match Substance Designer and bakers behavior
* &#91;Viewport&#93; Replace Hammersley table by a Fibonacci spiral

## 2.6.0

* Fix shaders blending and culling modes
* Rework dithering. Now if we have a render in linear, we apply it after the color profile

## 2.5.0

* Add support for Color Profiles (LUT) in viewports (Optional sRGB conversion)
* Add dithering to opacity in shaders
* Add parallax occlusion mapping to PBR shaders
* Add a way to hide custom params from the default shader UI
* Add a link to channel tags list in layering shader documentation
* Replace 'channel\_ao' tag by 'channel\_ambientocclusion'
* &#91;Viewport&#93; Some normal maps have clamped values which appear as artifacts
* Fix available channels in shaders doc
* Allow to define a custom shader UI
* Add a standard custom shader UI for material layering shaders
* Custom UI files are now searched relatively to a shaders/custom-ui folder in the shelves (like the mdl)
* Use the specular level channel in default shaders
* Fix vec3 shader params example
* Upgrade Painter to OpenGL core profile

## 2.4.0

* Fix the difference on the normal map combined exported and the one displayed in the viewport

## 2.2.0

* Add support for bindless textures in generic material for non Document textures
* Update custom shader sliders documentation
* Allow to define step precision for sliders
* Documentation for dynamic material layering

## 2.1.1

* Add a 'RGB2Gray' function in lib-utils

## 2.1.0

* Allow to define groups for shader parameters and materials/masks
* Add missing channels in documentation ('ao', 'diffuse', 'specularlevel')

## 2.0.4

* Normal unpack function incorrect with low alpha values
* Allow to read mesh vertex colors in custom shader
* &#91;Viewport&#93; Stretched environment map on some computers

## 2.0.0

* Allow to override Normal/AO additional maps by dedicated channel
* Change Height2Normal function to use Sobel method
* Add the possibility to define a mdl per shader
* Add a new mdl folder in the shelf
* Add diffuse and specular level channel presets
* Documentation update for tone mapping
* Fix reflections when in orthographic mode
* Fixed the vertical white glitch appearing at a specific location on the envmap
* Allow to define 'default\_color' for texture params

## 1.7.0

* Allow to sample external textures (from shelf)

## 1.6.0

* Expose gamma/tonemapping function to allow to override them
* Expose multiple texcoords

## 1.5.0

* Add line number and filename in shader error report

## 1.4.1

* All sRGB conversions follow the sRGB standard, except those done in the shaders that have close approximation
* Height channel to Normal map is converted to the wrong color space

## 1.4.0

* Add ambient occlusion channel
* Add new workflow for normal edition
* Add 'or' expression syntax for texture related auto parameters
* Fix pbr shader for Intel gpu on OSX

## 1.3.4

* Allow to interpolate binormals in fragment shader
* Fix Mikkt tangent space

## 1.3.3

* Fix spherical harmonics producing negative light intensity
* Exposure computation is different from Substance Designer (and fix exposure slider)
* Shadows should not be visible on 100% metallic surface

## 1.3.0

* Add shadow function
* Add support for opacity ('alpha\_test' and 'alpha\_blend')

## 1.2.0

* Ability to set required openGL states into custom shaders
* Fix inverted bitangents
* Add support for normal channel

## 1.0

* Add support for custom shaders
