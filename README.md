BENCHMARK POSTGRES & CLICKHOUSE FOR CITIZEN RECORDS
===================================================

## how to use
1. clone repo
2. copy `.env.example` into `.env`
3. run `docker compose up -d`
4. enter container using command `docker compose exec app bash`
5. generate data by running inside above container: `uv run generate_data.py` (may take ~20 min)

![Generated file sizes](misc/csv-sizes.png?raw=true "Generated CSV file sizes")

6. Load the csv into database using `uv run load_database.csv`
7. run benchmark script: `uv run benchmark.py`
