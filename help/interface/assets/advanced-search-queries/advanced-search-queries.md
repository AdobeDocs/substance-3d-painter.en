---
title: "Advanced search queries | Substance 3D Painter"
description: "Painter > Interface > Assets > Advanced search queries"
---

# Advanced search queries

Advanced search queries allow you to construct complex searches and reuse them as [Saved searches](../saved-searches/saved-searches.md).

Advanced queries can be used in the search bar and can contain -

1. **Path**  : allow to refine the result of a search by a folder/folder structure.
1. **Usage**  : List all the possible usage that are available in the application
1. **Text query**  : Allow to add any other type of query freely (like custom keywords)

Multiple selections are allowed when defining a new search query.

## Path

The path query allow to refine a query based on a path. The **Filter by Path** panel lists all the available libraries (which you can add yourself via Edit &gt; Settings &gt; Libraries).   
It is possible to use the path definition to filter by custom library path or by specific sub-folders in the hierarchy.

## Usage

Usage define what a resource is and how to use it in Substance 3D Painter. Some can be defined by the file type of the resource.   
For example-

* **pbr.glsl**: A shader file - it can only be used as a shader, and nothing else.
* **effect.sbsar**: A substance file - it can be a generator, a filter or even a material, so if its usage is not set in the original graph (in Designer), it will have to be indicated by the user in Painter at the moment of import.

## Text

The text query support multiple type of filtering, some being more advanced than the regular interface.   
They can be enabled by typing the right keywords.

* **Available search types**  :
  * "  **n:**  " : name
  * "  **s:**  " : shelf/library (includes "session" and "project")
  * "  **p:**  " : path
  * "  **u:**  " : usage
* **Escaping**  : it is possible to either use "  **\**  " before the character that need to be escaped or use quotes instead, example :
  * **a\ name\ with\ spaces**
  * **"a name with spaces"**
* **Specific attributes (or group)**  : to search in specific attributes, prepend a 'or group' with a type specifier. Example :
  * **n:a,b,c,d**  : name is a or b or c or d
* **Search behavior**  :
  * To filter specific usages, add the specific  **keyword**  to your search for example : "  **images**  ambient"
  * To add multiple request, use a comma "  **,**  ", for example : "cobalt  **,**  gold" (if a comma is you used, the search will only show a resource that match both keyword at the same time)
  * To search for an exact name, use an exclamation point "!" at the end, example :  **di!**  (will return  **dirt**  but not  **drips**  , this keyword disable the fuzzy matching)
  * To exclude a pattern from a search, use an hyphen "  **-**  ", for example :  **u:image n:-normal**  (will return images that don't contain "normal")
* **Matching functions (pattern suffix) :** 
  * **default**  : approximate matching (fuzzy)
  * **contains**  : !
  * **regex**  : #
  * **equal**  : =
  * **starts with**  : ^
  * **ends with**  : &amp;
