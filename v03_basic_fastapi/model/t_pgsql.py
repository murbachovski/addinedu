# PostgreSQL 접속 및 커넥션 풀 관련 모듈 불러오기
import psycopg
import psycopg_pool

# 외부 설정 파일(config.py)에서 DB 접속 설정값 불러오기
from config import config

# psycopg_pool을 사용한 커넥션 풀 생성
pool_default = psycopg_pool.ConnectionPool(
    config.PGSQL_TEST_DATABASE_STRING,          # DB 접속 문자열
    max_idle = config.PGSQL_TEST_POOL_MAX_IDLE,  # 최대 유휴 커넥션 유지 시간
    max_size = config.PGSQL_TEST_POOL_MAX_SIZE,  # 커넥션 풀 최대 크기
    min_size = config.PGSQL_TEST_POOL_MIN_SIZE   # 커넥션 풀 최소 크기
)

# TB_ADMIN 테이블의 모든 데이터를 조회하는 함수 정의
def list_admin():
    # 커넥션 풀에서 커넥션 하나 가져오기 (with문 사용하면 자동 반환됨)
    with pool_default.connection() as conn:
        # 커서 생성, row_factory를 dict_row로 설정하여 결과를 딕셔너리로 반환
        cur = conn.cursor(row_factory=psycopg.rows.dict_row)
        
        try:
            # SQL 실행: TB_ADMIN 테이블에서 모든 행 가져오기
            results = cur.execute("SELECT * FROM TB_ADMIN").fetchall()
        except psycopg.OperationalError as err:
            # DB 연결 또는 쿼리 중 에러 발생 시 출력
            print(f"Error querying : {err}")
        
    # 쿼리 결과 반환
    return results
