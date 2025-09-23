import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg') # 이미지 읽기 (np.ndarray)
print("shape: ", img.shape) # 이미지 크기 (높이, 너비, 채널수 출력)
print("최솟값: ", img.min()) # 전체 픽셀 중 최솟값 (B, G, R 중 최소)
print("최댓값: ", img.max()) # 전체 픽셀 중 최댓값
print("평균: ", img.mean()) # 전체 픽셀 값 평균

print("최댓값 위치: ",np.argmax(img))
# 최댓값의 1차원 (이미지를 1줄로 펼쳤을 때) 인덱스
print("정렬 후 앞부분: ", np.sort(img, axis=None)[:10])
# 전체를 1차원으로 펴서 정렬 후 상위 10개 출력

transposed = np.transpose(img, (1,0,2))
# 가로 세로 변환
print("가로 세로 변환 후 모양: ", transposed.shape)

cv.imshow("Original", img) #원본 이미지를 'Original' 창에 표시
cv.imshow("Transposed", transposed) # 전체 이미지를 'Transposed'창에 표시

cv.waitKey() 
cv.destroyAllWindows()
