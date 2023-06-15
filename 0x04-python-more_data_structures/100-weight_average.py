#!/usr/bin/python3

def weight_average(my_list=[]):
    sum2 = 0
    mul2 = 0
    denom = 0

    for i in range(len(my_list)):
        mul2 = my_list[i][0] * my_list[i][1]
        sum2 = sum2 + mul2
        denom = denom + my_list[i][1]

    result = sum2 / denom
    return result
