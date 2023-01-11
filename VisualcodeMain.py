import nahured.Modulo_Algebra as alg
import time
import random


Prueba = [
  [11,12,13,14,15,16],
  [21,22,23,24,25,26],
  [31,32,33,34,35,36],
  [41,42,43,44,45,46],
  [51,52,53,54,55,56],
  [61,62,63,64,65,66]
  ]

alfa = 1,1

for i in range(len(Prueba)):
  for j in range(len(Prueba[0])):
    alfa = i,j
    lamada = alg.divisionDeterminanteMa(Prueba,alfa)
    print(f"{lamada[0]}\n{lamada[1]}\n{lamada[2]}\n{lamada[3]}\n")

#mendigo = alg.CalcDeterminanteMa(Prueba)