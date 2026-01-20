class Actividad: 
    def __init__(self,tipo,duracion,hora):
        self.tipo = tipo
        self.duracion = duracion
        self.hora = hora

class Correr (Actividad): 
    def __init__(self, tipo, duracion, hora,distancia):
        super().__init__(tipo, duracion, hora)
        self.distancia = distancia

    def pedir_datos(self): 
        self.duracion = int(input("Cuántos minutos has estado corriendo?: "))
        self.distancia = float(input("Cuantos Km has recorrido?: "))
        

class Ciclismo (Actividad): 
    def __init__(self, tipo, duracion, hora,distancia,altmax,altmin):
        super().__init__(tipo, duracion, hora)
        self.distancia = distancia 
        self.altmax=altmax
        self.altmin=altmin

    def calculardesnivel(self, altmax, altmin):
        res = altmax-altmin
        self.desnivel = res  

    def pedir_datos(self):
        self.desnivel = self.desnivel
        self.duracion = int(input("Cuántos minutos has estado pedaleando?: "))
        self.distancia = float(input("Cuantos Km has recorrido?: "))        

class Gimnasio (Actividad): 
    def __init__(self, tipo, duracion, hora,entreno):
        super().__init__(tipo, duracion, hora)
        self.entreno = entreno
    
