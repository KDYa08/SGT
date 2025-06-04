import cv2

src = cv2.imread("lunar.jpg", cv2.IMREAD_COLOR)
dst = src.copy()

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

dst_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
ret, dst_binary = cv2.threshold(dst_gray, 100, 255, cv2.THRESH_BINARY)

# bitwise_not(이미지, 마스크)
# 마스크가 없는 경우 색상 반전
binary = cv2.bitwise_not(binary)
dst_binary = cv2.bitwise_not(binary)

# 이진화된 영상에서 검색 방법과 근사화 방법을 골라 윤곽선과 계층 구조를 반환합니다
# 윤곽선, 계층 구조 = cv2.findContours(이진화 영상, 검색 방법, 근사화 방법)
# 모든 윤곽선 검출 및 윤곽선의 모든 점 반환
contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
for i in range(len(contours)):
    # cv2.drawContours(src, [윤곽선], 윤곽선 인덱스, 색상, 두께)
    cv2.drawContours(src, [contours[i]], 0, (0, 0, 255), 2)
    print(i, hierarchy[0][i])

# 외곽 윤곽선만 검출 및 윤곽점들의 끝점만 반환
contours = cv2.findContours(dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
for contour in contours:
    print(cv2.boundingRect(contour))
    # 주어진 점을 감싸는 최소 크기의 사각형을 반환
    x, y, width, height = cv2.boundingRect(contour)
    cv2.rectangle(dst, (x, y), (x + width, y + height), (255, 255, 255), 2)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()