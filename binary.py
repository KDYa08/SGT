import cv2

src = cv2.imread("lunar.jpg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# cv2.threshold(회색조 영상, 임계값, 최댓값, 변형 타입)
# cv2.THRESH_BINARY은 픽셀의 값이 임계값 초과이면 최댓값 미만이면 0으로 설정
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()