.. _overview_section:

Project Overview
================

This project focuses on simulating and predicting the effects of earthquakes
on synthetic buildings composed of bays arranged in a 3D grid of size
**R × C × K**, where **R** is the number of floors, and **C** and **K** are the
number of bays along the building's width and depth, respectively.
Each building configuration is subjected to simulated seismic events, and the
resulting structural stress is analyzed using **finite element analysis (FEA)**.

This synthetic dataset is used to create a machine learning model that can
predict post-earthquake stress distributions based on pre-earthquake geometry
and loading.

Objective
---------

The primary objective of this project is to develop a **convolutional neural network (CNN)**
model capable of predicting the stress experienced by each bay in the building
following an earthquake.
The model takes as input the building’s structural characteristics—such as its
geometry and bay layout—along with the seismic input parameters, including the
earthquake's peak ground acceleration (PGA) and frequency.

By learning from the synthetic dataset generated through FEA simulations, the
CNN aims to estimate the resulting stress distribution across the building bays
with high spatial resolution.
This approach can potentially enable real-time assessment of structural vulnerability
without the need for computationally expensive simulations.