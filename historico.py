from clase_actividad import Ciclismo, Correr, Gimnasio
from jugador import Jugador
from metrica import Metrica
import os
from metrica import Metrica



class Historico: 
    def __init__ (self,nombre): 
        self.nombre = nombre 
        self.actividades = []
        self.metrica = []
        self.jugadores = []

    def registrar_actividad(self, actividad):
        print(type(actividad))
        if type(actividad) == Ciclismo:
            Jugador.ganar_exp(50)
            self.actividades.append(actividad)
        elif type(actividad) == Correr:
            Jugador.ganar_exp(50)
            self.actividades.append(actividad)
        elif type(actividad) == Gimnasio:
            Jugador.ganar_exp(50)
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




    def crear_metrica(self):
        peso = int(input("Dime tu peso: "))
        altura = float(input("Dime tu altura en metros: "))
        edad = int(input("Dime tu edad: "))

        metrica = Metrica(peso, altura, edad)
        imc = metrica.calcular_imc()

        print("Tu IMC es:", imc)



    def guardar_metrica(self):

        
        with open("medidasmetrica.txt", "a") as archivo:

            for metrica in self.metrica: 

                archivo.write(f"{metrica.peso}:{metrica.altura}:{metrica.edad}:{metrica.calcular_imc()}\n")
       
    
    def cargar_datos_metrica(self):
        filename = "metrica_"+self.nombre+".txt"
        if not os.path.exists(filename):
            return 
        with open(filename, "r") as fichero: 
            for linea in fichero:
                peso = linea.split(":")[0].strip()
                altura= linea.split(":")[1].strip()
                edad= linea.split(":")[2].strip()
                metrica = Metrica(peso, altura, edad)
                self.metrica.append(metrica)






    def guardar_jugadores(self):
        if os.path.exists("jugadores.txt"):
            os.remove("jugadores.txt")
        with open("jugadores.txt", "w") as fichero:
            for jugador in self.jugadores:
                fichero.write(f"{jugador.usuario}:{jugador.exp}:{jugador.nivel}:{jugador.avatar}:{jugador.mascota}:{jugador.metrica.peso}:{jugador.metrica.altura}:{jugador.metrica.edad}\n")


class Jugador:
    def __init__(self, usuario, avatar, mascota, peso, altura, edad):
        self.usuario = usuario
        self.exp = 0
        self.exp_max=100
        self.nivel = 1
        self.avatar=avatar
        self.mascota=mascota
        self.metrica = Metrica(peso, altura, edad)

    def ganar_exp(self, cantidad):
        self.exp += cantidad
        contador = 0
        while self.exp >= self.exp_max:
            self.exp -= self.exp_max
            self.nivel += 1
            contador += 1
        return contador

    def barra_exp(self):                     
        longitud = 175
        porcentaje = self.exp / self.exp_max
        if porcentaje > 1:
            porcentaje = 1
        llenos = int(longitud * porcentaje)
        vacios = longitud - llenos
        barra = "█" * llenos + "░" * vacios
        return f"Nivel {self.nivel} | {barra} {porcentaje*100:.1f}%"

    def __str__(self):
        return f"Usuario {self.usuario}, Nivel: {self.nivel}, EXP {self.exp}"
