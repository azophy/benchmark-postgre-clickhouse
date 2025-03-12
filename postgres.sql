CREATE TABLE citizens (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INT NOT NULL,
    gender TEXT CHECK (gender IN ('Male', 'Female', 'Other')),
    address TEXT,
    city TEXT,
    region TEXT,
    country TEXT,
    income NUMERIC(10,2),
    education_level TEXT CHECK (education_level IN ('None', 'Primary', 'Secondary', 'Tertiary')),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE employment (
    id SERIAL PRIMARY KEY,
    citizen_id INT REFERENCES citizens(id),
    company TEXT,
    position TEXT,
    salary NUMERIC(10,2),
    start_date DATE,
    end_date DATE NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE health_records (
    id SERIAL PRIMARY KEY,
    citizen_id INT REFERENCES citizens(id),
    visit_date DATE NOT NULL,
    hospital TEXT,
    diagnosis TEXT,
    cost NUMERIC(10,2),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE taxes (
    id SERIAL PRIMARY KEY,
    citizen_id INT REFERENCES citizens(id),
    tax_year INT NOT NULL,
    tax_paid NUMERIC(10,2),
    created_at TIMESTAMP DEFAULT NOW()
);
