#coding
def simple_encrypt(message):
    return message.replace(" ", "")[::-1]

# Test the function
message = input("Enter a message: ")
encrypted_message = simple_encrypt(I Love God)
print(f"Encrypted message: {encrypted_message}")