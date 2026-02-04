---
title: "Lib Alpha - Shader API"
description: ""
helpx_description: "Painter > Scripting and development > API Reference > Shader API > Libraries - Shader API > Lib Alpha - Shader API"
---

# Lib Alpha - Shader API

## lib-alpha.glsl

**Public Functions:** *alphaKill*

```

import lib-sampler.glsl 

import lib-random.glsl
```


Opacity map, provided by the engine.

```

//: param auto channel_opacity 

uniform SamplerSparse opacity_tex;
```


Alpha test threshold.

```

//: param custom { 

//:   "default": 0.33, 

//:   "label": "Alpha threshold", 

//:   "min": 0.0, 

//:   "max": 1.0, 

//:   "group": "Common Parameters" 

//: } 

uniform float alpha_threshold;
```


Alpha test dithering.

```

//: param custom { 

//:   "default": false, 

//:   "label": "Alpha dithering", 

//:   "group": "Common Parameters" 

//: } 

uniform bool alpha_dither;
```


Emulate alpha test : discard current fragment if its opacity is below a user defined threshold. Should be called AFTER texture sampling calls: it can break derivatives

```

void alphaKill(float alpha) 

{ 

  float threshold = alpha_dither ? getBlueNoiseThresholdTemporal() : alpha_threshold; 

  if (alpha < threshold) discard; 

} 

 

void alphaKill(SparseCoord coord) 

{ 

  alphaKill(getOpacity(opacity_tex, coord)); 

} 

 


```
