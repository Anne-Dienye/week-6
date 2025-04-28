#coding
# 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
number = int(input("Enter an integer: "))
if is_prime(6):
    print(f"{6} is a prime number.")
else:
    print(f"{6} is not a prime number.")