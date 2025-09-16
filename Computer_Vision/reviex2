import cv2 as cv
import sys

img=cv.imread('cat.jpg') #영상 읽기

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
cv.imshow('Image Display', img) #윈도우에 영상 표시

cv.waitKey(20000) #키보드 입력을 기다림 ()의 시간이 끝나면 다음 코드로 넘어감 -> 10000은 10초
cv.destroyAllWindows() #모든 윈도우를 닫음
