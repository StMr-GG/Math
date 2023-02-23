
import nahured.Modulo_Algebra as na

ordenes = {
    "suma": "100001011111",
    "resta": "010001011111",
    "multiplicacion": "110001011111",
    "inicio de lectura de la matriz": "001001011111",
    "fin de lectura de la matriz": "101001011111",
    "matrizA": "011001011111",
    "matrizB": "111001011111",
    "inicio de lectura del oredn de la matriz": "000101011111",
    "fin de lectura del orden de la matriz": "100101011111",
    "comienzo de columna": "010101011111",
    "fin de columna": "110101011111",
    "comienzo de fila": "001101011111",
    "fin de fila": "101101011111"

}

def binaDec(strA):
    bina = len(strA)
    a = 0
    for i in range(bina):
        a += int(strA[i])* 2**i
    return a

def decaBin(strA,bits):
    a = ""
    for i in range(bits):
        if strA % 2 != 0:
            a = a + "1"
        else:
            a = a + "0"
        strA = strA/2
        strA = int(strA)
    return a

def codecMatriz(mat,bit):
    a = ""
    a = a + decaBin(len(mat),bit)
    a = a + decaBin(len(mat[0]),bit)
    for i in mat:
        for f in i:
            a = a + decaBin(f,bit)
    return a

def decMatriz(cod,bits):
    cont = 2
    n = binaDec(cod[0:12])
    m = binaDec(cod[12:24])
    matriz = na.NuevaMatriz(n,m)
    for i in range(n):
        for f in range(m):
            matriz[i][f] =  binaDec(cod[cont*bits:cont*bits+bits])
            cont = cont +1
    return matriz

def DefMatriz(fun = 'es',matriz = [[]]):
    if fun == 'es':
        f = int(input("filas = "))
        c = int(input("columnas = "))
        matr = na.NuevaMatriz(f,c)
        matr2 = na.NuevaMatriz(f,c)
        fMax = len(matr)
        cMax = len(matr[0])
        #na.ImpMatriz(matr)
    if fun == 'ed':
        matr = matriz
        matr2 = matr
        fMax = len(matr)
        cMax = len(matr[0])

    acceso = True
    f = 0
    c = 0
    while acceso:
        fc1 = matr[f][c]
        f1 = f
        c1 = c
        matr2[f][c] = f'<{matr[f][c]}>'
        
        
        print(f'f {f} c {c} fc1 {fc1}\n')
        na.ImpMatriz(matr2)
        print('\n\n')

        lan = input(':')
        if lan == 'w':
            if f == -1:
                f = fMax-1
            else:
                f = f - 1
        if lan == 's':
            if f >= fMax-1:
                f = 0
            else:
                f = f + 1
        if lan == 'a':
            if c <= 0:
                c = cMax-1
            else:
                c = c - 1
        if lan == 'd':
            if c >= cMax-1:
                c = 0
            else:
                c = c + 1
        if lan == 'q':
            acceso = False
        if lan != 'w' and lan != 's' and lan != 'a' and lan != 'd' and lan != 'q':
            print('esto es lan ',lan)
            #matr[f][c] = int(input('valor'))
            matr[f][c] = int(lan)
            fc1 = matr[f][c]
            print(f'probar {matr[f][c]}')
        matr2[f1][c1] = fc1
        print('\n\n')
    return matr


def inicializacion():
    operacion = 'suma'
    A = []
    B = [[0]]

    print(len(A),len(B))
    terminar = True
    while terminar:
        camino = input('¿quieres Crear o Editar una matriz? C/E:  ')
        if camino == 'C' or camino == 'c':
            camino = input('¿que matriz quieres crear? A/B:  ')
            if camino == 'A' or camino == 'a':
                if len(A) > 1:
                    camino = input('¿seguro que queres sobre escribir la matriz A? S/N:  ')
                    if camino == 'S' or camino == 's':
                        print('vamos a sobre escribir la matriz A')
                        A = DefMatriz('es')
                    else:
                        continue
                else:
                    print('vamos a crear la matriz A')
                    A = DefMatriz('es')
            elif camino == 'B' or camino == 'b':
                if len(B) > 1:
                    camino = input('¿seguro que queres sobre escribir la matriz B? S/N:  ')
                    if camino == 'S' or camino == 's':
                        print('vamos a sobre escribir la matriz A')
                        B = DefMatriz('es')
                    else:
                        continue
                else:
                    print('vamos a crear la matriz B')
                    B = DefMatriz('es')
            else:
              print('Error, parametro incorrecto.')
              continue
        else:
            if len(A) == 0:
                print('no hay nada que editar en la matriz A')
            if len(B) ==0:
                print('no hay nada que editar en la matriz B')
            else:
                camino = input('¿que matriz quieres editar? A/B:   ')
                if camino == 'A':
                    A = DefMatriz('ed',A)
                else:
                    B = DefMatriz('ed',B)
        if len(A) > 1 and len(B) > 1:
            camino = input('ya creaste tus matrices ahora ¿quieres Continuar o necesitas Editarlos? C/E:   ')
            if camino == 'C' or camino == 'c':
                terminar = False
            else:
                continue
    
    camino = input('¿que operacion quieres hacer? Sumar Restar Multiplicar S/R/M:  ')
    if camino == 'S' or camino == 's':
        if len(A) == len(B) and len(A[0]) == len(B[0]):
            operacion = 'sumar'
        else:
            print('lo lamento pero no podemos sumar si son distintos')
    if camino == 'R' or camino == 'r':
        if len(A) == len(B) and len(A[0]) == len(B[0]):
            operacion = 'restar'
        else:
            print('lo lamento pero no podemos sumar si son distintos')
    else:
        if len(A[0]) == len(B):
            operacion = 'multiplicar'
        else:
            print('lo lamento pero no podemos sumar si son distintos')
    return A,B

MA,MB = inicializacion()

na.ImpMatriz(MA)
print()
na.ImpMatriz(MB)