---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/pipeline-and-integration/configuration/environment-variables.html"
breadcrumb-title: ""
description: Learn how to use environment variables in Substance 3D Painter to configure application behavior and pipeline integration.
helpx_creative_field: ""
helpx_description: Painter > Pipeline and integration > Configuration > Environment variables
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Environment variables
user-guide-description: ""
user-guide-title: ""
---


# Environment variables

This page list environment variables that can be used to override the default behavior of the application.

| Variable | Description | Version |
| --- | --- | --- |
| **SUBSTANCE\_PAINTER\_LICENSE** | Value: Direct path to a license file itself.Allow to override the default location of the license file. Example : if the license file is on **H:/allegorithmic/licenses/substance\_painter.key**, the variable data should be **"H:/allegorithmic/licenses/substance\_painter.key"**.  **Note:**  Use SUBSTANCE\_PAINTER\_2\_LICENSE instead for version earlier than 3.x (2017.x). | <ol data-preserve-html="true"><li data-preserve-html="true">1</li></ol> |
| **ALLEGO\_LICENSE\_IDLE\_DELAY** | Value: 7200Specify how long in seconds before releasing a license seat in case of a multi-user configuration. Default is 2 hours (7200s). | <ol data-preserve-html="true"><li data-preserve-html="true">1</li></ol> |
| **ALG\_PAINTER\_SKIP\_CHECK\_FOR\_UPDATES** | Value : 0 or 1 (1 = Disable update check)Allows to skip update check when the application starts. Disable the What's new panel. | <ol data-preserve-html="true"><li data-preserve-html="true">2.2</li></ol> |
| **SUBSTANCE\_PAINTER\_SVT\_HARDWARE\_ACCELERATION** | Value: 0 or 1 (1 = Enabled)Use the Sparse feature on the GPU. If not supported by the GPU or the Operating System the setting will be ignored. For compatible hardware configurations refer to the documentation : [Sparse Virtual Textures](../../../features/sparse-virtual-textures/sparse-virtual-textures.md)This variable override the parameter available in the [Settings](../../../interface/settings/settings.md) window. | <ol data-preserve-html="true"><li data-preserve-html="true">3</li></ol> |
| **SUBSTANCE\_PAINTER\_TEMP\_LOCATION** | Value: Direct path to a folderDefines where Substance Painter should write its temporary files (including the SVT cache).This variable override the parameter available in the [Settings](../../../interface/settings/settings.md) window. | <ol data-preserve-html="true"><li data-preserve-html="true">3</li></ol> |
| **SUBSTANCE\_PAINTER\_PREVIEWS\_MEMORY\_BUDGET** | Value: 500Defines the amount of memory (Ram) that the application can use to load and temporary store previews from the Assets window. When the limit of the budget is reached old previews are unloaded. This value only controls the display of previews in the Assets window.The value is defined in megabytes. Default value is 500MB. | <ol data-preserve-html="true"><li data-preserve-html="true">2</li></ol> |
| **SUBSTANCE\_PAINTER\_PLUGINS\_PATH** | Location of additional Python plugins. | 6.1 |
| **PYTHONPATH** | Additional Python modules to load with the Python integration of the application. For more information see [Loading external Python modules](https://helpx.adobe.com/substance-3d/unlisted/documentation/spdoc/loading-external-python-modules-205363420.html). | <ol data-preserve-html="true"><li data-preserve-html="true">1</li></ol> |
| **OCIO** | Path to a **config.ocio** file which will be used to drive the [Color management](../../../features/color-management/color-management.md) settings with OpenColorIO.  **Note:**  This environment variable has priority over the **PAINTER\_ACE\_CONFIG** variable. | <ol data-preserve-html="true"><li data-preserve-html="true">4</li></ol> |
| **PAINTER\_ACE\_CONFIG** | Path to a json file which will be used to drive the [Color management](../../../features/color-management/color-management.md) settings with Adobe ACE. | <ol data-preserve-html="true"><li data-preserve-html="true">1</li></ol> |
| **SUBSTANCE\_DISABLE\_SPECIFIC\_FEATURES** | Disable several functionalities inside the applications:<ul data-preserve-html="true"><li data-preserve-html="true">Links to external resources (help, webpages, samples, etc)</li><li data-preserve-html="true">Disable checks for updates</li><li data-preserve-html="true">Disable sending of usage statistics</li><li data-preserve-html="true">Disable export to Substance Share</li><li data-preserve-html="true">Disable Welcome and What's new panels</li></ul> | <ol data-preserve-html="true"><li data-preserve-html="true">1</li></ol> |
| **ALG\_PAINTER\_DEBUG\_FPS** | Display inside the viewport a counter of how many frames per second are rendered by the viewport. | <ol data-preserve-html="true"><li data-preserve-html="true">1</li></ol> |
| **SUBSTANCE\_PAINTER\_VRAM\_BUDGET** | Specify how much GPU memory Painter can uses. This define a global budget in MB. For example to define a limit of 4GB use the value 4000.A command line argument can also be used to perform the same action. See [Command lines](../../../pipeline-and-integration/configuration/command-lines/command-lines.md). | <ol data-preserve-html="true"><li data-preserve-html="true">2.1</li></ol> |
