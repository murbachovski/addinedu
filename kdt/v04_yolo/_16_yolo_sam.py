# Meta
    # https://segment-anything.com/demo
    # https://ai.meta.com/sam2/
    
from ultralytics import SAM
import time

# 1. 모델 로드
model = SAM("sam_b.pt")
str_time = time.time()

# 2. 모델 추론
model(
    "v04_yolo/distance.mp4",
    save=True
)
end_time = time.time()
all_time = end_time - str_time
print(f"걸린 시간: {all_time}")
print("SUCCESS")