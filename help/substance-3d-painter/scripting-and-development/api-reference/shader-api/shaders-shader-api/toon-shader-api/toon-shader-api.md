---
title: "Toon - Shader API | Substance 3D Painter"
description: "Painter > Scripting and development > API Reference > Shader API > Shaders - Shader API > Toon - Shader API"
---

# Toon - Shader API

## Basic toon shader

Import from libraries.

```

import lib-sampler.glsl
```


We define the global light position

```

const vec3 light_pos = vec3(10.0, 10.0, 10.0);
```


We **bind** the auto param world eye position to our uniform **camera\_pos**.

```

//: param auto world_eye_position 

uniform vec3 camera_pos;
```


We **bind** the document's channel **base color** to our uniform **basecolor\_tex**.

```

//: param auto channel_basecolor 

uniform SamplerSparse basecolor_tex;
```


We **bind** the **mesh curvature** to our uniform **curvature\_tex**. If no curvature is available, transparent texture is provided.

```

//: param auto texture_curvature 

uniform SamplerSparse curvature_tex;
```


We define a new custom tweak for this shader, along with its default value. This one is used to tweak the thickness of outline, when shadowed.

```

//: param custom { 

//:  "default": 0.4, 

//:   "min": 0.0, 

//:   "max": 1.0, 

//:   "label": "Unlit outline thickness" 

//: } 

uniform float unlit_outline_thickness;
```


We define a new custom tweak for this shader, along with its default value. This one is used to tweak the thickness of outline, when lit.

```

//: param custom { 

//:   "default": 0.1, 

//:   "min": 0.0, 

//:   "max": 1.0, 

//:   "label": "Lit outline thickness" 

//: } 

uniform float lit_outline_thickness;
```


Whether we prefer using the curvature or not.

```

//: param custom { 

//:   "default": false, 

//:   "label": "Use curvature" 

//: } 

uniform bool use_curvature;
```


Entry point of the shader.

```

void shade(V2F inputs) 

{
```


We compute a few useful values.

```

  vec3 V = normalize(camera_pos - inputs.position); 

  vec3 N = normalize(inputs.normal); 

  vec3 L = normalize(light_pos - inputs.position); 

  float NdV = dot(N, V); 

  float NdL = max(0.0, dot(N, L));
```


**Priority** is to performs the **outline detection**. Allow the user to choose whether he prefers using the curvature map for outline detection or not.

```

  if (use_curvature) { 

    float curv = textureSparse(curvature_tex, inputs.sparse_coord).r; 

    NdV = 1.0 - curv; 

  }
```


If outline condition is reach, exit with black color.

```

  if (NdV < mix(unlit_outline_thickness, lit_outline_thickness, NdL)) { 

    return; 

  }
```


Here, we perform a 4 steps discretization of color.

```

  vec3 color = getBaseColor(basecolor_tex, inputs.sparse_coord); 

  if (NdL > 0.75) { 

    color = color; 

  } else if (NdL > 0.5) { 

    color = color * 0.5; 

  } else if (NdL > 0.1) { 

    color = color * 0.1; 

  } 

  else
```


Fallback is black.

```

    color = vec3(0.0); 

 

  diffuseShadingOutput(color); 

} 

 


```
