import cv2

# 비디오 경로 설정
cap = cv2.VideoCapture("v4_yolo/traffic_cctv.mp4")

points = []

# 마우스 이벤트 처리 콜백 함수 정의
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"Clicked : {x}, {y}")

        # if len(points) == 6:
            # print(f"Points: {points}")
            # cv2.rectangle()
            # points.clear()

# 좌표 클릭 순서
# 1 4
# 2 3

# 윈도우 창 이름 설정
cv2.namedWindow("Get_Video_X_Y", cv2.WINDOW_NORMAL)

# 콜백 함수 등록
cv2.setMouseCallback("Get_Video_X_Y", mouse_callback)

while True:
    success, frame = cap.read()
    if not success:
        break
    
    re_frame = cv2.resize(frame, (1280, 720))
    cv2.namedWindow("Get_Video_X_Y", cv2.WINDOW_NORMAL)
    
    cv2.imshow("Get_Video_X_Y", re_frame)
    # cv2.imshow("Get_Video_X_Y", frame)
    
    if cv2.waitKey(1) & 0xFF == 27: # ESC
        break
    
cap.release()
cv2.destroyAllWindows()
