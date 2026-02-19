---
title: "Automated installation"
description: "Learn how to automate Substance 3D Painter installation for enterprise deployment and pipeline integration workflows."
helpx_description: Painter > Pipeline and integration > Installation and preferences > Automated installation
helpx_url: "https://helpx.adobe.com/substance-3d-painter/pipeline-and-integration/installation-and-preferences/automated-installation.html"
helpx_creative_field:
  - video
  - graphic-design
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - download-and-install
  - preparing-source-files
  - preflight
---




# Automated installation

When using the Substance 3D standalone installer, it is possible to install the application in silent mode for easier deployment.

We are using **InnoSetup** to generate the installer. The whole set of parameters that can be used with the installer is [available here](http://www.jrsoftware.org/ishelp/index.php?topic=setupcmdline).

## Installing in silent mode via command line

The flag to use to perform a silent install is **/SILENT**. The flag **/NCRC** can also be used to skip the CRC (verification) of the package in order to speed-up the process.

Example:

```

SubstancePainter_Installer.exe /NCRC /SILENT /DIR="C:InstallationFolder"
```


>[!NOTE]
>
> The installation path must be using single backslash character to separate folders, otherwise the installer will not recognize the path.
