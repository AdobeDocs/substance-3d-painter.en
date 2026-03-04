---
helpx_url: "https://helpx.adobe.com/substance-3d-painter/getting-started/system-requirements.html"
breadcrumb-title: ""
description: Review system requirements for Substance 3D Painter to ensure your computer meets hardware and software specifications.
helpx_creative_field: ""
helpx_description: Painter > Getting Started > System requirements
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: System requirements
user-guide-description: ""
user-guide-title: ""
---

# Supported systems

Below is a list of hardware and systems supported by the application:

## Windows

|  | Minimum | Recommended | Optimal |
| --- | --- | --- | --- |
| <b>OS</b> | Windows 11 64-bit Version 23H2 | Windows 11 64-bit Version 24H1 | Windows 11 64-bit Version 24H2 |
| <b>CPU</b> | Intel Core i5 AMD Ryzen 5 | Intel Core i7 AMD Ryzen 7 | Intel Core i9 AMD Ryzen 9 |
| <b>GPU</b> | NVIDIA GeForce RTX 2060 Super NVIDIA Quadro RTX 4000 AMD Radeon RX 5700 XT AMD Radeon Pro W5700 | NVIDIA GeForce RTX 3080 NVIDIA Quadro RTX A4000 AMD Radeon RX 6800 XT AMD Radeon Pro W7700 | NVIDIA GeForce RTX 4090 NVIDIA Quadro RTX 5000 Ada Generation AMD Radeon RX 7900 XTX AMD Radeon Pro W7800 |
| <b>VRAM</b> | 8 GB | 16 GB | 24 GB |
| <b>RAM</b> | 16 GB | 32 GB | 64 GB |
| <b>Storage</b> | SSD with 30 GB of available space | SSD with 50 GB of available space | SSD with 70 GB of available space |

### macos

|  | Minimum | Recommended | Optimal |
| --- | --- | --- | --- |
| <b>OS</b> | macOS 12 Monterey | macOS 13 Ventura | macOS 14 Sonoma |
| <b>CPU</b> | Apple M1 | Apple M2 Pro | Apple M4 Pro |
| <b>GPU</b> | Apple M1 | Apple M2 Pro | Apple M4 Pro |
| <b>RAM</b> | 16 GB | 32 GB | 64 GB |
| <b>Storage</b> | SSD with 30 GB of available space | SSD with 50 GB of available space | SSD with 70 GB of available space |

### Linux

|  | Minimum | Recommended | Optimal |
| --- | --- | --- | --- |
| <b>OS</b> | <b>Enterprise ETLA</b>  RHEL 8.6 or later or RHEL 9.2 or later <b>Steam</b> Ubuntu 22.04.1 LTS | <b>Enterprise ETLA</b>  RHEL 8.6 or later  or RHEL 9.4 or later  <b>Steam</b> Ubuntu 22.04.1 LTS or later | <b>Enterprise ETLA</b>  RHEL 8.6 or later  or RHEL 9.4 or later  <b>Steam</b> Ubuntu 22.04.1 LTS or later |

## General recommendations

To get good performance when using the UV Tile workflow we advise to use:

* 32GB of RAM
* GPU with 8GB of VRAM
* SSD to store both project and application cache.

Miscellaneous:

* Many Substance Apps depend on OpenSSL 1.1.1 for RHEL8/9 compatibility. For systems with newer OpenSSL versions, the customer will need to provide it manually
* For working in comfortable conditions we recommend a monitor with a vertical resolution greater than 1000 Pixels and wider than 1280 pixels.
* Exporting at <b>8K</b> (8192\*8192 pixels) requires a GPU with <b>more than</b> 2GB of VRam.
* Only versions 2019.x and above have been notarized in order to run on MacOS 10.15 (Catalina).
* To use the software via RDP (Remote Desktop) see the dedicated [documentation page](../../pipeline-and-integration/configuration/remote-desktop/remote-desktop.md).
* Crash on Ryzen CPU when baking, can be fixed by updating the BIOS.

