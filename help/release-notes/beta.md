---
description: Learn about the current Substance 3D Painter beta including new features and a full changelog.
title: Beta release
---

# Beta release notes

## V12.2.1

This Beta version of Substance 3D Painter adds native support for Windows on ARM (ARM64) systems. Expect more releases over the coming weeks as the team works to improve stability.

### Build 3

**Fixed**:

* &lbrack;Mac&rbrack;&lbrack;OpenPBR&rbrack; Texture artifacts in viewport with specific subsurface radius scale values
* &lbrack;Mac&rbrack; Mipmap bias from Texture filtering in Display Settings has no effect
* &lbrack;Windows&rbrack;&lbrack;Nvidia&rbrack; Generation of brush and material previews can lead to a TDR

### Build 2

Release date: **November 2, 2026**

**Added**:

* &lbrack;Baking&rbrack; Highpoly Matching Error visualization uses Match-by-Name

**Fixed**:

* &lbrack;Python&rbrack; Some deprecated functions raise a warning but don't say who they are
* &lbrack;Baking&rbrack; Cage geometry can have holes when painting on one UV island
* &lbrack;Mac&rbrack;&lbrack;Baking&rbrack; Performance issue in baking mode viewport with cage painting

### Build 1

Release date: **October 21, 2026**

**Added**:

* Substance 3D Painter now natively supports WinARM machines.

**Fixed**:

* &lbrack;Baking&rbrack; Performance issue in baking mode viewport on Mac with cage painting.
