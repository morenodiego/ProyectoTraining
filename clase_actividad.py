class Actividad: 
    def __init__(self,tipo,duracion,hora):
        self.tipo = tipo
        self.duracion = duracion
        self.hora = hora

class Correr (Actividad): 
    def __init__(self, tipo, duracion, hora,distancia):
        super().__init__(tipo, duracion, hora)
        self.distancia = distancia


class Cilcismo (Actividad): 
    def __init__(self, tipo, duracion, hora,distancia,altmax,altmin):
        super().__init__(tipo, duracion, hora)
        self.distancia = distancia 
        self.altmax=altmax
        self.altmin=altmin
    def calculardesnivel(self, altmax, altmin):
        self.desnivel=altmax-altmin
        return self.desnivel

class Gimnasio (Actividad): 
    def __init__(self, tipo, duracion, hora,entreno):
        super().__init__(tipo, duracion, hora)
        self.entreno = entreno

    
