#Juego TIC-TAC-TOE

import random 
import time
import os

def presentacion():
    print()
    print("         TIC-TAC-TOE")
    print()
    print()
    print("         Sale la ficha O")
    print()
    print("         Elige: O / X")
    print()
    print()

    ficha = ""
    while ficha != "O" and ficha != "X":
        ficha = input("             --> ").upper()

    if ficha == "O":
        humano = "O"
        computadora = "X"
    else:
        humano = "X"
        computadora = "O"
    
    return humano, computadora

def mostrar_tablero(tablero):
    #Muestra el tablero con las casillas vacias y cuando se colocan las fichas
    
    print()
    print("             TIC-TAC-TOE")
    print()
    print("       1         |2          |3")
    print("           {}     |      {}    |     {}".format(tablero[0], tablero[1], tablero[2]))
    print("                 |           |")
    print("       ----------+-----------+----------")
    print("       4         |5          |6")
    print("           {}     |       {}   |     {}".format(tablero[3], tablero[4], tablero[5]))
    print("                 |           |")
    print("       ----------+-----------+----------")
    print("       7         |8          |9")
    print("           {}     |       {}   |     {}".format(tablero[6], tablero[7], tablero[8]))
    print("                 |           |")
    print()

def seguir_jugando():

    #Devuelve True si el usuario quiere volver a jugar, sino devuelve False
    print()
    respuesta = input("         otra partida(s)? ").lower()
    if respuesta == "s" or respuesta == "si":
        return True
    else:
        return False

def ganador(tablero, jugador):
    #Comprueba el estado del tablero y si tiene un ganador: tiene tres fichas en raya
    if tablero[0] == tablero[1] == tablero[2] == jugador or \
       tablero[3] == tablero[4] == tablero[5] == jugador or \
       tablero[6] == tablero[7] == tablero[8] == jugador or \
       tablero[0] == tablero[3] == tablero[6] == jugador or \
       tablero[1] == tablero[4] == tablero[7] == jugador or \
       tablero[2] == tablero[5] == tablero[8] == jugador or \
       tablero[0] == tablero[4] == tablero[8] == jugador or \
       tablero[2] == tablero[4] == tablero[6] == jugador:
       return True
    else:
        return False
def tablero_lleno(tablero):
    #Devuelve true si el tablero esta lleno y false si todavia hay casillas vacias
    
    for i in tablero:
        if i == " ":
            return False
        else:
            return True
def casilla_libre(tablero, casilla):
    #Devuelve True si una casilla dada está vacía y False si está llena
    return tablero[casilla] == " "

def movimiento_jugador(tablero):
    #Devuelve la casilla eleiga por el jugador
    posiciones=["1","2","3","4","5","6","7","8","9"]
    posicion = None
    while True:
        if posicion not in posiciones:
            posicion = input("          Es tu turno(1-9): ")
        else:
            posicion = int(posicion)
            if not casilla_libre(tablero, posicion-1):
                print("         Esta pocision esta ocupada")
            else:
                return posicion-1
def movimiento_computadora(tablero,maquina, usuario):
    for i in range(9):
        copia = list(tablero)
        if casilla_libre(copia, i):
            copia[i] = maquina
            if ganador(copia, maquina):
                return i

    for i in range(9):
        copia = list(tablero)
        if casilla_libre(copia,i):
            copia[i] = usuario
            if ganador(copia,usuario):
                return i
    
    if computadora == "X":
        if tablero[4] == " ":
            return 4
        else:
            vacias = []
            for i in [0,2,6,8]:
                if tablero[i] == " ":
                    vacias.append(i)
            return random.choice(vacias)
    if computadora == "O":
        contador = 0
        for i in range(9):
            if tablero[i] == " ":
                contador += 1
        if contador == 7:
            if tablero[4] == " ":
                return 4

    while True:
        casilla = random.randint(0,8)
        if not casilla_libre(tablero, casilla):
            casilla = random.randint(0,8)
        else:
            return casilla
# -------------Programa principal-----------------------

jugando = True 
while jugando:

    tablero = [" "]*9

    os.system("cls")
    
    humano, computadora = presentacion()

    os.system("cls")
    
    mostrar_tablero(tablero)

    if humano == "O":
        turno = "Humano"
    else:
        turno = "Computadora"

    partida = True

    while partida:

        if tablero_lleno(tablero):
            print("                     Empate")
            partida = False
        
        elif turno == "Humano":
            casilla = movimiento_jugador(tablero)
            tablero[casilla] = humano
            turno = "Computadora"
            os.system("cls")
            mostrar_tablero(tablero)
            if ganador(tablero, humano):
                print("             Has ganado")
                partida = False
        elif turno == "Computadora":
            print("         La computadora esta pensando...")
            time.sleep(2)
            casilla = movimiento_computadora(tablero, computadora, humano)
        tablero[casilla] = computadora
        turno = "Humano"
        os.system("cls")
        mostrar_tablero(tablero)
        if ganador(tablero, computadora):
            print("             Has perdido")
            partida = False

    jugando = seguir_jugando()
