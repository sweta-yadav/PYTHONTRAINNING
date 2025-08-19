
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    rem = a % b
    a = b
    b = rem

print("GCD is:", a)
