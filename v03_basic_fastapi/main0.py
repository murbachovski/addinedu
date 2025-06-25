# pip install fastapi
# pip install uvicorn
# uvicorn main:app --reload

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

# 1. 홈 화면
@app.get("/")
def home():
    return "Hello"

# 2. 다른 화면
@app.get("/data")
def home():
    return "Do you want to get data?"

# 3. HTML 사용
# @app.get("/")
# def home():
#     # json 구조
#     return FileResponse('index.html')

# 4. POST
class Model(BaseModel):
    name : str
    age : int

# http://127.0.0.1:8000/docs 에서 POST 진행
@app.post("/send")
def post_data(data : Model):
    print(data)
    return "OK"


# 8000포트 사용 중일 경우
    # lsof -i :8000
    # kill -9 PID