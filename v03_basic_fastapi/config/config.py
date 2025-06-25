PGSQL_TEST_DATABASE_STRING = "host=127.0.0.1 dbname=t_db user=t_user password=1234 port=5432"
PGSQL_TEST_POOL_MIN_SIZE = 10
PGSQL_TEST_POOL_MAX_SIZE = 10
PGSQL_TEST_POOL_MAX_IDLE = 60

# 이 설정들은 PostgreSQL 연결을 효율적이고 안정적으로 관리하기 위한 것이에요.
# 실서비스에서는 수많은 유저가 동시에 DB에 접근하니까,
# 연결을 재사용하고, 수 제한을 두고, 유휴 연결은 정리하면서,
# 빠르고 안정적인 연결을 유지하려고 이런 설정들을 따로 관리해주는 거예요.