#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("")
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not j == len(matrix[i])-1:
                    print(matrix[i][j], end=" ")
                else:
                    print(matrix[i][j])
