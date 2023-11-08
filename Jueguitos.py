# importacion de libreias
import random
# funcion numero random
def crear_un_numero_aleatorio():
    numero_elegido = random(0,100)
    return numero_elegido
# funcion principal

# funcion final



import random
def crear_un_numero_aleatorio():
    numero_elegido = random(0,100)
    intentos = 0
    Sabes_el_numero = False
def comprobvar_si_el_numero_es_correcto_Y_contando_los_aciertos():

    while Sabes_el_numero == False:
        numero_que_dices = int(input("Introduce un numero:"))
        intentos = intentos + 1
        if numero_que_dices >= numero_elegido:
            print("Es un numero mas pequeño, vuelve aprobar.")
        if numero_que_dices <= numero_elegido:
            print("Es un numero mas grande, vuelve aprobar.")
        if numero_que_dices == numero_elegido :
            Sabes_el_numero = True
def preguntar_si_quiere_volver_a_jugar():
     if Sabes_el_numero == False:
        saber_si_quiere_volver_a_jugar = int(input("Quieres volver ajugar:"))
        if 
    