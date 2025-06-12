from ultralytics import YOLO
import cv2

model = YOLO("best.pt")
result1 = model("./test.jpg")
result2 = model("./test2.jpg")

plots1 = result1[0].plot()
plots2 = result2[0].plot()
plots2 = cv2.resize(plots2, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

cv2.imshow("plot1", plots1)
cv2.imshow("plot2", plots2)
cv2.waitKey(0)
cv2.destroyAllWindows()