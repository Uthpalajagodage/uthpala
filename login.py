import mysql.connector
from tkinter import *

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="hobbies.db"
)

# Create the login window
window = Tk()
window.title("Login")

# Create the username label and input field
username_label = Label(window, text="Username:")
username_label.pack()
username_input = Entry(window)
username_input.pack()

# Create the password label and input field
password_label = Label(window, text="Password:")
password_label.pack()
password_input = Entry(window, show="*")
password_input.pack()

# Define the login function
def login():
    # Get the username and password from the input fields
    username = username_input.get()
    password = password_input.get()

    # Query the database for the user's login information
    cursor = conn.cursor()
    sql = "SELECT * FROM users WHERE username = %s AND password = %s"
    values = (username, password)
    cursor.execute(sql, values)
    user = cursor.fetchone()
    cursor.close()

    # Check if the user was found in the database
    if user:
        print("Login successful!")
        # Add code to redirect to the main application here
    else:
        print("Incorrect username or password.")

# Create the login button
login_button = Button(window, text="Login", command=login)
login_button.pack()

# Start the login window
window.mainloop()
