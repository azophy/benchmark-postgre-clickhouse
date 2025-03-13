import csv
import random
import numpy as np
from datetime import datetime, timedelta

# Configuration
#NUM_CITIZENS = 50_000_000
NUM_CITIZENS = 50_000_000
EMPLOYMENT_RATIO = 0.6  # 60% of citizens have employment records
HEALTH_VISIT_RATIO = 0.4  # 40% of citizens have health records
TAX_PAYER_RATIO = 0.7  # 70% of citizens have tax records

# Helper function
def random_date(start_year=1950, end_year=2024):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

def generate_citizens():
    for i in range(1, NUM_CITIZENS + 1):
        print(f"create citizen{i}")
        yield [
            i, f"Citizen_{i}", random.randint(18, 90),
            random.choice(['Male', 'Female', 'Other']),
            f"Address_{i}", random.choice(["New York", "Los Angeles", "Chicago", "Houston", "Miami"]),
            random.choice(["East", "West", "North", "South"]), "USA",
            round(random.uniform(20000, 150000), 2),
            random.choice(["None", "Primary", "Secondary", "Tertiary"]),
            random_date(2000, 2024).strftime('%Y-%m-%d')
        ]

def generate_employment():
    num_employment = int(NUM_CITIZENS * EMPLOYMENT_RATIO)
    for i in range(num_employment):
        print(f"create employment {i}")
        yield [
            random.randint(1, NUM_CITIZENS),
            random.choice(["Company_A", "Company_B", "Company_C"]),
            random.choice(["Engineer", "Manager", "Technician"]),
            round(random.uniform(30000, 200000), 2),
            random_date(1990, 2024).strftime('%Y-%m-%d'),
            random_date(2000, 2025).strftime('%Y-%m-%d') if random.random() > 0.2 else None,
            random_date(2000, 2024).strftime('%Y-%m-%d')
        ]

def generate_health_records():
    num_health_visits = int(NUM_CITIZENS * HEALTH_VISIT_RATIO)
    for i in range(num_health_visits):
        print(f"create health record {i}")
        yield [
            random.randint(1, NUM_CITIZENS),
            random_date(2000, 2024).strftime('%Y-%m-%d'),
            random.choice(["Hospital_X", "Hospital_Y", "Hospital_Z"]),
            random.choice(["Flu", "Diabetes", "Heart Disease", "Injury"]),
            round(random.uniform(100, 10000), 2),
            random_date(2000, 2024).strftime('%Y-%m-%d')
        ]

def generate_taxes():
    num_tax_payers = int(NUM_CITIZENS * TAX_PAYER_RATIO)
    for i in range(num_tax_payers):
        print(f"create tax record {i}")
        yield [
            random.randint(1, NUM_CITIZENS),
            random.randint(2000, 2024),
            round(random.uniform(500, 50000), 2),
            random_date(2000, 2024).strftime('%Y-%m-%d')
        ]

def write_csv(filename, generator, headers):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(generator)

if __name__ == '__main__':
    print("Generating CSV files...")
    write_csv("csv/citizens.csv", generate_citizens(), ["id", "name", "age", "gender", "address", "city", "region", "country", "income", "education_level", "created_at"])
    write_csv("csv/employment.csv", generate_employment(), ["citizen_id", "company", "position", "salary", "start_date", "end_date", "created_at"])
    write_csv("csv/health_records.csv", generate_health_records(), ["citizen_id", "visit_date", "hospital", "diagnosis", "cost", "created_at"])
    write_csv("csv/taxes.csv", generate_taxes(), ["citizen_id", "tax_year", "tax_paid", "created_at"])
    print("CSV files generated successfully!")

