import cv2 as cv
import sys

img=cv.imread('cat.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
cv.rectangle(img, (190,300),(800,500),(0,0,255),2) #직사각형 그리기
cv.putText(img, '20232346', (190,300), cv.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),2) #글씨 쓰기

cv.imshow('Draw', img)

cv.waitKey()
cv.destroyAllWindows()
