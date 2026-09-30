---
title: "Threshold"
description: "Learn how to use Substance 3D Painter's Threshold filter."
---

# Threshold

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Threshold icon](./Resources/icon_threshold.png "Threshold")

<b>In:</b> Effects/adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The Threshold filter returns white when the comparison criteria set in the Mode parameter is met for the input pixel value relative to the Threshold value. It is similar to Histogram Scan, but with contrast always at its maximum level, providing a faster and more precise way to achieve similar results.

It is used either directly on a fill layer or on a mask (black and white output) to quickly create a high contrast mask from specific channels.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

| Parameter name | Description |
| --- | --- |
| <b>Threshold:</b> | Adjust the luminance value against which the input pixel value is compared. |
| <b>Mode:</b> | Select the comparison criterion used against the threshold value: Greater, Greater or equal, Lower, or Lower or equal. |
| <b>_mode:</b> | Select the internal mode value. |
| <b>_threshold:</b> | Adjust the internal threshold value. |
| <b>_threshold_min:</b> | Adjust the internal minimum threshold value. |
| <b>_threshold_max:</b> | Adjust the internal maximum threshold value. |
