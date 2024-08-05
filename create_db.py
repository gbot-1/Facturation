import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('Clients.db')
cursor = conn.cursor()

# Create a table for clients
cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        vat_number TEXT NOT NULL,
        vat_bool TEXT NOT NULL,
        address TEXT NOT NULL,
        town TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
