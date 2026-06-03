print("\n========== SMART NUMBER MATRIX ==========\n")

number_box = []
current_number = 1

for row_index in range(3):
    row_data = []

    for column_index in range(3):
        row_data.append(current_number)
        current_number += 1

    number_box.append(row_data)

for single_row in number_box:
    for value in single_row:
        print(f"[ {value} ]", end=" ")
    print()
