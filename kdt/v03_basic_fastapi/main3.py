# 간단한 DB 붙이기
# postgresql 사용
    # https://scoop.sh/
# -cmd
    # 	$ scoop install postgresql
    # 	$ pg_ctl start	
    # 	$ psql -U postgres
    # 	$ create user t_user with password '1234';
    # 	create database t_db with encoding='utf-8' owner t_user;
    # 	$ \(왼쪽 슬래시)q 로 나가기
    # 	$ psql -U t_user -d t_db
    # 	$ CREATE TABLE T_TB(
    # 	ADMIN_NO Serial NOT NULL,
    # 	LOGIN_ID Varchar(20) NOT NULL UNIQUE,
    # 	PASSWD Varchar(20) NOT NULL
    # 	);
    # 	$ INSERT INTO T_TB(LOGIN_ID, PASSWD) 	VALUES('kim', '123456')
    # 	$ select * from T_TB
# -새로운 cmd	
    # 	$ pip install "psycopg[binary, pool]"


from fastapi import FastAPI
from controller import admins, items, users

app = FastAPI()
app.include_router(admins.router)
app.include_router(items.router)
app.include_router(users.router)

@app.get("/")
def home():
    return "HOME"

