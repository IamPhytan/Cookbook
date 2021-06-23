import cv2
import numpy as np

img = cv2.imread("opencv_snippets/images/tablelands.jpg", cv2.IMREAD_COLOR)

# Editing image by using numpy slices and predefined color
# Colors in BGR : Blue, Green, Red
# np.uint8 : unsigned 8 bits, perfect for colors with values 0-255
red = np.array([0, 0, 255], dtype=np.uint8)
blue = np.array([200, 0, 0], dtype=np.uint8)

# Top:Bottom, Left:Right
img[50:250, 500:600] = red
img[200:250, 100:275] = blue

# Show result
cv2.imshow("Gros Morne", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
