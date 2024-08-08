import sqlite3

# Connect to your database
db_path = 'Clients.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Update the VAT_Bool value in the second row
update_query = """
UPDATE clients
SET VAT_Bool = 0
WHERE rowid = 2;
"""

# Execute the update query
cursor.execute(update_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("VAT_Bool in the second row has been updated to 0.")