#!/usr/bin/python3
if __name__ == "__main__":
    # This is main
    print()


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            if isinstance(my_list_1[i], (int, float)) and
            isinstance(my_list_2[i], (int, float)):
                new_list.append(my_list_1[i] / my_list_2[i])
            else:
                print("wrong type")
                new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
            continue
        except IndexError:
            print("out of range")
            continue
        return new_list
