def mostraTauler(tauler):
    print()
    for fila in tauler:
        print(' | '.join(fila))
        print('_' * 14)
    print()


def preguntaUser(torn):
    print(f"Torn del jugador {torn}")
    fila = input("Escriu la fila (a, b o c): ").lower()
    columna = input("Escriu la columna (1, 2 o 3): ")
    return fila, columna


def traduirFila(fila):
    if fila == 'a':
        return 1
    elif fila == 'b':
        return 2
    elif fila == 'c':
        return 3
    else:
        return None


def comprovaGuanyador(tauler, simbol):
    for i in range(1, 4):
        if tauler[i][1] == tauler[i][2] == tauler[i][3] == simbol:
            return True
    # Comprovar columnes
    for j in range(1, 4):
        if tauler[1][j] == tauler[2][j] == tauler[3][j] == simbol:
            return True
    # Comprovar diagonals
    if tauler[1][1] == tauler[2][2] == tauler[3][3] == simbol:
        return True
    if tauler[1][3] == tauler[2][2] == tauler[3][1] == simbol:
        return True
    return False


def jugar():
    tauler = [
        [' ', '1', '2', '3'],
        ['a', ' ', ' ', ' '],
        ['b', ' ', ' ', ' '],
        ['c', ' ', ' ', ' ']
    ]

    mostraTauler(tauler)

    torn = 'X'
    jugades = 0

    while jugades < 9:
        fila, columna = preguntaUser(torn)
        filaIndex = traduirFila(fila)

        if filaIndex is None or columna not in ['1', '2', '3']:
            print("\tPosició invàlida. Torna-ho a provar.")
            continue

        columnaIndex = int(columna)

        if tauler[filaIndex][columnaIndex] != ' ':
            print("\tAquesta casella ja està ocupada!")
            continue

        tauler[filaIndex][columnaIndex] = torn
        mostraTauler(tauler)

        if comprovaGuanyador(tauler, torn):
            print(f"-----El jugador {torn} ha guanyat!-----")
            return

        # Canviar torn
        torn = 'O' if torn == 'X' else 'X'
        jugades += 1

    print("-----Empat!-----")


if __name__ == "__main__":
    print("----UTILIZA EL MENÚ----")
