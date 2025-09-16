import cv2 as cv
import sys

img=cv.imread('cat.jpg') 

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) #BGR 컬러 영상을 명암 영상으로 전환
gray_small=cv.resize(gray,dsize=(0,0), fx=0.5, fy=0.5) #반으로 축소
#추가
color_resize=cv.resize(img, dsize=(0,0), fx=0.5, fy=3)

cv.imwrite('cat_gray.jpg', gray)
cv.imwrite('cat_gray_small.jpg', gray_small)
#추가
cv.imwrite('cat_color_resize.jpg', color_resize)

cv.imshow('Color image', img)
cv.imshow('Gray image', gray)
cv.imshow('Gray image small', gray_small)
#추가
cv.imshow('Color Resize', color_resize)

cv.waitKey()
cv.destroyAllWindows() 
