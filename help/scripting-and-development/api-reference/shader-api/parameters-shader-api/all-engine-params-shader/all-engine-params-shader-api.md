---
title: "All Engine Params - Shader API"
description: ""
helpx_description: "Painter > Scripting and development > API Reference > Shader API > Parameters - Shader API > All Engine Params - Shader API"
---

# All Engine Params - Shader API

## Engine parameters examples

## Texture parameters

Substance Painter uses a Sparse Virtual Texture (SVT) system to display textures in the viewport.

For more information about this system, go to the [online documentation](../../../../../features/sparse-virtual-textures/sparse-virtual-textures.md).

This system has repercussions on how to write shader code. We are providing helpers to simplify its use with the *SamplerSparse* structure and texture lookup functions (see [lib-sparse.glsl](../../libraries-shader-api/lib-sparse-shader-api/lib-sparse-shader-api.md)).

Basic usage:

```

// Defines the SamplerSparse structure 

import lib-sparse.glsl 

 

//: param auto TEXTURE_TAG 

uniform SamplerSparse uniform_tex;   // Texture sampler and its information
```


Texture parameters allow to use 'or' operator to define a fallback:

```

//: param auto TEXTURE_TAG_1 or TEXTURE_TAG_2 

uniform SamplerSparse uniform_tex; // if TEXTURE_TAG_1 exists then TEXTURE_TAG_1 else TEXTURE_TAG_2
```


Where *TEXTURE\_TAG* is one of the described tags below.

### Document's channels tags

All these textures are **premultiplied** and **dilated** to avoid seams problems.

**Texture set channels**

*channel\_ambientocclusion* *channel\_anisotropyangle* *channel\_anisotropylevel* *channel\_basecolor* *channel\_blendingmask* *channel\_diffuse* *channel\_displacement* *channel\_emissive* *channel\_glossiness* *channel\_height* *channel\_ior* *channel\_metallic* *channel\_normal* *channel\_opacity* *channel\_reflection* *channel\_roughness* *channel\_scattering* *channel\_specular* *channel\_specularlevel* *channel\_transmissive*

**User channels**

*channel\_user0* *channel\_user1* *channel\_user2* *channel\_user3* *channel\_user4* *channel\_user5* *channel\_user6* *channel\_user7*

### Mesh maps

*texture\_ambientocclusion* : Ambient Occlusion map  
*texture\_curvature* : Curvature map  
*texture\_id* : ID map  
*texture\_normal* : Tangent space normal map  
*texture\_normal\_ws* : World space normal map  
*texture\_position* : World space position map  
*texture\_thickness* : Thickness map

## Additional texture parameters

Basic usage:

```

//: param auto TEXTURE_TAG 

uniform sampler2D uniform_tex;   // The texture itself 

 

//: param auto TEXTURE_TAG_size 

uniform vec4 uniform_tex_size;   // The size of the texture (width, height, 1/width, 1/height)
```


Texture parameters allow to use 'or' operator to define a fallback:

```

//: param auto TEXTURE_TAG_1 or TEXTURE_TAG_2 

uniform sampler2D uniform_tex; // if TEXTURE_TAG_1 exists then TEXTURE_TAG_1 else TEXTURE_TAG_2 

 

//: param auto TEX_TAG_1_size or TEX_TAG_2_size 

uniform vec4 uniform_tex_size; // if TEX_TAG_1 exists then TEX_TAG_1_size else TEX_TAG_2_size
```


Where *TEXTURE\_TAG* is one of the described tags below.

*texture\_blue\_noise* : A blue noise texture  
*texture\_environment* : Environment map, **mip-mapped**, use [lib-env.glsl](../../libraries-shader-api/lib-env-shader-api/lib-env-shader-api.md) to use this one

## Other parameters

*aspect\_ratio* : a *float* containing the viewport *width / height* ratio

```

//: param auto aspect_ratio 

uniform float uniform_aspect_ratio;
```


*camera\_view\_matrix* : a *mat4* representing the transformation from world space to camera space

```

//: param auto camera_view_matrix 

uniform mat4 uniform_camera_view_matrix;
```


*camera\_view\_matrix\_it* : inverse transpose version of *camera\_view\_matrix*

```

//: param auto camera_view_matrix_it 

uniform mat4 uniform_camera_view_matrix_it;
```


*camera\_vp\_matrix\_inverse* : inverse of *projection \* camera\_view\_matrix* matrix

```

//: param auto camera_vp_matrix_inverse 

uniform mat4 uniform_camera_vp_matrix_inverse;
```


*environment\_exposure* : a *float* representing the envmap's exposure

```

//: param auto environment_exposure 

uniform float uniform_environment_exposure;
```


*environment\_max\_lod* : a *float* representing the envmap's depth of mip-map pyramid

```

//: param auto environment_max_lod 

uniform float uniform_max_lod;
```


*environment\_rotation* : a *float* representing the envmap's rotation around up axis  
 the value is in the range &#91;0,1&#93; and should be maped to the range &#91;0, 2\*pi&#93;

```

//: param auto environment_rotation 

uniform float uniform_environment_rotation;
```


*facing* : an *integer* indicating rendered faces (-1: back faces, 0: undefined, 1: front faces)  
 value of 0 means you can safely rely on glsl built-in variable *gl\_FrontFacing*

```

//: param auto facing 

uniform int uniform_facing;
```


*fovy* : a *float* representing the camera field of view along Y axis

```

//: param auto fovy 

uniform float uniform_fovy;
```


*is\_2d\_view* : a *bool* indicating whether the rendering is performed for 2D view or not

```

//: param auto is_2d_view 

uniform bool uniform_2d_view;
```


*is\_perspective\_projection* : a *bool* indicating whether the projection is perspective or orthographic

```

//: param auto is_perspective_projection 

uniform bool uniform_perspective_projection;
```


*main\_light* : a *vec4* indicating the position of the main light in the environment

```

//: param auto main_light 

uniform vec4 uniform_main_light;
```


*mvp\_matrix* : a *mat4* representing the model view projection matrix

```

//: param auto mvp_matrix 

uniform mat4 uniform_mvp_matrix;
```


*scene\_original\_radius* : a *float* representing the radius of the scene's bounding sphere before its normalization

```

//: param auto scene_original_radius 

uniform float uniform_scene_original_radius;
```


*screen\_size* : a *vec4* containing screen size data *(width, height, 1/width, 1/height)*

```

//: param auto screen_size 

uniform vec4 uniform_screen_size;
```


*world\_camera\_direction* : a *vec3* representing the world camera orientation

```

//: param auto world_camera_direction 

uniform vec3 uniform_world_camera_direction;
```


*world\_eye\_position* : a *vec3* representing the world eye position

```

//: param auto world_eye_position 

uniform vec3 uniform_world_eye_position; 

 


```
