---
title: "Layering Bind Materials - Shader API"
description: ""
helpx_description: "Painter > Scripting and development > API Reference > Shader API > Parameters - Shader API > Layering Bind Materials - Shader API"
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


To bind a channel from a material to a sampler, define an auto param with the id of the material followed by the channel tag (see the available channels in [all-engine-params.glsl](../all-engine-params-shader/all-engine-params-shader-api.md)):

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
