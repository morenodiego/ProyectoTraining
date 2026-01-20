from metrica import Metrica

def crear_metrica():
    peso = int(input("Dime tu peso: "))
    altura = float(input("Dime tu altura en metros: "))
    edad = int(input("Dime tu edad: "))

    metrica = Metrica(peso, altura, edad)
    imc = metrica.calcular_imc()

    print("Tu IMC es:", imc)

    guardar_metrica(peso, altura, edad, imc)


def guardar_metrica(peso, altura, edad, imc):
    with open("medidasmetrica.txt", "a") as archivo:
        archivo.write(f"{peso}:{altura}:{edad}:{imc}\n")
    print("Datos guardados correctamente")

crear_metrica()
