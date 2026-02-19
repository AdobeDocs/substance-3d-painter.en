---
title: "Lib Defines - Shader API"
description: "Access the Lib Defines shader API reference for Substance 3D Painter to define shader constants and preprocessor directives."
helpx_description: Painter > Scripting and development > API Reference > Shader API > Libraries - Shader API > Lib Defines - Shader API
helpx_url: "https://helpx.adobe.com/substance-3d-painter/scripting-and-development/api-reference/shader-api/libraries-shader-api/lib-defines-shader-api.html"
helpx_creative_field:
  - video
  - 3d-immersive
  - motion
helpx_experience_level:
  - any
helpx_learn_topic:
  - shading
  - symbols
  - creating-color-palettes
---




# Lib Defines - Shader API

## lib-defines.glsl

**Public Constants:** *M\_PI* *M\_2PI* *M\_INV\_PI* *M\_INV\_LOG2* *M\_GOLDEN\_RATIO*

Some useful constants

```

const float M_PI = 3.14159265; 

const float M_2PI = 2.0 * M_PI; 

const float M_INV_PI = 0.31830988; 

const float M_INV_LOG2 = 1.442695; 

const float M_GOLDEN_RATIO = 1.618034;
```


Blending modes constants

```

const int BlendingMode_Disable            =  0; 

const int BlendingMode_Replace            =  1; 

const int BlendingMode_Normal             =  2; 

const int BlendingMode_Darken             =  3; 

const int BlendingMode_Multiply           =  4; 

const int BlendingMode_ColorBurn          =  5; 

const int BlendingMode_LinearBurn         =  6; 

const int BlendingMode_Lighten            =  7; 

const int BlendingMode_Screen             =  8; 

const int BlendingMode_ColorDodge         =  9; 

const int BlendingMode_LinearDodge        = 10; 

const int BlendingMode_Overlay            = 11; 

const int BlendingMode_SoftLight          = 12; 

const int BlendingMode_HardLight          = 13; 

const int BlendingMode_VividLight         = 14; 

const int BlendingMode_LinearLight        = 15; 

const int BlendingMode_PinLight           = 16; 

const int BlendingMode_Difference         = 17; 

const int BlendingMode_Exclusion          = 18; 

const int BlendingMode_Tint               = 19; 

const int BlendingMode_Saturation         = 20; 

const int BlendingMode_Color              = 21; 

const int BlendingMode_Value              = 22; 

const int BlendingMode_Divide             = 23; 

const int BlendingMode_InverseDivide      = 24; 

const int BlendingMode_Passthru           = 25; 

const int BlendingMode_NM_Combine         = 26; 

const int BlendingMode_NM_Oriented        = 27; 

const int BlendingMode_NM_InverseOriented = 28; 

const int BlendingMode_Subtract           = 29; 

const int BlendingMode_InverseSubtract    = 30; 

const int BlendingMode_AddSub             = 31; 

 


```
