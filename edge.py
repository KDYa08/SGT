import cv2

src = cv2.imread("lunar.jpg", cv2.IMREAD_COLOR)
# cv2.Canny(영상, 하위 임계값, 상위 임계값)
# 픽셀이 상위 임계값(미분값)보다 크면 가장자리로 간주, 하위 임계값 보다 작으면 가장자리로 고려하지 않음
canny = cv2.Canny(src, 30, 255)

cv2.imshow("src", src)
cv2.imshow("canny", canny)
cv2.waitKey()
cv2.destroyAllWindows()