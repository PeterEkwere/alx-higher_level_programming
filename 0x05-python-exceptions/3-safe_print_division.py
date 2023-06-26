#!/usr/bin/python3

if __name__ == "__main__":
    # This is the main function
    print()


def safe_print_division(a, b):
    try:
        result = 0
        result = a / b
        return result
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
