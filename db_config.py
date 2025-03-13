import os

POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB=os.getenv('POSTGRES_DB')
POSTGRES_PORT=os.getenv('POSTGRES_PORT')

# ClickHouse Configuration
CLICKHOUSE_USER=os.getenv('CLICKHOUSE_USER')
CLICKHOUSE_PASSWORD=os.getenv('CLICKHOUSE_PASSWORD')
CLICKHOUSE_DB=os.getenv('CLICKHOUSE_DB')
CLICKHOUSE_HTTP_PORT=os.getenv('CLICKHOUSE_HTTP_PORT')
CLICKHOUSE_TCP_PORT=os.getenv('CLICKHOUSE_TCP_PORT')

# Configuration
DB_CONFIG = {
    "clickhouse": f"clickhouse+native://{CLICKHOUSE_USER}:{CLICKHOUSE_PASSWORD}@clickhouse:9000/{CLICKHOUSE_DB}",
    "postgresql": f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres:{POSTGRES_PORT}/{POSTGRES_DB}"
}

if __name__ == '__main__':
    import sqlalchemy as sa
    uri = DB_CONFIG['clickhouse']
    print('uri:',uri)
    engine = sa.create_engine(uri)
    with engine.connect() as conn:
        res = conn.execute(sa.text('SHOW TABLES;'))
        for row in res:
            print(row)


