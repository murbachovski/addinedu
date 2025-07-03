from ultralytics import solutions
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("v04_yolo/inout.mp4")

# 2. 이메일 인증
from_email="ai.murbachovski@gmail.com"
password="atcf mpye uhix pelu"
to_email="ai.murbachovski@gmail.com"

# 3. 모델 로드 및 알람 객체 생성
g_alarm = solutions.SecurityAlarm(
    model="yolo11n.pt",
    show=True,
    records=2, # => 경고 이메일을 전송하기 위한 최소 감지 수
    classes=[0] # => 원하는 클래스만 탐지   
)

# 4. 이메일 서버 인증
g_alarm.authenticate(from_email, password, to_email)

# 5. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("VIDEO CHECK")
        break
    
    results = g_alarm(frame)
    
# 6. 프로세스 종료
cap.release()
cv2.destroyAllWindows()
    
# 1. 원하는 객체만 탐지
# 2. 이메일 알람 문구 변경