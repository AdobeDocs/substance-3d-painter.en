---
title: "Lib Bayer - Shader API"
description: ""
helpx_description: "Painter > Scripting and development > API Reference > Shader API > Libraries - Shader API > Lib Bayer - Shader API"
---

# Lib Bayer - Shader API

## lib-bayer.glsl

**Public Functions:** *bayerMatrix8*

```

float bayerMatrix8(uvec2 coords) { 

  return (float(bayer(coords.x, coords.y)) + 0.5) / 64.0; 

} 

 


```
