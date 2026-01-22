from registro import registrar,iniciar_sesion
from historico import *

print("Bienvenido")

menu_inicial = int(input("1.Registrarte\n" \
"2. iniciar sesion\n"\
": " ))

if menu_inicial == 1: 
    registrar()
else: 
    usuario = iniciar_sesion()
    if usuario == "":
        print("No existe un usuario así en nuestro sistema")
        exit()

menu_actividad = int(input
("1.Ciclismo\n" \
"2.Correr\n"\
"3.Gimnasio\n"\
": "))


if menu_actividad == 1: 
    Ciclismo.pedir_datos()

elif menu_actividad == 2: 
    Correr.pedir_datos()
