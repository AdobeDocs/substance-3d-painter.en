---
title: "Some HDPI scaling values are not working"
description: ""
helpx_description: "Painter > Technical support > Technical Issues > Rendering Issues > Some HDPI scaling values are not working"
---

# Some HDPI scaling values are not working

On Windows, some HDPI scale values (used to scale the interface on monitors with high resolutions) may not work properly.   
This is because our window framework (Qt) does not support them. We are unable to fix it until it is actually managed by the providers of the framework itself.

Therefore here is the behavior you may encounter depending of your settings :

* 120 DPI (**125%** scaling) - rendered as 96 DPI (**100%** scaling)
* 144 DPI (**150%** scaling) - rendered as 192 DPI (**200%** scaling)
* 168 DPI (**175%** scaling) - rendered as 192 DPI (**200%** scaling)

For more details, see: <https://bugreports.qt.io/browse/QTBUG-55654>
