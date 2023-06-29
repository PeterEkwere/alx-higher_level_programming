#!/usr/bin/python3
if __name__ == "__main__":
    # This is main
    print()


def safe_print_list_integers(my_list=[], x=0):

    try:
        index = 0
        length = 0
        j = 0
        count = 0

        for j in my_list:
            length += 1

        while index < x and index < length:
            if isinstance(my_list[index], int):
                print("{:d}".format(my_list[index]), end="")
                count += 1
            index += 1
        print()
        return count
    except IndexError:
        pass
