#coding
def find_factors(n):
    factors = [i for i in range(1, abs(n) + 1) if n % i == 0]
    return factors

# Test the function
number = int(input("Enter an integer: "))
factors = find_factors(number)
print(f"The factors of {number} are: {factors}")