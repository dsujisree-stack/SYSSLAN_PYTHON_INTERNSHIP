print("\n======= MATRIX PERFORMANCE REPORT =======\n")

smart_matrix = [
    [7, 14, 21],
    [12, 18, 24],
    [30, 11, 9]
]

largest_row_total = 0
best_row_number = 0
complete_grid_total = 0

print("Matrix Preview:\n")

for row in smart_matrix:
    for value in row:
        print(f"| {value} |", end=" ")
    print()

print("\n====== Row Analysis ======\n")

for row_number in range(len(smart_matrix)):

    current_total = 0

    for single_value in smart_matrix[row_number]:
        current_total += single_value

    print(
        f"Row {row_number + 1} Score = "
        f"{current_total}"
    )

    complete_grid_total += current_total

    if current_total > largest_row_total:
        largest_row_total = current_total
        best_row_number = row_number + 1

print("\n====== Final Report ======")
print(f"Highest Row : Row {best_row_number}")
print(f"Highest Score : {largest_row_total}")
print(f"Complete Grid Total : {complete_grid_total}")
