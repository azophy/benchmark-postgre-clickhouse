import os
from sqlalchemy import create_engine

from db_config import DB_CONFIG

# Table mapping
TABLES = {
    "citizens.csv": "citizens",
    "employment.csv": "employment",
    "health_records.csv": "health_records",
    "taxes.csv": "taxes"
}

# Connect to database
def get_engine(db):
    return create_engine(DB_CONFIG[db])

# ClickHouse import function using file() table function
def import_csv_clickhouse(conn, csv_file, table_name):
    query = f"""
        INSERT INTO {table_name} SELECT * FROM file('{csv_file}', 'CSVWithNames')
    """
    conn.execute(query)

# PostgreSQL import function
def import_csv_postgresql(conn, csv_file, table_name):
    query = f"""
        COPY {table_name} FROM '{csv_file}' WITH CSV HEADER;
    """
    conn.execute(query)

# Run import process
def main():
    for db in ["clickhouse", "postgresql"]:
        print(f"Importing data into {db.upper()}...")
        engine = get_engine(db)
        with engine.connect() as conn:
            for csv_file, table_name in TABLES.items():
                if not os.path.exists(csv_file):
                    print(f"File {csv_file} not found, skipping...")
                    continue
                
                try:
                    if db == "clickhouse":
                        import_csv_clickhouse(conn, csv_file, table_name)
                    elif db == "postgresql":
                        import_csv_postgresql(conn, csv_file, table_name)
                    print(f"Successfully imported {csv_file} into {db}.{table_name}")
                except Exception as e:
                    print(f"Error importing {csv_file} into {db}.{table_name}: {e}")
        print("-")

if __name__ == "__main__":
    main()

