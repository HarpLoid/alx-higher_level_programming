#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    arg_count = len(argv)
    num_of_args = arg_count - 1

    if (arg_count == 1):
        print("{} arguments.".format(num_of_args))
    elif (arg_count > 1):
        print("{} arguments:".format(num_of_args))
        for i in range(1, arg_count):
            print("{}: {}".format(i, argv[i]))
    else:
        print("{} argument".format(num_of_args))
        print("{}: {}".format(i, argv[num_of_args]))
