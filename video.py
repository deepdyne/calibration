import time
import datetime
import cv2

cap = cv2.VideoCapture(2)
fps = 30
codecs = 'XVID'

size = (640,480)

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

fourcc = cv2.VideoWriter_fourcc(*codecs)
name = st + 'output.avi'
video = cv2.VideoWriter(name, fourcc, fps, size)

while (cap.isOpened()):
    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    video.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
video.release()
cv2.destroyAllWindows()
