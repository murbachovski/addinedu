from fastapi import FastAPI

app = FastAPI()

# 1. 홈 화면 구성
@app.get('/')
def home():
    return "GOOD"

# 2. 다른 화면 구성
@app.get("/items/{item_id}")
def read_item(item_id : int):
    # print("item_id:", item_id)
    return {"item_id": item_id}