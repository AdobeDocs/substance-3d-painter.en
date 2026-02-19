---
title: "Dynamic Stroke Performances"
description: "Learn about dynamic stroke performance considerations in Substance 3D Painter to optimize brush stroke rendering and responsiveness."
helpx_description: Painter > Painting > Dynamic strokes > Dynamic Stroke Performances
helpx_url: "https://helpx.adobe.com/substance-3d-painter/painting/dynamic-strokes/dynamic-stroke-performances.html"
helpx_creative_field:
  - video
  - 3d-immersive
  - painting-illustration
helpx_experience_level:
  - any
helpx_learn_topic:
  - painting
  - brushes
  - drawing
---




# Dynamic Stroke Performances

For Dynamic Strokes the performances of the Substance graph matters a lot because the Substance can be regenerated many time in a very short period. If a Substance computation is too heavy, it can create latency and therefore stutters and freezes when painting. All of that can end-up creating a bad painting experience. This page regroups information and recommendations on the use of the Dynamic Stroke feature.

## Dynamic Strokes computation can be heavy

Is is also important to know that the computation can have an impact in different contexts :

* **When painting**  : The Dynamic Stroke is generated (depending of its settings) while painting. Wrong configuration can make the painting slow and laggy.
* **When re-opening a project**  : Even if the painting process went fine, there is still a possibility that the computation stall when opening a project, making projects much longer to open than usual. That’s because the initial painting process went fine because the computation was spread over time, however it happens almost all at once when opening a project. This means a project could request thousands of unique Substance to generate if the Dynamic Stroke wasn’t properly configured.
* **Memory consumption**  : Generating a lot of variations for a Substance graph could end-up consuming a lot of memory (because these generations are volatile as they are made on the fly).

## Using Jitters and Spacing settings

While it is easy to implement impressive or advanced effects inside the Substance itself, it can sometimes be more beneficial to keep it simple and use instead native settings of Substance 3D Painter’s tool parameters. These settings are much faster to compute for the paint engine :

* **Jitter**  : These parameters allow to create randomness very cheaply by changing some attributes without recomputing the Substance (such as the angle, position and opacity).
* **Spacing**  : The smaller the spacing is, the more stamps are created when painting a stroke. Sometimes there is no need for a continuous brush stroke and using a large spacing can also help see better the alpha/material used.

## When and which type of Random to use

The Random Seed is a great way to generate uniqueness. The problem is that the generation can be costly and in the case of the Dynamic Stroke feature it can happen quite often if not tweaked properly. It is important to understand when to use the Random Seed and when to avoid it and rather prefer an alternative method to get the best trade-of between visuals and performance :

* **Random Seed Per Stamp**  : In this case a new unique Substance generation will happen for each Stamp. This is fine for creating unique nails on a wood plank for example, but not if you are creating ink/paint trails.
* **Random Seed Per Stroke**  : A unique Random Seed is created for the current brush stroke. This is useful when having few stamps but the need for a new set of variations with each strokes (like a spray effect).
* **Static Random Seed**  : The Substance is generated once and will never change. Optimal for performances but maybe too restrictive depending of your needs.

What about  **Time**  ($time) ?   
 Time may be handy for creating some very specific looks but it is actually one of the most expensive variable to use in a Substance graph. The reason is because it is very hard to get similar values from one brush stroke to the other, so the brush engine will likely generate new variations all the time. Avoid it if you can, use the spacing and the Stamp Index instead which combined can lead to similar results.

## StampIndex and StampCycleCount usage

The  **StampIndex**  is the ID of an individual stamp inside a brush stroke. By default it starts at 0 and increase by 1 for each new stamp. The  **StampCycleCount**  is a way to limit the amount of unique indexes and tells Substance 3D Painter to recycle/re-use the already generated Substance graphs. When the current ID reaches the limit Substance 3D Painter will start again from 0, creating a loop.

The best solution for having randomness while keeping good performances is therefore to take advantage of the Cycle Count with the following :

* **StampIndex as RandomSeed**  : When creating a Substance graph it is possible to set the Random Seed as Absolute. By doing so you can feed it a custom value which can be the Stamp Index. This will create a unique Substance graph version for each stamp inside your stroke.
* **Combined with the StampCycleCount**  : you can actually create a limited set of new variations and then re-use them.
* **Random Start**  : If the cycle count is set to start from a random value instead of 0, this means it will use get a different Substance version at the beginning for each stroke inside the pool of already generated graphs.

## Disabling computation based on parameters values

Substance 3D Painter cannot determine when tweaking a parameter that it can result in the same output, simply because the computation is hidden within the Substance graph. This is basically a black box.

In order to help performance when tweaking parameters and painting with Dynamic Strokes, it is possible to specify when new graph instances should be generated by using conditional values in the userdata fields of the Substance graph.

Possible values are:

| *Variable* | *Usage* |
| --- | --- |
| **IsStampIndexActive** | Used to determine if the Stamp Index should change during painting. |
| **IsRandomSeedActive** | Used to determine if the Random Seed should change during painting. |
| **IsTimeActive** | Used to determine if the Time ($time) should increment during painting. |

For example:

```

IsRandomSeedActive=input.roundness_jitter>0 || input.flip_x_jitter || input.flip_y_jitter
```


In this case, the random seed will be changed only if the graph parameter (identifier)  **roundness\_jitter**  is greater than 0 or if the boolean  **flip\_x\_jitter**  or  **flip\_y\_jitter**  are enabled. If the condition is not met, the graph won't be regenerated. Graph parameters have to be prefixed by "  **input.**  " to be recognized.
