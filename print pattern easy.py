def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

rows = int(input("Number of rows: "))
print_pattern(rows)
