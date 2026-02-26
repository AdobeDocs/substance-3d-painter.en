---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/painting/presets/creating-particles-presets/overview-of-the-particle-editor.html"
breadcrumb-title: ""
description: Learn about the particle editor in Substance 3D Painter to create custom particle brush presets for texture painting.
helpx_creative_field: ""
helpx_description: Painter > Painting > Presets > Creating particles presets > Overview of the particle editor
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Overview of the particle editor
user-guide-description: ""
user-guide-title: ""
---

# Overview of the particle editor

This page covers several aspects of PopcornFX particle editor. Some of window titles and parameters may be subject to change depending on the version of the editor used.

## Viewport setup

### How to import your own mesh

Copy-paste your mesh in the “Meshes” folder of your Pack. Then in the Editor open your mesh and click on “Build”.

Now, in your particle system, go to “Backdrop” in the treeview, right-click on “3D Layers”, “New Backdrop”, “CNEdEditorBackdrop\_Model3D”, and select your mesh in “resource model”.

In Substance 3D Painter, the Mesh is scaled to be inside a box of size &#91;-1;1&#93; on each Axis. To get the right scale with Substance 3D Painter in the Editor, you should either import a mesh which is already scaled to fits in that box (easy way), or play with Scales in the Editor.

Note: only FBX mesh format are supported.

#### How to display the grid

Ctrl-G. You can customize the color of the grid in “Editor Properties” “GridColor”.

## Emitter

### How to create “OnCollide” events

The Physics Evolver handles collision with backdrop meshes in the scene. In Substance 3D Painter the scene will be your mesh.

First in the Physics Evolver set “WorldInteractionMode” to “OneWay” to enable particle collision. Then create an event called “OnCollide”, the Physics Evolver will trigger it on collision with the scene.

In Substance 3D Painter, the scene is the model you are working on, and all events called “OnCollide” will be overridden by the Emitter particle system of the current brush.

#### How to fire particles from the camera

On the top of the viewport, enable the 4th button “Constrain spawns on camera plane”.

Substance 3D Painter will by default fire Emitters from the camera.

#### How to emit particles on the top like rain

Disable “Constrain spawns on camera plane” if enabled.

Create a Particle Attribute called “Global”, now Substance 3D Painter will spawn your particles at the origin.

To spawn on the top of the mesh, add a Shape Sampler BOX or CYLINDER, place it on top, and sample it in your Spawner Script.

For example with a Shape Sampler BOX called “Spawn”, add this to your Spawner Script:

*Position = Spawn.samplePosition();*

## Receiver

### How to spawn the Emitter while creating/editing a Receiver

To get even closer to the Substance 3D Painter workflow while editing your Receiver, you can setup the Editor to override the particle system spawned.

In the treeview of your Receiver, select “Editor Properties”, then enable “UserOverSpawn” and select your emitter in “OverSpawnEffect”.

You still must open your Emitter to set the “OnCollide” events to spawn the Receiver you are currently editing.

#### How to setup particle fields

Here is the description of the particles field you must have in your Receiver:

*“Size” float*

The multiplicator of the brush size in Substance 3D Painter.

*“Opacity” float*

The multiplicator of the brush opacity in Substance 3D Painter.

*“UV” float3*

The texture coordinate on the mesh of particles.

In a Evolver Script, sample your Shape Sampler “Mesh” with the parametric coordinate given by the Projection Evolver:

UV = Mesh.sampleTexcoord(pCoords);

*“Normal” float3*

The normal of the mesh surface beneath particles.

In a Evolver Script, sample the Shape Sampler “Mesh” with the parametric coordinate given by the Projection Evolver:

Normal = normalize(Mesh.sampleNormal(pCoords));

*“Seed” int*

Just a randomly generated value for Substance 3D Painter:

In a Evolver Script add:

Seed = int(rand(0,20000000));

*“pCoords” int3*

Not used by Substance 3D Painter, but indispensable to do the particle projection on the mesh and sample other fields.

#### How to project particle on the mesh

Add a Projection Evolver in the “State\_0” of your Receiver.

