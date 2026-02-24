import random
import string

print("🔐 Welcome to Password Generator")

# Ask user for password length
length = int(input("Enter password length: "))

# Define characters to use
letters = string.ascii_letters      # a-z + A-Z
digits = string.digits              # 0-9
symbols = string.punctuation        # !@#$%^&* etc

all_characters = letters + digits + symbols

# Generate password
password = ""

for i in range(length):
    random_char = random.choice(all_characters)
    password += random_char

print("\n✅ Your Generated Password is:")
print(password)
