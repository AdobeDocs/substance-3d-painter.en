---
title: "Preferences and content migration | Substance 3D Painter"
description: "Painter > Pipeline and integration > Resource management > Preferences and content migration"
---

# Preferences and content migration

This page describes how to migrate data from the preferences and Shelf/Assets to use them in the new versions.

After the release of version 7.2, the preferences and Shelf location have changed in order to make them common across the multiple version of the application (Substance 3D standalone, Steam and Creative Cloud Desktop). This change means previous preferences and custom resources **are now ignored** by default (**but not lost**). Since the **Shelf** has been renamed **Assets**, the migration involve a few steps detailed below.

## Migrating Shelf and Asset resources

The default user's resource location has changed which means any content that was put in the Documents folder is now ignored by new versions of the application. To restore this content simply move the files from one location to the other.

### Where to find the content

The Shelf or Assets path can be found at the following locations:

<table data-preserve-html="true" style="width: 100.0%;"><colgroup> <col style="width: 15.0%;"/> <col style="width: 15.0%;"/> <col style="width: 70.0%;"/> </colgroup><tbody><tr><th>Platform</th><th>Version</th><th>Path</th></tr><tr><td rowspan="2"><strong>Windows</strong></td><td><strong>7.2</strong> or newer</td><td colspan="1">C:&#92;Users&#92;username&#92;Documents&#92;Adobe&#92;Adobe Substance 3D Painter</td></tr><tr><td colspan="1">Legacy</td><td colspan="1">C:&#92;Users&#92;username&#92;Documents&#92;Allegorithmic&#92;Substance Painter</td></tr><tr><td rowspan="2"><strong>Mac</strong></td><td colspan="1"><strong>7.2</strong> or newer</td><td colspan="1">/Users/username/Documents/Adobe/Adobe Substance 3D Painter</td></tr><tr><td colspan="1">Legacy</td><td colspan="1">/Users/username/Documents/Allegorithmic/Substance Painter</td></tr><tr><td rowspan="2"><strong>Linux</strong></td><td colspan="1"><strong>7.2</strong> or newer</td><td colspan="1">/home/username/Documents/Adobe/Adobe Substance 3D Painter</td></tr><tr><td>Legacy</td><td colspan="1">/home/username/Documents/Allegorithmic/Substance Painter</td></tr></tbody></table>

### How to migrate the Shelf content

The old Shelf content is just files on the disk, so migrating them is just about putting these files in the right place.

1. Close the application
1. Navigate to the old Shelf folder
1. Copy or cut the sub-folders (alphas, procedurals, materials, etc)
1. Navigate to the new Assets folder
1. Paste the sub-folders you previously copied inside the Assets folder, overwrite if prompted to do so.

Now restart the application, the content should now appear in the Assets window.

>[!NOTE]
>
> Make sure to copy the sub-folders and not just the parent folder of the resources. The parent folder has been renamed from **shelf** to **assets**, so copying just the parent folder won't make the resources visible to the application.

### How to migrate the Shelf presets

Shelf presets are saved inside a configuration file. To migrate these presets:

1. Close the application
1. Navigate to the old Shelf folder
1. Copy or cut the Shelf.ini file
1. Navigate to the new Assets folder
1. Paste the file and overwrite the existing one

Now restart the application, the saved searches should appear in the dedicated section or the Assets window.

## Migrating preferences

We recommend to manually re-adjust the application settings from the interface. This is it the safest way to migrate information without introducing compatibility issues.

Otherwise take a look at the following page to know where preferences are now located: [Preferences and application data location](https://helpx.adobe.com/content/help/en/substance-3d/unlisted/documentation/spdoc/application-preferences-location-147095594.html).
