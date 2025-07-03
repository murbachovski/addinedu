from ultralytics import solutions
import cv2

# 1. 비디오 경로
cap = cv2.VideoCapture("v04_yolo/distance.mp4")

# 2. 좌표 설정
region_points = {
    "region-01" : [(161, 142), (145, 321), (471, 323), (470, 128)]
}
# 클릭 좌표 : (139, 142)
# 클릭 좌표 : (137, 369)
# 클릭 좌표 : (482, 366)
# 클릭 좌표 : (475, 140)


# 3. 모델 로드 및 구역 생성
y_region = solutions.RegionCounter(
    model="yolo11n.pt",
    region=region_points,
    show=True
)

# 4. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("비디오 확인")
        break
    re_frame = cv2.resize(frame, (640, 480))
    results = y_region(re_frame)
    
    # 5. q 키 눌러서 나가기
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

# 구역 설정을 3구역 이상 설정!!!