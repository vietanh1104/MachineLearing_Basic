from cv2 import cv2
import time
img = cv2.imread("image.jpg", 1)
cap = cv2.VideoCapture(0)
ptime = 0
while True:
    ret, frame = cap.read()
    print(ret)
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(frame, str(int(fps)), (100,50), cv2.FONT_HERSHEY_COMPLEX, 2, (50,50,50), 4 )
    cv2.imshow("cua so anh", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
