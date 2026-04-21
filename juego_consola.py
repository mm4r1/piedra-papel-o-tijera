from logica import opciones, elegir_computador, decidir_ganador

continuar_juego = True

print("bienvenido al juego!")

while continuar_juego:
    partidas = int(input("cuantas rondas te gustaría jugar?: "))
    puntaje1 = 0
    puntaje2 = 0
    while True:
        print("\nelige tu opción")
        print("piedra, papel o tijera")
        jugador = input("ingresa tu opción: ").lower().strip()

        while jugador not in opciones:
            print("error. opción inválida")
            jugador = input("ingresa tu opción: ").lower().strip()
    
        computador = elegir_computador()
        print("la computadora eligió: ", computador)

        resultado = decidir_ganador(jugador, computador)
        if resultado == "empate":
            print("Empate")
        elif resultado == "ganar":
            print("ganaste!")
            puntaje1 += 1
        else:
            print("Perdiste :(")
            puntaje2 += 1
    
        print(f"puntaje || jugador: {puntaje1} | computador: {puntaje2}")
    
        if puntaje1 == partidas:
            print("felicidades! has ganado la partida!! :D")
            break
        elif puntaje2 == partidas:
            print("el computador ha ganado la partida :(")
            break
        
    print("quieres seguir jugando?")
    print("1. si \n2. no")
    seguir = input("elige una opción: ").strip()
    while seguir not in ["1", "2"]:
        print("error. opción inválida")
        print("quieres seguir jugando?")
        print("1. si \n2. no")
        seguir = input("elige una opción: ").strip()
    if seguir == "2":
        print("nos vemos!")
        continuar_juego = False