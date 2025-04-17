import cv2

# 이미지를 원래 색상의 방식으로 불러옴
image = cv2.imread("lunar.jpg", cv2.IMREAD_ANYCOLOR)

# cv2.imshow("창이름", 이미지)
# 이미지 창을 출력함
cv2.imshow("Moon", image)
# 키 입력 대기함수(키 입력하기 전까지 파이썬을 중지함)
cv2.waitKey()
# 모든 윈도우 창 제거
cv2.destroyAllWindows()