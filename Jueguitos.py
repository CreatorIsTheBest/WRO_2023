# importacion de libreias

# funcion numero random

# funcion principal


def main():
    Numero_secreto = crear_un_numero_aleatorio()
    Respuesta = input("¿Cual es el nuemro?: ")
    acertado = False
    while acertado == False:
        if Respuesta >= Numero_secreto:
            print("Mas pequeño")
        if Respuesta <= Numero_secreto:
            print("Mas Grande")
        if Respuesta == Numero_secreto:
            print("Correcto!!!!!")
            acertado = True
            if input("¿Quieres volver a jugar (y/n)?") == "y":
                print("Genial!")
                main()

if input("¿Quieres jugar? (y/n)") == "y":
    main()

# funcion final