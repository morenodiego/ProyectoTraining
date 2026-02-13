from metrica import Metrica
class Jugador:
    def __init__(self, usuario, experiencia, nivel, avatar, mascota, peso, altura, edad):
        self.usuario = usuario
        self.exp = 0
        self.exp_max=100
        self.nivel = 1
        self.avatar=avatar
        self.mascota=mascota
        self.metrica = Metrica(peso, altura, edad)

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

    def __str__(self):
        return f"Usuario {self.usuario}, Nivel: {self.nivel}, EXP {self.exp}"
