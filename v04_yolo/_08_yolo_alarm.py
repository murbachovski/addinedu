from ultralytics import solutions
import cv2

# 비디오 로드
cap = cv2.VideoCapture(0)

# 이메일 인증 정보
from_email = "ai.murbachovski@gmail.com"
password = "tstu qwji fdyr vmtd"
to_email = "ai.murbachovski@gmail.com"

# Initialize security alarm object
securityalarm = solutions.SecurityAlarm(
    show=True,  # display the output
    model="yolo11n.pt",  # i.e. yolo11s.pt, yolo11m.pt
    records=1,  # total detections count to send an email
)

securityalarm.authenticate(from_email, password, to_email)  # authenticate the email server

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    results = securityalarm(im0)

cap.release()
cv2.destroyAllWindows()  # destroy all opened windows

# 1. 2단계 인증 
    # https://myaccount.google.com/security?gar=WzJd&hl=ko&utm_source=OGB&utm_medium=act
# 2. 보안 키 생성
    # https://myaccount.google.com/apppasswords?pli=1&rapt=AEjHL4PSrpXldpx2bS-x7jVf4R6nKaOjsNTO69IN1BW5ZXIN9Pizuxd7-mhVwM7TL4EuHOQfjmT37NHyusln_X4JJfHj9uObkfDuHdIoykBGJxNsRXadO-g