Each frames, the Projection Evolver will project particles on the nearest surface of a Shape Sampler.

The Projection Evolver can fill out the parametric coordinate of the projection in the particle field specified by “OutputParametricCoordsField” (see “pCoords” particle field).

And it can reproject a vector on the surface of the mesh with “ReprojectedField”.

Here, we want to project particles on the Sampler Shape “Mesh”, fill out parametric coordinates in the int3 particle field “pCoords”, and project the “Velocity” on the surface too:

#### How to sample the mesh

In Substance 3D Painter, all Shape Samplers called “Mesh” and of “ShapeType” “MESH”, will be overridden with the mesh used in Substance 3D Painter.<b>  
</b>

In the Editor, set it to the same mesh as your backdrop.

To sample things in a Script, just write “Mesh.sample~Something~(pCoords)” in a Script, here is the documentation:

<https://wiki.popcornfx.com/index.php/CParticleSamplerShape#Script_bindings>

Some useful code snippets you will need:

```

// UV is the texture coordinate of the particle on the mesh

// Must be after CParticleEvolver_Projection

UV = Mesh.sampleTexcoord(pCoords);

// Normal is the Normal of the surface on the mesh just below the particle

// Must be after CParticleEvolver_Projection

Normal = normalize(Mesh.sampleNormal(pCoords));
```


## General tips

### How to import Emitter/Receiver in Substance 3D Painter

In Substance 3D Painter, do “File” &gt; “Import particles” or Ctrl-Alt-R then choose your Emitter.pkfx or Receiver.pkfx in you Pack.

Substance 3D Painter will automatically detect requirements (particle fields, OnCollide events) to decide if your pkfx is either an Emitter, Receiver or nothing compatible.

Now, you should see your Emitter/Receivers in the Shelf.

#### How to debug particle with a viable particle size

As the “Size” particle field must be between 0 and 1 to be a multiplier of the brush size in Substance 3D Painter, particles will be far too big in the Editor. So, add a custom field float “BBSize” set to 0.01 in the Spawner Script, to be used in the Billboard Particle Renderer as the “SizeField” to better see particle.

#### How to not mess up with evolver order

The order of the evolver can be very important.

For example, you might want to always have your 2 last evolvers to be the Projection Evolver then the Script Evolver which samples the UV and Normal with the pCoords generated by the Projection Evolver.

Keep in mind that the order of the evolvers is literally the order of execution inside a frame, and that Substance 3D Painter will gather particle field values and the end of each frame.

#### How to sample the mesh’s normal map

Substance 3D Painter will replace all Texture Samplers called “NormalMap” with the normal map of the mesh (if imported).

Thats the only texture you can have for now, all other texture will not be accessible by Substance 3D Painter.

Once you have add you Texture Sampler called “NormalMap”, you can sample it in a script :

<http://www.popcornfx.com/wiki/index.php/CParticleSamplerTexture>

Some useful code snippets:

```

// In Evolver Script convert the NormalMap texture in tangent space to world space normal

// /!\ the "Normal" particle field must always be the normal of the mesh not influenced by the normal map

// /!\ dont forget to initialize your particle fields in your Spawn Script

// otherwise pCoords and Normal will be invalid at the first update

float normalFactor = 1.0; // change the intensity of the normal map

float3 meshnormal = Normal;

float4 rawtangent = Mesh.sampleTangent(pCoords);

float3 binormal = normalize(cross(meshnormal, rawtangent.xyz) * rawtangent.w);

float3 tangent = normalize(cross(meshnormal, binormal));

float3 tsNormal = normalize(((NormalMap.sample(UV).xyz * 2.0 - 1.0).xyz) * float3(-normalFactor, normalFactor, 1));

float3 normal = normalize(tsNormal.x * tangent + tsNormal.y * binormal + tsNormal.z * meshnormal);
```


#### How to create turbulence

In the Editor, create a Turbulence Sampler.

<http://www.popcornfx.com/wiki/index.php/CParticleSamplerProceduralTurbulence>

