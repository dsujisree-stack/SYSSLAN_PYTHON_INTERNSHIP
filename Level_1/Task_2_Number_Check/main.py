print("\n======= NUMBER FINDER SYSTEM =======\n")

smart_grid = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]

print("Grid Numbers:")
for line in smart_grid:
    print(line)

try:
    user_number = int(input("\nEnter a number to search: "))

    number_found = False

    for row in smart_grid:
        if user_number in row:
            number_found = True
            break

    if number_found:
        print(f"✅ {user_number} is available in the grid!")
    else:
        print(f"❌ {user_number} is not found in the grid.")

except ValueError:
    print("Please enter numbers only!")
