import os
print("SUMA DE MATRICES")
def restaMatriz():
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

        # Se declara la segunda matriz con el num de filas y columnas dados por el usuario
        matriz2 = [[0 for x in range(row)] for y in range(col)]
        print("SEGUNDA MATRIZ")
        # Se utiliza un ciclo para solicitar los valores de la segunda matriz
        for i in range(col):
            for j in range(row):
                matriz2[i][j] = float(input("Valor[" + str(i) + "][" + str(j) + "]:"))
        # Se declara una tercer matriz para almacenar el resultado de la resta
        matriz3 = [[0 for x in range(row)] for y in range(col)]

        # Se utiliza un ciclo para realizar la sresta
        for i in range(col):
            for j in range(row):
                matriz3[i][j] = matriz1[i][j] - matriz2[i][j]
        return matriz3
def sumaMatriz():
    # se solicita al usuario el numero de columnas de las matrices
        col = int(input("NUMERO DE FILAS:"))
    # se solicita al usuario el numero de filas de las matrices
        row = int(input("NUMERO DE COLUMNA:"))
    # Se declara la primer matriz con el num de filas y columnas dados por el usuario
        matriz1 =[[0 for x in range(row)] for y in range(col)]
        print("PRIMER MATRIZ")
    #Se utiliza un ciclo para solicitar los valores de la primer matriz
        for i in range(col):
            for j in range(row):
                matriz1[i][j] = float(input("Valor[" + str(i) + "][" + str(j) + "]:"))

    # Se declara la segunda matriz con el num de filas y columnas dados por el usuario
        matriz2 =[[ 0 for x in range(row)] for y in range(col)]
        print("SEGUNDA MATRIZ")
    #Se utiliza un ciclo para solicitar los valores de la segunda matriz
        for i in range(col):
            for j in range(row):
                matriz2[i][j] = float(input("Valor[" + str(i) + "][" + str(j) + "]:"))
    # Se declara una tercer matriz para almacenar el resultado de la suma
        matriz3 =[[0 for x in range(row)] for y in range(col)]

    #Se utiliza un ciclo para realizar la suma
        for i in range(col):
            for j in range(row):
                matriz3[i][j] = matriz1[i][j]+ matriz2[i][j]
        return matriz3

def menu():
        """
        Función que limpia la pantalla y muestra nuevamente el menu
        """
        os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
        print("Selecciona una opción")
        print("\t1 - Suma de matrices")
        print("\t2 - Resta de matrices")
        print("\t3 - salir")

while True:
        menu()
        # solicituamos una opción al usuario
        opcionMenu = input("inserta un numero valor >> ")

        if opcionMenu == "1":
            Matriz = sumaMatriz()
            print("RESULTADO")
            for i in Matriz:
                print(i)
        elif opcionMenu == "2":
            Matriz = restaMatriz()
            print("RESULTADO")
            for i in Matriz:
                print(i)
        elif opcionMenu =="3":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
