#!/usr/bin/python3
def safe_print_list(my_list=[], x):
    count = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            count += 1
            return count
        except IndexError:
            print()
            return count
