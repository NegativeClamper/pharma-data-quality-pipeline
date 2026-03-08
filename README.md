# pharma-data-quality-pipeline
# 🧬 Automated Clinical Data Quality Pipeline (ETL)

## 📌 The Business Problem
In clinical trials, data integrity is paramount. Raw patient logs often contain duplicate entries, missing critical codes, and biological anomalies (e.g., impossible heart rate readings) due to sensor errors or manual entry mistakes. If this raw data is loaded directly into an analytics warehouse, it corrupts trial reporting and compliance.

## 🛠️ The Solution
I engineered a modular ETL (Extract, Transform, Load) pipeline in Python to automate the cleaning and validation of daily clinical trial data before it reaches the data warehouse.

* **Extract:** Generates synthetic daily patient logs (10,000+ records) mimicking real-world messiness (injected duplicates, nulls, and outliers).
* **Transform:** Utilizes **Pandas** to enforce strict data quality rules:
  * Automatically detects and drops identical duplicate records.
  * Imputes missing `error_code` values to maintain schema integrity.
  * Applies boolean filtering to remove biological anomalies (e.g., filtering out heart rates < 40 or > 200 BPM).
* **Load:** Securely ingests the validated, clean dataset into a local **SQLite** relational database for downstream analytics.

## 🏗️ Architecture
The pipeline is fully modularized for enterprise scalability:
* `config.py`: Centralized configuration for biological thresholds and file paths.
* `extract.py` / `transform.py` / `load.py`: Isolated logic modules.
* `main.py`: The pipeline orchestrator.

## 🚀 How to Run Locally
1. Clone the repository.
2. Install pandas, sqlite3
3. bash
   python main.py
   
