from AHORCADO import ahorcado
from FLOTA import HUNDIR_FLOTA
from PEDRA_PAPER_TISORES import pedra_paper_tisores
from JOC_Siete_i_medio import JOC_Siete_i_medio

if __name__ == "__main__":
    op = -1
    while op < 1 or op > 4:
        print("+------SELECCIONA EL JUEGO QUE QUIERES JUGAR-------+")
        print("| 1. Ahorcado                                      |")
        print("| 2. Hundir la flota                               |")
        print("| 3. Pedra Paper Tisores                           |")
        print("| 4. 7,5                                           |")
        print("+--------------------------------------------------+")
        op = int(input("Selecciona un juego para iniciar: "))

    if op == 1:
        ahorcado.juego()
    elif op == 2:
        HUNDIR_FLOTA.jugar()
    elif op == 3:
        pedra_paper_tisores.juego()
    elif op == 4:
        JOC_Siete_i_medio.jugar()
