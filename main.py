import math as m
import numpy as np

from scipy.sparse.linalg import spsolve
from eliminacao import eliminacao_gaussiana
from fat_lu import fat_lu

if __name__ == '__main__':
    
    bookSolution = [-29.247105, 19.0, 10.0, -28.0, 13.853892, 19.0, 0.0, -28.0, 9.235928, 22.0, 0.0, -16.0, -9.235928, 22.0, 16.0, -24.629141, 16.0]
    
    graus = 45
    radianos = graus * (m.pi / 180)
    a = m.sin(radianos)
    
    A   =   [
            [-a,   0,  0,  1,  a,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
            [-a,   0, -1,  0, -a,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
            [ 0,  -1,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
            [ 0,   0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
            [ 0,   0,  0, -1,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
            [ 0,   0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
            [ 0,   0,  0,  0, -a, -1,  0,  0,  a,  1,  0,  0,  0,  0,  0,  0,  0 ],
            [ 0,   0,  0,  0,  a,  0,  1,  0,  a,  0,  0,  0,  0,  0,  0,  0,  0 ],
            [ 0,   0,  0,  0,  0,  0,  0, -1, -a,  0,  0,  1,  a,  0,  0,  0,  0 ],
            [ 0,   0,  0,  0,  0,  0,  0,  0, -a,  0, -1,  0, -a,  0,  0,  0,  0 ],
            [ 0,   0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  1,  0,  0,  0 ],
            [ 0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0 ],
            [ 0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  a,  0 ],
            [ 0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -a,  0 ],
            [ 0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -a, -1,  0,  0,  1 ],
            [ 0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  a,  0,  1,  0,  0 ],
            [ 0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -a, -1 ]
            ]
    
    B   =   [0, 0, 0, 10, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 10, 0]
    
    #implementação das bibliotecas
    numpySolution = np.linalg.solve(A, B)
    scipySolution = spsolve(A, B)
    
    #nossa implementação
    eliminacao = eliminacao_gaussiana(A, B)
    fatLu = fat_lu(A, B)
    
    #comparacao dos resultados
    print("Solucoes do livro:")
    for i in range(len(bookSolution)):
        print("{:.2f}".format(bookSolution[i]), end=' ')
    print()
    print()

    print("Solucoes do numpy:")    
    for i in range(len(numpySolution)):
        print("{:.2f}".format(numpySolution[i]), end=' ')
    print()
    print()

    print("Solucoes do scipy:")    
    for i in range(len(scipySolution)):
        print("{:.2f}".format(scipySolution[i]), end=' ')
    print()
    print()

    print("Solucoes da eliminacao de Gauss:")
    for i in range(len(eliminacao)):
        print("{:.2f}".format(eliminacao[i]), end=' ')
    print()
    print()
    
    print("Solucoes da fatoracao LU:")
    for i in range(len(fatLu)):
        print("{:.2f}".format(fatLu[i]), end=' ')
    print()
    print()