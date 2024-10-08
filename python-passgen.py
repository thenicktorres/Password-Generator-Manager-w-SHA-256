import random  # Importing the random module to generate random choices
import string  # Importing the string module to access collections of letters, digits, and punctuation


def generate_password(length: int = 10):  # Default password length is set to 10, but can be changed
    alphabet = string.ascii_letters + string.digits + string.punctuation  # Combining letters, digits, and punctuation to form the set of possible characters
    password = ''.join(random.choice(alphabet) for i in range(length))  # Randomly selecting 'length' number of characters from the alphabet
    return password  


password = generate_password()


print(f"Generated password: {password}")