class Player:
    def __init__(self):
        self.nivel=1
        self.exp=0
        self.exp_sig_niv=50

    def completar_actividad(self):
        print("\nActividad completada. Has recibido +10 EXP")
        self.exp=self.exp+10
        self.subir_nivel()
        self.mostrar_barra()

    def subir_nivel(self):
        while self.exp>=self.exp_sig_niv:
            self.exp=self.exp - self.exp_sig_niv
            self.nivel=self.nivel + 1
            self.exp_sig_niv = int(self.exp_sig_niv * 1.2)
            print(f"¡Subiste al nivel {self.nivel}! Ahora necesitas {self.exp_sig_niv} EXP para el siguiente nivel.")
            

    def mostrar_barra(self):
        largo = 30
        llenado = int((self.exp / self.exp_sig_niv) * largo)
        barra = "█" * llenado + "-" * (largo - llenado)
        print(f"Nivel {self.nivel} | EXP: [{barra}] {self.exp}/{self.exp_sig_niv}")