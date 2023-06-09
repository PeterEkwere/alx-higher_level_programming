#!/usr/bin/python3
if __name__ == "__main__":
    # this is a script to be imported
    print("this is a script")


def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    for i in range(0, len(my_list)):
        if i == idx:
            return my_list[idx]
