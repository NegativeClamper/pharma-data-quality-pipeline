import pandas as pd
import config

def clean_clinical_data():
    print("Starting data transformation...")
    df = pd.read_csv(config.RAW_DATA_FILE)

    initial_rows = len(df)
    df = df.drop_duplicates()
    print(f"   -> Dropped {initial_rows - len(df)} duplicate rows.")

    df['error_code'] = df['error_code'].fillna("None")

    df = df[(df["heart_rate"] >= config.MIN_HEART_RATE) & (df["heart_rate"] <= config.MAX_HEART_RATE)]

    print(f"Transformation complete, clean rows remaining: {len(df)}")

    return df