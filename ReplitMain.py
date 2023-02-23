from nahured.Modulo_Algebra import *
import time
import random

n = 4
Aa = [[1,3,8],[4,7,3]]
Bb = [[5,3],[6,8]]
A=[[-427946, 517991, 402995, 293352, -497650], [567207, 691619, 533387, 392009, -666542], [695246,-844474, 653998, 479430, 808142], [1194134, -1453233, 1124382, 822421, 1390373], [-1088330, 1322643, -1024745, 748518, -1268907]]
B=[[1061, -1201, 907, 857, 1335], [1360, 1777, 1284, -977, 1698], [1716, -2024, 1690, 1022, -1838], [2911, 3561, -2845, 1833, 3168], [-2657, 3214, 2454, 1909, -3142]]
a=[[11,11,11,11],[22,22,22,22],[33,33,33,33],[44,44,44,44]]
b=[[101,181,119,113],[22,22,22,22],[33,33,33,33],[44,44,44,44]]
c=[[0,3,22,0],[84,9,6,34],[3,14,29,81],[62,23,3,67]]
d=[[0,3,22],[84,9,6],[3,14,29]]
e=[[0,3,22,0,2],[84,9,6,34,2],[3,14,29,81,2],[62,23,3,67,2],[9,45,3,79,2]]
  
if __name__ == "__main__":
  if not "Strassen":
    Ra=[[0 for x in range(n)] for y in range(n)] 
    Rb=[[0 for x in range(n)] for y in range(n)] 
    random.seed(a=123456, version=2)
    for i in range(n):
      for j in range(n):
        Ra[i][j]=random.randint(-10000, 10000)
        Rb[i][j]=random.randint(-10000, 10000)
    
    print(f"Test con matrices {n}x{n}")
    st1= time.time()
    res1= MultiplicarMatriz2(Ra,Rb)
    #print(f"\nResult={res1}")
    et1=round((time.time()-st1), 4)
    print(f"Tiempo algoritmo Naive: \t{et1}")
    st2= time.time()
    res2= Strassen(Ra,Rb)
    #print(f"\nResult={res2}")
    et2=round((time.time()-st2), 4)
    print(f"Tiempo algoritmo Stranssen: \t{et2}")
    print(f"Delta t={et1-et2}")

  if not "Triangular":
    Mat= NuevaMatriz(n,n)
    random.seed(a=123456, version=2)
    for i in range(n):
      for j in range(n):
        Mat[i][j]=random.randint(0, 100)
    """ImpMatriz(c)
    print("Sup-------------------")
    Tsup, Tinf=MatricesTriangulares(c)
    ImpMatriz(Tsup)
    print("Inf-------------------")
    ImpMatriz(Tinf)"""
    """Sup=MatrizTriaSup(c)
    print("\nSuperior")
    ImpMatriz(Sup)
    Inf=MatrizTriaInf(c)
    print("\nInferior")
    ImpMatriz(Inf)"""
  
  if not "Determinante":
    print(f"Test metodos para calculo de determinantes")
    st1= time.time()
    res1= DeterminanteMatriz(c)
    #print(f"\nResult={res1}")
    et1=round((time.time()-st1), 4)
    print(f"Tiempo metodo 1: \t{et1}")


  


  if not "Inversa":
    print(f"Test metodos para calculo de matriz inversa")
    st1= time.time()
    res1= MatrizInversa(c)
    #print(f"\nResult={res1}")
    et1=round((time.time()-st1), 4)
    print(f"Tiempo algoritmo 1: \t{et1}") 