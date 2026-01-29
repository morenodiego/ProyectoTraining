from registro import registrar,iniciar_sesion
from historico import Historico
from clase_actividad import Ciclismo, Correr, Gimnasio, Actividad

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

historico = Historico(usuario)

if menu_actividad == 1: 
    hora = int(input("Cuando horas enteras has entrenado : "))
    min = int(input("y cuantos mimnutos: "))
    dur = hora/60 + min
    dist = float(input("Cuantos kilometros enteros: "))
    altmax = int(input("Cuanto ha sido la altmura maxima: "))
    altmin = int(input("Y la minima: "))
    act = Ciclismo(dur, "2-1-25",dist,altmax,altmin)
    historico.registrar_actividad(act)

elif menu_actividad == 2: 
    hora = int(input("Cuando horas enteras has entrenado : "))
    min = int(input("y cuantos mimnutos: "))
    dur = hora/60 + min
    dist = float(input("Cuantos kilometros enteros: "))
    act =Correr(dur,"2-1-25", dist)
    historico.registrar_actividad(act)



historico.guardad_datos()