# 실습 영상 구하기
    # https://www.pexels.com/ko-kr/search/videos/people/
# 좌표값 구하기 코드 제공
    # OK


from ultralytics import solutions
import cv2

# 비디오 경로 설정
cap = cv2.VideoCapture("v4_yolo/crowd.mp4")

# 특정 좌표 설정
region_points = {
    "region-01" : [(30, 683), (64, 1037), (672, 1029), (614, 713)]
}

# 구역 설정
region = solutions.RegionCounter(
    model="yolo11n.pt",
    region=region_points,
    show=True,
    conf=0.2,
)

# 비디오 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    # region1 = region.region_counts.get(("region-01"), 0)
    # region2 = region.region_counts.get(("region-02"), 0)
    # region3 = region.region_counts.get(("region-03"), 0)
    # region4 = region.region_counts.get(("region-04"), 0)
    # print(f"region1: {region1}, region2: {region2}, region3: {region3}, region4: {region4}")
    
    # re_frame = cv2.resize(frame, (1280, 720))
    # cv2.namedWindow("Ultralytics Solutions", cv2.WINDOW_NORMAL)
    
    # 특정 구역 계산
    im0 = region(frame)
    
# 비디오 해제
cap.release()
cv2.destroyAllWindows()

# 1. 터미널에 구역 탐지 객체 수 출력
# 2. 영상 화면에 구역 탐지 객체 수 출력 => 17:20분 까지 진행