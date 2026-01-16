from clase_actividad import *
class Historico: 
    def __init__ (self,nombre): 
        self.nombre = nombre 
        self.actividad = []

    def registrar_actividad(self, actividad):
        if actividad == "Ciclismo":
            act = Ciclismo(actividad, 120, "hora",100,700,200)

        elif actividad == "Gimnasio":
            with open("actividades.txt","a") as archivo:
                archivo.write(f"{self.nombre},{self.actividad}\n")


    



             