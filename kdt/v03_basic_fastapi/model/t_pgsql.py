# Postgresql 접속 및 커넥션 풀 관련 모듈 가져오기
import psycopg
import psycopg_pool

# 설정 파일(config/cofig.py)에서 DB 설정값 불러오기
from config import config

# psycopg_pool을 사용한 커넥션 풀 생성
pool_default = psycopg_pool.ConnectionPool(
    config.PGSQL_TEST_DATABASE_STRING,        # DB 접속 문자열
    max_idle=config.PGSQL_TEST_POOL_MAX_IDLE, # 최대 유효 커넥션 유지 시간
    max_size=config.PGSQL_TEST_POOL_MAX_SIZE, # 커넥션 풀 최대 크기
    min_size=config.PGSQL_TEST_POOL_MIN_SIZE  # 커넥션 풀 최소 크기
)

# T_TB 테이블의 모든 데이터를 조회하는 함수 정의
def list_admin():
    with pool_default.connection() as conn:
        cur = conn.cursor(row_factory=psycopg.rows.dict_row)
        
        try:
            # SQL 실행
            results = cur.execute("SELECT * FROM T_TB").fetchall()
        except psycopg.OperationalError as err:
            # DB 연결 또는 쿼리 중 에러 발생 시 출력
            print(f"DB 및 쿼리문 확인해주세요. {err}")
    
    # 쿼리 결과 반환
    return results
            