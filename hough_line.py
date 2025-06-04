import numpy as np
import cv2

src = cv2.imread("lunar.jpg")
dst = src.copy()

# 외곽선 검출
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 255)

# cv2.HoughLinesP(이진화 영상, 픽셀 간격, 각도 단위(라디안), 선으로 판단할 최소 교차점 수, 최소 길이, 점 간격의 허용 범위)
lines = cv2.HoughLinesP(canny, 0.8, np.pi / 180, 90, minLineLength = 10, maxLineGap = 100)

for i in lines:
    # 시각화
    cv2.line(dst, (int(i[0][0]), int(i[0][1])), (int(i[0][2]), int(i[0][3])), (0, 0, 255), 2)

cv2.imshow("dst", dst)
cv2.imshow("canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()