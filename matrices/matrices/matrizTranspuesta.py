import numpy
def matrizTranspuesta():
# se solicita al usuario el numero de columnas de las matrices
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
    print("Matriz normal:")
    for i in matriz1:
        print(i)
    row = len(matriz1)
    col = len(matriz1[0])
    return [[matriz1[j][i] for j in range(row)] for i in range(col)]

mat=matrizTranspuesta()
print("Matriz transpuesta: ")
for i in mat:
    print(i)