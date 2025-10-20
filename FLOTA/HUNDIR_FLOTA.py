import random as rnd

# VARIABLES GLOBALES
longitud_tablero = 6
tablero_jugador = [[0] * longitud_tablero for _ in range(longitud_tablero)]
tablero_ordenador = [[0] * longitud_tablero for _ in range(longitud_tablero)]


# <editor-fold desc="FUNCIONES">
def iniciar_tablero():
    for i in range(longitud_tablero):
        for j in range(longitud_tablero):
            tablero_jugador[i][j] = 0
            tablero_ordenador[i][j] = 0


def colocar_barcos_aleatoriamente(tablero, barcos):
    for longitud in barcos:
        colocado = False
        while not colocado:
            orientacion = rnd.choice(['H', 'V'])  # HORIZONTAL O VERTICAL
            if orientacion == 'H':
                fila = rnd.randint(0, longitud_tablero - 1)
                col = rnd.randint(0, longitud_tablero - longitud)

                # COMPROBAR ESPACIO LIBRE
                espacio_libre = True
                for i in range(longitud):
                    if tablero[fila][col + i] != 0:
                        espacio_libre = False
                        break

                if espacio_libre:
                    for i in range(longitud):
                        tablero[fila][col + i] = 1
                    colocado = True

            else:
                fila = rnd.randint(0, longitud_tablero - longitud)
                col = rnd.randint(0, longitud_tablero - 1)

                espacio_libre = True
                for i in range(longitud):
                    if tablero[fila + i][col] != 0:
                        espacio_libre = False
                        break

                if espacio_libre:
                    for i in range(longitud):
                        tablero[fila + i][col] = 1
                    colocado = True


def print_tableros(jugador, ordenador):
    print("---TU TABLERO--- \t ---TABLERO OPONENTE---")
    for i in range(longitud_tablero):
        print()
        # TABLERO DEL JUGADOR (MOSTRAR BARCOS)
        for j in range(longitud_tablero):
            if jugador[i][j] == 0:
                print("O", end="  ")
            elif jugador[i][j] == 1:
                print("X", end="  ")  # BARCOS VISIBLES
            elif jugador[i][j] == 2:
                print("·", end="  ")
            elif jugador[i][j] == 3:
                print("-", end="  ")

        print("   ", end="")  # SEPARACION DE LOS TABLEROS

        # TABLERO DEL ORDENADOR (MOSTRAR BARCOS)
        for j in range(longitud_tablero):
            if ordenador[i][j] == 0 or ordenador[i][j] == 1:
                print("O", end="  ")  # NO MOSTRAR LOS BARCOS
            elif ordenador[i][j] == 2:
                print("·", end="  ")
            elif ordenador[i][j] == 3:
                print("-", end="  ")
    print()


def disparo(tablero, fila, col):
    if tablero[fila][col] == 1:  # HAY BARCO
        tablero[fila][col] = 2
        print("----TOCADO!----")
        return True
    elif tablero[fila][col] == 0:  # AGUA
        tablero[fila][col] = 3
        print("----AGUA!----")
        return False
    else:
        print("Ya habías disparado aquí.")
        return False


def quedan_barcos(tablero):
    for fila in tablero:
        for celda in fila:
            if celda == 1:
                return True
    return False


# </editor-fold>


def jugar():
    print(r"""
                    __     __                   ___       __  ___      
    |__| |  | |\ | |  \ | |__)    |     /\     |__  |    /  \  |   /\  
    |  | \__/ | \| |__/ | |  \    |___ /~~\    |    |___ \__/  |  /~~\ 
        """)

    iniciar_tablero()
    barcos = [3, 2, 2, 1]  # FLOTA
    colocar_barcos_aleatoriamente(tablero_jugador, barcos)
    colocar_barcos_aleatoriamente(tablero_ordenador, barcos)

    # IMPRIMIR EL TABLERO INICIALMENTE (DESPUÉS DE COLOCAR BARCOS)
    print("\n----------- TABLEROS INICIALES -----------")
    print_tableros(tablero_jugador, tablero_ordenador)

    turno_jugador = True

    while quedan_barcos(tablero_jugador) and quedan_barcos(tablero_ordenador):

        # EL TABLERO SE IMPRIMIRÁ AL FINAL DEL TURNO ANTERIOR
        if turno_jugador:
            print("\n----Tu turno de disparo----")

            fila = int(input("Fila (0-5): "))
            col = int(input("Columna (0-5): "))

            if 0 <= fila < longitud_tablero and 0 <= col < longitud_tablero:
                disparo(tablero_ordenador, fila, col)
                turno_jugador = False
            else:
                print("Coordenadas fuera del tablero.")
                continue  # VOLVER A PEDIR COORDENADAS SIN CANVIAR DE TURNO
        else:
            print("\n---Turno del ordenador---")
            fila, col = rnd.randint(0, 5), rnd.randint(0, 5)
            print(f"El ordenador dispara a ({fila}, {col})")
            disparo(tablero_jugador, fila, col)
            turno_jugador = True

        # IMPRIMIR EL TABLERO DESPUÉS DE CADA DISPARO
        print("\n----------- TABLEROS ACTUALIZADOS -----------")
        print_tableros(tablero_jugador, tablero_ordenador)

    # Imprime el resultado final del juego
    if quedan_barcos(tablero_jugador):
        print("\n-----Has perdido, el ordenador hundió tu flota-----")
    else:
        print("\n----Victoria! Hundiste toda la flota enemiga-----")


if __name__ == "__main__":
    jugar()
