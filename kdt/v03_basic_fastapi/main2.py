from fastapi import FastAPI
from controller import users, items

app = FastAPI()
app.include_router(users.router)
app.include_router(items.router)

# 홈 화면 구성
@app.get("/")
def home():
    return "HOME"