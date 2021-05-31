import cv2

# Open Image : Filepath (str), imread flag (Enum Value)
# With IMREAD_COLOR, the image is opened in BGR (Blue Green Red)
# Returns the image in a Numpy array
img = cv2.imread("opencv_snippets/images/westernbrookpond.jpg", cv2.IMREAD_COLOR)

# Show image shape
# Height, Width, Number of channels (3 in color, 1 in grayscale)
img_shape = img.shape
print(img_shape)

# Show image in window : window name (str), image (np.ndarray)
cv2.imshow("Gros Morne", img)

# Window disappears automatically. Need to pause program with `waitKey`.
# `waitKey` parameter : delay in ms before capturing a key event
# destrowAllWindows at the end
cv2.waitKey(0)
cv2.destroyAllWindows()
