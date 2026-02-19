---
title: "Creating A New Particle Script"
description: "Learn how to create a new particle script in Substance 3D Painter to define custom particle brush behavior and effects."
helpx_description: Painter > Painting > Presets > Creating particles presets > Creating A New Particle Script
helpx_url: "https://helpx.adobe.com/substance-3d-painter/painting/presets/creating-particles-presets/creating-a-new-particle-script.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - 3d
  - xr
  - virtual-photography
---




# Creating A New Particle Script

Download the pre-setuped PopcornFX Package: [Templates\_EmitterReceiver.pkkg](https://helpx.adobe.com/content/dam/help/en/substance-3d/documentation/spdoc/files/67403778/68419585/1/1411557944000/templates-emitterreceiver.pkkg)

This package is a "start kit" that contains an emitter and a receiver we will edit and import in Substance 3D Painter.

## Popcorn fx setup

Launch PopcornFX Editor, create a new project, then open it.

In your project, right-click on an empty area and select "Import Popcorn Package". Then choose "Templates\_EmitterReceiver.pkkg".

Now, you should have:

* A particle system "\_Emitter" which is a base template of an Emitter.
* A particle system "\_Receiver" which is a base template of a Receiver.
* A sphere mesh used as the default backdrop of the scene

"\_Emitter" and "\_Receiver" are already "Painter ready". They have already been configured with the necessary evolvers, fields, backdrops etc…

## Import your mesh

PopcornFX only supports  **FBX**  , be sure to export your mesh in this format. During the export step, check the size of your mesh to try to fit with correct units in "real world".

Copy-paste it in the "meshes" folder of your project (in PopcornFX, you can right click on the "meshes" folder and select "Open File Location").

Come back to the editor, open your mesh (double click on it) and click on "  **Build**  ". Close the window, and save the change.

## Emitter/Receiver editing

We will duplicate existing particles systems and adapt them to correctly take the new mesh into account.

Right-click on the particle system "\_Emitter" (in the "Particles" folder), and select "Clone" (or "Duplicate") to create your own Emitter.

Open it and, in the "Particle Treeview" window (bottom left), select "  **Layer\_Model**  " which should be located in : "Editor Properties =&gt; Backdrop =&gt; 3D Layers".

Then, in the "Node Properties" window replace "dummymesh.fbx" by your model. Save the modification (File =&gt; Save) and close the emitter window.

Now,  **clone "\_Receiver**   **"**  (in the "Particles" folder), to create your own Receiver from this one.

Open it and, as for the emitter, replace the dummy mesh by your model in"Layer\_Model". We  **modified the mesh**   **displayed at the screen**  , but we also need to modify  **the mesh**   **used by the particles**  .

To do so, in the "Particle Treeview" window, click on "  **Shape**  " which should be located in : "Particle Effect =&gt; Spawner =&gt; Layer\_1 =&gt; Samplers =&gt; Mesh".

Then, replace the "MeshResource" by your model.

Once it’s done, there is one last thing to do: we need to "link" the emitter and the receiver with the one we have just created.

In the treeview of your Receiver, select "Editor Properties", then select your emitter in "OverSpawnEffect". Save the receiver.

Open your emitter (the one we previously duplicated) and in the "Particle Treeview" window, click on "Events" which should be located in : "Particle Effect =&gt; Spawner". Then replace the receiver by your receiver by clicking on "Extern".   
It’s done! Now if you select the 3D view (of your emitter or receiver), you can create particles by pressing "space" button.

## Optional: modify the receiver behavior

Open your receiver, and in the "Particles Treeview" window, select " CParticleEvolver\_Script " (the top one which is dedicated to you :)) which should be located in : "Particle Effect =&gt; Layer\_1 =&gt; State\_0".

In the "Specialized Node Editor" window, in the function, add "Life = 0.5;" to change the particles lifetime. Then use "Ctrl+s" shortcut to save you script. You should be able to notice the difference in the 3D view.

For more informations on how it works visit the link below:

<http://wiki.popcornfx.com/index.php/Main_Page>

## Import Emitter/Receiver in Substance 3D Painter

In Substance 3D Painter, do "File" &gt; "Import particles" or Ctrl-Alt-R then choose your Emitter and your Receiver (both in .pkfx format) in you Pack.

Substance 3D Painter will automatically detect requirements (particle fields, OnCollide events) to decide if your pkfx is either an Emitter, Receiver or nothing compatible.

Now, you should see your Emitter/Receivers in the Shelf (in "Emitters" and "Receivers" tabs).

To use them, you first need to click on the "Toggle particles" button.

Then, in the "Tool" window, in "Physics" you’ll have the possibility to select your emitter (to replace "default\_emitter") and your receiver (to replace default\_receiver).

You can now right click in the "Tool" window and save the tool.
