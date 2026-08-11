---
title: Dripping Rust
description: Learn how to use Substance 3D Painter's Dripping Rust generator.
---

# Dripping Rust

<table>
  <tr style="border: 0;">
    <td style="border: 0;" valign="top"><img src="../../../assets/generators/icon_dripping_rust.webp" alt=""/><br><strong>In:</strong> generator, grayscale, color</td>
    <td style="border: 0;" valign="top"><strong>Description</strong><br>The Dripping Rust generator creates streaks of rust that flow downward, simulating corrosion caused by gravity and water runoff.<br><br>The Dripping Rust generator outputs a monochrome (black and white) texture. As a result, it’s useful for generating masks to make a dripping rust effect.<br><br>Baked position, curvature and ambient occlusion are required as image inputs. <a href="../../../baking/baking.md">Learn more about baking here</a>.</td>
  </tr>
</table>

## Inputs

| Input name | Description |
| --- | --- |
| **Curvature** Grayscale | Use the baked Curvature map. |
| **Ambient occlusion** Grayscale | Use the baked Ambient Occlusion map. |
| **Position** Color | Use the baked Position map. |

## Parameters

<table>
  <tr>
    <th>Parameter name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><strong>Seed</strong></td>
    <td>Set the seed value used to generate the dirt texture. <br><ul><li>Click Random to switch to another random seed.</li><li>Click the pencil to see the current seed value, and enter a specific value if desired.</li></ul></td>
  </tr>
  <tr>
    <td><strong>Invert</strong></td>
    <td>Invert specific internal maps (e.g., Curvature, AO) before they're combined into the final mask.</td>
  </tr>
  <tr>
    <td><strong>Rust Spreading</strong></td>
    <td>Adjust the expanding of the dripping rust effect.</td>
  </tr>
  <tr>
    <td><strong>Rust Contrast</strong></td>
    <td>Adjust the contrast of the dripping rust effect.</td>
  </tr>
  <tr>
    <td><strong>Spreading Smoothness</strong></td>
    <td>Adjust the expanding softness of the dripping rust effect.</td>
  </tr>
  <tr>
    <td><strong>Drips Intensity</strong></td>
    <td>Adjust the length of the dripping rust effect.</td>
  </tr>
  <tr>
    <td><strong>Drips Smoothness</strong></td>
    <td>Adjust the softness of the dripping rust effect.</td>
  </tr>
  <tr>
    <td><strong>Drips Samples Amount</strong></td>
    <td>Adjust the quality of the effect (more samples for better quality).</td>
  </tr>
  <tr>
    <td><strong>Position axis</strong></td>
    <td>Switch between Y-Green channel, X-Red channel and B-Blue channel to change the direction of the dripping rust effect.</td>
  </tr>
</table>
