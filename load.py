import sqlite3
import config

def load_to_sql(df):
    print(f"🗄️ Connecting to database: {config.DB_NAME}...")
    conn = sqlite3.connect(config.DB_NAME)
    df.to_sql(name= config.TABLE_NAME, con= conn, if_exists= 'replace', index= False)
    conn.close()
    print(f"✅ Data successfully loaded into table: {config.TABLE_NAME}")