import math

# Function for square
def area_square(side):
    return side * side

# Function for rectangle
def area_rectangle(length, breadth):
    return length * breadth

# Function for circle
def area_circle(radius):
    return math.pi * radius * radius

# Function for triangle
def area_triangle(base, height):
    return 0.5 * base * height

# Main program
print("1. Square")
print("2. Rectangle")
print("3. Circle")
print("4. Triangle")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    side = float(input("Enter side of square: "))
    print("Area of Square =", area_square(side))

elif choice == 2:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    print("Area of Rectangle =", area_rectangle(length, breadth))

elif choice == 3:
    radius = float(input("Enter radius: "))
    print("Area of Circle =", area_circle(radius))

elif choice == 4:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of Triangle =", area_triangle(base, height))

else:
    print("Invalid choice!")