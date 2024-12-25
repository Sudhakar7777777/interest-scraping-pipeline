import sqlite3
import os

def test_database_storage():
    db_path = 'db/test_db.sqlite3'
    # Store data in SQLite
    data = [
        {'Tenure': 'Years >= 1 < 2', 'USD Interest Rate': '5.75'},
        {'Tenure': 'Years >= 2 < 3', 'USD Interest Rate': '4.60'},
    ]
    store_data_in_sqlite(data, db_path)

    # Verify data is in the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM interest_rates')
    rows = cursor.fetchall()
    assert len(rows) > 0
    conn.close()

    # Clean up
    os.remove(db_path)
