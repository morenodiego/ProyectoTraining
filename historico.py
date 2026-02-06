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
        elif type(actividad) == Gimnasio:
            self.actividades.append(actividad)


    def cargar_datos(self):
        filename = "actividades_"+self.nombre+".txt"
        if not os.path.exists(filename):
            return 
        with open(filename, "r") as fichero: 
            for linea in fichero:
                if linea.split(":")[1].strip() == "ciclismo": 
                    nombre = linea.split(":")[0].strip()
                    duracion = linea.split(":")[2].strip()
                    distancia = linea.split(":")[3].strip()
                    desnivel = linea.split(":")[4].strip()    
                    act = Ciclismo(duracion, "2-1-25",distancia,desnivel)
                    self.actividades.append(act)
                
                elif linea.split(":")[1].strip() =="correr": 
                    nombre = linea.split(":")[0].strip()
                    duracion = linea.split(":")[2].strip()
                    distancia = linea.split(":")[3].strip()
                     
                    act = Correr(duracion, "2-1-25",distancia)
                    self.actividades.append(act)
                
                elif linea.split(":")[1].strip() == "gimnasio":
                    nombre = linea.split(":")[0].strip()
                    duracion = linea.split(":")[2].strip()
                    act = Gimnasio(duracion, "2-1-25")
                    self.actividades.append(act)
                


     
           



    def guardad_datos(self):
        filename = "actividades_"+self.nombre+".txt"

        with open(filename, "w") as fichero:

            for actividad in self.actividades:
                if type(actividad) == Ciclismo:
                    fichero.write(f"{self.nombre}:ciclismo:{actividad.duracion}:{actividad.distancia}:{actividad.desnivel}\n")

                elif type(actividad) == Correr:
                    fichero.write(f"{self.nombre}:correr:{actividad.duracion}:{actividad.distancia}\n")

                elif type(actividad) == Gimnasio: 
                    fichero.write(f"{self.nombre}:gimnasio:{actividad.duracion}:{str(actividad.entreno)}\n")

