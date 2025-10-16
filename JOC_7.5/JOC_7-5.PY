from CARD import Card
import random


def crearBaraja():
    palos = ["oros", "copas", "bastos", "espadas"]
    valores = [1, 2, 3, 4, 5, 6, 7, "J", "Q", "K"]
    baraja = []
    for palo in palos:
        for valor in valores:
            baraja.append(Card(valor, palo))
    random.shuffle(baraja)
    return baraja


def robarCarta(baraja, cartas):
    cartas.append(baraja.pop())


def calcularPuntos(cartas):
    return sum(carta.puntos() for carta in cartas)


def comprovarGanador(cartas):
    return calcularPuntos(cartas) > 7.5


def jugar():
    #Crear baraja
    baraja = crearBaraja()

    #Cartas de la banca y jugador
    cartas_banca = []
    robarCarta(baraja, cartas_banca)
    print("--------COGIENDO CARTAS INCIALES---------------")
    print(f"La banca tiene: {cartas_banca[0]}")

    cartas_jugador = []
    robarCarta(baraja, cartas_jugador)
    print(f"El jugador tiene: {cartas_jugador[0]}")
    print("-----------------------------------------------")

    #Turno del jugador
    while True:
        print(f"Puntos jugador: {calcularPuntos(cartas_jugador)}")
        if comprovarGanador(cartas_jugador):
            print("Te has pasado de 7.5! Pierdes")
            return

        decision = ""
        while decision.lower() not in ["s", "n"]:
            decision = input("Quieres coger otra carta o plantarte? (s/n): ")

        if decision.lower() == "s":
            robarCarta(baraja, cartas_jugador)
            print("--------NUEVA CARTA COGIDA---------------")
            print(f"Has robado: {cartas_jugador[-1]}")
            print("-----------------------------------------")
        else:
            break

    #Turno de la banca
    while calcularPuntos(cartas_banca) < 5.5:
        robarCarta(baraja, cartas_banca)
        print(f"La banca roba: {cartas_banca[-1]}")

    # Mostrar resultados
    puntos_jugador = calcularPuntos(cartas_jugador)
    puntos_banca = calcularPuntos(cartas_banca)
    print(f"\nPuntos jugador: {puntos_jugador}")
    print(f"Puntos banca: {puntos_banca}")

    if puntos_banca > 7.5 or puntos_jugador > puntos_banca:
        print("¡Gana el jugador!")
    elif puntos_banca == puntos_jugador:
        print("Empate")
    else:
        print("Gana la banca")


if __name__ == "__main__":
    jugar()
