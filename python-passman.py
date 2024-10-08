import hashlib  # Importing the hashlib module to use cryptographic hash functions
import getpass  # Importing getpass to securely handle password input without echoing it on the screen

password_manager = {}  # Dictionary to store usernames and their hashed passwords

# Function to create a new account
def create_account():
    username = input("Enter your desired username: ")  # Prompting the user to enter a username
    password = getpass.getpass("Enter your desired password: ")  # Prompting the user to enter a password securely
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hashing the password using SHA-256
    password_manager[username] = hashed_password  # Storing the username and hashed password in the dictionary
    print("Account created successfully!")  # Confirmation message for account creation

# Function to handle user login
def login():
    username = input("Enter your username: ") 
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hashing the entered password using SHA-256

    # Checking if the username exists and the entered password matches the stored hashed password
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successful!")  # Successful login message
    else:
        print("Invalid username or password.")  # Error message if login fails


def main():
    while True: 
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ") 
        if choice == "1":
            create_account()  
        elif choice == "2":
            login()  
        elif choice == "0":
            break 
        else:
            print("Invalid choice.")  

# Ensuring the main function runs only if the script is executed directly
if __name__ == "__main__":
    main()