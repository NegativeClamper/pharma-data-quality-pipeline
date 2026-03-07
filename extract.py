# extract.py
import pandas as pd
import random
from faker import Faker
import config

fake = Faker()

# --- Helper Functions ---
def heart_rate():
    if random.random() < 0.05:
        return fake.random_element([900, 1000, 0, -50, -3453, 456])
    else:
        return fake.random_int(min=40, max=150)

def get_bp_values():
    systolic = fake.random_int(min=90, max=180)
    diastolic = fake.random_int(min=60, max=120)
    return f"{systolic}/{diastolic} mmHg"

def unique_patient_id():
    unique_num = fake.unique.random_int(min=0, max=999999)
    return f"PT-{unique_num:06d}"

def trial_stage():
    return fake.random_element(elements=["Phase 1", "Phase 2", "Completed"])

def get_error_code():
    if random.random() < 0.80:
        return None
    else:
        return fake.random_element(["E-001", "E-002", "E-404"])


# extract.py (Bottom Section)

def generate_clinical_data():
    print(f"Starting extraction: Generating {config.NUM_ROWS_TO_GENERATE} records...")
    
    patient_data = []
    
    # Use the config variable instead of hardcoding 10000
    for _ in range(config.NUM_ROWS_TO_GENERATE):
        patient_data.append({
            "patient_id": unique_patient_id(),
            "heart_rate": heart_rate(),
            "blood_pressure": get_bp_values(),
            "trial_stage": trial_stage(),
            "error_code": get_error_code()
        })

    # Injecting the 50 duplicates
    duplicates = patient_data[0:50]
    patient_data.extend(duplicates)

    # Convert to DataFrame and save using the config file path
    df = pd.DataFrame(patient_data)
    df.to_csv(config.RAW_DATA_FILE, index=False)
    
    print(f"Extraction complete! Saved to {config.RAW_DATA_FILE}.")
    
