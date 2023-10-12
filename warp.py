#!/usr/bin/env python3
import cv2
from cv2 import getPerspectiveTransform, warpPerspective
import numpy as np
# Load the images

def warpImage(img0, srcpts, dstpts) -> np.ndarray:
    if type(img0) is str:
        img0 = cv2.imread(img0)
    print(f"srcpts={srcpts}")
    print(f"dstpts={dstpts}")
    print(f"img0.shape={img0.shape} min/max={np.min(img0)}/{np.max(img0)}")
    cv2.imwrite("out/simg0-original.png", img0)
    img1 = img0[:,:,::-1]
    cv2.imwrite("out/simg1-rgb2bgr.png", img1)
    if len(img1.shape) == 3:
        img2 = (img0[:,:,0]*0.299 + img0[:,:,1]*0.587 + img0[:,:,2]*0.114)
        img3 = (img1[:,:,0]*0.299 + img1[:,:,1]*0.587 + img1[:,:,2]*0.114)
        img4 = (img0[:,:,1]/3 + img0[:,:,2]/3 + img0[:,:,0]/3)
    else:
        img2 = img0
        img3 = img1
        img4 = img0

    cv2.imwrite("out/simg2-rgb2grayscale.png",  img2)
    cv2.imwrite("out/simg3-bgr2grayscale.png",  img3)
    cv2.imwrite("out/simg4-mean2grayscale.png", img4)
    if len(img2.shape) != 2:
        return None
    resmatrix = getPerspectiveTransform(np.float32(srcpts), np.float32(dstpts))
    dsize = (np.int32(np.max(dstpts[:,0])), np.int32(np.max(dstpts[:,1])))
    print(f"resmatrix={resmatrix}")
    print(f"dsize={dsize}")
    res = warpPerspective(img2, resmatrix, dsize)
    print(f"res.shape={res.shape} min/max={np.min(res)}/{np.max(res)}")
    return res
