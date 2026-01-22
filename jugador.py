class Jugador:
    def __init__(self, usuario, avatar, mascota):
        self.usuario = usuario
        self.exp = 0
        self.nivel = 1
        self.avatar=avatar
        self.mascota=mascota

    def subir_exp(self, exp):
        self.exp = self.exp+exp
        if self.exp >= 100:
            self.nivel = self.nivel + 1
            self.exp = self.exp - 100
    
    def __str__(self):
        return f"Usuario{self.usuario}, Nivel: {self.nivel}, EXP {self.exp}"
    