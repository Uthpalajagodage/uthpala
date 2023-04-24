import mysql.connector

# Connect to the MySQL server
cnx = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="hobbies.db"
)

# Prompt the user for input
username = input("Enter username: ")
email = input("Enter email: ")
password = input("Enter password: ")

# Create a cursor object
cursor = cnx.cursor()

# Execute an INSERT statement to add the new user
query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
values = (username, email, password)
cursor.execute(query, values)
cnx.commit()

# Print a success message
print(f"User '{username}' has been added to the system.")

# Close the cursor and connection
cursor.close()
cnx.close()
