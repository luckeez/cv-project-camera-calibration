import cv2
from spawn_block import locations
print(locations)
breakpoint()

input_image = "images/clean_view.png"

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"[{x}, {y}],")
        with open('coordinates_log.txt', 'a') as f:
            f.write(f"[{x}, {y}],\n")
        cv2.circle(img, (x, y), 2, (0, 255, 0), -1)
        cv2.imshow('image', img)

img = cv2.imread(input_image)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

