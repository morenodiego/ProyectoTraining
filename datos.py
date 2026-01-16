from metrica import Metrica
def crear_metrica(): 
    peso = int(input("Dime tu peso: "))
    altura = float(input("Dime tu altura en metros: "))
    edad = int(input("Dime tu edad: "))
    metrica = Metrica(peso, altura, edad)
    print(metrica.calcular_imc())

def guardar_metrica(metrica):
    with open("mediasmetrica.txt", "a") as archivo:
        
datos()

    # Primero revisamos si el usuario ya existe
    #with open("medidasmetrica.txt", "r") as archivo:
    #    for linea in archivo: 
    #        peso_guardado = linea.split(":")[0] 
    #        while peso_guardado == peso:
    #            print("Ya pesabas eso")
    #            return datos()
    #        altura_guardado = linea.split(":")[1] 
    #        while altura_guardado == altura:
    #            print("Ya tenías esa altura")
    #            return datos()
    #        edad_guardado = linea.split(":")[2] 
    #        while edad_guardado == edad:
    #            print("Ya tenías esa edad")
    #            return datos()
    #        imc_guardado = linea.split(":")[3] 
    #        while imc_guardado == imc:
    #            print("Ya tenías ese IMC")
    #            return datos()
            


    # Si no existe, lo guardamos
    #with open("medidasmetrica.txt", "a") as archivo:
    #    archivo.write(f"{peso}:{altura}:{edad}:{imc} \n")
    #print("Datos guardados correctamente")