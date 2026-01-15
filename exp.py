class Player(Actividad):
    def __init__(self, usuario, nivel):
        self.usuario=usuario
        self.nivel=1

    def subir_nivel(self, nivel, tipo):
        super().__init__(tipo)
        self.nivel=nivel + 1
        return f"El jugador {self.usuario} ha subido al nivel {self.nivel} en la actividad {self.tipo}."