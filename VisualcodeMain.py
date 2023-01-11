import nahured.Modulo_Algebra as alg
import time
import random


Prueba1 = [
  [11,12,13,14,15,16],
  [21,22,23,24,25,26],
  [31,32,33,34,35,36],
  [41,42,43,44,45,46],
  [51,52,53,54,55,56],
  [61,62,63,64,65,66]
  ]

Prueba = [
  [2,1,-3,2],
  [-4,2,4,-1],
  [-2,1,1,4],
  [1,-2,-1,4]]

alfa = 1,0
"""def Calculo(A):
  for i in range(len(A)*2):
    if i < len(A):
      la = 0
      for j in range(len(A)):
        sa = 1
        for k in range(len(A)):
          sa = sa * A[(k+j) % len(A)][(k) % len(A[0])]
        la = la + sa
    else:
      la1 = 0
      for j in range(len(A)):
        sa1 = 1
        for k in range(len(A)):
          sa1 = sa1 * A[((k+j)*-1) % len(A)][(k) % len(A[0])]
        la1 = la1 + (sa1 * -1)
  return la + la1
"""

almada = alg.CalcDeterminanteMa(Prueba)

#almada = alg.divisionDeterminanteMa(Prueba,al)

#alg.ImpMatriz(almada)

popo = alg.MatrizDeterminante(almada)

alg.ImpMatriz(popo)

print()
kaka = alg.MatrizTranspuesta(popo)
alg.ImpMatriz(kaka)
mela = 1/12
kaka2 = alg.MultiplicarMatriz(kaka,mela)

print()

alg.ImpMatriz(kaka2)

"""for i in range(len(almada[0])):
  for j in range(len(almada[0][0])):
    alg.ImpMatriz(almada[i][j])
    print()
"""


#alg.ImpMatriz(almada)

#mendigo = alg.CalcDeterminanteMa(Prueba)