import numpy as np
import cv2

from coordinates import joints_3d

# Mappa tra descrizioni testuali e indici
joint_descriptions = [
    "pelvis", "spine_01", "spine_02", "spine_03",
    "clavicle_l", "upperarm_l", "lowerarm_l", "hand_l",
    "index_01_l", "index_02_l", "index_03_l",
    "middle_01_l", "middle_02_l", "middle_03_l",
    "pinky_01_l", "pinky_02_l", "pinky_03_l",
    "ring_01_l", "ring_02_l", "ring_03_l",
    "thumb_01_l", "thumb_02_l", "thumb_03_l",
    "clavicle_r", "upperarm_r", "lowerarm_r", "hand_r",
    "index_01_r", "index_02_r", "index_03_r",
    "middle_01_r", "middle_02_r", "middle_03_r",
    "pinky_01_r", "pinky_02_r", "pinky_03_r",
    "ring_01_r", "ring_02_r", "ring_03_r",
    "thumb_01_r", "thumb_02_r", "thumb_03_r",
    "neck_01", "head",
    "thigh_l", "calf_l", "foot_l", "ball_l",
    "cc_base_l_bigtoe1", "cc_base_l_indextoe1", "cc_base_l_midtoe1",
    "cc_base_l_pinkytoe1", "cc_base_l_ringtoe1",
    "thigh_r", "calf_r", "foot_r", "ball_r",
    "cc_base_r_bigtoe1", "cc_base_r_indextoe1", "cc_base_r_midtoe1",
    "cc_base_r_pinkytoe1", "cc_base_r_ringtoe1"
]

# Scheletro definito con descrizioni
skeleton = [
    ("pelvis", "spine_01"), ("spine_01", "spine_02"), ("spine_02", "spine_03"),
    ("spine_03", "clavicle_l"), ("clavicle_l", "upperarm_l"), ("upperarm_l", "lowerarm_l"), ("lowerarm_l", "hand_l"),
    ("hand_l", "index_03_l"), # ("hand_l", "index_01_l"), ("index_01_l", "index_02_l"), ("index_02_l", "index_03_l"),
    ("hand_l", "middle_03_l"), # ("hand_l", "middle_01_l"), ("middle_01_l", "middle_02_l"), ("middle_02_l", "middle_03_l"),
    ("hand_l", "pinky_03_l"), # ("hand_l", "pinky_01_l"), ("pinky_01_l", "pinky_02_l"), ("pinky_02_l", "pinky_03_l"),
    ("hand_l", "ring_03_l"), # ("hand_l", "ring_01_l"), ("ring_01_l", "ring_02_l"), ("ring_02_l", "ring_03_l"),
    ("hand_l", "thumb_03_l"), # ("hand_l", "thumb_01_l"), ("thumb_01_l", "thumb_02_l"), ("thumb_02_l", "thumb_03_l"),
    ("spine_03", "clavicle_r"), ("clavicle_r", "upperarm_r"), ("upperarm_r", "lowerarm_r"), ("lowerarm_r", "hand_r"),
    ("hand_r", "index_03_r"), # ("hand_r", "index_01_r"), ("index_01_r", "index_02_r"), ("index_02_r", "index_03_r"),
    ("hand_r", "middle_03_r"), # ("hand_r", "middle_01_r"), ("middle_01_r", "middle_02_r"), ("middle_02_r", "middle_03_r"),
    ("hand_r", "pinky_03_r"), # ("hand_r", "pinky_01_r"), ("pinky_01_r", "pinky_02_r"), ("pinky_02_r", "pinky_03_r"),
    ("hand_r", "ring_03_r"), # ("hand_r", "ring_01_r"), ("ring_01_r", "ring_02_r"), ("ring_02_r", "ring_03_r"),
    ("hand_r", "thumb_03_r"), # ("hand_r", "thumb_01_r"), ("thumb_01_r", "thumb_02_r"), ("thumb_02_r", "thumb_03_r"),
    ("spine_03", "neck_01"), ("neck_01", "head"),
    ("pelvis", "thigh_l"), ("thigh_l", "calf_l"), ("calf_l", "foot_l"), ("foot_l", "ball_l"),
    ("ball_l", "cc_base_l_bigtoe1"), ("ball_l", "cc_base_l_indextoe1"),
    ("ball_l", "cc_base_l_midtoe1"), ("ball_l", "cc_base_l_pinkytoe1"), ("ball_l", "cc_base_l_ringtoe1"),
    ("pelvis", "thigh_r"), ("thigh_r", "calf_r"), ("calf_r", "foot_r"), ("foot_r", "ball_r"),
    ("ball_r", "cc_base_r_bigtoe1"), ("ball_r", "cc_base_r_indextoe1"),
    ("ball_r", "cc_base_r_midtoe1"), ("ball_r", "cc_base_r_pinkytoe1"), ("ball_r", "cc_base_r_ringtoe1")
]

# Carica immagine e matrice
input_image = "images/giulia.png"
output_image = "outputs/output_joints.png"
matrix = np.load("camera_matrix.npy")

# Funzione per proiettare un punto 3D in coordinate 2D
def project_3d_to_2d(matrix, point_3d):
    point_3d = np.append(np.array(point_3d), 1)
    projected = np.dot(matrix, point_3d)
    return [projected[0] / projected[2], projected[1] / projected[2]]

# Funzione per disegnare punti e scheletro
def draw_points_and_skeleton(input_image, output_image, points_2d, skeleton, joint_descriptions):
    image = cv2.imread(input_image)
    if image is None:
        raise ValueError("Impossibile caricare l'immagine di input.")
    
    red = (0, 0, 255)  # Colore dei punti
    blue = (255, 0, 0) # Colore dello scheletro
    point_size = 10
    line_thickness = 15

    # Creare una mappa tra descrizioni e coordinate 2D
    joint_map = {desc: points_2d[i] for i, desc in enumerate(joint_descriptions)}

    # Trova tutti i punti usati nello scheletro
    used_joints = set([joint for connection in skeleton for joint in connection])

    # Disegna lo scheletro
    for start, end in skeleton:
        start_point = joint_map[start]
        end_point = joint_map[end]
        cv2.line(image, (int(start_point[0]), int(start_point[1])), (int(end_point[0]), int(end_point[1])), blue, line_thickness)

    # Disegna i punti utilizzati
    for joint in used_joints:
        point = joint_map[joint]
        cv2.circle(image, (int(point[0]), int(point[1])), point_size, red, -1)

    # Salva l'immagine
    cv2.imwrite(output_image, image)

# Proietta i punti 3D in 2D
predicted_points = [project_3d_to_2d(matrix, point) for point in joints_3d]

# Disegna punti e scheletro
draw_points_and_skeleton(input_image, output_image, predicted_points, skeleton, joint_descriptions)

print("Output image:", output_image)
