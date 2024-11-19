import numpy as np
import cv2
import matplotlib.pyplot as plt

input_image = "view2.png"

matrix = np.load("camera_matrix.npy")

# Funzione per proiettare un punto 3D in coordinate 2D
def project_3d_to_2d(matrix, point_3d):
    point_3d = np.append(np.array(point_3d), 1)
    projected = np.dot(matrix, point_3d)
    return [projected[0] / projected[2], projected[1] / projected[2]]

world_points = [
    [535.6, 103.4, 939.6], # pollice sx
    [-545.7, 127.7, 932.2], # pollice dx
    [67, 54, 1243], # clavicola sx
    [-73, 54, 1243], # clavicola dx
]

# Funzione per disegnare i punti su un'immagine
def draw_points(input_image, output_image, predicted_points, gt_points = None):
    image = cv2.imread(input_image)
    green, red = (0, 255, 0), (0, 0, 255)
    point_size = 5

    if gt_points is not None:
        for point in gt_points:
            cv2.circle(image, (int(point[0]), int(point[1])), point_size, green, -1)

    for point in predicted_points:
        cv2.circle(image, (int(point[0]), int(point[1])), point_size, red, -1)

    cv2.imwrite(output_image, image)

predicted_points = [project_3d_to_2d(matrix, point) for point in world_points]
draw_points(input_image,  "output.png", predicted_points)

print(predicted_points)

