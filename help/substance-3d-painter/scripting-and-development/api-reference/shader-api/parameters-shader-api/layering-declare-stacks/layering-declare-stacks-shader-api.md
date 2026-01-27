---
title: "Layering Declare Stacks - Shader API | Substance 3D Painter"
description: "Painter > Scripting and development > API Reference > Shader API > Parameters - Shader API > Layering Declare Stacks - Shader API"
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
