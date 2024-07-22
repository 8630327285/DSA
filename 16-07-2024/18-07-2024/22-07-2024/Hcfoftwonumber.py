def compute_hcf(a, b):
    # Method to compute HCF using Euclidean algorithm
    while b:
        a, b = b, a % b
    return a

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Compute HCF
hcf = compute_hcf(num1, num2)

# Output the result
print(f"The HCF of {num1} and {num2} is: {hcf}")
