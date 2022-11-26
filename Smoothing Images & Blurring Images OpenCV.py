import cv2
import numpy as np
import matplotlib.pyplot as plt 

img = cv2.imread('lena.jpg')
averaging = cv2.blur(img, (1,1)) # filter{matrix} : for pixels
gblur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img,3)
bilateralFilter = cv2.bilateralFilter(img, 9,75,75)


cv2.imshow('image', img)
cv2.imshow('averaging', averaging)
cv2.imshow('gblur', gblur)
cv2.imshow('madian', median)
cv2.imshow('bilateralFilter',bilateralFilter)

cv2.waitKey(0)
cv2.destroyAllWindows()