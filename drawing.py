import cv2
import numpy as np

# src를 np.uint8 형식으로 (height, width, channel) 배열을 생성한다.
src = np.zeros((768, 1366, 3), dtype=np.uint8)

# cv2.line(영상, (x1, y1), (x2, y2), (B, G, R), 굵기, 안티에일리어싱 속성 or 내부 채우기 등))
src = cv2.line(src, (100, 100), (1200, 100), (0, 0, 255), 3, cv2.LINE_AA)

# cv2.circle(영상, (x1, y1), 반지름, (B, G, R), 굵기, 안티에일리어싱 속성)
src = cv2.circle(src, (300, 300), 50, (0, 255, 0), cv2.FILLED, cv2.LINE_4)

# cv2.rectangle(영상, (x1, y1), (x2, y2), (B, G, R), 굵기, 안티에일리어싱 속성)
src = cv2.rectangle(src, (500, 200), (1000, 400), (255, 0, 0), 5, cv2.LINE_8)

# cv2.ellipse(영상, (x1, y1), (장축, 단축), 시작 각도, 끝 각도, (B, G, R), 굵기)
src = cv2.ellipse(src, (1200, 300), (100, 50), 0, 90, 180, (255, 255, 0), 2)

# cv2.putText(영상, 텍스트, (x1, y1), 폰트 종류, 글자 크기, 색상, 굵기)
src = cv2.putText(src, "Singul", (900, 600), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)

cv2.imshow("src", src)
cv2.waitKey()
cv2.destroyAllWindows()