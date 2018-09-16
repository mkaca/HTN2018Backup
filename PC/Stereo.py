import cv2
import numpy as np
from matplotlib import pyplot as plt

imgL = cv2.imread("L.png",0)
imgR = cv2.imread("R.png",0)
print(np.shape(imgL))
rectifyL = None
rectifyR = None
translationVector = np.array([15,0,0])
#cv2.stereoRectify(imgL,imgR,0,15,(240,240),0,translationVector,0,0,rectifyL, rectifyR)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()


cv2.imshow("L",imgL)
cv2.imshow("R",imgR)
cv2.waitKey(0)