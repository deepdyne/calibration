

# MEMO
command which i've used is below

```
$ lsusb # whether web cam is recognized             
$ ls /dev/video* # to check device no of camera
$ dmesg | grep uvcvideo # to confirm if moddule has recognized or not
[110537.967704] uvcvideo: Found UVC 1.00 device HD Webcam C525 (046d:0826)
[110538.253373] uvcvideo 1-1:1.2: Entity type for entity Extension 5 was not initialized!
[110538.253380] uvcvideo 1-1:1.2: Entity type for entity Processing 2 was not initialized!
[110538.253384] uvcvideo 1-1:1.2: Entity type for entity Camera 1 was not initialized!
[110538.253388] uvcvideo 1-1:1.2: Entity type for entity Extension 6 was not initialized!
[110538.253392] uvcvideo 1-1:1.2: Entity type for entity Extension 7 was not initialized!
[110538.253396] uvcvideo 1-1:1.2: Entity type for entity Extension 8 was not initialized!
```


# References
- chessboard picture for calibration
  - https://github.com/opencv/opencv/blob/master/samples/data/chessboard.png
- doc of cv2
  - https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html#calibratecamera
- src of script
  - https://qiita.com/a2kiti/items/38171e6842b6332bba7b




