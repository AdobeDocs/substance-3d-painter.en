---
breadcrumb-title: ""
description: Review system requirements for Substance 3D Painter to ensure your computer meets hardware and software specifications.
title: System requirements
user-guide-description: ""
user-guide-title: ""
---

# Supported systems

Below is a list of hardware and systems supported by the application:

## Windows

|  | Minimum | Recommended | Optimal |
| --- | --- | --- | --- |
| **OS** | Windows 11 64-bit Version 23H2 | Windows 11 64-bit Version 24H1 | Windows 11 64-bit Version 24H2 |
| **CPU** | Intel Core i5 AMD Ryzen 5 | Intel Core i7 AMD Ryzen 7 | Intel Core i9 AMD Ryzen 9 |
| **GPU** | NVIDIA GeForce RTX 2060 Super NVIDIA Quadro RTX 4000 AMD Radeon RX 5700 XT AMD Radeon Pro W5700 | NVIDIA GeForce RTX 3080 NVIDIA Quadro RTX A4000 AMD Radeon RX 6800 XT AMD Radeon Pro W7700 | NVIDIA GeForce RTX 4090 NVIDIA Quadro RTX 5000 Ada Generation AMD Radeon RX 7900 XTX AMD Radeon Pro W7800 |
| **VRAM** | 8 GB | 16 GB | 24 GB |
| **RAM** | 16 GB | 32 GB | 64 GB |
| **Storage** | SSD with 30 GB of available space | SSD with 50 GB of available space | SSD with 70 GB of available space |

### macos

|  | Minimum | Recommended | Optimal |
| --- | --- | --- | --- |
| **OS** | macOS 15 Sequoia | macOS 27 Golden gate | macOS 27 Golden Gate |
| **CPU** | Apple M1 | Apple M2 Pro | Apple M4 Pro |
| **GPU** | Apple M1 | Apple M2 Pro | Apple M4 Pro |
| **RAM** | 16 GB | 32 GB | 64 GB |
| **Storage** | SSD with 30 GB of available space | SSD with 50 GB of available space | SSD with 70 GB of available space |

>[!WARNING]
>
> For pipelines built with the [VFX Reference Platform](https://vfxplatform.com/) in mind, Substance 3D Painter can still be installed on macOS 14 Sonoma. However, Painter is no longer tested on OS versions below the minimum system requirements, so stability is not guaranteed.

### Linux

| Enterprise | Steam |
| --- | --- |
| RHEL 8<br>RHEL 9 | Ubuntu 22.04 |

## General recommendations

To get good performance when using the UV Tile workflow we advise to use:

* 32GB of RAM
* GPU with 8GB of VRAM
* SSD to store both project and application cache.

Miscellaneous:

* Many Substance Apps depend on OpenSSL 1.1.1 for RHEL8/9 compatibility. For systems with newer OpenSSL versions, the customer will need to provide it manually
* For working in comfortable conditions we recommend a monitor with a vertical resolution greater than 1000 Pixels and wider than 1280 pixels.
* Exporting at **8K** (8192\*8192 pixels) requires a GPU with **more than** 2GB of VRam.
* Only versions 2019.x and above have been notarized in order to run on MacOS 10.15 (Catalina).
* To use the software via RDP (Remote Desktop) see the dedicated [documentation page](../pipeline-and-integration/configuration/remote-desktop.md).
* Crash on Ryzen CPU when baking, can be fixed by updating the BIOS.

## Unsupported configurations

**Windows**

* Virtual machines are not supported.
* Windows Server is not supported.

**Mac**

* Only official Apple configurations are supported.
* eGPUs are not currently supported and may have stability issues.

**Linux**

* Mesa drivers on Linux are not supported.

**Any platform**

* Integrated GPUs are not supported on x86-64 (Intel, AMD) CPUs.

## Minimum GPU driver versions

Below is a list of the minimum GPU driver versions required for the application to run without issue. This list is subject to change as new versions are released.

To download new drivers, see: [GPU has outdated drivers](../technical-support/technical-issues/gpu-issues/gpu-has-outdated-drivers.md).

| OS | NVIDIA | AMD | Intel |
| --- | --- | --- | --- |
| **Windows** | GeForce 442.50 Quadro 442.50 | Radeon 19.7.1 Radeon Pro / FirePro 18.Q4 | 15.33 |
| **Linux** | 535.171.04 or later | Radeon 22.40.6 | Unsupported |

>[!NOTE]
>
> On **Mac OS** the GPU driver is provided by the operating system itself. Update to the latest version of your OS to access the newest driver.

### Drivers compatibility issues

For a detailed list of GPU drivers issues per constructor please take a look a the [dedicated documentation page](../technical-support/technical-issues/gpu-issues/gpu-drivers-compatibility.md).

## GPU raytracing for baking

To enable GPU raytracing via Optix or DXR the minimum drivers recommended above must be installed.

**DXR** requires the following minimum configuration as well:

* **Windows 10** version 1809, see [this page](https://experienceleague.adobe.com/en/docs/substance-3d/bakers/features/gpu-raytracing) for more information
* **GPU with Pascal architecture** (Nvidia GeForce 10XX)

>[!TIP]
>
> GPU raytracing runs optimally on dedicated ray tracing hardware such as NVIDIA GeForce RTX or NVIDIA Quadro RTX GPUs.

## Supported graphic tablets

Below is a list of compatible graphic tablets which have been tested with Substance 3D Painter version **7.4.2**:

+++Wacom

**Models:** Intuos Pro (M size), Intuos (S size)

| OS | Driver version |
| --- | --- |
| Windows | 6.3.45-1 |
| macOS | 6.3.45-3 |

+++

+++XPen

**Model:** Deco 01

| OS | Driver version |
| --- | --- |
| Windows | XP-PENWin_3.2.2.211027 |
| macOS | XP-PENMac_3.2.3_211203 |
| Linux | XP-PEN-pentablet-3.2.1.211019-1 |

+++

+++Huion

**Model:** Q11K

| OS | Driver version |
| --- | --- |
| Windows | XP-PENWin_3.2.2.211027 |
| macOS | XP-PENMac_3.2.3_211203 |

+++

+++Xencelabs

**Model:** Pen Tablet Medium

| OS | Driver version |
| --- | --- |
| Windows | XencelabsWin_1.2.1-14 |
| macOS | XencelabsMac_1.2.1-18 |
| Linux | XencelabsLinux_1.1.0-2 |

+++

## Supported 3Dconnexion SpaceMouse models

Below is a list of compatible driver versions for the [3Dconnection Space Mouse](https://3dconnexion.com/us/spacemouse/) which have been tested with Substance 3D Painter version **8.1.**

The driver versions apply to the **Compact**, **Pro** and **Enterprise** models.

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
