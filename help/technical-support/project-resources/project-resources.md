---
title: "Project resources"
description: ""
helpx_description: "Substance 3D Painter"
---

# Project resources and settings

Managing project resources can help set a good foundation for your project's performance in Painter.

+++Downscale baked maps
Sometimes not all baked maps need to be at 2k or 4k resolutions. Don't hesitate to bake a batch at 2k, then rebake at a lower resolution to see if there is a visual difference.

+++

+++Manage imported bitmaps
Imported images can drastically affect performance, so it is important to be mindful of what is imported. If your Texture Sets are set to 2k and won't be exported at a higher resolution anyways, using an 8k image won't have any positive impact - its quality will be capped at 2k, as it is the Texture Set's resolution.

Format also matters - EXR, HDR and even PNG are much heavier than a JPG, and not all images may need the level of quality of an EXR (like Base Color vs. Height detail for example).

+++

+++Adjust shader settings
Specular quality at Ultra will give a more accurate result, but the setting is costly. The more effects enabled at once in the shader, the heavier the calculation is. Whenever possible, split complex materials to another Texture Set with a separate shader. If displacement is enabled, be careful with the tessellation parameter.

+++

+++Adjust file options
Use <b>File &gt; Save &gt; Save and reduce file</b> <b>size </b>to flush unneeded data, and use <b>Remove unused resources</b> to get rid of files imported to the project that are not being used anywhere inside the project.

+++
