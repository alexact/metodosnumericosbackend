import numpy

def gaussJordan(m):
    #creamos una matriz, un vector lleno de ceros, y el vector solucion con la misma cantidad de zeros
    matrix = numpy.zeros((m,m))
    vector = numpy.zeros((m))
    x = numpy.zeros((m))
    #se llena la matriz y el vector
    for r in range(0, m):
        for c in range(0, m):
            matrix[(r), (c)] =float(input("Elemento a[" + str(r)+"," +str(c)+"] "))
        vector[(r)]=float(input('b[]'+str(r+1)+']: '))
    #asi funciona el metodo
    for k in range(0, m):
        for r in range(k+1, m):
            factor=(matrix[r,k]/matrix[k,k])
            print(factor)
            vector[r]=vector[r]-(factor*vector[k])
            for c in range(0,m):
                matrix[r,c]=matrix[r,c]-(factor*matrix[k,c])

    x[m-1]=vector[m-1]/matrix[m-1, m-1]

    for r in range(m-2, -1, -1):
        suma = 0
        for c in range(0,m):
            suma=suma+matrix[r,c]*x[c]
        x[r]=(vector[r]-suma)/matrix[r, r]
    return x

m = int(input('Valor de m:'))
print(gaussJordan(m))