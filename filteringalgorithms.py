import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#0 (default) is for which camera to choose

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #cvt is convert color
    #In rgb is all three values are color
    #Where as hues is the color, the intensity of the color present and
    #I is the brightness
    lower_skinvalue= np.array([0, 30, 60])
    upper_skinvalue = np.array([20, 150, 255])

    mask = cv2.inRange(hsv, lower_skinvalue, upper_skinvalue)
    #the mask will be everything with in the hsv level
    res = cv2.bitwise_and(frame, frame, mask=mask)
    #applied to frame and in the frame where mask is true
    #if it is in the range the mask will be white
    #if not the value is zero

    #kernel = np.ones((15,15), np.float32)/225
    #martix of 15x15 ones
    #divide by 15*15= 225 to create average of 15*15 filter
    #smoothed = cv2.filter2D(res, -1, kernel)
    #less background noise but we also loose a lot of clarity

    #blur =cv2.GaussianBlur(res, (15,15),0)
    #similar to the last but we get a little clarity

    #median = cv2.medianBlur(res, 15)
    #very useful for removing background noises

    #bilateral = cv2.bilateralFilter(res, 15, 75,75)
    #this filter is useless

    #normal filters are not enough so we need morphological transformation to remove noise

    #first two are erosion and dialation
    #erosion removes the color that is diffrent
    #if all colors pixels are black and 1 is white it will remove that white pixel
    #dialation is the opposite it looks for similar values until it cant


    kernel= np.ones((6,6), np.uint8)
    #erosion =cv2.erode(mask, kernel, iterations=1)
    #black patches formed inside the image
    #dialation =cv2.dilate(mask, kernel, iterations=1)
    # black patches formed in the background

    #closing and opening is another method
    #opening helps to remove false positive
    # closing helps to remove false negative

    opening= cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    #diffrence betwwen input image and opening of the image
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # diffrence betwwen closing of the imput image and input image



    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    #cv2.imshow('smooth', smoothed)
    #cv2.imshow('blur', blur)
    #cv2.imshow('median', median)
    #cv2.imshow('bilateral', bilateral)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    k=cv2.waitKey(5) & 0xFF
    if k== 27 :
        break
cv2.destroyAllWindows()
cap.release()



