# importacion de libreias
import random

# funcion numero random


Intentos =  0

def crear_un_numero_aleatorio():
    return random.randrange(0,100)

# funcion principal


def main():
    acertado = False
    Numero_secreto = crear_un_numero_aleatorio()
    while acertado == False:
        Respuesta = int(input("¿Cual es el nuemro?: "))
        if Respuesta >= Numero_secreto:
            print("Mas pequeño")
            Intentos = Intentos + 1
        if Respuesta <= Numero_secreto:
            print("Mas Grande")
            Intentos = Intentos + 1
        if Respuesta == Numero_secreto:
            print("Correcto!!!!!")
            acertado = True
            if input("¿Quieres volver a jugar (y/n)?") == "y":
                print("Genial!")
                print("Has necesitado: ",Intentos," intentos")
                main()

if input("¿Quieres jugar? (y/n)") == "y":
    main()

# funcion final
