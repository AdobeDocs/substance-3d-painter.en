---
breadcrumb-title: ""
description: Access the Lib Bayer shader API reference for Substance 3D Painter to create Bayer dithering patterns in custom shaders.
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
