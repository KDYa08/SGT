import cv2

src = cv2.imread("lunar.jpg", cv2.IMREAD_COLOR)

# # src[높이, 너비].copy()
# # dst = src[높이, 너비]를 사용하면 안되는 이유는 얕은 복사(shallow copy)와 깊은 복사(deep copy)의 차이 때문이다
# # 얕은 복사는 같은 메모리방을 사용하기 때문에 원본을 훼손 시킬수 있기 때문이다
# # 변수에 변수를 저장하면 값이 아닌 메모리 주소를 저장하기에 같은 메모리방을 쓴다
# # 깊은 복사는 메모리방에 있는 값을 복사하여 새로운 메모리에 저장하기 때문에 원본이 훼손되지 않는다
# dst = src[0:80, 100:200].copy()

dst = src.copy()
# roi에 src의 특정 부분을 저장한다
roi = src[0:80, 100:200]
# dst의 높이와 너비를 똑같이 설정하고 roi를 저장한다
dst[0:80, 0:100] = roi

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()