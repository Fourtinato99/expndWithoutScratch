import cv2 as cv
import numpy as np
width = 1500
zero = np.zeros((955,width,3),dtype=np.uint8)
img = cv.imread('molly.jpg')
gg =img[10,10]
zero = np.where(zero==0 , img[10,10] , zero)
print(img.shape)
cv.imshow('molly',img)
x = img.shape[1]
y = img.shape[0]
xs = (width-x)//2
zero[0:y,xs:xs+x,:] = img[:,:,:]

cv.imshow('molly modefied', zero)

cv.imwrite('mollymod.jpg',zero)
cv.waitKey(0)