# ITS 오픈 데이터 사이트 및 API 문서 링크
# https://www.its.go.kr/opendata/
# https://www.its.go.kr/opendata/opendataList?service=traffic#moveData

import urllib  # 웹 데이터를 요청하기 위한 모듈
import json  # JSON 데이터를 파싱하기 위한 모듈
import pandas as pd  # 데이터프레임으로 변환/처리를 위한 pandas
import cv2  # OpenCV 모듈 (영상 처리용)

# ITS Open API 키 설정 (발급받은 키)
key = "db5c00dc1fce45c49049bff225a0fea6"

# 도로 유형(ex: 고속도로 / its: 국도)
Type = "its"

# 최소 경도 영역
minX = float(120.95)

# 최대 경도 영역
maxX = float(127.02)

# 최소 위도 영역
minY = float(30.55)

# 최대 위도 영역
maxY = float(37.60)

# 출력 결과 형식
getType = "json"

url_cctv = f"https://openapi.its.go.kr:9443/cctvInfo?apiKey={key}&type={Type}&cctvType=1&minX={minX}&maxX={maxX}&minY={minY}&maxY={maxY}&getType={getType}"

# 구성한 URL로부터 응답 데이터를 요청
response = urllib.request.urlopen(url_cctv)

# 응답받은 데이터를 UTF-8로 디코딩하여 문자열로 변환
json_str = response.read().decode("utf-8")

# 문자열 형태의 JSON 데이터를 파이썬 객체(dict)로 변환
json_object = json.loads(json_str)

# 'response' > 'data' 항목 내 CCTV 리스트를 pandas DataFrame 형태로 변환 (중첩 키는 ','로 구분)
cctv_play = pd.json_normalize(json_object["response"]["data"], sep=',')

# CCTV 스트리밍 URL 중 N번째 항목 선택
test_url = cctv_play["cctvurl"][137]

# 선택한 CCTV 스트리밍 URL을 OpenCV VideoCapture 객체로 불러오기
cap = cv2.VideoCapture(test_url)

# 비디오 프레임 처리 루프 시작
while cap.isOpened():
    success, frame = cap.read()  # 프레임 읽기 성공 여부와 프레임 데이터 반환
    
    if success:
        cv2.namedWindow("OpenAPI", cv2.WINDOW_NORMAL)  # 창 크기 조절 가능하게 설정
        cv2.imshow("OpenAPI", frame)  # 프레임을 화면에 출력
        
        # 키보드에서 'q' 키를 누르면 루프 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("q를 눌러서 종료했습니다.")
            break  # 루프 종료
        
# 비디오 캡처 객체 해제
cap.release()

# 모든 OpenCV 윈도우 종료
cv2.destroyAllWindows()
