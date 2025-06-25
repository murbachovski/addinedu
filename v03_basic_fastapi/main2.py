# pip install fastapi
# pip install uvicorn

from fastapi import FastAPI
from controller import items, users

app = FastAPI()
app.include_router(items.router)
app.include_router(users.router)

@app.get("/")
def home():
    # json 구조
    return {"Hello:" "here is HOME"}