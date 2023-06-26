#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers




def main():
    # Edge case 1: Empty list
    my_list = []
    x = 5
    print("Number of integers printed:", safe_print_list_integers(my_list, x))

    # Edge case 2: List with integers and non-integers
    my_list = [1, 2, "3", 4.5, "five", 6]
    x = 4
    print("Number of integers printed:", safe_print_list_integers(my_list, x))

    # Edge case 3: List with only non-integers
    my_list = ["one", "two", "three"]
    x = 3
    print("Number of integers printed:", safe_print_list_integers(my_list, x))

    # Edge case 4: List with more elements than x
    my_list = [1, 2, 3, 4, 5, 6]
    x = 4
    print("Number of integers printed:", safe_print_list_integers(my_list, x))

    # Edge case 5: List with fewer elements than x
    my_list = [1, 2, 3]
    x = 5
    print("Number of integers printed:", safe_print_list_integers(my_list, x))

    # Edge case 6: List with all integers
    my_list = [10, 20, 30, 40, 50]
    x = 5
    print("Number of integers printed:", safe_print_list_integers(my_list, x))

    # Edge case 7: List with a mix of integers and non-integers at the beginning
    my_list = ["one", "two", 3, 4, 5]
    x = 5
    print("Number of integers printed:", safe_print_list_integers(my_list, x))

    # Edge case 8: List with a mix of integers and non-integers at the end
    my_list = [1, 2, 3, "four", "five"]
    x = 5
    print("Number of integers printed:", safe_print_list_integers(my_list, x))

    # Edge case 9: List with a mix of integers and non-integers in the middle
    my_list = [1, "two", 3, "four", 5]
    x = 5
    print("Number of integers printed:", safe_print_list_integers(my_list, x))

    # Edge case 10: List with x equal to zero
    my_list = [1, 2, 3, 4, 5]
    x = 0
    print("Number of integers printed:", safe_print_list_integers(my_list, x))


if __name__ == "__main__":
    main()
