
def productoEscalar(producto):

        col = int(input("NUMERO DE FILAS:"))

        row = int(input("NUMERO DE COLUMNAS:"))

        matriz = [[0 for x in range(row)] for y in range(col)]
        print("PRIMER MATRIZ")

        for i in range(col):
            for j in range(row):
                matriz[i][j] = float(input("Valor["+str(i)+"]["+str(j)+"]:"))

        for i in range(col):
            for j in range(row):
                matriz[i][j]= matriz[i][j]*producto

        return matriz

producto = float(input("Ingrese el producto escalar: "))
Matriz = productoEscalar(producto)

for i in Matriz:
    print (i)