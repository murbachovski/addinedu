# conda create -n sahi python=3.10
# conda activate sahi
# pip install sahi
# pip install torch
# pip install ultralytics

# from sahi.utils.file import download_from_url
# from sahi.utils.ultralytics import download_yolo11n_model
from sahi.predict import get_prediction
from sahi import AutoDetectionModel


# Download YOLO11 model
model_path = "models/yolo11n.pt"
# download_yolo11n_model(model_path)

# # Download test images
# download_from_url(
#     "https://raw.githubusercontent.com/obss/sahi/main/demo/demo_data/small-vehicles1.jpeg",
#     "demo_data/small-vehicles1.jpeg",
# )
# download_from_url(
#     "https://raw.githubusercontent.com/obss/sahi/main/demo/demo_data/terrain2.png",
#     "demo_data/terrain2.png",
# )
# print("DOWNLOAD SUCCESS")

# 모델 로드
detection_model = AutoDetectionModel.from_pretrained(
    model_type="ultralytics",
    model_path=model_path
)

# 모델 예측
results = get_prediction(
    "demo_data/small-vehicles1.jpeg",
    detection_model
    )

# 결과 저장
results.export_visuals(export_dir="sahi/def")
print("============")
print("SAHI_SUCCESS")