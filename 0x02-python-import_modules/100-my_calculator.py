#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    num_of_args = len(argv) - 1

    if num_of_args < 3 or num_of_args > 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    operator_list = ['+', '-', '*', '/']
    a = int(argv[1])
    operator = str(argv[2])
    b = int(argv[3])

    if operator in operator_list and operator == operator_list[0]:
        print("{:d} {} {:d} = {:d}".format(a, operator_list[0], b, add(a, b)))
    elif operator in operator_list and operator == operator_list[1]:
        print("{:d} {} {:d} = {:d}".format(a, operator_list[1], b, sub(a, b)))
    elif operator in operator_list and operator == operator_list[2]:
        print("{:d} {} {:d} = {:d}".format(a, operator_list[2], b, mul(a, b)))
    elif operator in operator_list and operator == operator_list[3]:
        print("{:d} {} {:d} = {:d}".format(a, operator_list[3], b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
