# main.py
import config
from extract import generate_clinical_data
from transform import clean_clinical_data
from load import load_to_sql

def run_pipeline():
    print("🚀 Starting Clinical ETL Pipeline...")
    
    # Step 1: Extract
    generate_clinical_data()
    
    # Step 2: Transform
    df = clean_clinical_data()
    
    # Step 3: Load
    load_to_sql(df)
    
    print("✅ Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()