import numpy as np
import cv2

world_coordinates = [
    #[x, y, z],
    # ALL 63
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

# image in 1170x658
image_coordinates = [
    # ALL 63
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


b = []
for i in range(len(image_coordinates)):
  b.append(image_coordinates[i][0])
  b.append(image_coordinates[i][1])

A = []
for i in range(len(image_coordinates)):
  wc = world_coordinates[i]
  ic = image_coordinates[i]
  a1 = [wc[0], wc[1], wc[2], 1, 0, 0, 0, 0, -wc[0]*ic[0], -wc[1]*ic[0], -wc[2]*ic[0]]
  a2 = [0, 0, 0, 0, wc[0], wc[1], wc[2], 1, -wc[0]*ic[1], -wc[1]*ic[1], -wc[2]*ic[1]]
  A.append(a1)
  A.append(a2)

b = np.array(b)
A = np.array(A)

x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
x = np.append(x, 1)


# Reshape del vettore a una matrice 3x4

print("Residuati:")
print(residuals)

print("Valori singolari di A:")
print(s)


print("prima del reshape: ")
print(x)
xx = x.reshape(3, 4)
print("dopo il reshape: ")
print(xx)


print("PROVALO:")
test_wc = np.append(np.array(world_coordinates[13]), 1)
print("input:", test_wc)

test_result = np.dot(xx, test_wc)
print(test_result[0]/test_result[2], test_result[1]/test_result[2])

errors = []
for i in range(len(image_coordinates)):
  input = np.append(np.array(world_coordinates[i]), 1)
  result = np.dot(xx, input)
  ic = [result[0]/result[2], result[1]/result[2]]
  print(f"calc result: [{ic[0]:.1f}, {ic[1]:.1f}]")
  print(f"real result: [{image_coordinates[i][0]:.1f}, {image_coordinates[i][1]:.1f}]\n")
  error = (image_coordinates[i][0]-ic[0])**2 + (image_coordinates[i][1]-ic[1])**2
  #print("error: ", error)
  errors.append(error)

print("average error: ", sum(errors)/len(errors))

def project_3dTo2d(transformation_matrix, point_3d):
  point_3d = np.append(np.array(point_3d), 1)
  result = np.dot(transformation_matrix, point_3d)
  ic = [result[0]/result[2], result[1]/result[2]]
  return ic

import matplotlib.pyplot as plt

def draw_points(input_image, gt_2d, calc_2d, output_image, rescale=None):
    image = cv2.imread(input_image)

    red = (0, 0, 255)
    green = (0, 255, 0)
    point_size = 5

    for point in gt_2d:
        point = [int(x) for x in point]
        cv2.circle(image, point, point_size, green, -1)
    for point in calc_2d:
        point = [int(x) for x in point]
        cv2.circle(image, point, point_size, red, -1)

    cv2.imwrite(output_image, image)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.imsave("sium.png", image_rgb)

# gt_2d = [
#     [32, 371], # pollice sx
#     [1141, 347], # pollice dx
#     [446, 513], # clavicola sx
#     [753, 512], # clavicola dx
# ]

# Punti rossi - predicted
gt_3d = [
    [535.6, 103.4, 939.6], # pollice sx
    [-545.7, 127.7, 932.2], # pollice dx
    [67, 54, 1243], # clavicola sx
    [-73, 54, 1243], # clavicola dx
]

gt_2d = image_coordinates
gt_3d = world_coordinates

predicted = [project_3dTo2d(xx, point) for point in gt_3d]

draw_points("view3.png", gt_2d, predicted, "output2.png")