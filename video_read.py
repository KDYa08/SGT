import cv2

capture = cv2.VideoCapture("sky.mp4")

# cv2.waitKey는 키가 입력되기 전에는 -1을 가지다 키가 입력되면 해당키의 유니코드를 출력
# 응용으로 cv2.waitKey(1) < ord("q") 는 q를 눌렀을 때 정지됨
# ord의 반대는 chr
while cv2.waitKey(1) < 0:
    # cap_prop_pos_frames는 현재 프레임, cap_prop_frame_count는 전체 프레임
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        # capture.set은 해당 속성을 설정
        # 현재 프레임을 0으로 설정
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # ret은 영상출력여부를 True, False로 반환
    # frame 해당 영상의 프레임을 가져옴
    ret, frame = capture.read()
    cv2.imshow("sky", frame)

# 해당 영상을 닫고 메모리 해제
capture.release()
cv2.destroyAllWindows()