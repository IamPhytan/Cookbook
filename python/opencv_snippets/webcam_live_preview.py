import cv2


def fool_proof_webcam():
    # Create a named window
    # This window will be called by its name, hence the variable
    window_name = "Live Video Feed"
    cv2.namedWindow(window_name)

    # Get first available camera : index=0 (int)
    cap = cv2.VideoCapture(0)

    # Check if video capturing was initialized
    # Fool-proof method, yet not necessary
    # frame : check if a frame has been grabbed (boolean)
    # frame : frame from camera (np.ndarray)
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:
        ret, frame = cap.read()
        # Convert frame from BGR to Grayscale
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow(window_name, output)
        # Wait for key event at each millisecond (delay = 1)
        # waitKey returns ord() of pressed key
        # 27: ASCII code for ESC = ord(ESC)
        if cv2.waitKey(1) == 27:
            break

    # Destroy window and release camera
    cv2.destroyWindow(window_name)
    cap.release()


def simple_webcam():
    # Capture
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        cv2.imshow("Webcam", frame)
        # Update each 30 ms
        # Retrieve 8 least significant bits from code (0-255)
        k = cv2.waitKey(30) & 0xFF
        # Loop will only break by pressing 'q'
        if k == ord("q"):
            print(k)
            break

    cv2.destroyAllWindows()
    cap.release()


if __name__ == "__main__":
    fool_proof_webcam()
    simple_webcam()
