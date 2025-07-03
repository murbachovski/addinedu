from sahi.predict import get_sliced_prediction
from sahi import AutoDetectionModel

# 1. 모델 경로
model_path = "models/yolo11n.pt"

# 2. 모델 로드
detect_model = AutoDetectionModel.from_pretrained(
    model_type="ultralytics",
    model_path=model_path,
    confidence_threshold=0.4
)

# 3. 슬라이스 기반 객체 탐지 설정
results = get_sliced_prediction(
    "demo_data/small-vehicles1.jpeg",
    detect_model,
    slice_width=256,  # 가로 크기
    slice_height=256, # 세로 크기
    overlap_height_ratio=0.2,
    overlap_width_ratio=0.2,
    verbose=2
)

# 4. 예측 결과 저장
results.export_visuals(export_dir="./sahi/slice")
print("=======")
print("SAHI SUCCESS")