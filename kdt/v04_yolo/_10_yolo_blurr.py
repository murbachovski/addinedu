from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("v04_yolo\input_det_video.mp4")

# 2. 모델 로드 및 블러 객체 생성
blurrer = solutions.ObjectBlurrer(
    model="yolo11n.pt",
    show=True,
    blur_ratio=0.5
)

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("비디오 확인 바람")
        break
    # 4. 모델 예측
    results = blurrer(frame)
    
cap.release()
cv2.destroyAllWindows()