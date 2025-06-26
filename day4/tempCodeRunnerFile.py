class InvalidEmailError(Exception):
   pass

# Function to validate email addresses
def validate_email(email):
    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email address format.")

email = input("Enter your email address: ")

try:
    raise validate_email(email)
except InvalidEmailError as i:
    print(i)
