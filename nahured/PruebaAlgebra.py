def Pendiente_Recta(P1,P2):
  return((P2[1]-P1[1])/(P2[0]-P1[0]))

a=[-5,1]
b=[-6,3]

print(Pendiente_Recta(a,b))

def Poligono_Irregular(Lista_de_Puntos,Puntos):
  contador = 0
  

def AreaDePoligonoIrregular(Lista_de_Puntos):
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