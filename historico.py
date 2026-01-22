from clase_actividad import Ciclismo, Correr, Gimnasio

class Historico: 
    def __init__ (self,nombre): 
        self.nombre = nombre 
        self.actividades = []

    def registrar_actividad(self, actividad):
        print(type(actividad))
        if type(actividad) == "<class 'clase_actividad.Ciclismo'>":
            
            self.actividades.append(actividad)

        elif actividad == "Gimnasio":
            pass

    def guardad_datos(self): 

        with open("actividades.txt", "w") as fichero:
            for actividad in self.actividades:
                if type(actividad) == "Ciclismo":
                    fichero.write(f"{self.nombre}:{actividad.duracion} minutos, {actividad.distancia} distancia,{actividad.desnivel}desnivel.\n")

                elif type(actividad) == "Correr":
                    fichero.write(f"{actividad.duracion} minutos, {actividad.distancia} distancia.\n")

                elif type(actividad) == "Gimnasio": 
                    fichero.write(f"{actividad.desnivel}desnivel,{actividad.duracion} minutos, {actividad.distancia} distancia.\n")



             