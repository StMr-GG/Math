import math

"""
    este es mi modulo de algebra para python

    contiene funciones basicas y otras que ire implementando mas adelante


"""

def my_sqrt(x):
  return x**0.5
#modulo matematico creado por Nahuel Alejandro Burgos usando la libreria math
raiz2 = math.sqrt #cambio la referencia del modulo matematico math (sqrt) que es de la raiz cuadrada a raiz2 para facilitar mi codigo
pi = math.pi
cos = math.cos
sin = math.sin
tan = math.tan


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
    if type(Mb)== int:
      matriz = Ma
      for i in range(len(Ma)):
        for j in range(len(Ma[0])):
          matriz[i][j]+= Mb
    elif type(Ma)== int:
      matriz = Mb
      for i in range(len(Mb)):
        for j in range(len(Mb[0])):
          matriz[i][j]+= Ma
    else:
      matriz = []
      for i in range(len(Ma)):
          matriz2 = []
          for j in range(len(Ma[0])):
              m = Ma[i][j] + Mb[i][j]
              matriz2.append(m)
          matriz.append(matriz2)
        
    return matriz
def ResMatriz(Ma,Mb):
    """este modulo ingresamos 2 matrices y las resta
        te retorna una matriz sumada
            Ma = Matriz 1
            Mb = Matriz 2"""
    if type(Mb)== int:
      matriz = Ma
      for i in range(len(Ma)):
        for j in range(len(Ma[0])):
          matriz[i][j] -= Mb
    elif type(Ma) == int:
      matriz = Mb
      for i in range(len(Mb)):
        for j in range(len(Mb[0])):
          matriz[i][j] -= Ma
    else:
      matriz = []
      for i in range(len(Ma)):
          matriz2 = []
          for j in range(len(Ma[0])):
              matriz2.append(Ma[i][j] - Mb[i][j])
          matriz.append(matriz2)
    return matriz

def MultiplicarMatriz(Ma,Mb):
    if type(Mb)== int:
      matriz = Ma
      for i in range(len(Ma)):
        for j in range(len(Ma[0])):
          matriz[i][j] *= Mb
    elif type(Ma) == int:
      matriz = Mb
      for i in range(len(Mb)):
        for j in range(len(Mb[0])):
          matriz[i][j] *= Ma
    else:
      if len(Ma[0]) != len(Mb):
        raise ValueError(f"las filas y las columnas de las matrices no coinciden por ende no se puede multiplicar \nel numero de columnas de matriz 1 es {len(Ma[0])}\nel numero de filas de matriz 2 es {len(Mb)}")
      matriz =[[]for _ in range(len(Ma))]
      for i in range(len(Ma)):
          for k in range(len(Ma)):
              m = 0
              n = 0
              for j in range(len(Mb)):
                  m = Ma[i][k] * Mb[k][j]
                  n = m + n
              matriz[i].append(n)
    return matriz

def MultiplicarMatriz_v2(Ma,Mb):
    if len(Ma[0]) != len(Mb):
        raise ValueError(f"las filas y las columnas de las matrices no coinciden por ende no se puede multiplicar \nel numero de columnas de matriz 1 es {len(Ma[0])}\nel numero de filas de matriz 2 es {len(Mb)}")
    matriz =[[0 for fil in range(len(Mb))] for col in range(len(Ma[0]))]
    for i in range(len(Ma)):
        for k in range(len(Mb[0])):
            for j in range(len(Mb)):
              matriz[i][j]+= Ma[i][k] * Mb[k][j]
    return matriz
def SubdividirMatriz(M):
  a= b= c= d= M

  while len(a) > len(M)/2:
    a= a[:len(a)//2]
    b= b[:len(b)//2]
    c= c[len(c)//2:]
    d= d[len(d)//2:]

  while len(a[0]) > len(M[0])//2:
    for i in range(len(a[0])//2):
      a[i]= a[i][:len(a[i])//2]
      b[i]= b[i][len(b[i])//2:]
      c[i]= c[i][:len(c[i])//2]
      d[i]= d[i][len(d[i])//2:]

  return a, b, c, d

def Strassen(Ma,Mb,n):
  """if n==1:
    matriz= [[0]]
    matriz[0][0]= Ma[0][0] * Mb[0][0]
    return matriz"""
  if n==64:
    return MultiplicarMatriz_v2(Ma,Mb)

  else:
    a,b,c,d= SubdividirMatriz(Ma)
    e,f,g,h= SubdividirMatriz(Mb)

    p1= Strassen(a, ResMatriz(f,h), n/2) #p1=a*(f-h)
    p2= Strassen(SumaMatriz(a,b), h, n/2) #p2=(a+b)*h
    p3= Strassen(SumaMatriz(c,d), e, n/2) #p3=(c+d)*e
    p4= Strassen(d, ResMatriz(g,e), n/2) #p4=d*(g-e)
    p5= Strassen(SumaMatriz(a,d), SumaMatriz(e,h), n/2) #p5=(a+d)*(e+h)
    p6= Strassen(ResMatriz(b,d), SumaMatriz(g,h), n/2) #p6=(b-d)*(g+h)
    p7= Strassen(ResMatriz(a,c), SumaMatriz(e,f), n/2) #p7=(a-c)*(e+f)
    
    Matriz11= SumaMatriz(ResMatriz(SumaMatriz(p5, p4), p2), p6)
    Matriz12= SumaMatriz(p1, p2)
    Matriz21= SumaMatriz(p3, p4)
    Matriz22= SumaMatriz(ResMatriz(ResMatriz(p5, p3), p7), p1)

    m=len(Matriz11)
    Matriz= [[0 for fil in range(m*2)] for col in range(m*2)]
    for i in range(m):
      for j in range(m):
        Matriz[i][j]= Matriz11[i][j]
        Matriz[i][j+m]= Matriz12[i][j]
        Matriz[i+m][j]= Matriz21[i][j]
        Matriz[i+m][j+m]= Matriz22[i][j]

    return Matriz