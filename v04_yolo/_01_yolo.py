# ultralytics
# https://www.ultralytics.com/
# pip install ultralytics
# pip install opencv-python

from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolo11n.pt")

results = model("/Users/jini/Downloads/jini/강의/3_애드인에듀/애드인에듀_동서대학교(301)/강의준비/py39/v6_yolo/input.png", save=True)

# 3. 예측 결과 확인
print(results)