Then you have 2 way to sample the Turbulence and affect particles:

##### The easy way

In the Physics Evolver of your layer, set “VelocityFieldSampler” to your Turbulence Sampler name, and set “Drag” to a value &gt; 0.

##### The parameterized way

You adjust turbulence with attributes by sampling the velocity field generated by your Turbulence Sampler in a Evolver Script:

Create 2 Particle Attributes:

* float “TurbulencePower” minmax: &#91;0;5&#93;
* float “TurbulenceScale” minmax: &#91;0.001; 5&#93; (needs to be &gt; 0)

Then create 3 Particle Fields:

float “TurbPower” and float “TurbScale”

To store attributes in them in the Spawner Script:

* TurbScale = 1.0 / TurbulenceScale;
* TurbPower = TurbulencePower;

float3 "VelocityField" in rotate mode.

It will be used as the “VelocityField” in the Physics Evolver (already set by default to the field “VelocityField”).

So before your Physics Evolver, in a Script Evolver, sample your Turbulence Sampler called “Turb”:

VelocityField = Turb.sample(Position \* TurbScale) \* TurbPower;

#### How to correctly use dt, the delta time

Delta time is the simulation time in seconds between each frame updates. In the Editor the delta time is updated with the real elapsed time. In Substance 3D Painter the delta time is fixed, and each updates is launched as soon as le last one is finished.

A game running at 60 FPS will have a delta time of 1/60= 0.016 seconds, so try to get your brushes running around 0.016s of delta time.

* Big deltas time &gt; 0.016s
* PRO fast update

As the time between updates is large, the movement of particles will be larger, so the Brush will run faster in Substance 3D Painter.

* CON approximation

PopcornFX is a kind-of big discretisation system, so bigger the dt is, bigger the imprecisions will be. See large delta time implication on turbulences: <http://www.popcornfx.com/wiki/index.php/CParticleEvolver_Physics#Dealing_with_turbulences_at_low_framerates>

* CON splats

If the delta time is large, particle movement between frame is large too. So, in Substance 3D Painter little spots might appears instead of straight lines.

This happens because Substance 3D Painter will draw one stroke point for each particles at the end of each frames, and don’t draw lines for each particles between the last and current frame.

* Little delta time &lt; 0.016s
* PRO precision

Smaller is the delta time, smaller distance between brush strokes will be, so sharper will be the drawing. And the discretisation of the simulation will be better too.

* CON slow

Smaller is the delta time, greater the number of updates will be necessary to draw the same distance distance.

Final tips on delta times : a good way to get the to right dt could be to start with a large one (0.1s) then decrease step by step to get the result you want.

#### How to expose parameters of your particle system

Substance 3D Painter will gather Particle Attributes of particle systems and expose them in the Physic Brush parameters:

<http://www.popcornfx.com/wiki/index.php/Particle_effect_attributes>

In PopcornFX you have the feature called “Attributes in Evolve” which allow you access Attribute in Evolve scripts: do not do that . Instead create particle field and store attribute in them in the Spawner Script, then use those particle field in Evovler Scripts. (this could be fixed in the future)

#### How to detect problematic particles

You should never have particles with weird particle field values, so make sure you break on problematic from times to times:

<http://www.popcornfx.com/wiki/index.php/Particle_tips_BreakOnProblematicParticle>

#### How to resolve particle systems problems in Substance 3D Painter

In the Substance 3D Painter installation directory, you should find a file called “popcorn.htm”. This file contain all the logs of PopcornFX, take a look inside to see what could happen wrong.

#### How to correctly initialize particle fields

To get valid pCoords UV and Normal from the first frame, add this to your Spawner Script:

<b>  
</b>

```

// PostEval() will be called after particles have been translated to their respective spawn locations

// so, PostEval() is executed in world space

function void PostEval()

{

// we need to initialize correctly the values needed by Substance 3D Painter:

pCoords = Mesh.projectParametricCoords(Position);

UV = Mesh.sampleTexcoord(pCoords);

Normal = normalize(Mesh.sampleNormal(pCoords));

}
```
