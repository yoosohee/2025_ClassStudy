import cv2 as cv
import sys

cap=cv.VideoCapture(0,cv.CAP_MSMF) 
#웹캡과 연결 시도, 결과를 cap이라는 객체에 저장
#웹캠이 하나이므로 웹캠 번호 0으로 지정
#CAP_DSHOW: 웹캠 화면을 화면에 바로 표시

if not cap.isOpened(): #연결 실패하면 cap의 isOpend 함숫값이 False가 됨
    sys.exit('카메라 연결 실패')
    
while True: #동영상을 띄워주기 위해 무한 반복
    ret,frame=cap.read() #read로 프레임 읽어옴.
    #ret:성공 여부, frame: 프레임 내용
    
    if not ret: #만약 프레임 얻는 데 실패하며 영상 내보내기 종료
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break
    
    cv.imshow('Video display', frame) #성공하면 화면에 표시
    
    key=cv.waitKey(1) #1ms동안 키보드 입력 기다림
    if key==ord('q'): #'q'키가 들어오면 루프를 빠져나감
        break
    
cap.release() #카메라와 연결을 끊음
cv.destroyAllWindows()
