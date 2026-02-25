---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/getting-started/glossary.html"
breadcrumb-title: ""
description: Access the glossary for Substance 3D Painter to understand key terms and concepts used throughout the documentation.
helpx_creative_field: ""
helpx_description: Painter > Getting Started > Glossary
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Glossary
user-guide-description: ""
user-guide-title: ""
---


# Glossary

Substance 3D Painter is a 3D application that relies on a lot of techniques and technical keywords which can be difficult to understand at first.   
This page lists the most common keywords used by the application alongside a short explanation of the concept behind it.

| *Keyword* | *Definition* |
| --- | --- |
| **Alignment** | The alignment is how a brush will be oriented toward the 3D mesh when painting. |
| **Alpha** | An alpha is a mask that can be used to paint details or complex shapes, for example a bar-code or a logo. |
| **Bake** | A bake (or baking) refer to the action of computing information from a 3D mesh and saving it into a Texture based on the UV information of a mesh. |
| **Bit Depth** | The bit depth is the amount of information that can be stored in a texture (per color). The higher the number, the better the precision of the information. However performance decrease with high numbers when doing computations. |
| **Brush** | A brush is a tool to paint on a mesh. A brush is defined by multiple parameters that control its behavior (such as the size and the opacity). |
| **Camera** | The camera is the object that allow to control the position and the direction of where you look at in a 3D or 2D viewport. |
| **Channel** | A channel is a texture with a specific behavior. Some channels are used to define the color of a material, some other channel are used to control the behavior light over a surface. |
| **Clone** | The clone is a tool used to replicate part of the painting/texture at other location. |
| **Content / Mask** | The content and the mask refer to the two main properties of a layer. The content is the actual painting stored in the channels that are contained in a layer, while the mask is used to display/hide the content. A black mask is equal to an invisible content. |
| **Diffusion** | The diffusion is a way or generating information outside the UV island of a mesh. It works by bleeding the last pixels near the border of an UV island, creating blurred colors. |
| **Dilation / Padding** | On the same idea as the diffusion, the dilation is a way of generating information outside UV island by extending pixels colors. |
| **Effect** | An effect is an element that can be added on a layer, either on the content or the mask. Substance 3D Painter support various type of effects such as filters. |
| **Environment** | An environment is an image that is used to compute the lighting of a scene, it is a usually an HDR texture that represent a wide range of color information. |
| **Export** | The action of exporting is the way of generating flattened textures from the painting realized inside the application. The textures created from the export can be used in other application. |
| **FOV / Field of View** | The FOV is the extent of the observable world by the Camera. |
| **Fill** | The Fill is an action (which can be an effect or a layer) that can load a color, a texture or even a material over the whole 3D Mesh. |
| **Filter** | A filter is a Substance effect that can modify the previous information. For example a blur filter will soften a previous image. Filters can also be more complex and modify a full material. |
| **Filtering** | Filtering refer to the way texture are displayed inside a 3D viewport. Most common are nearest (pixels are read as-is, making an image appera blocky up-close) and bilinear (pixels are interpolated, making an image appear blurry up close). |
| **GPU** | The GPU (Graphic Processing Unit) is the part of a computer that perform quick computation for producing images. |
| **Generator** | A Generator is a Substance that generate new information/images usually based on additional textures. For example some mask generator use baked texture to create complex masks. |
| **Histogram** | An histogram is a graphical representation of the distribution of color values. It is used to visualize how colors are balanced inside an image between shadows, midtones and highlights. |
| **Iray** | Iray is a path-tracer renderer created by NVIDIA, used to project a realistic lighting over the 3D mesh. Since it is an advanced renderer, it is meant for creating pretty images and not to be use for real-time work. |
| **Jitter** | The jitter is a property of the brush to produce random behavior when painting. |
| **Layer** | A layer is an element that contains multiple channels with additional property such as a blending mode and an opacity. |
| **Layer stack** | A layer stack is a place where layers can be managed and organized. Layers are organized from bottom to top. The bottom layer will be drawn first and then each layer above will be added one by one on top of eahc other. |
| **Lazy Mouse** | The lazy mouse is a behavior of the brush tool. It slow down the brush path to enhance the precision when painting, created a delay/offset between the mouse cursor and the actual painting. |
| **Level** | A level is an effect that allow to control a range or color/grayscale information via an histogram. It can be used to invert color or darken/brighten color for example. |
| **Log** | A log is a text file where are wrote information from the software, usually related to the computer running the application. |
| **Low / High poly mesh** | A low and a high poly mesh are both 3D mesh, one is with a low density of polygons while the other is with a higher amount of polycount (often 100 times bigger). Usually the high mesh information are baked down to the low mesh. |
| **Material** | A material define the properties to represent a specific matter. On a 3D Mesh, the material is also used to define groups of polygon faces. |
| **Mesh** | A mesh is a 3D object defined by multiple information. In Substance 3D Painter a mesh is defined by polygons (usually triangles). A mesh can be created in a 3D modeling application such as  **Blender**  or  **Autodesk Maya**  . |
| **Mesh map** | A mesh map is a map baked from a mesh that contains information relative to the mesh. It can be an information of position or an information of occlusion for example. |
| **Mip-Map** | A mip-map is a pre-computed texture, usually present as a sequence of image each time at a lower resolution than the original texture. |
| **Mode** | A mode refer to the setup of the interface which gives access to a specific set of tools and controls depending of the mode. |
| **Noise** | A noise is a procedural and random image, that usually represent organic shapes and color/grayscale values. |
| **Normal** | A normal is a special texture that deform the way a light behave on the surface of a 3D Mesh to simulate details that doesn't exist in the geometry. |
| **OpenGL / DirectX** | OpenGL and DirectX are both an application programming interface (API) used for rendering 2D and 3D information. They also define the normal map format. |
| **Orthographic** | An Orthographic projection is a means of representing three-dimensional objects in two dimensions in which all the projection lines are orthogonal to the projection plane. |
| **PBR / PBS** | Physically based Rendering (PBR) or Physically Based Shading (PBS) is a model in computer graphics that seeks to render graphics in a way that more accurately models the flow of light in the real world. |
| **Packing** | Packing is the action of storing multiple images inside one texture. Because textures are composed of separated Red, Green, and Blue channels, they can store different information which can be read independently in an other application. |
| **Particles** | Particles are a kind of tool that generate brush strokes based on physical properties or other complex behaviors. |
| **Perspective** | Perspective is an approximate representation or a object or scene seen by the human eye on a flat surface (like a screen). It's a simulation of depth and scale. |
| **Pixel / Texel** | A pixel is a dot in an image, it is the smallest element possible that contains color information. The bigger the resolution, the more pixels are available allowing a better definition and more details. Texels are pixels inside a texture. |
| **Plugin** | Plugins are programming functions (often expressed via scripting) that can be added to the software, extending the possibilities of the application. |
| **Post-Process** | A post-process is a visual effect applied on the screen once the 3D image has been rendered, often to simulate special behavior like color correction or bloom. |
| **Procedural** | Procedural is a terme to describe process that are generated by a computer based on a series of parameters. It can be simply mathematics results such as numbers or complex images. |
| **Projection** | A projection is the action of applying from a specific point of view (such as the Camera) an image/object onto the surface of the 3D Mesh. |
| **Resolution (Power of 2)** | The resolution define the size of a texture on its X and Y axis (or width and height). Often in a power of 2 scale (2, 4, 8, 16... 512, 1024, 2048...) because it is optimized for computations on a GPU. |
| **Scripting** | Scripting is the act or using specific command via a text based file format to execute specific behaviors. |
| **Shader** | A shader define the behavior of a material when it receives lighting information. Some shader can be simple (like toon shading) or more advanced (like skin shading that simulate light absorption in a surface). |
| **Shelf** | A shelf is the location in the application where ressource of multiple kind are organized. It can go from simple images to more complex tools. |
| **Smart Mask** | Smart Masks behave like smart materials, but instead of being layers, they are effects defined to generate mask only based on the current 3D Mesh. |
| **Smart Material** | A smart material is a group of layers saved as one file. Smart material can adapt to each project in Substance 3D Painter, allowing to create materials that will change depending on the current 3D mesh. |
| **Smudge** | The Smudge is a tool for bleeding, spreading or mixing colors. It is often used to soften pixels. |
| **Stencil** | A stencil is an image aligned to the screen and used with a camera projection to paint on the 3D Mesh. |
| **Substance** | A Substance is a file format that allow to generate texture based on a set of parameters (which involve procedural computations). These parameters can be modified to create variations. |
| **Symmetry** | The symmetry is an option of a tool that allow to paint at two places at the same time in mirror. |
| **Template** | A template is a set of predefined option used when creating a new project. It can define the default resolution or the default baking setting for example. |
| **Texel Ratio** | The texel ratio is the rule that compare the size of an UV island (2D) and the geometry of the 3D mesh related to it. A good texel ratio means a even unfolding of the geometry in 2D. This is important to keep the look and the quality of the painting/texturing consistent on the 3D Mesh. |
| **Texture** | A texture is a file containing pixels in 2 dimensions defined by a resolution. The pixels can be grayscale or colored. When colored, the pixels can have an information of transparency (if supported by the file format). |
| **Texture Set** | In Substance 3D Painter a texture set represent a part of a mesh that has specific UVs to be painted on. The Texture Set is created per unique material detected when importing a 3D mesh. |
| **Tilling** | Tilling is the repetition of a texture where seams are not visible at the borders, it is meant to simulate an infinite plane. Example : grass or pavements. |
| **Tool** | A tool refer to an action that allow to interact with the 3D Mesh, often to paint or apply effects. |
| **Toolbar** | The toolbar is the location where all the icon shortcuts to the tools are available. |
| **UDIM** | UDIM is a way or splitting the UVs of a 3D mesh across multiple ranges to increase the general texture resolution. |
| **UV** | UV are information defined on a 3D Mesh that indicate how it can be unfolded to become a flat shape. This information is used to project a texture onto a 3D Mesh. Substance 3D Painter only allow to paint in the range 0-1 which represent the size of a texture. Other ranges are only supported via the UDIM system. |
| **VRam** | The VRam is the memory of the GPU (Graphic Card), used to store information and texture when doing computations. The more VRam the better for working with Substance 3D Painter. |
| **Viewport** | The viewport is the place where the 3D or 2D scene is displayed on the screen. This is also where it is possible to interact with the tools and the 3D Mesh by controlling the camera. |
