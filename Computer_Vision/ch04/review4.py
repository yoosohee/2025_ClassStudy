# Otsu 알고리즘으로 임곗값 구하기

import cv2 as cv
import sys 

img=cv.imread('cat.jpg')

t, bin_img=cv.threshold(img[:,:,2], 0,255, cv.THRESH_BINARY+cv.THRESH_OTSU) # 이미지의 이진화 + 오츄 알고리즘으로 임곗값을 구해라
print('오츄 알고리즘이 찾은 최적 임곗값= ', t)

cv.imshow('R channel', img[:,:,2]) #R채널 영상
cv.imshow('R channel binarization', bin_img) #R채널 이진화 영상

cv.waitKey()
cv.destroyAllWindows()
