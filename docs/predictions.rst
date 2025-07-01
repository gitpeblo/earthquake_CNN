Model Predictions
=================

The model achieves a Mean Squared Error (MSE) of approximately 0.017 on the
test set, corresponding to a Root Mean Squared Error (RMSE) of about 13.0%
relative to the normalized image intensity range [0, 1].

To visualize the predicted stress for an entire building, the model outputs
for each individual bay are first reshaped to match the size and layout of
the original bay template.
These predicted bay images are then systematically reassembled according to
their spatial positions within the building’s grid, effectively reconstructing
the full post-earthquake stress map of the building.

Similarly, the ground truth bay images are extracted and arranged in the same
manner, allowing direct comparison between predicted and true stress
distributions on a building-wide scale.