from ultralytics import YOLO
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("v04_yolo/distance.mp4")

# 2. 모델 로드
model = YOLO("yolo11s.pt")
# 11n => s => m => l => x
# YOLO11n	640	39.5	56.1 ± 0.8	1.5 ± 0.0	2.6	6.5
# YOLO11s	640	47.0	90.0 ± 1.2	2.5 ± 0.0	9.4	21.5
# YOLO11m	640	51.5	183.2 ± 2.0	4.7 ± 0.1	20.1	68.0
# YOLO11l	640	53.4	238.6 ± 1.4	6.2 ± 0.1	25.3	86.9
# YOLO11x	640	54.7	462.8 ± 6.7	11.3 ± 0.2	56.9	194.9

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("VIDEO CHECK")
        break
    results = model.track(frame, persist=True)
    annotated_frame = results[0].plot()
    
    # 4. 결과 화면 출력
    cv2.imshow("YOLO_TRACKING", annotated_frame)
    
    # 5. q키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
