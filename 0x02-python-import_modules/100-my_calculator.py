#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
else:
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == '+':
        result = add(a, b)
    elif sys.argv[2] == '*' and len(sys.argv[2]) == 1:
        result = mul(a, b)
    elif sys.argv[2] == '-':
        result = sub(a, b)
    elif sys.argv[2] == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

print("{}".format(result))
