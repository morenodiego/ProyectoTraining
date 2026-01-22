class Experiencia:
    def __init__(self):
        self.nivel = 1
        self.exp = 0
        self.exp_max = 100

    def ganar_exp(self, cantidad):
        self.exp += cantidad
        contador = 0
        while self.exp >= self.exp_max:
            self.exp -= self.exp_max
            self.nivel += 1
            contador += 1
        return contador


    def barra_exp(self):
        longitud = 175
        porcentaje = self.exp / self.exp_max
        if porcentaje > 1:
            porcentaje = 1
        llenos = int(longitud * porcentaje)
        vacios = longitud - llenos
        barra = "█" * llenos + "░" * vacios
        return f"Nivel {self.nivel} | {barra} {porcentaje*100:.1f}%"


e = Experiencia()
e.ganar_exp(150)
niveles_subidos = e.ganar_exp(300)
if niveles_subidos > 0:
    print(f"¡Has subido {niveles_subidos} niveles!")
print(e.barra_exp())