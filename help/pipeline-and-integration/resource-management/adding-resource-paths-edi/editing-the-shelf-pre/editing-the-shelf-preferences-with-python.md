---
title: "Edit Shelf Preferences with Python | Substance 3D Painter"
description: "Painter > Pipeline and integration > Resource management > Adding resource paths by editing preferences manually > Edit Shelf Preferences with Python"
---

# Editing the Shelf Preferences with Python

Below are example Python scripts to modify Windows registry in order to manipulate resource paths.

## Registry key path

See the table below to use the appropriate registry key path:

<table data-preserve-html="true"> <colgroup> <col/> <col/> <col/> </colgroup> <tbody> <tr> <th>System</th> <th>Version</th> <th>Path</th> </tr> <tr> <td rowspan="2"><p><strong>Windows</strong></p><p>(registry)</p></td> <td><strong>7.2</strong> or newer</td> <td>HKEY&#95;CURRENT&#95;USER&#92;Software&#92;Adobe&#92;Adobe Substance 3D Painter</td> </tr> <tr> <td>Legacy</td> <td>HKEY&#95;CURRENT&#95;USER&#92;Software&#92;Allegorithmic&#92;Substance Painter</td> </tr> <tr> <td rowspan="2"><p><strong>Mac</strong></p><p>(library)</p></td> <td><strong>7.2</strong> or newer</td> <td>/Users/&#91;username&#93;/Library/Preferences/com.adobe.Adobe Substance 3D Painter.plist</td> </tr> <tr> <td>Legacy</td> <td>/Users/&#91;username&#93;/Library/Preferences/com.substance3d.Substance Painter.plist</td> </tr> <tr> <td rowspan="2"><strong>Linux</strong></td> <td><strong>7.2</strong> or newer</td> <td>/home/&#91;username&#93;/.config/Adobe/Adobe Substance 3D Painter.conf</td> </tr> <tr> <td>Legacy</td> <td>/home/&#91;username&#93;/.config/Allegorithmic/Substance Painter.conf</td> </tr> </tbody> </table>

## Adding a new path

Adding a resource path requires to check which one exist already in order to increment the list with a new one.

The following code adds in the registry key a new shelf path after checking what is the current number of path already defined.

>[!NOTE]
>
> The sub-key **Shelf** (alongside **pathInfos**) may not be present in the registry. To make it appear start the application, open the preferences (Edit &gt; Settings) then click OK and close the application.

```

import winreg 

 

RegistryKeyName = "SOFTWARE\Adobe\Adobe Substance 3D Painter\Shelf\pathInfos" 

 

ShelfName = "myshelf" #Needs to be lowercase 

ShelfPath = "C:/Temp" 

ShelfStatus = "false" #false = not disabled 

 

RegConnection = winreg.ConnectRegistry( None, winreg.HKEY_CURRENT_USER ) 

  

## Open parent registry key

Key = winreg.OpenKey( RegConnection, RegistryKeyName, winreg.KEY_READ  ) 

 

## Iterate over each sub-key to retrieve the biggest Shelf number

SubKeyCount = winreg.QueryInfoKey( Key )[0] 

ShelfNumber = 0 

 

for x in range(SubKeyCount) : 

 SubKeyName = winreg.EnumKey(Key, x) 

 ShelfNumber = max( ShelfNumber, int(SubKeyName) ) 

 

ShelfNumber += 1 

 

## Create the new Key and add its values

NewKey = winreg.CreateKey( Key, str( ShelfNumber ) ) 

 

winreg.SetValueEx( NewKey, "disabled", 0, winreg.REG_SZ, ShelfStatus) 

winreg.SetValueEx( NewKey, "name", 0, winreg.REG_SZ, ShelfName) 

winreg.SetValueEx( NewKey, "path", 0, winreg.REG_SZ, ShelfPath) 

 

NewKey.Close() 

 

## Increment the Shelf path counter

Count = winreg.QueryValueEx( Key, "size" ) 

Key.Close() 

 

Key = winreg.OpenKeyEx( RegConnection, RegistryKeyName, 0, winreg.KEY_SET_VALUE  ) 

winreg.SetValueEx( Key, "size", 0, winreg.REG_DWORD, Count[0] + 1 ) 

Key.Close()
```


## Disabling or enabling a resource path

Any path created can be removed when not needed anymore, but also disabled for the default path which cannot be removed altogether.

The following code parse the Windows Registry and disable the default shelf (named "starter\_assets").

```

import winreg 

 

RegistryKeyName = "SOFTWARE\Adobe\Adobe Substance 3D Painter\Shelf\pathInfos" 

RegConnection = winreg.ConnectRegistry( None, winreg.HKEY_CURRENT_USER ) 

 

## Open registry key

Key    = winreg.OpenKey( RegConnection, RegistryKeyName, winreg.KEY_READ ) 

SubKeyCount  = winreg.QueryInfoKey( Key )[0] 

 

## Iterate over each sub-key

for x in range(SubKeyCount) : 

 SubKeyName = winreg.EnumKey(Key, x) 

 SubKey = winreg.OpenKey( 

  RegConnection, 

  RegistryKeyName + "\" + SubKeyName, 

  winreg.KEY_READ ) 

 SubKeyValueCount = winreg.QueryInfoKey( SubKey )[1] 

 

## Read subkey values

 Values = [] 

 for i in range( SubKeyValueCount ) : 

  Values.append( winreg.EnumValue( SubKey, i ) ) 

 

## Note : Values is a table of tuples

 FoundKey = False 

 for Value in Values : 

  if Value[0] == "name" : 

   if Value[1] == "starter_assets" : 

    FoundKey = True 

 

 SubKey.Close() 

 

## Found the path ? Then we edit the Key

 if FoundKey : 

  print( " - Editing Windows Registry" ) 

 

## Re-Open key in edition mode

  SubKey  = winreg.OpenKey(   

   winreg.HKEY_CURRENT_USER, 

   RegistryKeyName + "\" + SubKeyName, 

   0, 

   winreg.KEY_SET_VALUE ) 

 

## Assign new value

  winreg.SetValueEx(SubKey, "disabled", 0, 1, "true" ) #use "false" to Enable that shelf path 

 

  SubKey.Close() 

 

## Finish

Key.Close()
```
