#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division



def main():
    # Edge cases for division
    print("Edge Case 1:")
    safe_print_division(10, 2)

    print("Edge Case 2:")
    safe_print_division(0, 5)

    print("Edge Case 3:")
    safe_print_division(-10, 2)

    print("Edge Case 4:")
    safe_print_division(10, 0)

    print("Edge Case 5:")
    safe_print_division(3, 2)

    print("Edge Case 6:")
    safe_print_division(-8, 4)

    print("Edge Case 7:")
    safe_print_division(15, -3)

    print("Edge Case 8:")
    safe_print_division(0, 0)

    print("Edge Case 9:")
    safe_print_division(1, 1)

    print("Edge Case 10:")
    safe_print_division(-7, -2)


if __name__ == "__main__":
    main()
