rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

for i in range(rows):
    for j in range(cols):
        # Print X in first row, last row, first col, last col
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()
