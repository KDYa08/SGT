import cv2

src = cv2.imread("lunar.jpg", cv2.IMREAD_COLOR)
# BGR에서 HSV형식으로 변경
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# 색상, 채도, 명도로 값을 각각 분리
h, s, v = cv2.split(hsv)

# 색상 범위를 0~32로 설정(색상 범위는 0~180으로 설정)
h = cv2.inRange(h, 0, 32)
# bitwise_and(영상1, 영상2, 마스크(이진화영상))
# bitwsie_and는 영상1과 영상2의 동일한 부분만 표시하고 나머지 부분은 0으로 처리합니다.
# 마스크가 있는 경우에는 1만 표시하고 0은 제거한다
sunlight = cv2.bitwise_and(hsv, hsv, mask = h)
sunlight = cv2.cvtColor(sunlight, cv2.COLOR_HSV2BGR)

cv2.imshow("sunlight", sunlight)
cv2.waitKey()
cv2.destroyAllWindows()