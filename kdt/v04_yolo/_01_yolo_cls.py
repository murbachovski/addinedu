from ultralytics import YOLO
import cv2

# 1. 모델 로드
model = YOLO("yolo11n-cls.pt")

# 2. 모델 예측
results = model(
    "v04_yolo/input.jpg"
)

# 3. 결과 확인
# print(results)
result_image = results[0].plot()
cv2.imwrite("./result.jpg", result_image)

