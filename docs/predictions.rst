Model Predictions
=================

The model achieves a Mean Squared Error (MSE) of approximately 0.017 on the
test set, corresponding to a Root Mean Squared Error (RMSE) of about 13.0%
relative to the normalized image intensity range [0, 1].

.. figure:: _static/predictions/predictions_bay.png
   :width: 80%
   :align: center
   :alt: Single bay prediction before assembling

   Example of prediction for a single bay, before assembling, showing
   the ground truth (left), the model prediction (center), and an overlay
   comparison (right).

To visualize the predicted stress for an entire building, the model outputs
for each individual bay are first reshaped to match the size and layout of
the original bay template.
These predicted bay images are then systematically reassembled according to
their spatial positions within the building’s grid, effectively reconstructing
the full post-earthquake stress map of the building.

Similarly, the ground truth bay images are extracted and arranged in the same
manner, allowing direct comparison between predicted and true stress
distributions on a building-wide scale.

--

The following images correspond to the post-earthquake stress distribution and
the model prediction for the same building shown earlier in the data section.
They provide a detailed comparison at the building level, complementing the
bay-level visualization presented previously.

.. raw:: html

    <div style="display: flex; justify-content: center; gap: 40px;">

      <div style="text-align: center;">
        <img src="_static/predictions/groundtruth_DP_A_1000.png" width="400px" alt="Post-earthquake reconstructed image">
        <p><em>Post-earthquake stress for the building</em></p>
      </div>

      <div style="text-align: center;">
        <img src="_static/predictions/predicted_DP_A_1000.png" width="400px" alt="Predicted reconstructed image">
        <p><em>Model prediction of post-earthquake stress</em></p>
      </div>

    </div>

