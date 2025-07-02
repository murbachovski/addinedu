from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolo11n.pt")

# 2. 모델 예측
results = model(
    "v04_yolo\input_pen.jpg",
    save=True,
    # conf=0.1, # 임계치 설정
    # save_txt=True, # 결과 정보 저장 여부
    # save_conf=True,
    # save_crop=True,
    # max_det=5,
    
)

# 상황 : 탐지된 결과값이 book만 탐지될 수 있도록 수정해주세요.