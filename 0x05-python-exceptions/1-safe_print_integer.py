#!/usr/bin/python3
if __name__ == "__main__":
    # This is main
    print()


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
    except TypeError:
        return False
