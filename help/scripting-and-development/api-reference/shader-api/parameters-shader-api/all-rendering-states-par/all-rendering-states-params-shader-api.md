---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/scripting-and-development/api-reference/shader-api/parameters-shader-api/all-rendering-states-params-shader-api.html"
breadcrumb-title: ""
description: Access the All Rendering States Params shader API reference for Substance 3D Painter to control rendering state parameters.
helpx_creative_field: ""
helpx_description: Painter > Scripting and development > API Reference > Shader API > Parameters - Shader API > All Rendering States Params - Shader API
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: All Rendering States Params - Shader API
user-guide-description: ""
user-guide-title: ""
---


# All Rendering States Params - Shader API

## Rendering states examples

## Backface culling

Cull back faces:

```

//: state cull_face on
```


Draw front and back faces:

```

//: state cull_face off
```


## Blending

No blending, fully opaque objects:

```

//: state blend none
```


Standard blending mode for back to front draw order:

```

//: state blend over
```


Standard blending mode for back to front draw order. Assume color is pre-multiplied by alpha:

```

//: state blend over_premult
```


Additive blending mode:

```

//: state blend add
```


Multiplicative blending mode:

```

//: state blend multiply
```


## Shader sampling locality

By default, document channels are sampled using untransformed texture coordinates for rendering optimizations during painting.

If artifacts appear set the *nonlocal* state to *on* .

```

//: state nonlocal on 

 


```
