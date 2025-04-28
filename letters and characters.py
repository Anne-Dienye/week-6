#coding
import random
import string

# Function to encrypt a message with random interval
def encrypt_with_interval(message):
    interval = random.randint(2, 20)
    encrypted = []
    for i, char in enumerate(message):
        encrypted.append(char)
        if i < len(message) - 1:  # Add random letters between characters
            encrypted.extend(random.choices(string.ascii_letters, k=interval))
    return ''.join(encrypted), interval

# Test the function
message = input("Enter a message: ")
encrypted_message, interval = encrypt_with_interval(message)
print(f"Encrypted message: {encrypted_message}")
print(f"Interval used: {interval}")