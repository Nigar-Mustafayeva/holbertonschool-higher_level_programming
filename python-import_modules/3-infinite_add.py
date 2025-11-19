#!/usr/bin/python3
import sys

def sum_command_line_arguments():
    """
    Calculates and prints the sum of all numerical command-line arguments.
    """
    total = 0
    # sys.argv[0] is the script name, so we start from index 1 for arguments
    for arg in sys.argv[1:]:
        try:
            # Convert argument to an integer and add to total
            total += int(arg)
        except ValueError:
            # Handle cases where an argument is not a valid integer
            print(f"Warning: '{arg}' is not a valid number and will be ignored.")
    print(f"{total}")

if __name__ == "__main__":
    sum_command_line_arguments()
