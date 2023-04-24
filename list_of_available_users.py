import mysql.connector

# Connect to the MySQL server
cnx = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="hobbies.db"
)

# Create a cursor object
cursor = cnx.cursor()

# Execute a SELECT statement to retrieve the user data
query = "SELECT username, email FROM users"
cursor.execute(query)

# Fetch all the rows
rows = cursor.fetchall()

# Print the user data
print("List of available users:")
for row in rows:
    print(f"Username: {row[0]}, Email: {row[1]}")

# Close the cursor and connection
cursor.close()
cnx.close()
