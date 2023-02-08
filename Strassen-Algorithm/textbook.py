# Diego Araque - A01026037
# Uriel Martinez - A01781698
# Luis Fernando - A01745186
# Marco Antonio - A01025334

import csv
import numpy as np

def parce_csv(route):
    """
    Funcion que lee un archivo y regresa una
    np array de cada renglon del mismp 
    """
    file = csv.reader(open(route), delimiter=',')

    matrix = [row for row in file]
    
    # Elements are parsed as string
    # so we need to pass them to integers
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = int(matrix[i][j])

    return np.array(matrix)
    
def textBook(A, B):
    # scalar multiplications
    scalars = 0
    # create a matrix in numpy filled with zeros
    # the order of the matrix, will have the same order
    # as matrixA and matrixB. The type of the array will be of numbers
    matrixC = np.zeros((A.shape[0], A.shape[1]), dtype = int)
    # iterate for each row of the matrix
    for rows in range(A.shape[0]):
        # iterate for each value of the row, in other words for the columns
        for colsA in range(A.shape[1]):
            # iterate matrix B columns
            for colsB in range(B.shape[1]):
                # make mulyiplications and sums of each level
                matrixC[rows, colsA] += A[rows, colsB]*B[colsB, colsA]
                # since a multiplication was done, we increase the counter
                scalars += 1
    print("Scalar Multiplications: ", scalars)
    print(matrixC)


if __name__ == "__main__":
    """"
    Matrixes
    """
    pathMatrixA = input("Path of the matrix A: ")
    pathMatrixB = input("Path of the matrix B: ")
    matrixA = parce_csv(pathMatrixA)
    matrixB = parce_csv(pathMatrixB)
    
    print("Textbook Algorithm:")
    textBook(matrixA, matrixB)
