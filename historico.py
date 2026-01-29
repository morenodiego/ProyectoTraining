from clase_actividad import Ciclismo, Correr, Gimnasio
import os
class Historico: 
    def __init__ (self,nombre): 
        self.nombre = nombre 
        self.actividades = []

    def registrar_actividad(self, actividad):
        print(type(actividad))
        if type(actividad) == Ciclismo:
            
            self.actividades.append(actividad)

        elif actividad == Gimnasio:
            pass


    def cargar_datos(self): 
        pass
     
           



    def guardad_datos(self):
        filename = "actividades.txt"
        if os.path.exists(filename):
            os.remove(filename)
        with open(filename, "a") as fichero:

            for actividad in self.actividades:
                if type(actividad) == Ciclismo:
                    fichero.write(f"{self.nombre}:ciclismo:{actividad.duracion}:{actividad.distancia}:{actividad.desnivel}\n")

                elif type(actividad) == Correr:
                    fichero.write(f"{self.nombre}:correr:{actividad.duracion}:{actividad.distancia}\n")

                elif type(actividad) == Gimnasio: 
                    fichero.write(f"{self.nombre}:gimnasio:{actividad.entreno}\n")

