---
title: "Lib Bayer - Shader API"
description: "Access the Lib Bayer shader API reference for Substance 3D Painter to create Bayer dithering patterns in custom shaders."
helpx_description: Painter > Scripting and development > API Reference > Shader API > Libraries - Shader API > Lib Bayer - Shader API
helpx_url: "https://helpx.adobe.com/substance-3d-painter/scripting-and-development/api-reference/shader-api/libraries-shader-api/lib-bayer-shader-api.html"
helpx_creative_field:
  - 3d-immersive
  - motion
helpx_experience_level:
  - any
helpx_learn_topic:
  - shading
  - pbr
  - gradients
---




# Lib Bayer - Shader API

## lib-bayer.glsl

**Public Functions:** *bayerMatrix8*

```

float bayerMatrix8(uvec2 coords) { 

  return (float(bayer(coords.x, coords.y)) + 0.5) / 64.0; 

} 

 


```
