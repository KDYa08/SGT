import cv2

image = cv2.imread("lunar.jpg", cv2.IMREAD_ANYCOLOR)

cv2.imshow("Mooon", image)
cv2.destroyAllWindows()