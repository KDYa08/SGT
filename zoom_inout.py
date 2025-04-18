import cv2

src = cv2.imread("lunar.jpg", cv2.IMREAD_COLOR)
height, width, channel= src.shape

# 둘의 파라메타는 이미지, 출력 이미지 크기, 테두리 외삽법이다
# pyrUp 테두리 외삽법은 BORDER_DEFAULT만 사용가능하다
# pyrDown 테두리 외삽법은 BORDER_CONSTANT 외에 사용가능하다
# 다른 테두리 외삽법과 방식은 구글링과 gpt를 이용
dst = cv2.pyrUp(src, dstsize=(width * 2, height * 2), borderType=cv2.BORDER_DEFAULT)
dst2 = cv2.pyrDown(src)

cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()