import os
import cv2

vidcap = cv2.VideoCapture('2019-04-10 10:47:59output.avi')
success,image = vidcap.read()
count = 0
path = 'frames'
success = True

while success:
  cv2.imwrite(os.path.join(path, "%s.png" % str(count).zfill(8)), image)
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