## Unsupported configurations

<b>Windows</b>

* Virtual machines are not supported.
* Windows Server is not supported.

<b>Mac</b>

* Only official Apple configurations are supported.
* eGPUs are not currently supported and may have stability issues.

<b>Linux</b>

* Mesa drivers on Linux are not supported.

<b>Any platform</b>

* Integrated GPUs are not supported on x86-64 (Intel, AMD) CPUs.

## Minimum GPU driver versions

Below is a list of the minimum GPU driver versions required for the application to run without issue. This list is subject to change as new versions are released.

To download new drivers, see: [GPU has outdated drivers](../../technical-support/technical-issues/gpu-issues/gpu-has-outdated-drivers/gpu-has-outdated-drivers.md).

| OS | NVIDIA | AMD | Intel |
| --- | --- | --- | --- |
| <b>Windows</b> | GeForce 442.50 Quadro 442.50 | Radeon 19.7.1 Radeon Pro / FirePro 18.Q4 | 15.33 |
| <b>Linux</b> | 535.171.04 or later | Radeon 22.40.6 | Unsupported |

>[!NOTE]
>
> On **Mac OS** the GPU driver is provided by the operating system itself. Update to the latest version of your OS to access the newest driver.

### Drivers compatibility issues

For a detailed list of GPU drivers issues per constructor please take a look a the [ dedicated documentation page](../../technical-support/technical-issues/gpu-issues/gpu-drivers-compatibility/gpu-drivers-compatibility.md).

## GPU raytracing for baking

To enable GPU raytracing via Optix or DXR the minimum drivers recommended above must be installed.

<b>DXR</b> requires the following minimum configuration as well:

* <b>Windows 10</b> version 1809, see [this page](https://experienceleague.adobe.com/en/docs/substance-3d/bakers/features/gpu-raytracing) for more information
* <b> GPU with Pascal architecture</b> (Nvidia GeForce 10XX)

>[!TIP]
>
> GPU raytracing runs optimally on dedicated ray tracing hardware such as NVIDIA GeForce RTX or NVIDIA Quadro RTX GPUs.

## Supported graphic tablets

Below is a list of compatible graphic tablets which have been tested with Substance 3D Painter version <b>7.4.2</b>:

+++Wacom
<b>Models:</b> Intuos Pro (M size), Intuos (S size)


| OS | Driver version |
| --- | --- |
| Windows | 6.3.45-1 |
| macOS | 6.3.45-3 |


+++

+++XPen
<b>Model:</b> Deco 01


| OS | Driver version |
| --- | --- |
| Windows | XP-PENWin\_3.2.2.211027 |
| macOS | XP-PENMac\_3.2.3\_211203 |
| Linux | XP-PEN-pentablet-3.2.1.211019-1 |


+++

+++Huion
<b>Model:</b> Q11K


| OS | Driver version |
| --- | --- |
| Windows | XP-PENWin\_3.2.2.211027 |
| macOS | XP-PENMac\_3.2.3\_211203 |


+++

+++Xencelabs
<b>Model:</b> Pen Tablet Medium


| OS | Driver version |
| --- | --- |
| Windows | XencelabsWin\_1.2.1-14 |
| macOS | XencelabsMac\_1.2.1-18 |
| Linux | XencelabsLinux\_1.1.0-2 |


+++

## Supported 3Dconnexion SpaceMouse models

Below is a list of compatible driver versions for the [3Dconnection Space Mouse](https://3dconnexion.com/us/spacemouse/) which have been tested with Substance 3D Painter version <b>8.1.</b>

The driver versions apply to the <b>Compact</b>, <b>Pro</b> and <b>Enterprise</b> models.

| OS | Driver version |
| --- | --- |
| Windows | 10.8.6.3431 |
| macOS | 10.7.2.3454 |

## Languages

The software interface is available in the following languages:

* English (United States)
* German
* Spanish
* French
* Italian
* Japanese
* Korean
* Portuguese (Brazil)
* Chinese (simplified)
