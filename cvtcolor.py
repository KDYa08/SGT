import cv2

src = cv2.imread("lunar.jpg", cv2.IMREAD_COLOR)
# cvtColor(영상, 변화 방식)
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()