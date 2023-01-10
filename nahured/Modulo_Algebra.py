import math

"""
    este es mi modulo de algebra para python

    contiene funciones basicas y otras que ire implementando mas adelante


"""


RadToGrad = lambda r: (180*r)/pi
#convierte los radianes (Rad) a grados (Grad) (lambda es una funcion de una sola linea)

GradToRad = lambda g: (pi*g)/180
#convierte los grados (Grad) a radianes (Rad)

def ParOImpar(a='null',p='null'):
    """esta funcion nos indica si el nuero que ingresamos es par o es impar
    
        esta funcion depende de 2 parametros a y p
            donde a es el numero para verificar si es par o inpar
            p viene de (print) y es por si quieres que el valor lo imprima en consola o no
                para que el valor se imprima en consola tienes que escribir cualquier cosa
                si no lo quieres no tienes que declarar el parametro ya que por defecto 
                tiene valor y utilizo ese valor para indicar que no va a ser imprimido en consola
    """
    if a != 'null':
        if a % 2 == 0:
            if p != 'null':
                print(a, "es par.")
                return 0
            else:
                return 0
        else:
            if p != 'null':
                print(a, "es impar.")
                return 1
            else:
                return 1
    elif a == 'null':
        a = int(input("Ingrese un número: "))
        if a % 2 == 0:
            if p != 'null':
                print(a, "es par.")
                return 0
            else:
                return 0
        else:
            if p != 'null':
                print(a, "es impar.")
                return 1
            else:
                return 1


def TeoremaDePitagoras(co='null', ca='null', h='null', alfa='null', beta ='null'):

    #alfa es el angulo arriba del angulo recto por el lado del cateto opuesto
    #beta es el angulo  por debajo del angulo recto por el lado del cateto adyacente

    if alfa == 'null' and beta != 'null':
        alfa = 90-beta

    if co == 'null' and h != 'null' and ca != 'null' and h>ca: #por si no declaramos co la funcion devlvera pitagoras de co
        return raiz2((h**2) - (ca**2)) #h tiene que ser mayor a ca para poder resolverlo

    if ca == 'null' and h != 'null' and co != 'null' and h>co: #por si no declaramos ca la funcion devlvera pitagoras de ca
        return raiz2((h**2) - (co**2)) #h tiene que ser mayor a co para poder resolverlo

    if h == 'null' and co != 'null' and ca != 'null': #por si no declaramos h la funcion devlvera pitagoras de h
        return raiz2((co**2) + (ca**2))
    
    if co == 'null' and alfa != 'null' and h != 'null':#por si tenemos el angulo alfa
        return h*(sin(GradToRad(alfa)))
    
    if h == 'null' and alfa != 'null' and ca != 'null':#por si tenemos el angulo alfa
        return ca/sin(GradToRad(alfa))
    
    if ca == 'null' and alfa != 'null' and h != 'null':#por si tenemos el angulo alfa
        return h*(cos(GradToRad(alfa)))
    
    return 'argumentos completos'

def AreaPerimetroDeCuadrilatero( #datos sacados de fuormulia
    area = 'null',
    perimetro = 'null',
    l = 'null',
    a = 'null',
    b = 'null',
    B = 'null',
    c = 'null',
    d = 'null',
    D = 'null',
    h = 'null',
    cuadrado = 'null',
    rectangulo = 'null',
    trapecio = 'null',
    paralelogramo = 'null',
    rombo = 'null'):

    if area != 'null':
        if cuadrado != 'null': #l son los lados del cuadrado
            return l**2
        
        if rectangulo != 'null': #h es la parte mas corta del rectangulo/ b es la parte mas larga del rectangulo
            return b*h
        
        if trapecio != 'null': #B es la parte mas larga "la base" del trapecio/ b es la parte mas pequea "el techo" del trapecio/ a y c son los costados "las paredes" del trapecio 
            return ((B + b)*h)/2
        
        if paralelogramo != 'null': #b la parte mas larga del paralelogramo/ h la distancia "altura" entre las partes mas largas del paralelogramos
            return b*h
        
        if rombo != 'null': #D altura del rombo/ d anchura del rombo
            return (D*d)/2
    
    if perimetro != 'null':
        if cuadrado != 'null': #l son los lados del cuadrado
            return 4*l
        
        if rectangulo != 'null': #b es la parte mas larga del rectangulo/ h es la parte mas corta del rectangulo
            return 2*b +2*h
        
        if trapecio != 'null': #B es la parte mas larga "la base" del trapecio/ b es la parte mas pequea "el techo" del trapecio/ a y c son los costados "las paredes" del trapecio 
            return a+b+c+b
        
        if  paralelogramo != 'null': #b la parte mas corta del paralelogramo/ a parte mas corta del paralelogramo (o inclinada)
            return 2*b+2*a
        
        if rombo != 'null': #l son los lados del rombo
            return 4*l

def AreaPerimetroDeTriangulo(b='null',h='null',l='null',a='null',c= 'null',area='null',perimetro='null'):
    if area != 'null':
        return ((b*h)/2)
    
    if perimetro != 'null':
        if a != 'null' and b != 'null':
            return (2*a+b)
        if l != 'null':
            return 3*l
        if a != 'null' and b != 'null' and c != 'null':
            return (a+b+c)

def AreaPerimetroDeCirculo(area='null',perimetro='null',r='null'):
    if area != 'null':
        return (pi*(r**2))
    if perimetro != 'null':
        return ((2*pi)*r)

def DistanciaEntreDosPuntos(A,B):
    x1, y1 = A
    x2, y2 = B
    return(raiz2(((x2 - x1)**2)+((y2-y1)**2)))

def SumatoriaTotal(x, xfin):
    y = 0
    for i in range (xfin):
        i += 1
        x += x
        y = x
    return y

def AreaDePoligonoIrregular(puntos):
    x= []
    y= []
    x1 = []
    y1 = []
    for i in puntos:
        for l in range(len(i)):
            s = i[l]
            h = ParOImpar(l)
            if h == 0:
                x.append(s)
            elif h == 1:
                y.append(s)
    x.append(x[0])
    #print('x: ',x)
    y.append(y[0])
    #print('y: ',y)
    for i in range(len(x)-1):
        x1.append(x[i]*y[i+1])
    for i in range(len(y)-1):
        y1.append(y[i]*x[i+1])
    return ((sum(x1)-sum(y1))/2)

def area_of_polygon(points):
    area = 0.0
    n = len(points)
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[i][1] * points[j][0]
    return abs(area) / 2.0

def SumaMatriz(Ma,Mb):
    """este modulo ingresamos 2 matrices y las suma
        te retorna una matriz sumada
            Ma = Matriz 1
            Mb = Matriz 2"""
    matriz = []
    for i in range(len(Ma)):
        matriz2 = []
        for j in range(len(Ma[i])):
            m = Ma[i][j] + Mb[i][j]
            matriz2.append(m)
        matriz.append(matriz2)
    return matriz

def MultiplicarMatriz(Ma,Mb):
    if len(Ma[0]) != len(Mb):
        raise ValueError(f"las filas y las columnas de las matrices no coinciden por ende no se puede multiplicar \nel numero de columnas de matriz 1 es {len(Ma[0])}\nel numero de filas de matriz 2 es {len(Mb)}")
    matriz = [[]for _ in range(len(Ma))]
    for i in range(len(Ma)):
        for j in range(len(Ma)):
            m = 0
            n = 0
            for h in range(len(Mb)):
                m = Ma[i][h] * Mb[h][j]
                n = m + n
            matriz[i].append(n)
    return matriz

