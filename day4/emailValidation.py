import re

pattern = r"^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$"

class InvalidEmailError(Exception):
   pass

# Function to validate email addresses
def validate_email(email, pattern):
    if re.match(pattern, email):
        print("Valid")
    else:
        raise validate_email(email,pattern)

try:
    email = input("Enter your email address: ")
    validate_email(email, pattern)
except InvalidEmailError as i:
    print(i)
