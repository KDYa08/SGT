import cv2

src = cv2.imread("lunar.jpg")
dst = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# cv2.HoughCircles(회색조 이미지, 검출 방법, 해상도 비율, 원 사이의 최소 거리, canny 임계값, 중심 임계값(낮을수록 많은 원 검출), 최소 크기, 최대 크기)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1 = 230, param2 = 20, minRadius=20, maxRadius=50)

for i in circles[0]:
    # i = [중심x, 중심y, r]
    print(i)
    cv2.circle(dst, (int(i[0]), int(i[1])), int(i[2]), (255, 255, 255), 2)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()