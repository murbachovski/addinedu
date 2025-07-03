from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("v04_yolo/inout.mp4")

# 2-1. 좌표 설정
count_points1 = [(282, 357), (415, 357)] # 640, 480
# count_points2 = [(135, 355), (260, 358)] # 640, 480

# 2-2. 객체 생성
counter1 = solutions.ObjectCounter(
    model="yolo11n.pt",
    show=True,
    region=count_points1
)

# counter2 = solutions.ObjectCounter(
#     model="yolo11n.pt",
#     show=True,
#     region=count_points2
# )

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("VIDEO CHECK")
        break
    # 3-1. 리사이즈 
    re_frame = cv2.resize(frame, (640, 480))
    
    # 4. 모델 예측
    results1 = counter1(re_frame)
    # results2 = counter2(re_frame)

cap.release()
cv2.destroyAllWindows()