import time
import pandas as pd
from sqlalchemy import create_engine

from db_config import DB_CONFIG

# Queries to benchmark
QUERIES = {
    "total_citizens": "SELECT COUNT(*) FROM citizens;",
    "avg_income_by_region": "SELECT region, AVG(income) FROM citizens GROUP BY region;",
    "employment_rate": "SELECT COUNT(DISTINCT citizen_id) / (SELECT COUNT(*) FROM citizens) * 100 FROM employment;",
    "tax_revenue": "SELECT SUM(tax_paid) FROM taxes WHERE tax_year >= 2020;",
    "healthcare_costs": "SELECT hospital, SUM(cost) FROM health_records GROUP BY hospital;"
}

# Connect to databases
def get_engine(db):
    return create_engine(DB_CONFIG[db])

# Run benchmark
def run_benchmark(db):
    engine = get_engine(db)
    results = {}
    with engine.connect() as conn:
        for name, query in QUERIES.items():
            start = time.time()
            df = pd.read_sql(query, conn)
            end = time.time()
            results[name] = round(end - start, 3)
    return results

# Execute benchmark for both databases
def main():
    print("Running benchmarks...")
    for db in ["clickhouse", "postgresql"]:
        print(f"Benchmarking {db.upper()}...")
        results = run_benchmark(db)
        for query, duration in results.items():
            print(f"{query}: {duration} sec")
        print("-")

if __name__ == "__main__":
    main()

