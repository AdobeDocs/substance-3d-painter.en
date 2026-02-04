---
title: "Corrupted project file"
description: ""
helpx_description: "Painter > Technical support > Workflow Issues > Project Issues > Corrupted project file"
---

# A project has been processed as a text file and is now corrupted

Sometimes the following error can appear when loading a project :

```

[Hdf5Archive] Archive 'project.spp' appears to have been processed as a text file and is irremediably corrupted. 

[Project management] The selected project 'project.spp' isn't valid!
```


This error means the project has been modified outside of Substance 3D Painter and  **cannot be read back properly**  .   
 It usually happens when a versioning software (such as  **Perforce**  ) processed the Substance 3D Painter project  **as a text file instead of a binary file**  . The only solution is to add a new rule/exception to the versioning software to force the processing of  **spp files as binary**  . For more information with  **Perforce**  , see the dedicated documentation : <https://www.perforce.com/perforce/r16.1/manuals/cmdref/p4_typemap.html>
