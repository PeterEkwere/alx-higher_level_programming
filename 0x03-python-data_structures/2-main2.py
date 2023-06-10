#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list


test_cases = [
        ([1, 2, 3, 4, 5], 2, 10),  # Replace element at index 2 with 10
        ([1, 3, 3, 4, 5], -1, 10),  # Index out of range (negative)
        ([1, 2, 3, 4, 5], 5, 10),  # Index out of range (greater than list length)
        ([], 0, 10),  # Empty list
        ([1], 0, 10),  # Replace only element in the list
        ([1, 2, 3], 1, 10),  # Replace element at index 1 with 10
        ([1, 2, 3, 4, 5], 3, 0),  # Replace element at index 3 with 0
        ([1, 2, 3, 4, 5], 4, 100),  # Replace last element in the list
        ([1, 2, 3, 4, 5], 0, 100),  # Replace first element in the list
        ([1, 2, 3, 4, 5], 2, 2.5)  # Replace element at index 2 with a float
    ]
for i, test_case in enumerate(test_cases):
    my_list, idx, element = test_case
    result = replace_in_list(my_list, idx, element)
    print(f"Test case {i+1}:")
    print(f"Original list: {my_list}")
    print(f"Updated list: {result}")
    print()

