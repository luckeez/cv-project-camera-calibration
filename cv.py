import numpy as np
import cv2
import matplotlib.pyplot as plt

world_points = [
    #[x, y, z],
    [-230.0, 15.0, 10.0],
    [-230.0, 137.5, 10.0],
    [-230.0, 260.0, 10.0],
    [0.0, 15.0, 10.0],
    [0.0, 137.5, 10.0],
    [0.0, 260.0, 10.0],
    [230.0, 15.0, 10.0],
    [230.0, 137.5, 10.0],
    [230.0, 260.0, 10.0],
    [-230.0, 15.0, 218.3],
    [-230.0, 137.5, 218.3],
    [-230.0, 260.0, 218.3],
    [0.0, 15.0, 218.3],
    [0.0, 137.5, 218.3],
    [0.0, 260.0, 218.3],
    [230.0, 15.0, 218.3],
    [230.0, 137.5, 218.3],
    [230.0, 260.0, 218.3],
    [-230.0, 15.0, 426.7],
    [-230.0, 137.5, 426.7],
    [-230.0, 260.0, 426.7],
    [0.0, 15.0, 426.7],
    [0.0, 137.5, 426.7],
    [0.0, 260.0, 426.7],
    [230.0, 15.0, 426.7],
    [230.0, 137.5, 426.7],
    [230.0, 260.0, 426.7],
    [-230.0, 15.0, 635.0],
    [-230.0, 137.5, 635.0],
    [-230.0, 260.0, 635.0],
    [0.0, 15.0, 635.0],
    [0.0, 137.5, 635.0],
    [0.0, 260.0, 635.0],
    [230.0, 15.0, 635.0],
    [230.0, 137.5, 635.0],
    [230.0, 260.0, 635.0],
    [-230.0, 15.0, 843.3],
    [-230.0, 137.5, 843.3],
    [-230.0, 260.0, 843.3],
    [0.0, 15.0, 843.3],
    [0.0, 137.5, 843.3],
    [0.0, 260.0, 843.3],
    [230.0, 15.0, 843.3],
    [230.0, 137.5, 843.3],
    [230.0, 260.0, 843.3],
    [-230.0, 15.0, 1051.7],
    [-230.0, 137.5, 1051.7],
    [-230.0, 260.0, 1051.7],
    [0.0, 15.0, 1051.7],
    [0.0, 137.5, 1051.7],
    [0.0, 260.0, 1051.7],
    [230.0, 15.0, 1051.7],
    [230.0, 137.5, 1051.7],
    [230.0, 260.0, 1051.7],
    [-230.0, 15.0, 1260.0],
    [-230.0, 137.5, 1260.0],
    [-230.0, 260.0, 1260.0],
    [0.0, 15.0, 1260.0],
    [0.0, 137.5, 1260.0],
    [0.0, 260.0, 1260.0],
    [230.0, 15.0, 1260.0],
    [230.0, 137.5, 1260.0],
    [230.0, 260.0, 1260.0],
]

# image in 2787x1568
image_points = [
    [1611, 898],
    [1612, 785],
    [1612, 670],
    [1395, 898],
    [1394, 787],
    [1397, 672],
    [1183, 898],
    [1183, 787],
    [1182, 670],
    [1645, 919],
    [1646, 786],
    [1646, 652],
    [1398, 916],
    [1400, 785],
    [1397, 653],
    [1150, 918],
    [1149, 787],
    [1148, 653],
    [1695, 945],
    [1696, 787],
    [1695, 626],
    [1397, 945],
    [1401, 786],
    [1397, 628],
    [1101, 944],
    [1102, 786],
    [1102, 628],
    [1766, 979],
    [1768, 785],
    [1765, 589],
    [1400, 981],
    [1401, 787],
    [1399, 590],
    [1034, 981],
    [1032, 785],
    [1034, 589],
    [1882, 1042],
    [1883, 782],
    [1883, 527],
    [1399, 1042],
    [1403, 784],
    [1400, 529],
    [919, 1044],
    [921, 786],
    [922, 530],
    [2102, 1159],
    [2104, 788],
    [2101, 414],
    [1403, 1158],
    [1406, 785],
    [1404, 412],
    [704, 1156],
    [710, 783],
    [708, 415],
    [2685, 1468],
    [2688, 786],
    [2685, 112],
    [1409, 1475],
    [1408, 786],
    [1413, 96],
    [132, 1468],
    [132, 786],
    [130, 104],
]


# Preparazione dei vettori per il sistema lineare
b = []
A = []

for i in range(len(image_points)):
    wp = world_points[i]
    ip = image_points[i]
    
    b.extend([ip[0], ip[1]])
    
    A.append([wp[0], wp[1], wp[2], 1, 0, 0, 0, 0, -wp[0] * ip[0], -wp[1] * ip[0], -wp[2] * ip[0]])
    A.append([0, 0, 0, 0, wp[0], wp[1], wp[2], 1, -wp[0] * ip[1], -wp[1] * ip[1], -wp[2] * ip[1]])

# Conversione in array NumPy
b = np.array(b)
A = np.array(A)

# Calcolo dei parametri della matrice di trasformazione
x, residuals, rank, singular_values = np.linalg.lstsq(A, b, rcond=None)
x = np.append(x, 1)  # Aggiunta del termine omogeneo
transformation_matrix = x.reshape(3, 4)

# Output dei risultati
print("Residuati:", residuals)
print("Valori singolari di A:", singular_values)
print("Matrice di trasformazione:")
print(transformation_matrix)

# Funzione per proiettare un punto 3D in coordinate 2D
def project_3d_to_2d(matrix, point_3d):
    point_3d = np.append(np.array(point_3d), 1)
    projected = np.dot(matrix, point_3d)
    return [projected[0] / projected[2], projected[1] / projected[2]]

# Calcolo dell'errore medio
errors = []
for i in range(len(image_points)):
    projected_point = project_3d_to_2d(transformation_matrix, world_points[i])
    error = (image_points[i][0] - projected_point[0])**2 + (image_points[i][1] - projected_point[1])**2
    errors.append(error)

average_error = sum(errors) / len(errors)
print("Errore medio:", average_error)

# Funzione per disegnare i punti su un'immagine
def draw_points(input_image, gt_points, predicted_points, output_image):
    image = cv2.imread(input_image)
    green, red = (0, 255, 0), (0, 0, 255)
    point_size = 5

    for point in gt_points:
        cv2.circle(image, (int(point[0]), int(point[1])), point_size, green, -1)
    for point in predicted_points:
        cv2.circle(image, (int(point[0]), int(point[1])), point_size, red, -1)

    cv2.imwrite(output_image, image)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.show()

# Generazione e visualizzazione dei punti proiettati
predicted_points = [project_3d_to_2d(transformation_matrix, point) for point in world_points]
draw_points("view3.png", image_points, predicted_points, "output.png")
