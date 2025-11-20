#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:          # outer loop for each row
       for element in row:     # inner loop for each element in row
        print(element, end=" ")
       print("$\n")   
    print()
print_matrix_integer(matrix=[[]])
