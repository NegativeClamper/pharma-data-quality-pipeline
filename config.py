# config.py

# File Paths & Database Names
RAW_DATA_FILE = "daily_clinical_logs.csv"
DB_NAME = "clinical_trials.db"
TABLE_NAME = "clinical_data"

# Generation Parameters
NUM_ROWS_TO_GENERATE = 10000

# Biological Thresholds (For the Transform phase)
MIN_HEART_RATE = 40
MAX_HEART_RATE = 200