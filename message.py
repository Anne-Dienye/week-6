#coding
def decrypt_with_interval(encrypted_message, interval):
    decrypted = encrypted_message[::interval + 1]  # Extract characters at the interval
    return decrypted

# Test the decryption
encrypted_message = input("Enter the encrypted message: ")
interval = int(input("Enter the interval used: "))
decrypted_message = decrypt_with_interval(encrypted_message, interval)
print(f"Decrypted message: {decrypted_message}")