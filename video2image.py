import os
import cv2

vidcap = cv2.VideoCapture('20190417_142912_edited.mp4')
success,image = vidcap.read()
count = 0
path = 'frames'
success = True
fps = 300

while success:
  print(count)
  if count % fps == 0:
    cv2.imwrite(os.path.join(path, "%s.png" % str(count).zfill(8)), image)
    success,image = vidcap.read()
    print('Read a new frame: ', success)

  count += 1
