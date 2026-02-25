---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/scripting-and-development/api-reference/shader-api/libraries-shader-api/lib-env-shader-api.html"
breadcrumb-title: ""
description: Access the Lib Env shader API reference for Substance 3D Painter to work with environment maps and lighting in custom shaders.
helpx_creative_field: ""
helpx_description: Painter > Scripting and development > API Reference > Shader API > Libraries - Shader API > Lib Env - Shader API
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Lib Env - Shader API
user-guide-description: ""
user-guide-title: ""
---


# Lib Env - Shader API

## lib-env.glsl

**Public Functions:** *envSampleLOD* *envIrradiance*

Needed for math constants

```

import lib-defines.glsl
```


Engine provided parameters

```

//: param auto texture_environment 

uniform sampler2D environment_texture; 

//: param auto environment_rotation 

uniform float environment_rotation; 

//: param auto environment_exposure 

uniform float environment_exposure; 

//: param auto environment_irrad_mat_red 

uniform mat4 irrad_mat_red; 

//: param auto environment_irrad_mat_green 

uniform mat4 irrad_mat_green; 

//: param auto environment_irrad_mat_blue 

uniform mat4 irrad_mat_blue;
```


Helper that allows one to sample environment. Rotation is taken into account. The environment map is a panoramic env map behind the scene, that's why there is extra computation from dir vector.

```

vec3 envSampleLOD(vec3 dir, float lod) 

{ 

  // WORKAROUND: Intel GLSL compiler for HD5000 is bugged on OSX: 

  // https://bugs.chromium.org/p/chromium/issues/detail?id=308366 

  // It is necessary to replace atan(y, -x) by atan(y, -1.0 * x) to force 

  // the second parameter to be interpreted as a float 

  vec2 pos = M_INV_PI * vec2(atan(-dir.z, -1.0 * dir.x), 2.0 * asin(dir.y)); 

  pos = 0.5 * pos + vec2(0.5); 

  pos.x += environment_rotation; 

  return textureLod(environment_texture, pos, lod).rgb * environment_exposure; 

}
```


Return the irradiance for a given direction. The computation is based on environment's spherical harmonics projection.

```

vec3 envIrradiance(vec3 dir) 

{ 

  float rot = environment_rotation * M_2PI; 

  float crot = cos(rot); 

  float srot = sin(rot); 

  vec4 shDir = vec4(dir.xzy, 1.0); 

  shDir = vec4( 

    shDir.x * crot - shDir.y * srot, 

    shDir.x * srot + shDir.y * crot, 

    shDir.z, 

    1.0); 

  return max(vec3(0.0), vec3( 

      dot(shDir, irrad_mat_red * shDir), 

      dot(shDir, irrad_mat_green * shDir), 

      dot(shDir, irrad_mat_blue * shDir) 

    )) * environment_exposure; 

} 

 


```
