import cv2

src = cv2.imread("lunar.jpg", cv2.IMREAD_COLOR)

# cv2.resize(이미지, 절대 크기, 상대크기, 보간법)
# 출력 크기는 절대 크기와 상대 크기로 나뉜다
# 절대 크기를 사용하려면 dsize에 값을 할당한다
# 상대 크기는 절대 크기에 (0, 0)을 입력하고 fx와 fy에 비율을 입력한다
# 일반적으로 INTER_LINEAR(쌍 선형 보간법)을 가장 많이 사용한다
# 이미지를 확대할 때 INTER_CUBIC(바이큐빅 보간법), INTER_LINEAR(쌍 선형 보간법)을 자주 사용
# 이미지를 축소할 때 INTER_AREA(영역 보간법)을 가장 많이 사용
# 이미지를 확대할 때 영역 보간법을 사용시 이웃 보간법과 비슷한 결과를 반환
dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.8, fy=0.7, interpolation=cv2.INTER_LINEAR)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()