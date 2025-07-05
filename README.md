# addinedu
```
0. Install Anaconda
1. Install VSCode
2. Python
3. FastAPI
4. YOLO
5. HuggingFace
6. OpenAPI
7. Transformers
8. BLIP
9. BERT
10. OCR
```

# OpenAPI
```
key = ""
url_cctv = f"https://openapi.its.go.kr:9443/cctvInfo?apiKey={key}&type={Type}&cctvType=1&minX={minX}&maxX={maxX}&minY={minY}&maxY={maxY}&getType={getType}"
```

# OpenAPI 설명
<p align="center">
  <img src="https://github.com/user-attachments/assets/9e80f6a1-f7c2-47ee-b162-a59e9cc888fb" width="1000">
</p>

# OCR 이미지 다운로드 경로
```
https://cran.r-project.org/web/packages/tesseract/vignettes/intro.html
```

# Anaconda 환경 셋팅
## 가상환경 생성
```
conda create -n "가상환경 이름" python=3.9
$  conda create -n py39 python=3.9
```

가상환경 실행
```
conda activate "가상환경 이름"
$  conda activate py39
```

가상환경 종료
```
conda deactivate 
```

라이브러리 설치
```
pip install "설치할 라이브러리"
pip install ultralytics
```

# 강의 내용 참고 자료
## FastAPI<br>
[FastAPI_1](https://youtu.be/Iub7-ZhEScw?si=_5V9Zuml0qgniJVd)<br>
[FastAPI_2](https://youtu.be/i87EnmzMNnU?si=_SGrf7xoPmLcEbWM)<br>
[FastAPI_3](https://youtu.be/lPTJzA8KroA?si=S8xaZJZMuYuSAkka)<br>

## OpenAPI<br>
[ITS 국가교통정보센터](https://its.go.kr/opendata/opendataList?service=cctv)<br>
```
1. 인증키 신청
2. 인증키 발급
3. kdt/v05_openapi/_03_api_yolo.py 코드 확인
4. 발급 받은 인증키 넣어준 뒤 실행
```

## HuggingFace<br>
[허깅페이스](https://huggingface.co/)<br>
```
1. 회원가입
2. 이메일 인증
3. 인증키 발급
4. 원하는 모델 검색
5. 인증키 적용
```
