import cv2
import time

# web cam
video = cv2.VideoCapture(0)
video.read()
time.sleep(1.0)

# first frame
first_frame = None
count = 0

while True:
    check, frame = video.read()

    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame,(21,21),0)

    ###
    ########## detect motion
    ###

    # get first frame
    if first_frame is None:
        first_frame = gray_frame
        continue

    # difference of frame
    diff_frame = cv2.absdiff(first_frame,gray_frame)
    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # find contours
    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 50000 :
            continue
    
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),6)


    cv2.imshow("Capturing",gray_frame)
    cv2.imshow("Delta",diff_frame)
    cv2.imshow("THRES",thresh_frame)
    cv2.imshow("Countour",frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()