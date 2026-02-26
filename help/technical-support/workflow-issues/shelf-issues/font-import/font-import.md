---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/technical-support/workflow-issues/shelf-issues/font-import.html"
breadcrumb-title: ""
description: Learn how to fix font file import issues in Substance 3D Painter to successfully import and use font resources.
helpx_creative_field: ""
helpx_description: Substance 3D Painter
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Font file cannot be imported
user-guide-description: ""
user-guide-title: ""
---

# Font file cannot be imported

With the introduction of the [Text resource](../../../../painting/text-resource/text-resource.md), fonts file are automatically gathered on startup. Font files can also be manually imported.

In these cases a few error messages may appear:

* When drag and dropping a file into Painter's interface.
* When Painter is discovering fonts on the disk (library crawling).

## How to fix the problem

If an error message is raised about a <b>corrupted file</b>, try to find an alternate version of it and Painter's may be able to load it. Note that only <b>.ttf</b> and <b>.otf</b> formats are supported.

If an error message is raised about a <b>licensing issue</b>, then the font is simply not compatible with Painter and cannot be imported.

### Messages overview

|  |  |
| --- | --- |
| <b>Error message</b> | <b>Explanation</b> |
| There are issues in the “LIBRARYNAME” library affecting 4 font file(s): FONTNAME, FONTNAME, FONTNAME,… | This message gather a short list of font filenames that have been identified has not being importable inside Painter. These files will be ignored and won't appear in the Assets window. |
| Font issues found. For details, go to https://... | Generic message to indicate an issue has been found with fonts. |
| Can’t import FONTNAME because of its licensing restrictions. For details, go to https://... | Painter needs to be able to embed fonts into its project file to use them. Font that don't allow it (specified in their metadata) therefore cannot be imported. |
| Can’t import FONTNAME because the file is corrupted or an unsupported type. For details, go to https://... | Painter cannot read the font file provided. |
