from ultralytics import YOLO

# 모델은 n, s, m, l, x가 있으며 순서대로 정확도는 올라가지만 GPU를 차지하는 비율이 높아진다
model = YOLO('yolo11s.pt')

# 여러가지 파라미터가 있지만 epochs는 전체 데이터셋의 학습 횟수를 정한다
model.train(data='./medic.yaml', epochs=20, batch=4)