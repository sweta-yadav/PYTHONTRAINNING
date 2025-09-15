# Pattern Printing Program

n = int(input("Enter any number: "))

# Total size (outer border adds 2 rows/cols)
size = n + 2

for i in range(size):
    for j in range(size):
        # Border condition
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("A", end=" ")
        else:
            # Inside pattern
            if i % 2 == 1:   # odd rows → X
                print("X", end=" ")
            else:            # even rows → $
                print("$", end=" ")
    print()
    