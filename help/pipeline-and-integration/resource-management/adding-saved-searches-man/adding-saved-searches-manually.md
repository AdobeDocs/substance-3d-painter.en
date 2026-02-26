---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/pipeline-and-integration/resource-management/adding-saved-searches-manually.html"
breadcrumb-title: ""
description: Learn how to add saved searches manually in Substance 3D Painter to quickly access frequently used resource filters.
helpx_creative_field: ""
helpx_description: Painter > Pipeline and integration > Resource management > Adding saved searches manually
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Adding saved searches manually
user-guide-description: ""
user-guide-title: ""
---

# Adding saved searches manually

Assets search queries (or saved searches) can be defined by editing a configuration file. This page explains how.

## Location of the configuration file

In order to add custom saved queries, navigate to the to the user's Documents folder and open the **Shelf.ini** file.

<table data-preserve-html="true" style="width: 100.0%;"> <colgroup> <col style="width: 15.0%;"/> <col style="width: 15.0%;"/> <col style="width: 70.0%;"/> </colgroup> <tbody> <tr> <th>Platform</th> <th>Version</th> <th>Path</th> </tr> <tr> <td rowspan="2"><strong>Windows</strong></td> <td><strong>7.2</strong> or newer</td> <td colspan="1">C:&#92;Users&#92;username&#92;Documents&#92;Adobe&#92;Adobe Substance 3D Painter</td> </tr> <tr> <td colspan="1">Legacy</td> <td colspan="1">C:&#92;Users&#92;username&#92;Documents&#92;Allegorithmic&#92;Substance Painter</td> </tr> <tr> <td rowspan="2"><strong>Mac</strong></td> <td colspan="1"><strong>7.2</strong> or newer</td> <td colspan="1">/Users/username/Documents/Adobe/Adobe Substance 3D Painter</td> </tr> <tr> <td colspan="1">Legacy</td> <td colspan="1">/Users/username/Documents/Allegorithmic/Substance Painter</td> </tr> <tr> <td rowspan="2"><strong>Linux</strong></td> <td colspan="1"><strong>7.2</strong> or newer</td> <td colspan="1">/home/username/Documents/Adobe/Adobe Substance 3D Painter</td> </tr> <tr> <td>Legacy</td> <td colspan="1">/home/username/Documents/Allegorithmic/Substance Painter</td> </tr> </tbody> </table>

## Example

Below is an exmaple of content that can be put in the configuration file:

```

[filters] 

size=4 

1name=Grunge 

1query="u:basematerial=,smartmaterial=,smartmask=,texture=,procedural=,brush=,alpha= grunge" 

2name=Procedural 

2query="u:procedural=" 

3name=Environment 

3query="u:environment=" 

4name=Default Filters 

4query="p:/allegorithmic/^ u:filters="
```


Here is how the syntax works:

* **Size**: is determines the number of custom presets that need to be read and loaded by the application.
* **Number**: at the start of the line defines the current preset it targets (ex:  **1/**).
* **Query**: (after the number) defines the actual search terms used. In the example it uses  **u:**  for usages,  **p:**  for paths, or a string for a search term. The query content has to be wrapped in quotes. To learn about the terms that can be used, [see this page](../../../interface/assets/advanced-search-queries/advanced-search-queries.md).
* **Name**: the named of the preset.
