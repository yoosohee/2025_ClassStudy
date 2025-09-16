#비디오에서 수집한 영상 캡처 후 이어붙이기

import cv2 as cv
import numpy as np
import sys

cap=cv.VideoCapture(0,cv.CAP_MSMF)

if not cap.isOpened():
    sys.exit('카메라 연결 실패')
    
frames=[]
while True:
    ret,frame=cap.read()
    
    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break
    
    cv.imshow('Video display', frame)
    
    key=cv.waitKey(1)
    if key==ord('c'):
        frames.append(frame)
    elif key==ord('q'):
        break
    
cap.release() #카메라 연결 해제(자원을 풀어줌)
cv.destroyAllWindows()

if len(frames)>0: #만약 캡처한 프레임이 있으면
    imgs=frames[0] #이걸 이미지로 두고
    for i in range(1,min(3,len(frames))): #최대 3장까지 가로로 이어붙여서 보여줌
        imgs=np.hstack((imgs,frames[i])) #이미지를 수평 방향으로 이어 붙임
        #hstack은 horizontal stack이라는 의미로 가로로 나란히 붙인다는 뜻
        
        
    #frames[0]:첫번째 캡처된 이미지
    #frames[1]:두번째 캡처된 이미지    
    cv.imshow('collected images', imgs)
    
    cv.waitKey() #캡처된 이미지의 창이 뜨면 보여주고, 키보드 입력이 있으면
    cv.destroyAllWindows() #종료
