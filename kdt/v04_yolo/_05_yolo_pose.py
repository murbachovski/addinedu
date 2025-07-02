from ultralytics import YOLO
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture(0)

# 2. 모델 로드
model = YOLO("yolo11n-pose.pt")

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        print("비디오 확인 부탁드립니다.")
        break
    
    # 4. 모델 예측
    results = model(frame)
    annotated_frame = results[0].plot()
    
    # 5. 화면 구성
    cv2.namedWindow("YOLO_POSE", cv2.WINDOW_NORMAL)
    cv2.imshow("YOLO_POSE", annotated_frame)
    
    # 6. q 키 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q키를 눌러서 종료")
        break

cap.release()
cv2.destroyAllWindows()

# 관절 키포인트 개수 : 17개
