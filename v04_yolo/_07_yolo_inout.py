# 실습 영상 구하기

from ultralytics import solutions
import cv2

# 비디오 경로 설정
cap =cv2.VideoCapture("v4_yolo/traffic_cctv.mp4")
# cap =cv2.VideoCapture(0)

# w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# video_writer = cv2.VideoWriter(
#     "test.avi",
#     cv2.VideoWriter_fourcc(*"MJPG"),
#     fps,
#     (w, h)
# )

count_points = [(12, 138), (1266, 452)] # line
# count_points = [(), (), (), ()] # rectangle
# count_points = [(), (), (), (), (), (), ()] # polygon

# count 객체 생성
counter = solutions.ObjectCounter(
    model="yolo11n.pt",
    show=True,
    region=count_points,
    # tracker='botsort.yaml'
    # classes=[]
)

# 비디오 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        break
    # re_frame = cv2.resize(frame, (640, 480))
    re_frame = cv2.resize(frame, (1280, 720))
    # results = counter(frame)
    re_results = counter(re_frame)
    
    # video_writer.write(results.plot_im)
    
cap.release()
# video_writer.release()
cv2.destroyAllWindows()