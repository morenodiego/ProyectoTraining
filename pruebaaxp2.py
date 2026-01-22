class Jugador:
    def __init__(self):
        self.nivel = 1
        self.exp = 0
        self.exp_max = 100

    def ganar_exp(self, cantidad):
        self.exp += cantidad
        while self.exp >= self.exp_max:
            self.exp -= self.exp_max
            self.nivel += 1
            return f"¡Subiste al nivel {self.nivel}!"

    def barra_exp(self, longitud=175):
        porcentaje = self.exp / self.exp_max
        llenos = int(longitud * porcentaje)
        vacios = longitud - llenos
        barra = "█" * llenos + "░" * vacios
        return f"Nivel {self.nivel} | {barra} {porcentaje*100:.1f}%"


p = Jugador()
p.ganar_exp(150)
print(p.barra_exp())

