---
title: "All Custom Params - Shader API"
description: ""
helpx_description: "Painter > Scripting and development > API Reference > Shader API > Parameters - Shader API > All Custom Params - Shader API"
---

# All Custom Params - Shader API

## Custom parameters sample shader

**Please note that all custom tweaks need at least a *default* value.**

Group your parameters by adding a *group* value.

Hide a parameter in the UI by setting a *visible* value to *false* .

Add a tooltip on the parameter by setting a *description* value.

## Color parameters

```

//: param custom { "default": 0, "label": "Color RGB", "widget": "color" } 

uniform vec3 u_color_float3; 

//: param custom { "default": 1, "label": "Color RGBA", "widget": "color" } 

uniform vec4 u_color_float4;
```


## Spinboxes parameters

```

//: param custom { "default": 0, "label": "Int spinbox" } 

uniform int u_spin_int1; 

//: param custom { "default": 0, "label": "Int2 spinbox" } 

uniform ivec2 u_spin_int2; 

//: param custom { "default": 0, "label": "Int3 spinbox" } 

uniform ivec3 u_spin_int3; 

//: param custom { "default": 0, "label": "Int4 spinbox" } 

uniform ivec4 u_spin_int4; 

//: param custom { "default": 0, "label": "Float spinbox" } 

uniform float u_spin_float1; 

//: param custom { "default": 0, "label": "Float2 spinbox" } 

uniform vec2 u_spin_float2; 

//: param custom { "default": 0, "label": "Float3 spinbox" } 

uniform vec3 u_spin_float3; 

//: param custom { "default": 0, "label": "Float4 spinbox" } 

uniform vec4 u_spin_float4;
```


## Slider parameters

```

//: param custom { "default": 0, "label": "Int slider", "min": 0, "max": 10 } 

uniform int u_slider_int1; 

//: param custom { "default": 0, "label": "Int slider", "min": 0, "max": 10, "step": 2 } 

uniform int u_slider_int1_stepped; 

//: param custom { "default": 0, "label": "Int2 slider", "min": 0, "max": 10 } 

uniform ivec2 u_slider_int2; 

//: param custom { "default": 0, "label": "Int3 slider", "min": 0, "max": 10 } 

uniform ivec3 u_slider_int3; 

//: param custom { "default": 0, "label": "Int4 slider", "min": 0, "max": 10 } 

uniform ivec4 u_slider_int4; 

//: param custom { "default": 0, "label": "Float slider", "min": 0.0, "max": 1.0 } 

uniform float u_slider_float1; 

//: param custom { "default": 0, "label": "Float2 slider", "min": 0.0, "max": 1.0 } 

uniform vec2 u_slider_float2; 

//: param custom { "default": [0.2, 0.5, 0.8], "label": "Float3 slider", "min": 0.0, "max": 1.0 } 

uniform vec3 u_slider_float3; 

//: param custom { "default": 0, "label": "Float4 slider", "min": 0.0, "max": 1.0, "step": 0.02 } 

uniform vec4 u_slider_float4_stepped;
```


## Bool parameters

```

//: param custom { "default": false, "label": "Boolean" } 

uniform bool u_bool;
```


## Sampler parameters

The texture is defined by its name in the shelf and must be in the *Textures* or *Environments* category.

```

//: param custom { "default": "", "default_color": [1.0, 1.0, 0.0, 1.0], "label": "Texture" } 

uniform sampler2D u_sampler1; 

//: param custom { "default": "texture_name", "label": "Texture" } 

uniform sampler2D u_sampler2; 

//: param custom { "default": "texture_name", "label": "Texture", "usage": "texture" } 

uniform sampler2D u_sampler3; 

//: param custom { "default": "texture_name", "label": "Texture", "usage": "environment" } 

uniform sampler2D u_sampler4;
```


## Combobox parameters

```

//: param custom { 

//:   "default": -1, 

//:   "label": "Combobox", 

//:   "widget": "combobox", 

//:   "values": { 

//:     "Value -1": -1, 

//:     "Value 0": 0, 

//:     "Value 10": 10 

//:   } 

//: } 

uniform int u_combobox;
```


Shader entry point

```

vec4 shade(V2F inputs) 

{ 

  // We simply return the value of the RGB color picker 

  return vec4(u_color_float3, 1.0); 

} 

 


```
