import cv2
import time

# web cam
video = cv2.VideoCapture(0)

while True:
    video = cv2.VideoCapture(0)
    check, frame = video.read()

    cv2.imshow("Capturing",frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()