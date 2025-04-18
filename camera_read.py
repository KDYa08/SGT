import cv2

# 내장 카메라 또는 외장 카메라의 정보를 받아옴
capture = cv2.VideoCapture(0)

# captuer.set(카메라 속성(proid), 값(value))
# 카메라의 속성값을 조정하는 명령어
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 출력 1
# cv2.waitKey(33)이 0 미만 일때(키를 누르지 않았을 때)
while cv2.waitKey(33) < 0:
    # ret은 카메라의 정상작동 판단(정상 작동시 True)
    # frame은 현재 카메라의 프레임을 저장합니다
    ret, frame = capture.read()

    # 현재 프레임을 시각화합니다
    cv2.imshow("VideoFrame", frame)

# 출력 2
# while True:
#     ret, frame = capture.read()
#     cv2.imshow("vidoeframe", frame)

#     if cv2.waitKey(1) & 0xFF == 27:
#         break

capture.release()
cv2.destroyAllWindows()