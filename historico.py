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
        elif type(actividad) == Correr:
            
            self.actividades.append(actividad)


        elif actividad == Gimnasio:
            self.actividades.append(actividad)


    def cargar_datos(self):
        with open("actividades.txt", "r") as fichero: 
            for linea in fichero:
                if linea.split(":")[1].strip() ==  "ciclismo": 
                    nombre = linea.split(":")[0].strip()
                    duracion = linea.split(":")[2].strip()
                    distancia = linea.split(":")[3].strip()
                    desnivel = linea.split(":")[4].strip()    
                    act = Ciclismo(duracion, "2-1-25",distancia,desnivel)
                    self.registrar_actividad(act)
                
                elif linea.split(":")[1].strip() =="correr": 
                    nombre = linea.split(":")[0].strip()
                    duracion = linea.split(":")[2].strip()
                    distancia = linea.split(":")[3].strip()
                     
                    act = Correr(duracion, "2-1-25",distancia)
                    self.registrar_actividad(act)
                


     
           



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

