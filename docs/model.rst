Convolutional Neural Network Model
==================================

.. https://github.com/vdumoulin/conv_arithmetic


Our predictive model is a **convolutional decoder** that generates the
post-earthquake stress image of a single building bay, conditioned on a vector
of input parameters.

The conditioning vector corresponds to the **X matrix** described in :ref:`data`,
and includes:

- the building geometry (length, width, height, wall thickness)
- seismic parameters (PGA, dominant frequency)
- viewpoint (encoded via one-hot vectors)
- bay location indices (row and column within the bay grid)

These features are provided as an 11-dimensional metadata vector per bay,
representing both the physical structure and the earthquake characteristics.

Architecture
------------

The model performs **regression** from this metadata vector to a full-resolution
RGB image, using two main stages:

1. A **fully connected projection block** transforms the input condition vector
into a 2D feature map
2. A stack of **transposed convolutional layers** upsamples this feature map
to the desired image resolution

The condition vector is first normalized via **BatchNorm1d**, and then passed
through two fully connected layers with ReLU activations.
The final output is reshaped into a 2D map with 3 feature maps (RGB).

This intermediate representation is then upsampled via a sequence of
**ConvTranspose2d** layers.
Each block doubles the spatial resolution while reducing the number of channels,
progressively reconstructing the bay-level stress pattern.
The final layer is a **Conv2d** followed by a Sigmoid activation, which maps
the output into the [0, 1] range, consistent with the normalized target images.

Graphical Overview
------------------

The figure below shows the model architecture, highlighting the linear
projection phase, the upsampling blocks, and the final convolutional output:

.. image:: _static/graph_decoder.png
   :width: 100%
   :align: center
   :alt: Model architecture

--

This architecture allows the model to learn how complex structural and seismic
configurations translate into stress responses at the bay level, producing
realistic and spatially detailed output images from compact metadata inputs.
