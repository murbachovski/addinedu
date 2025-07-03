import cv2

# 비디오 경로 설정
cap = cv2.VideoCapture("v04_yolo/inout.mp4")

# 마우스 이벤트 처리 콜백 함수 정의
points = []
def mouse_callback(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"클릭 좌표 : {x, y}")
        
# 윈도우 창 설정
cv2.namedWindow("GET_X_Y", cv2.WINDOW_NORMAL)

# 콜백 함수 등록
cv2.setMouseCallback("GET_X_Y", mouse_callback)

# 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("CHECK VIDEO")
        break
    
    re_frame = cv2.resize(frame, (640, 480))
    
    # cv2.namedWindow("GET_X_Y", cv2.WINDOW_NORMAL)
    cv2.imshow("GET_X_Y", re_frame)
    
    # q 키 종료
    if cv2.waitKey(100) & 0xFF == ord('q'):
        print("종료")
        break

cap.release()
cv2.destroyAllWindows()

# 좌표 순서
# 1 4
# 2 3
