---
breadcrumb-title: ""
description: Access the Lib Emissive shader API reference for Substance 3D Painter to create emissive materials and glowing effects.
title: Lib Emissive - Shader API
user-guide-description: ""
user-guide-title: ""
---

# Lib Emissive - Shader API

## lib-emissive.glsl

**Public Functions:** *pbrComputeEmissive*

Import from library

```

import lib-sparse.glsl
```


The emissive channel texture.

```

//: param auto channel_emissive 

uniform SamplerSparse emissive_tex;
```


A value used to tweak the emissive intensity.

```

//: param custom { 

//:   "default": 1.0, 

//:   "label": "Emissive Intensity", 

//:   "min": 0.0, 

//:   "max": 100.0, 

//:   "group": "Common Parameters" 

//: } 

uniform float emissive_intensity;
```


Compute the emissive radiance to the viewer's eye

```

vec3 pbrComputeEmissive(SamplerSparse emissive, SparseCoord coord) 

{ 

  return emissive_intensity * textureSparse(emissive, coord).rgb; 

} 

 


```
