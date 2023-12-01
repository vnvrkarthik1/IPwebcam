import cv2
video = cv2.VideoCapture(0)
while True:
    _,frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('g',frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()