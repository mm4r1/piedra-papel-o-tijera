import random

opciones = ["piedra", "papel", "tijera"]
puntaje1 = 0
puntaje2 = 0
continuar_juego = True

print("bienvenido al juego!")
while continuar_juego:
    print("\nelige tu opción")
    print("piedra, papel o tijera")
    jugador = input("ingresa tu opción: ").lower().strip()

    while jugador not in opciones:
        print("error. opción inválida")
        jugador = input("ingresa tu opción: ").lower().strip()
    
    computador = random.choice(opciones)
    print("la computadora eligió: ", computador)

    if jugador == computador:
        print("Empate")
    elif jugador == "piedra" and computador == "tijera":
        print("Ganaste!")
        puntaje1 += 1
    elif jugador == "tijera" and computador == "papel":
        print("Ganaste!")
        puntaje1 += 1
    elif jugador == "papel" and computador == "piedra":
        print("Ganaste!")
        puntaje1 += 1
    else:
        print("Perdiste :(")
        puntaje2 += 1
    
    print(f"puntaje || jugador: {puntaje1} | computador: {puntaje2}")
    
    if puntaje1 == 3:
        print("felicidades! has ganado la partida!! :D")
        break
    elif puntaje2 == 3:
        print("el computador ha ganado la partida :(")
        break
        
    print("quieres seguir jugando?")
    print("1. si \n 2. no")
    seguir = input("elige una opción: ").strip()
    while seguir not in ["1", "2"]:
        print("error. opción inválida")
        print("quieres seguir jugando?")
        print("1. si \n 2. no")
        seguir = input("elige una opción: ").strip()
    if seguir == 2:
        continuar_juego = False