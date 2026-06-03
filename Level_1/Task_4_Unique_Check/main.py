print("\n======= GRID UNIQUENESS ANALYZER =======\n")

number_grid = [
    [12, 25, 38],
    [41, 25, 57],
    [63, 72, 81]
]

collected_numbers = []
duplicate_values = []

print("Grid Preview:\n")

for row in number_grid:
    for item in row:
        print(f"[ {item} ]", end=" ")
    print()

for row in number_grid:
    for number in row:

        if number in collected_numbers:
            duplicate_values.append(number)

        else:
            collected_numbers.append(number)

print("\n====== Analysis Result ======\n")

if len(duplicate_values) == 0:
    print("🎉 All numbers are unique!")
else:
    print("⚠️ Duplicate numbers found!")
    print("Repeated Numbers:", duplicate_values)

total_numbers = len(collected_numbers) + len(duplicate_values)

unique_percentage = (
    len(collected_numbers) / total_numbers
) * 100

print(
    f"\nUnique Score: "
    f"{unique_percentage:.2f}%"
)
