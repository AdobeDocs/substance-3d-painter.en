---
title: "Layering Bind Materials - Shader API"
description: "Access the Layering Bind Materials shader API reference for Substance 3D Painter to bind materials in layered workflows."
helpx_description: Painter > Scripting and development > API Reference > Shader API > Parameters - Shader API > Layering Bind Materials - Shader API
helpx_url: "https://helpx.adobe.com/substance-3d-painter/scripting-and-development/api-reference/shader-api/parameters-shader-api/layering-bind-materials-shader-api.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - materials
  - pbr
  - shading
---




# Layering Bind Materials - Shader API

## Material layering: bind materials as shader parameters

A material is defined by a unique identifier 'id'. Additional parameters:

* 'default': the default material resource name to be used.
* 'size': the texture size of the material maps.
* 'group': the UI group of the material selection widget.

Example:

```

//:  materials [ 

//:    { 

//:       "id": "Material1", 

//:       "default": "Concrete 044", 

//:       "size": 512, 

//:       "group": "Material 1" 

//:    }, { 

//:       "id": "Material2", 

//:       "default": "Leaves elm", 

//:       "size": 1024, 

//:       "group": "Material 2" 

//:    } 

//:  ]
```


To bind a channel from a material to a sampler, define an auto param with the id of the material followed by the channel tag (see the available channels in [all-engine-params.glsl](../../../../../help/scripting-and-development/api-reference/shader-api/parameters-shader-api/all-engine-params-shader/all-engine-params-shader-api.md)):

```

//: param auto Material1.channel_basecolor 

uniform sampler2D basecolor_tex1; 

//: param auto Material1.channel_metallic 

uniform sampler2D metallic_tex1; 

//: param auto Material1.channel_roughness 

uniform sampler2D roughness_tex1; 

 

//: param auto Material2.channel_basecolor 

uniform sampler2D basecolor_tex2; 

//: param auto Material2.channel_metallic 

uniform sampler2D metallic_tex2; 

//: param auto Material2.channel_roughness 

uniform sampler2D roughness_tex2; 

 


```
