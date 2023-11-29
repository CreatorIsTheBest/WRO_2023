# importacion de libreias
import random

# funcion numero random

def crear_un_numero_aleatorio():
    return random.randrange(0,100)

# funcion principal


def main():
    acertado = False
    Intentos =  0
    Numero_secreto = crear_un_numero_aleatorio()
    while acertado == False:
        Respuesta = int(input("¿Cual es el numero?: "))
        if Respuesta > Numero_secreto:
            print("Mas pequeño")
            Intentos = Intentos + 1
        elif Respuesta < Numero_secreto:
            print("Mas Grande")
            Intentos = Intentos + 1
        else:
            print("Correcto!!!!!")
            print("Has necesitado: ",Intentos," intentos")
            acertado = True
            if input("¿Quieres volver a jugar (y/n)?") == "y":
                print("Genial!")
                main()

if input("¿Quieres jugar? (y/n)") == "y":
    main()

# funcion final
