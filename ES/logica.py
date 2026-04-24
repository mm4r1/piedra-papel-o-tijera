import random

opciones = ["piedra", "papel", "tijera"]

def elegir_computador():
    return random.choice(opciones)

def decidir_ganador(jugador, computador):
    if jugador == computador:
        return "empate"
    elif jugador == "piedra" and computador == "tijera":
        return "ganar"
    elif jugador == "tijera" and computador == "papel":
        return "ganar"
    elif jugador == "papel" and computador == "piedra":
        return "ganar"
    else:
        return "perder"