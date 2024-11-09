import sqlite3

# Connect to your database
db_path = 'Clients.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Update the VAT_Bool value in the second row
update_query = """
UPDATE clients
SET address = "Drève de Limauges, 10"
WHERE rowid = 2;
"""

# Execute the update query
cursor.execute(update_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("VAT_Bool in the second row has been updated to 0.")

# import sqlite3

# # Connect to your database
# db_path = 'Clients.db'
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# # Get the table name (you should replace this with the actual table name)
# table_name = 'clients'
# last_name_column = 'last_name'  # Replace with your actual last name column name

# # Create a temporary table to hold the sorted data
# create_temp_table_query = f"""
# CREATE TABLE {table_name}_sorted AS
# SELECT * FROM {table_name}
# ORDER BY {last_name_column} ASC;
# """

# # Execute the query to create the sorted table
# cursor.execute(create_temp_table_query)

# # Drop the original table
# drop_original_table_query = f"DROP TABLE {table_name};"
# cursor.execute(drop_original_table_query)

# # Rename the temporary sorted table to the original table name
# rename_table_query = f"ALTER TABLE {table_name}_sorted RENAME TO {table_name};"
# cursor.execute(rename_table_query)

# # Commit the changes and close the connection
# conn.commit()
# conn.close()

# print(f"Database sorted by {last_name_column} and saved back to {db_path}.")