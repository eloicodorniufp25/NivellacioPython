import random


# <editor-fold desc="FUNCIONES">
def escullNivell():
    opcioValida = False
    while not opcioValida:
        try:
            nivell = int(input('Introdueix nivell:\n Baix (1 vida) \n Mig (2 vides) \n Alt (3 vides)\n'))
            if 1 <= nivell <= 3:
                opcioValida = True
            else:
                print('Opció incorrecta. Tria 1, 2 o 3.')
        except ValueError:
            print('Error: has de introduir un número enter.')
    return nivell


def comparaResultat(opUser, opRival, puntUser, puntRival):
    # User Pedra
    if opUser == 0:
        if opRival == 0:
            print('El rival ha tret, pedra. Resultat: Empatat')
        elif opRival == 1:
            print('El rival ha tret, paper. Resultat: guanya PC')
            puntRival += 1
        else:
            print('El rival ha tret, Tisores. Resultat: guanya User')
            puntUser += 1

    # User Paper
    elif opUser == 1:
        if opRival == 0:
            print('El rival ha tret, pedra. Resultat: guanyaUser')
            puntUser += 1
        elif opRival == 1:
            print('El rival ha tret, paper. Resultat: empat')
        else:
            print('El rival ha tret, Tisores. Resultat: guanya PC')
            puntRival += 1

    # User Tisores
    else:
        if opRival == 0:
            print('El rival ha tret, pedra. Resultat: guanyaPC')
            puntRival += 1
        elif opRival == 1:
            print('El rival ha tret, paper. Resultat: guanyaUser')
            puntUser += 1
        else:
            print('El rival ha tret, Tisores. Resultat: Empat')

    print(f'El resultat es:\n User: {puntUser}\n Pc: {puntRival}')
    return puntUser, puntRival
# </editor-fold>

def juego():
    nivell = escullNivell()
    puntUser = 0
    puntRival = 0
    while puntUser < nivell and puntRival < nivell:
        try:
            opUser = int(input('Escull la teva elecció: \n0-Piedra \n1-Papel \n2-Tisores \n'))
            opRival = random.randint(0, 2)
            puntUser, puntRival = comparaResultat(opUser, opRival, puntUser, puntRival)
        except ValueError:
            print('Tiene que ser un numero')
    if puntUser == nivell:
        print('Joc acabat, Has guanyat!')
    else:
        print('Joc acabat, Has perdut!')


if __name__ == "__main__":
    print("----UTILIZA EL MENÚ----")