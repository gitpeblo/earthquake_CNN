Project Overview
================

This project focuses on simulating and visualizing the effects of earthquakes
on synthetic buildings composed of bays arranged in a 3D grid of size
**R × C × K**, where **R** is the number of floors, and **C** and **K** are the
number of bays along the building's width and depth, respectively.
Each building configuration is subjected to simulated seismic events, and the
resulting structural stress is analyzed using **finite element analysis (FEA)**.

For each building, we therefore have:

- **4 input images** showing the structure from four cardinal directions (front, back, left, right)
- **4 output images** visualizing the resulting stress after an earthquake, also from the same four directions

The stress levels are visualized by **color-coding each bay**, allowing for
quick interpretation of high-stress regions. This synthetic dataset is used to
explore machine learning models that can predict post-earthquake stress
distributions based on pre-earthquake geometry and loading.