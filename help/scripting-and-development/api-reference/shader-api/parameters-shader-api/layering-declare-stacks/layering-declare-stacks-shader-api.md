---
title: "Layering Declare Stacks - Shader API"
description: "Access the Layering Declare Stacks shader API reference for Substance 3D Painter to create custom material layering stacks."
helpx_description: Painter > Scripting and development > API Reference > Shader API > Parameters - Shader API > Layering Declare Stacks - Shader API
helpx_url: "https://helpx.adobe.com/substance-3d-painter/scripting-and-development/api-reference/shader-api/parameters-shader-api/layering-declare-stacks-shader-api.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - layers
  - materials
  - replacing-backgrounds
---




# Layering Declare Stacks - Shader API

## Material layering: declare editable stacks

An editable stack is defined by a unique identifier and a list of document channels. Possible channel id(s) are: *ambientocclusion* *anisotropyangle* *anisotropylevel* *basecolor* *blendingmask* *diffuse* *displacement* *emissive* *glossiness* *height* *ior* *metallic* *normal* *opacity* *reflection* *roughness* *scattering* *specular* *specularlevel* *transmissive* *user0* *user1* *user2* *user3* *user4* *user5* *user6* *user7*

Example:

```

//:  stacks [ 

//:    { 

//:      "id": "Mask1", 

//:      "channels": [ 

//:        {"id": "opacity"} 

//:      ] 

//:    }, { 

//:      "id": "Mask2", 

//:      "channels": [ 

//:        {"id": "opacity"}, 

//:        {"id": "user0"} 

//:      ] 

//:    } 

//:  ]
```


To bind a channel from a stack to a sampler parameter, prefix the channel tag with the stack identifier:

```

//: param auto Mask1.channel_opacity 

uniform sampler2D mask_tex1; 

//: param auto Mask2.channel_opacity 

uniform sampler2D mask_tex2; 

 


```
