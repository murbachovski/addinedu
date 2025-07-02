from ultralytics import YOLO
import cv2

# 1. 모델 로드
model = YOLO("yolo11n.pt")

# 2. 모델 예측
results = model(
    "v04_yolo/input_det_video.mp4",
    save=True
)

# 3. 결과 확인
# results_image = results[0].plot()
# cv2.imwrite("여러분이 이미지를 저장할 이름", results_image)