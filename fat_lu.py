import numpy as np

def substituicoes_sucessivas(A, b):
    n = len(A)
    x = n * [0]
    
    for i in range(0, n):
        s = 0
        
        for j in range(0, i):
            s = s + A[i][j] * x[j]
        
        x[i] = (b[i]-s)/A[i][i]

    return x

def identidade(n):
    m = []

    for i in range(0, n):
        linha = [0] * n
        linha[i] = 1
        m.append(linha)
    
    return m

def lu(A, B):
    n = len(A)

    L = identidade(n)

    for k in range(0, n-1):
    
        for i in range(k+1, n):
            m = - A[i][k]/A[k][k]
            L[i][k] = -m
            
            for j in range(k+1, n):
                A[i][j] = m * A[k][j] + A[i][j]
            
            A[i][k] = 0
    
    return L, A

def substituicoes_retroativas(A, b):
    n = len(A)
    x = n * [0] 
    
    for i in range(n-1, -1, -1):
        s = 0
        
        for j in range(i+1, n):
            s = s + A[i][j] * x[j]
        
        x[i] = (b[i] - s)/A[i][i]
    
    return x

def lux(L,U,B):
    y = substituicoes_sucessivas(L, B)
    x = substituicoes_retroativas(U, y)

    return x

def fat_lu(A, B):
    L, U = lu(A, B)
    x = lux(L, U, B)

    return x