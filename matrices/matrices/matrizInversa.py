import numpy
def matrizInver():
    col = int(input("NUMERO DE FILAS:"))
    # se solicita al usuario el numero de filas de las matrices
    row = int(input("NUMERO DE COLUMNAS:"))
    # Se declara la primer matriz con el num de filas y columnas dados por el usuario
    matriz1 = [[0 for x in range(row)] for y in range(col)]
    print("PRIMER MATRIZ")
    # Se utiliza un ciclo para solicitar los valores de la primer matriz
    for i in range(col):
        for j in range(row):
            matriz1[i][j] = float(input("Valor[" + str(i) + "][" + str(j) + "]:"))
    print(numpy.linalg.inv(matriz1))

matrizInver()