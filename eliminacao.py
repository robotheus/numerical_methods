import math as m
import numpy as np

def eliminacao_gaussiana(A, B):
    n = len(A)
    X = [0] * n

    for k in range(n - 1):
        A, B = pivoteamento_parcial(k, A, B)
        
        for i in range(k + 1, n):
            m = A[i][k] / A[k][k]
            A[i][k] = 0

            for j in range(k + 1, n):
                A[i][j] = A[i][j] - (m * A[k][j])
            
            B[i] = B[i] - (m * B[k])

    X[n - 1] = B[n - 1] / A[n - 1][n - 1]

    for k in range(n - 2, -1, -1):
        s = 0
        
        for j in range(k + 1, n):
            s = s + (A[k][j] * X[j])
        
        X[k] = (B[k] - s) / A[k][k]

    return X

def pivoteamento_parcial(k, A, B):
    n = len(A)
    pivot_max = m.fabs(A[k][k])
    linha_pivo = k

    for r in range(k + 1, n):
        if m.fabs(A[r][k]) > pivot_max:
            pivot_max = m.fabs(A[r][k])
            linha_pivo = r

    if linha_pivo != k:
        A[k], A[linha_pivo] = A[linha_pivo], A[k]
        B[k], B[linha_pivo] = B[linha_pivo], B[k]
    
    return A, B