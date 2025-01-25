# cv-project-camera-calibration

#### Script description

- **spawn_block.py, grid_blocks.py**: script to spawn training blocks (grid) and arbitrary blocks (test) in the unreal Engine scenario
- **log_coordinates.py**: script to log the coordinate of an arbitrary 2D point (mouse click) in an image.
- **coordinates.py**: contains the coordinates of our grid blocks (training set), both in 3D and 2D spaces.
- **compute_camera_matrix.py**: script to compute the camera matrix using the pairs of known points extracted from Unreal Engine and from the images, taking them as input from the file *coordinates.py*.
- **test_camera_matrix.py**: script to test our camera matrix, using test points, and plot the results in the image.
- **plot_joints.py**: script to output the final result, plotting the skeleton joints in the image.