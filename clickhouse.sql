CREATE TABLE citizens (
    id UInt64,
    name String,
    age UInt8,
    gender Enum8('Male' = 1, 'Female' = 2, 'Other' = 3),
    address String,
    city String,
    region String,
    country String,
    income Float64,
    education_level Enum8('None' = 1, 'Primary' = 2, 'Secondary' = 3, 'Tertiary' = 4),
    created_at DateTime DEFAULT now()
) ENGINE = MergeTree()
ORDER BY (region, city, age);

CREATE TABLE employment (
    citizen_id UInt64,
    company String,
    position String,
    salary Float64,
    start_date Date,
    end_date Date DEFAULT '2100-01-01',
    created_at DateTime DEFAULT now()
) ENGINE = MergeTree()
ORDER BY (citizen_id, start_date);

CREATE TABLE health_records (
    citizen_id UInt64,
    visit_date Date,
    hospital String,
    diagnosis String,
    cost Float64,
    created_at DateTime DEFAULT now()
) ENGINE = MergeTree()
ORDER BY (citizen_id, visit_date);

CREATE TABLE taxes (
    citizen_id UInt64,
    tax_year UInt16,
    tax_paid Float64,
    created_at DateTime DEFAULT now()
) ENGINE = SummingMergeTree()
ORDER BY (citizen_id, tax_year);
