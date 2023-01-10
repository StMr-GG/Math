import nahured.Modulo_Algebra as alg
import time

A = [[1,3,8],[4,7,3]]
B = [[5,3],[6,8],[6,4]]

m=[[-427946, 517991, 402995, 293352, -497650], [567207, 691619, 533387, 392009, -666542], [695246,-844474, 653998, 479430, 808142], [1194134, -1453233, 1124382, 822421, 1390373], [-1088330, 1322643, -1024745, 748518, -1268907]]
a=[[1061, -1201, 907, 857, 1335], [1360, 1777, 1284, -977, 1698], [1716, -2024, 1690, 1022, -1838], [2911, 3561, -2845, 1833, 3168], [-2657, 3214, 2454, 1909, -3142]]

st1= time.time()
print(f"\nResult={alg.MultiplicarMatriz(m,a)}")
et1=(time.time()-st1)*10000
print(f"Tiempo de ejecucion: {et1}")

st2= time.time()
print(f"\nResult={alg.MultiplicarMatriz_v2(m,a)}")
et2=(time.time()-st2)*10000
print(f"Tiempo de ejecucion: {et2}")
print(f"Dif: {et1-et2}")

"""st3= time.time()
print(f"\nResult={alg.MultiplicarMatriz_zip(m,a)}")
et3=(time.time()-st3)*10000
print(f"Tiempo de ejecucion: {et3}")
print(f"Dif: {et1-et3}")"""
