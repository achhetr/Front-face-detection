import cv2
import time

# web cam
video = cv2.VideoCapture(0)

front_face_cascades = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    video = cv2.VideoCapture(0)
    check, frame = video.read()

    # find face in the frame
    faces = front_face_cascades.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=7)
    
    # add rectangle in the matching area
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),6)

    cv2.imshow("Capturing",frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()