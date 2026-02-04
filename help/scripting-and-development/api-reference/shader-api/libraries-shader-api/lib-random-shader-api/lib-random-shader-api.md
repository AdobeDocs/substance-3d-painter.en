---
title: "Lib Random - Shader API"
description: ""
helpx_description: "Painter > Scripting and development > API Reference > Shader API > Libraries - Shader API > Lib Random - Shader API"
---

# Lib Random - Shader API

## lib-random.glsl

**Public Functions:** *getBlueNoiseThreshold* *getBlueNoiseThresholdTemporal* *fibonacci1D* *fibonacci2D* *fibonacci2DDitheredTemporal*

Import from library

```

import lib-defines.glsl
```


A 2D blue noise texture containing scalar values

```

//: param auto texture_blue_noise 

uniform sampler2D texture_blue_noise;
```


Blue noise texture resolution

```

const ivec2 texture_blue_noise_size = ivec2(256);
```


Current frame random seed

```

//: param auto random_seed 

uniform int alg_random_seed;
```


Get an uniform random value based on pixel coordinates.

```

float getBlueNoiseThreshold() 

{ 

  return texture(texture_blue_noise, gl_FragCoord.xy / vec2(texture_blue_noise_size)).x + 0.5 / 65536.0; 

}
```


Get an uniform random value based on pixel coordinates and frame id.

```

float getBlueNoiseThresholdTemporal() 

{ 

  return fract(getBlueNoiseThreshold() + M_GOLDEN_RATIO * alg_random_seed); 

}
```


Return the i*th* number from fibonacci sequence.

```

float fibonacci1D(int i) 

{ 

  return fract((float(i) + 1.0) * M_GOLDEN_RATIO); 

}
```


Return the i*th* couple from the fibonacci sequence. nbSample is required to get an uniform distribution.

```

vec2 fibonacci2D(int i, int nbSamples) 

{ 

  return vec2( 

    (float(i)+0.5) / float(nbSamples), 

    fibonacci1D(i) 

  ); 

}
```


Return the i*th* couple from the fibonacci sequence. nbSample is required to get an uniform distribution. This version has a per frame and per pixel pseudo-random rotation applied.

```

vec2 fibonacci2DDitheredTemporal(int i, int nbSamples) 

{ 

  vec2 s = fibonacci2D(i, nbSamples); 

  s.x += getBlueNoiseThresholdTemporal(); 

  return s; 

} 

 


```
