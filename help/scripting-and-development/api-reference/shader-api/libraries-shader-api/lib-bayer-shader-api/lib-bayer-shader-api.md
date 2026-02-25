---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/scripting-and-development/api-reference/shader-api/libraries-shader-api/lib-bayer-shader-api.html"
breadcrumb-title: ""
description: Access the Lib Bayer shader API reference for Substance 3D Painter to create Bayer dithering patterns in custom shaders.
helpx_creative_field: ""
helpx_description: Painter > Scripting and development > API Reference > Shader API > Libraries - Shader API > Lib Bayer - Shader API
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Lib Bayer - Shader API
user-guide-description: ""
user-guide-title: ""
---


# Lib Bayer - Shader API

## lib-bayer.glsl

**Public Functions:** *bayerMatrix8*

```

float bayerMatrix8(uvec2 coords) { 

  return (float(bayer(coords.x, coords.y)) + 0.5) / 64.0; 

} 

 


```
