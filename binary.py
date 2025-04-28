#coding
def to_binary(n):
    if n <= 0:
        return "Input must be a positive integer."
    return bin(n)[2:]  # Use bin() and strip the '0b' prefix

# Test the function
number = int(input("Enter a positive integer: "))
binary_representation = to_binary(number)
print(f"The binary representation of {number} is {binary_representation}.")