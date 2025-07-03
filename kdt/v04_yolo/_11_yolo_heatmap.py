from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("v04_yolo/distance.mp4")

# 2. 모델 로드 및 Heatmap 객체 생성
y_heatmap = solutions.Heatmap(
    model="yolo11n.pt",
    show=True,
    # colormap=cv2.COLORMAP_PARULA
    colormap=cv2.COLORMAP_MAGMA
)

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("VIDEO CHECK")
        break
    # 4. 모델 예측
    results = y_heatmap(frame)
    
cap.release()
cv2.destroyAllWindows()