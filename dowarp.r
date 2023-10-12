#!/usr/bin/env Rscript



library(reticulate)
library(jpeg)
cv2=import('cv2')

warp = import("warp")

h = 600
w = 100

#    srcpts = np.float32( [[562, 71], [220, 3575], [550, 3636], [935, 121]])
srcpts = rbind(c(562,71), c(220,3575), c(550,3636), c(935,121))
dstpts = rbind(c(0,0), c(0,h), c(w,h), c(w,0))

for (i in 1:10) {
	img2 = warp$warpImage("data/sample.jpg", srcpts, dstpts)
}

cv2$imwrite("out/warped-from-R.jpg", img2)

#plot(c(),c(), xlim=c(0,w), ylim=c(0,h), type="n", xlab="", ylab="",asp=1)


#rasterImage(img1, 0, 0, w, h)







