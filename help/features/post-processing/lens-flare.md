---
title: "Lens-flare"
description: ""
helpx_description: "Substance 3D Painter"
helpx_url: "https://helpx.adobe.com/substance-3d-painter/features/post-processing/lens-flare.html"
---

# Lens flare

![](../../assets/v12_post_flare.jpg)

Simulates the optical artifacts produced when bright light sources interact with camera lens elements, creating halos, streaks, and ghost reflections.

| <b>Parameter</b> | <b>Description</b> |
| --- | --- |
| <b>Resolution</b> | Sets the internal rendering resolution for the lens flare effect. Higher values produce sharper streaks but could impact performance. |
| <b>Camera</b> | Selects the camera model used to simulate the flare. Possible values are:<ul data-preserve-html="true"> <li data-preserve-html="true"><b>Panoramic Lens</b> (shorter focal length) </li> <li data-preserve-html="true"><b>Telephoto Lens</b> (longer focal length).</li> </ul> |
| <b>Amount</b> | Controls the overall intensity of the flare effect. The value can go beyond 1.0 to increase the intensity. |
| <b>Threshold</b> | Determines the minimal luminosity of the image required to generate a flare. Lower values cause more areas to produce flares, while higher values restrict the effect to very bright light sources. |
| <b>Aperture scale</b> | Scales the size of the aperture shape used for the flare computation, affecting the overall size of the flare elements. |
| <b>Coat thickness</b> | Simulates the anti-reflective coating on lens elements. Coating thickness affects how light scatters, and so changes the color of the flares. |
| <b>Coat IOR</b> | Simulates the index of refraction of the lens: how light passes through its thickness. Lower values produce more concentrated ghosts. |
| <b>Occlusion scale</b> | Sets the size of the affected center area. |
| <b>Occlusion smoothness</b> | Controls how gradually the lens flare fades. Higher values create softer transitions. |
| <b>Unique ghosts</b> | Defines how varied the flare shapes are. Higher values may significantly impact performance. |
| <b>Ghost position scale</b> | Controls the spread and size of the flare ghosts. |
| <b>Aperture texture</b> | Defines the shape of the lens aperture used to generate the flare pattern. The texture controls the diffraction and ghost shapes. |
