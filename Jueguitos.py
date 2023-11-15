# importacion de libreias
import random

# funcion numero random

acertado = False
Intentos =  0

def crear_un_numero_aleatorio():
    numero_elegido = random(0,100)
    return numero_elegido

# funcion principal

def main():
    Numero_secreto = crear_un_numero_aleatorio()
    while acertado == False:
        Respuesta = input("¿Cual es el nuemro?: ")
        if Respuesta >= Numero_secreto:
            print("Mas pequeño")
            Intentos = Intentos + 1
        elif Respuesta <= Numero_secreto:
            print("Mas Grande")
            Intentos = Intentos + 1
        else:
            print("Correcto!!!!!")
            acertado = True
            if input("¿Quieres volver a jugar (y/n)?") == "y":
                print("Genial!")
                print("Has necesitado: ",Intentos," intentos")
                main()

if input("¿Quieres jugar? (y/n)") == "y":
    main()

# funcion final
