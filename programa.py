from registro import registrar,iniciar_sesion
from historico import *
print("Bienvenido")

menu_inicial = int(input("1.Registrarte\n" \
"2. iniciar sesion\n" ))

if menu_inicial == 1: 
    registrar()
else: 
    usuario = iniciar_sesion()
    if usuario == "":
        print("No existe un usuario así en nuestro sistema")
        exit()

actividad = input("Actividad?: ")
registro = Historico(usuario)
registro.registrar_actividad(actividad)
