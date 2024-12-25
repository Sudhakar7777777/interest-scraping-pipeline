import sqlite3
import logging

def store_data_in_sqlite(data, db_path='db/db.sqlite3'):
    """Store scraped data in SQLite database"""
    try:
        logging.debug(f"Connecting to SQLite database at {db_path}")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS interest_rates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tenure TEXT NOT NULL,
                usd_interest_rate TEXT NOT NULL,
                date_scraped TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        for entry in data:
            cursor.execute('''
                INSERT INTO interest_rates (tenure, usd_interest_rate)
                VALUES (?, ?)
            ''', (entry['Tenure'], entry['USD Interest Rate']))

        conn.commit()
        conn.close()
        logging.debug(f"Data stored in {db_path}")
    except Exception as e:
        logging.error(f"Error storing data: {str(e)}")
        raise
