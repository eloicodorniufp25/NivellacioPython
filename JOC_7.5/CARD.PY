class Card:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def puntos(self):
        # Si es un número (1–7), devuelve su valor
        if isinstance(self.valor, int):
            return self.valor
        # Si es figura (J, Q, K), vale 0.5
        return 0.5

    def __str__(self):
        return f"{self.valor} de {self.palo}"
