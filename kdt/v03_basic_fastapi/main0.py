# 가상환경 생성
    # conda create -n fapi python=3.10
# 가상환경 입장
    # conda activate fapi
# 가상환경 안에서 설치
    # pip install fastapi
    # pip install uvicorn
# python==3.10.18

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

# 1. 홈 화면 구성
@app.get("/")
def home():
    return "Welcom!!!"

# 2. 다른 화면 구성
@app.get("/data")
def get_data():
    return "Do you want to get data?"

# 3. HTML 화면 구성
@app.get("/my_html")
def get_html():
    return FileResponse('C:/Users/DSU/Desktop/kdt/v03_basic_fastapi/index.html')

# 4. POST
class Model(BaseModel):
    name : str
    age : int

@app.post("/send")
def post_data(data : Model):
    print(data)
    return "SUCCESS"