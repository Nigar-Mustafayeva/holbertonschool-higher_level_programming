#!/usr/bin/python3
import sys


def sum_command_line_arguments():
    total = 0
    for arg in sys.argv[1:]:
        total += int(arg)
    print(f"{total}")


if __name__ == "__main__":
    sum_command_line_arguments()
