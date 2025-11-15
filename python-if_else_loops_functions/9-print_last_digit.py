#!/usr/bin/python3

def print_last_digit(number):
    """Prints the last digit of a number and returns it"""
    last = abs(number) % 10
    print("{}".format(last), end="")
    return last
