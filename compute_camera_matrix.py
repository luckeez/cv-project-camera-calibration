import numpy as np
import cv2
import matplotlib.pyplot as plt
from coordinates import world_points, image_points

'''
Script to compute the camera matrix using the pairs of known points extracted 
from Unreal Engine and from the images, taking them as input from the file coordinates.py.
'''

# Prepare the arrays for the linear system
b = []
A = []

for i in range(len(image_points)):
    wp = world_points[i]
    ip = image_points[i]
    
    b.extend([ip[0], ip[1]])
    
    A.append([wp[0], wp[1], wp[2], 1, 0, 0, 0, 0, -wp[0] * ip[0], -wp[1] * ip[0], -wp[2] * ip[0]])
    A.append([0, 0, 0, 0, wp[0], wp[1], wp[2], 1, -wp[0] * ip[1], -wp[1] * ip[1], -wp[2] * ip[1]])

b = np.array(b)
A = np.array(A)

# Compute the parameters of the trasformation matrix
x, residuals, rank, singular_values = np.linalg.lstsq(A, b, rcond=None)
x = np.append(x, 1)  # Add the omogeneous term
transformation_matrix = x.reshape(3, 4)

# Save the transformation matrix
np.save("camera_matrix.npy", transformation_matrix)

# Output results
print("Residuati:", residuals)
print("Valori singolari di A:", singular_values)
print("Matrice di trasformazione:")
print(transformation_matrix)
