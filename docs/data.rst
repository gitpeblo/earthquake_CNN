Data and Preprocessing
======================

Each synthetic building is rendered from **four viewpoints**, corresponding to
the cardinal directions around the structure, i.e., front, back, left and right
view.

These views are captured **both before and after** the simulated earthquake:

- The **pre-quake images** represent the building geometry
- The **post-quake images** display stress distributions computed via finite element analysis (FEA)

The post-quake images use **color-coded bays** to indicate the level of stress — higher stress regions are shown in warmer colors (e.g., red), and lower stress in cooler tones (e.g., blue or green).

Example pre-/post-Earthquake
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is an example of one building’s input and its corresponding output after
the application of the earthquake, both from the front view:

.. raw:: html

    <div style="display: flex; justify-content: center; gap: 40px;">

      <div style="text-align: center;">
        <img src="_static/data/example_input_DesignPointA15.png" width="300px" alt="Input image">
        <p><em>Input (pre-earthquake geometry)</em></p>
      </div>

      <div style="text-align: center;">
        <img src="_static/data/example_output_DesignPointA15.png" width="300px" alt="Output image">
        <p><em>Output (post-earthquake stress)</em></p>
      </div>

    </div>

Note that our analysis focuses only on a subset of the total bays within each
building (in the examples above, the third column of bays).
In this representation, the finite elements are shown as a mesh that subdivides
the central bays.
The mesh resolution and bay layout are consistent across all buildings,
ensuring that stress patterns can be compared between different designs.
However, they may correspond to different physical sizes.
This size and layout information is stored in accompanying metadata files
provided alongside the images.

---

Each image is uniquely identified by: the **building ID**, the
**view direction**, the **earthquake scenario**, and the shape of the **bay grid**.

