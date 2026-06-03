print("\n======= FIBONACCI MASTER =======\n")

try:
    total_terms = int(
        input("Enter number of terms: ")
    )

    first_number = 0
    second_number = 1

    fibonacci_list = []

    even_count = 0
    odd_count = 0

    for _ in range(total_terms):

        fibonacci_list.append(
            first_number
        )

        if first_number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        next_value = (
            first_number +
            second_number
        )

        first_number = second_number
        second_number = next_value

    print(
        "\n====== Fibonacci Report ======\n"
    )

    print(
        "Generated Sequence:"
    )

    print(fibonacci_list)

    print(
        f"\nHighest Number : "
        f"{max(fibonacci_list)}"
    )

    print(
        f"Even Numbers : "
        f"{even_count}"
    )

    print(
        f"Odd Numbers : "
        f"{odd_count}"
    )

except ValueError:
    print(
        "⚠️ Please enter numbers only!"
    )
