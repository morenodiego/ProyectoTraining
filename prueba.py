ejercicios = {}
ejerc = int(input("1. Añadir ejercicio //  2.Salir:        "))
while ejerc != 2 : 
    ejercicio = input("Que ejecicio has hecho:  ")
    series = int(input("Cuantas series en total: "))
    ejercicios[ejercicio] = series
    print (ejercicios)
    ejerc = int(input("1. Añadir ejercicio" "2.Salir"))
else:
    pass
