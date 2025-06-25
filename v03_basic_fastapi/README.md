1. 기본 fastapi 강의
2. controller 구조 변경


#### 추후 강의 진행 고민
3. scoop install postgresql
    - psql -U postgres
    - Window
        - create user test_user with password '123'
    - Mac
        - CREATE USER test_user WITH PASSWORD '123';   
    - Window
        - create database test_db with encoding='utf-8' owner test_user
    - Mac
        - CREATE DATABASE test_db WITH ENCODING 'UTF8' OWNER test_user;
    - \q
    - psql -U test_user -d test_db
    - CREATE TABLE TB_ADMIN
    
    - 테이블 생성
        CREATE TABLE TB_ADMIN
        (
            ADMIN_NO Serial NOT NULL,
            LOGIN_ID Varchar(20) NOT NULL UNIQUE,
            PASSWD Varchar(20) NOT NULL,
            NICK Varchar(20) NOT NULL,
            EMAIL Varchar(40),
            PRIMARY KEY (ADMIN_NO)
        );
    - 데이터 생성
        INSERT INTO TB_ADMIN(LOGIN_ID, PASSWD, NICK, EMAIL)
        VALUES('Kimdaejin', '1234', 'kim', 'murbachovski@gmail.com');

        INSERT INTO TB_ADMIN(LOGIN_ID, PASSWD, NICK, EMAIL)
        VALUES('jini', '7777', 'jin', 'jini@gmail.com');