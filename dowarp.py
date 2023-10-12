#!/usr/bin/env python3
import cv2
import numpy as np
import warp


imgfile="data/sample.jpg"
img = cv2.imread(imgfile)  # queryImage
h,w = img.shape[0:2]
srcpts = np.float32( [[562, 71], [220, 3575], [550, 3636], [935, 121]])
dstw=100
dsth=600
dstpts = np.float32( [[0, 0], [0, dsth], [dstw, dsth], [dstw, 0]])

res = warp.warpImage(img, srcpts, dstpts)
print(f"res.shape={res.shape} min/max={np.min(res)}/{np.max(res)}")
cv2.imwrite("out/res-from-python.png", res)
