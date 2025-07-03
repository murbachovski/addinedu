# pip install ftfy
# pip install regex
# https://github.com/ultralytics/CLIP/blob/main/data/prompts.md

from ultralytics import YOLOWorld
import cv2

cap = cv2.VideoCapture("v04_yolo/input_det_video.mp4")

# 1. 모델 로드
model = YOLOWorld(
    "yolov8s-world.pt",
    )

# 2. 텍스트 기반 추론
model.set_classes(["person walking"])

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("VIDEO CHECK")
        break
    results = model.predict(frame)
    annotated_frame = results[0].plot()
    
    # 3-1. 리사이즈
    resize_annotated_frame = cv2.resize(annotated_frame, (640, 480))
    # 4. 화면 출력
    cv2.imshow("YOLO_CLIP", resize_annotated_frame)
    
    # 5. q 키 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()