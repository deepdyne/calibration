import time
import datetime
import cv2

cap = cv2.VideoCapture(2)
fps = 30
codecs = 'XVID'

# 録画する動画のフレームサイズ（webカメラと同じにする）
size = (640,480)

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

# 出力する動画ファイルの設定
fourcc = cv2.VideoWriter_fourcc(*codecs)
name = st + 'output.avi'
video = cv2.VideoWriter(name, fourcc, fps, size)

while (cap.isOpened()):
    ret, frame = cap.read()

    # 画面表示
    cv2.imshow('frame', frame)

    # 書き込み
    video.write(frame)

    # キー入力待機
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 終了処理
cap.release()
video.release()
cv2.destroyAllWindows()
