---
title: "Application failed to start because of Qt"
description: ""
helpx_description: "Painter > Technical support > Technical Issues > Startup Issues > Application failed to start because of Qt"
---

# Application failed to start because of Qt

The following error message may appear when starting the application:

> 

This application failed to start because no Qt platform plugin could be initialized&#46; Reinstalling the application may fix this problem&#46;

Available platforms plugins are: minimal, offscreen, webgl, windows&#46;

This error can be produced because another software defined environment variable that conflicts with the application.

Make sure to remove the following variables from the current environment before starting the application:

```

QT_PLUGIN_PATH 

QML2_IMPORT_PATH
```


>[!NOTE]
>
> These variables can be inherited from a Python context as well, for example with **pyinstaller**. Make sure to remove them from the context in which the application is launched.
