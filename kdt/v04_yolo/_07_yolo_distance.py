from ultralytics import solutions
import cv2

# 1. Video Path
cap = cv2.VideoCapture("v04_yolo\distance.mp4")

# 2. 모델 로드
# model = YOLO("")
distance_cal = solutions.DistanceCalculation(
    model="yolo11n.pt",
    show=True
)

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("비디오 확인 필요")
        break
    
    # 4. 모델 예측
    results = distance_cal(frame)
    
cap.release()
cv2.destroyAllWindows()
