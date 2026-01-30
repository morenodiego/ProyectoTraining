class Actividad: 
    def __init__(self,duracion,hora):
        self.duracion = duracion
        self.hora = hora

class Correr (Actividad): 
    def __init__(self, duracion, hora,distancia):
        super().__init__(duracion, hora)
        self.distancia = distancia
         

    def registar(self): 
        self.duracion = int(input("Cuántos minutos has estado corriendo?: "))
        self.distancia = float(input("Cuantos Km has recorrido?: "))
        

class Ciclismo (Actividad): 
    def __init__(self, duracion, hora,distancia,altmax,altmin):
        super().__init__(duracion, hora)
        self.distancia = distancia 
        self.altmax=altmax
        self.altmin=altmin
        self.desnivel = altmax - altmin


    def registar(self):
        self.desnivel = self.desnivel
        self.duracion = int(input("Cuántos minutos has estado pedaleando?: "))
        self.distancia = float(input("Cuantos Km has recorrido?: "))



class Gimnasio (Actividad): 
    def __init__(self, duracion, hora,entreno):
        super().__init__(duracion, hora)
        self.entreno = {}
    
    def entrenamineto(self):
        menu = int(input("1. Añadir un nuevo ejercicio\n"  "2. Salir \n : "))
        while menu == 1: 
            ejercicio = input("Cual es el ejercicio que has hecho")
            series = input("Cuantas series ")
        

