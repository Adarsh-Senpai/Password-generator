import random
import string

# Step 1: Prompt the user to specify the desired length of the password
password_length = int(input("Enter the desired password length: "))

# Step 2: Generate a password using a combination of random characters
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(password_length))

# Step 3: Display the generated password
print(f"Generated Password: {password}")
