# 0. 간단한 DB 붙이기
# 1. https://scoop.sh/
    # PowerShell 명령어 두 줄 붙여 넣기 입력 : A 필수
# 2. scoop install postgresql
# 3. 새로운 터미널에서 pg_ctl_\ start
# 4. 새로운 터미널에서 psql -U postgres
# 5. DB 사용자 생성
# 5-1. create user t_user with password '1234';
# 6. DB 생성
# 6-1. create database t_db with encoding='utf-8' owner t_user;
# 7. \q 로 빠져 나오기
# 8. psql -U t_user -d t_db
# 9. TABLE 생성
'''
CREATE TABLE T_TB(
    ADMIN_NO Serial NOT NULL,
    LOGIN_ID Varchar(20) NOT NULL UNIQUE,
    PASSWD Varchar(20) NOT NULL
)
'''
# 10. DATA 생성
'''
INSERT INTO T_TB(
    LOGIN_ID, PASSWD
)
values('jini', '999');
'''
# 11. select * FROM T_TB;
# 12. pip install "psycopg[binary, pool]"
# 13. config 폴더 생성
'''
./config/config.py
PGSQL_TEST_DATABASE_STRING = "host=127.0.0.1 dbname=t_db user=t_user password=1234 port=5432"
PGSQL_TEST_POOL_MIN_SIZE = 10
PGSQL_TEST_POOL_MAX_SIZE = 10
PGSQL_TEST_POOL_MAX_IDLE = 60
'''
# 14. model 폴더 생성
# 15. model/t_pgsql.py 생성 후 코드 작성
# 16. controller/admins.py 생성 후 코드 작성

from fastapi import FastAPI
from controller import items, users, admins

app = FastAPI()
app.include_router(items.router)
app.include_router(users.router)
app.include_router(admins.router)

@app.get("/")
def home():
    # json 구조
    return {"Hello:" "here is HOME"}