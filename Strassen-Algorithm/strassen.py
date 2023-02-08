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


scalarMult = 0
def multiply(A, B):
    global scalarMult
    try:
        if len(A) > 2 and len(B) > 2: # exepction here (when an scalar arrives, there is no length)
            # divide matrixes in half
            a11, a12, a21, a22 = divide_half(A)
            b11, b12, b21, b22 = divide_half(B)
            return operations(a11, a12, a21, a22, b11, b12, b21, b22,A)
        elif len(A) == 2 and len(B) == 2:
            # Base case 
            return operations(A[0][0], A[0][1], A[1][0], A[1][1], B[0][0], B[0][1], B[1][0], B[1][1],A)
    except:
        # since a multiplication is done, we increase the value
        scalarMult +=1
        # At some point A and B will be scalars A=num B=num
        return A * B


def operations(a11, a12, a21, a22, b11, b12, b21, b22, A):
    # strassen formulas
    # we get a value once they are scalars, if not, they keep being called recursively
    # until we get that multiplication. If not only sums are performed
    m1 = multiply((a11 + a22), (b11 + b22))
    m2 = multiply((a21 + a22), b11)
    m3 = multiply(a11, (b12 - b22))
    m4 = multiply(a22, (b21 - b11))
    m5 = multiply((a11 + a12), b22)
    m6 = multiply((a21 - a11), (b11 + b12))
    m7 = multiply((a12 - a22), (b21 + b22))

    c11 = m1 + m4 - m5 + m7
    c12 = m3 + m5
    c21 = m2 + m4 
    c22 = m1 - m2 + m3 + m6
    
    # we create a matrix with the same order as the matrixes we are multiplying
    # with zeros
    result = np.zeros((A.shape[0], A.shape[1]), dtype = int)
    # we divide get the half of the matrix
    half = len(result)//2
    # we fill the matrix with the values we got from the operations
    result[0:half, 0:half] = c11
    result[0:half, half:] = c12
    result[half:, 0:half] = c21
    result[half:, half:] = c22
    
    return result


def divide_half(m):
    """
    Divide a matrix in 4 to make the algorithm feasable
    """
    half = len(m)//2
    subM11 = np.array( [[elem for elem in row[0:half]] for row in m[0:half]] )
    subM12 = np.array( [[elem for elem in row[half:]] for row in m[0:half]] )
    subM21 = np.array( [[elem for elem in row[0:half]] for row in m[half:]] )
    subM22 = np.array( [[elem for elem in row[half:]] for row in m[half:]] )

    return subM11, subM12, subM21, subM22


if __name__ == "__main__":
    """"
    Matrixes
    """
    pathMatrixA = input("Path of the matrix A: ")
    pathMatrixB = input("Path of the matrix B: ")
    matrixA = parce_csv(pathMatrixA)
    matrixB = parce_csv(pathMatrixB)
    
    # Strassen Algorithm
    print("Strassen Algorithm:")
    matrixC = multiply(matrixA, matrixB)
    print("Scalar multiplications: ",scalarMult)
    print(matrixC)
