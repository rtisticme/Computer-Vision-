import cv2
import numpy as np

img = cv2.imread('hand.jpg')

#color_image=1, grayscale=0, unchanged =-1

#retval,  threshold = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)
#any pixel value below 210 will we white
#any pixel valueabove 210 will we black
#so the output is not good so we can convert to grayscale to make it easier
retval,  threshold = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

retval2,  threshold2 = cv2.threshold(grayscale, 210, 255, cv2.THRESH_BINARY)

#gaussian adaptive threshold
gaus =cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

#otashu threshold

retval2,  ots = cv2.threshold(grayscale, 210, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)



cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus', gaus)
cv2.imshow('ots', ots)
cv2.waitKey(0)
cv2.destroyAllWindows()

