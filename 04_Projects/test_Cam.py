import cv2

cam = cv2.VideoCapture(0)

while True : 
    st , frame = cam.read()
    if cv2.waitKey(33) & 0xff == ord("x"):
        break 
    
cam.release()
cv2.destroyAllWindows()
