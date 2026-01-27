---
title: "All Rendering States Params - Shader API | Substance 3D Painter"
description: "Painter > Scripting and development > API Reference > Shader API > Parameters - Shader API > All Rendering States Params - Shader API"
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
