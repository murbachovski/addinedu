from ultralytics import YOLO
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv002.stream/playlist.m3u8")

# 2. 모델 로드
model = YOLO("yolo11n.pt")

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        print("비디오 확인 부탁드립니다!!")
        break
    
    # 4. 모델 예측
    results = model(frame)
    annotated_frame = results[0].plot()
    
    # 5. 결과 화면 출력
    cv2.namedWindow("YOLO", cv2.WINDOW_NORMAL)
    cv2.imshow("YOLO", annotated_frame)
    
    # 6. 종료 버튼
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q키를 눌러서 종료했습니다.")
        break

cap.release()
cv2.destroyAllWindows()