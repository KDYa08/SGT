import cv2

src = cv2.imread("lunar.jpg", cv2.IMREAD_COLOR)

# src의 세로, 가로, 채널을 받아옵니다
# 채널은 색상에 따라 1(회색, 흑백), 3(RGB, hsv), 4(RGBA)가 있습니다
height, width, channel = src.shape

# 회전 행렬 생성 함수
# cv2.getRotationMatrix2D((회전점), 회전 각도, 확대 비율)
matrix = cv2.getRotationMatrix2D((width//2, height//2), 90, 1)

# 회전 변환을 계산하는 함수
# cv2.warpAffine(영상, 회전 행렬, 출력 크기)
dst = cv2.warpAffine(src, matrix, (width, height))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()