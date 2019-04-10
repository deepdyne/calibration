import numpy as np
import csv

csv_file = open("./mtx.csv", "r", encoding="utf-8", errors="", newline="" )
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

p_matrix = []
p_matrix.append("")
for row in f:
    for cell in row:
        p_matrix.append(cell)
    # only add 0 to 4th column
    # coz there is no extrinsic parameters in monocular camera especially in my case
    p_matrix.append("0.000000000000000000e+00")

text_file = open("calib_cam_to_cam.txt", "w") # NOTE: name and format are compliant with KITTI dataset
text_file.write("P_rect_02:%s" % " ".join(p_matrix))
text_file.close()

