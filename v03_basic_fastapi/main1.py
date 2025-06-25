# pip install fastapi
# pip install uvicorn

from fastapi import FastAPI
# from typing import Union

app = FastAPI()

@app.get("/")
def home():
    # json 구조
    return {"Hello:" "here is HOME"}

@app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
def read_item(item_id: int):
    # return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# 1. 첫 번째 그냥 실행
# 2. 터미널에서 uvicorn main:app --reload

# Window
# 3. run.bat 파일 생성 후 uvicorn main:app --reload 내용 넣기

# Mac
# 4. run.sh 파일 생성 후 uvicorn main:app --reload 내용 넣기
# 5. chmod 777 ./run.sh
# 6. ./run.sh

# http://127.0.0.1:8000/items/1
# http://127.0.0.1:8000/items/1?q=bye

# 문서 검색
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redocs

# 종료했지만 이미 실행 중이라고 나올때
# lsof -i :8000
# PID 알아낸 후 => kill -9 PID

# MVC 구조로 편집
    # Model, View, Controller

# HTML
# 1. from fasatapi.responses import FileResponse
# 2. index.html 생성
# 3. return FileResponse('index.html)
