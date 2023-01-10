"""
    este modulo obtendra todas las funciones que definene a la fisica como
        * Mecanica:
            Vectores y sus propiedades
                Movimiento Rectilineo Uniforme (MRU)
                    Velocidad instantanea
                    Velocidad media
        * Mecanica de luidos
        * Ondas
        * Termodinamicas
        * Electromagnetismo
        * optica
        * fisicaa Moderna
"""

def MRU(p="Print?",MRU = "3",v = "velocidad",x="posicion",X0 = "posicionInicial", Xf = "posicionFinal", t = "tiempo", t0 = "tiempoInicial", tf = "tiempoFinal"):
    """
    este es el modulo de Movimiento rectilineo uniforme:
    tenes que espesificar que queres 
        velocidad instantanea en MRU escribi: "instantanea" o "inst" o "i" o 1
            para la velocidad instantanea vas a necesitar
                v = velocidad
                x = posicion
                t = tiempo
                una tiene que ser la incognita (la incognita no lo pongas)

        velocidad media en MRU escribi: "media" o "med" o "m" 0 2
            para la velocidad media vas a necesitar
                v = velocidad
                X0 = posicion inicial
                Xf = posicion final
                t0 = tiempo inicial
                tf = tiempo final
                una tiene que ser la incognita (la incognita no lo pongas)
    """
    resultado = 0
    if MRU == "instantanea" or MRU == "inst" or MRU == "i" or MRU == 1:
        if x is int and t is int:
            resultado = x/t
        elif t == int and v == int:
            resultado = t*v
        elif x == int and v == int:
            resultado = x/v
        else:
            print("holi")
            #raise ValueError(f"fijate si x {x} {type(x)} t {t} {type(t)} y v {v} {type(v)} no sean str y que algunos de ellos tenga una incognita")
    elif MRU == "media" or MRU == "med" or MRU == "m" or MRU == 2:
        if Xf == int and X0 == int and t0 == int and tf == int:
            resultado = ((Xf-X0)/(tf-t0))
        elif tf == int and t0 == int and v == int and X0 == int:
            resultado = (tf - t0) * v + X0
        elif tf == int and t0 == int and v == int and Xf == int:
            resultado = (tf - t0) * v - Xf
        elif Xf == int and X0 == int and tf == int and v == int:
            resultado = ((Xf-X0)/(tf-v))
        elif Xf == int and X0 == int and t0 == int and v == int:
            resultado = ((Xf-X0)/(v + t0))
        else:
            raise ValueError(f"fijate bien si todos los valores son un entero y si dejaste una incognita")
    elif MRU == None:
        raise ValueError(f"che existe una variable MRU que llenar bien")
    if p == "print?":
        return resultado
    if p != "print?":
        print(f"este es el resultado de {MRU}: {resultado}")
        return resultado