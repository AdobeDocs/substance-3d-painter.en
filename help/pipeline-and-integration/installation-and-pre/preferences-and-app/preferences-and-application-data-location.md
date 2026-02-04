---
title: "Preferences and application data location | Substance 3D Painter"
description: "Painter > Pipeline and integration > Installation and preferences > Preferences and application data location"
---

# Preferences and application data location

This page regroups information on where the application preferences are stored per version and platform.  
It can be useful to know where preferences are stored in case you want to add **custom shelfs** (for studios installations) or removing these preferences to perform a **clean installation** of the application.

## Preferences

This path is the location of the application preferences (saved shortcuts, Shelf/Asset paths, interface layout, etc).

<table data-preserve-html="true"><colgroup> <col/> <col/> <col/> </colgroup><tbody><tr><th>System</th><th>Version</th><th>Path</th></tr><tr><td rowspan="2"><p><strong>Windows</strong></p><p>(registry)</p></td><td><strong>7.2</strong> or newer</td><td>HKEY&#95;CURRENT&#95;USER&#92;Software&#92;Adobe&#92;Adobe Substance 3D Painter</td></tr><tr><td>Legacy</td><td>HKEY&#95;CURRENT&#95;USER&#92;Software&#92;Allegorithmic&#92;Substance Painter</td></tr><tr><td rowspan="2"><p><strong>Mac</strong></p><p>(library)</p></td><td><strong>7.2</strong> or newer</td><td>/Users/&#91;username&#93;/Library/Preferences/com.adobe.Adobe Substance 3D Painter.plist</td></tr><tr><td>Legacy</td><td>/Users/&#91;username&#93;/Library/Preferences/com.substance3d.Substance Painter.plist</td></tr><tr><td rowspan="2"><strong>Linux</strong></td><td><strong>7.2</strong> or newer</td><td>/home/&#91;username&#93;/.config/Adobe/Adobe Substance 3D Painter.conf</td></tr><tr><td>Legacy</td><td>/home/&#91;username&#93;/.config/Allegorithmic/Substance Painter.conf</td></tr></tbody></table>

## Application data

This path is the location of the additional application data (Assets thumbnails, log file, etc).

<table data-preserve-html="true"><colgroup> <col/> <col/> <col/> <col/> </colgroup><tbody><tr><th>Platform</th><th>Version</th><th colspan="2">Path</th></tr><tr><td rowspan="4"><strong>Windows</strong></td><td rowspan="2"><strong>7.2</strong> or newer</td><td colspan="1">App Data (local)</td><td colspan="1">C:&#92;Users&#92;&#91;username&#93;&#92;AppData&#92;Local&#92;Adobe&#92;Adobe Substance 3D Painter</td></tr><tr><td colspan="1">App Data (roaming)</td><td colspan="1">C:&#92;Users&#92;&#91;username&#93;&#92;AppData&#92;Roaming&#92;Adobe&#92;Adobe Substance 3D Painter</td></tr><tr><td rowspan="2">Legacy</td><td colspan="1">App Data (local)</td><td colspan="1">C:&#92;Users&#92;&#91;username&#93;&#92;AppData&#92;Local&#92;Allegorithmic&#92;Substance Painter</td></tr><tr><td colspan="1">App Data (roaming)</td><td colspan="1">C:&#92;Users&#92;&#91;username&#93;&#92;AppData&#92;Roaming&#92;Allegorithmic&#92;Substance Painter</td></tr><tr><td rowspan="2"><strong>Mac</strong></td><td colspan="1"><strong>7.2</strong> or newer</td><td colspan="2">/Users/&#91;username&#93;/Library/Application Support/Adobe/Adobe Substance 3D Painter</td></tr><tr><td colspan="1">Legacy</td><td colspan="2">/Users/&#91;username&#93;/Library/Application Support/Allegorithmic/Substance Painter</td></tr><tr><td rowspan="2"><strong>Linux</strong></td><td colspan="1"><strong>7.2</strong> or newer</td><td colspan="2">/home/&#91;username&#93;/.local/share/Adobe/Adobe Substance 3D Painter</td></tr><tr><td>Legacy</td><td colspan="2">/home/&#91;username&#93;/.local/share/Allegorithmic/Substance Painter</td></tr></tbody></table>

>[!NOTE]
>
> Some of the directories in the paths mentioned above may be hidden by default. Type the path manually in the file explorer or display hidden files to view them.
