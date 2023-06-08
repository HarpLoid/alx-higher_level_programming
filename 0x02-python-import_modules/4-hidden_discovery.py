#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    names_sorted = sorted(name for name in names if not name.startswith("__"))
    for name in names_sorted:
        print("{}".format(name))
