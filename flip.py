import cv2

# IMREAD_ANYCOLOR vs IMREAD_COLOR
# IMREAD_ANYCOLOR는 가능한 원래 색상의 이미지를 불러옴
# IMREAD_COLOR는 BGR로 이미지를 불러옴
src = cv2.imread("lunar.jpg", cv2.IMREAD_COLOR)

# flipcode < 0 xy축 대칭
# flipcode = 0 x축 대칭
# flipcode > 0 y축 대칭
x = cv2.flip(src, 0)
xy = cv2.flip(src, -1)
y = cv2.flip(src, 1)

cv2.imshow("src", src)
cv2.imshow("x", x)
cv2.imshow("xy", xy)
cv2.imshow("y", y)
cv2.waitKey()
cv2.destroyAllWindows()