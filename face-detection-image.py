import cv2


front_face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)
check, frame = video.read()

img = frame
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faces = front_face_cascade.detectMultiScale(gray_img,
                                            scaleFactor=1.2,
                                            minNeighbors=7)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("detected_face",img)
cv2.waitKey(0)
cv2.destroyAllWindows()