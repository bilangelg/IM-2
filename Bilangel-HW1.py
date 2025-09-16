print('======Using List======\n')

rows = int(input("Enter row: "))
cols = int(input("Enter col: "))

matrix = []

for r in range(rows):
    print(f"\nRow {r+1}")
    row_data = []
    for c in range(cols):
        num = float(input(f"Enter number{c+1}: "))
        row_data.append(num)
    matrix.append(row_data)

print("\nThe numbers are:\n")
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

search_val = float(input("\nSearch: "))

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == search_val:
            print(f"Number {search_val} found at Row {r}, Col {c}")

print("\n======Using Tuple======\n")

rows = int(input("Enter row: "))
cols = int(input("Enter col: "))

matrix = []

for r in range(rows):
    print(f"\nRow {r+1}")
    row_data = []
    for c in range(cols):
        num = float(input(f"Enter number{c+1}: "))
        row_data.append(num)
    matrix.append(tuple(row_data))

matrix = tuple(matrix)

print("\nThe numbers are:\n")
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

search_val = float(input("\nSearch: "))

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == search_val:
            print(f"Number {search_val} found at Row {r}, Col {c}")

print("\n======Using Dictionary======\n")

rows = int(input("Enter row: "))
cols = int(input("Enter col: "))

matrix = {} 

for r in range(rows):
    print(f"\nRow {r+1}")
    for c in range(cols):
        num = float(input(f"Enter number{c+1}: "))
        matrix[(r, c)] = num  

print("\nThe numbers are:\n")
for r in range(rows):
    for c in range(cols):
        print(matrix[(r, c)], end=" ")
    print()

search_val = float(input("\nSearch: "))

for key, value in matrix.items():
    if value == search_val:
        print(f"Number {search_val} found at Row {key[0]}, Col {key[1]}")
