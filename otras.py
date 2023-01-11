
def nueva_matriz(m,n):
  matriz =[[0 for fil in range(m)] for col in range(n)]
  return matriz
def MultiplicarMatriz_v2(Ma,Mb):
    if len(Ma[0]) != len(Mb):
        raise ValueError(f"las filas y las columnas de las matrices no coinciden por ende no se puede multiplicar \nel numero de columnas de matriz 1 es {len(Ma[0])}\nel numero de filas de matriz 2 es {len(Mb)}")
    matriz =nueva_matriz(len(Mb),len(Ma[0]))
    for i in range(len(Ma)):
        for k in range(len(Mb[0])):
            for j in range(len(Mb)):
              matriz[i][j]+= Ma[i][k] * Mb[k][j]
    return matriz
def MultiplicarMatriz_zip(Ma,Mb):
    if len(Ma[0]) != len(Mb):
        raise ValueError(f"las filas y las columnas de las matrices no coinciden por ende no se puede multiplicar \nel numero de columnas de matriz 1 es {len(Ma[0])}\nel numero de filas de matriz 2 es {len(Mb)}")
    matriz = [[sum(ma * mb for ma, mb in zip(i, j))
               for j in zip(*Mb)] for i in Ma]
    return matriz

columna = 6
fila = 6

matriz = [[0 for col in range(columna - 1)]for fil in range(fila - 1)]

print(matriz)