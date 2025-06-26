Data and Preprocessing
======================

Each synthetic building is rendered from **four viewpoints**, corresponding to the cardinal directions around the structure:

- front view
- back view
- left view
- right view

These views are captured **both before and after** the simulated earthquake:

- The **pre-quake images** represent the building geometry
- The **post-quake images** display stress distributions computed via finite element analysis (FEA)

The post-quake images use **color-coded bays** to indicate the level of stress — higher stress regions are shown in warmer colors (e.g., red), and lower stress in cooler tones (e.g., blue or green).

---

Example Input-Output Pair
-------------------------

Below is an example of one building’s input and output from the front view:

**Input (pre-earthquake):**

.. image:: _static/data/example_input_DesignPointA15.png
   :width: 400px
   :align: center
   :alt: Pre-earthquake front view

**Output (post-earthquake stress):**

.. image:: _static/data/example_output_DesignPointA15.png
   :width: 400px
   :align: center
   :alt: Post-earthquake stress front view

---

Note that our analysis focuses only on a subset of the total bays within each
building (in the examples above, the third column of bays).
In this representation, the finite elements are shown as a mesh that subdivides
the central bays.
The mesh resolution and bay layout are consistent across all buildings,
ensuring that stress patterns can be compared between different designs.
However, they may correspond to different physical sizes.
This size and layout information is stored in accompanying metadata files
provided alongside the images.

Each image is uniquely identified by: the **building ID**; the
**view direction**; the **earthquake scenario**; the size of the **bay grid**.

