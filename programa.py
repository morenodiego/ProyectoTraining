from registro import registrar,iniciar_sesion
from historico import Historico
from clase_actividad import Ciclismo, Correr, Gimnasio, Actividad
from jugador import Jugador

print("Bienvenido")

menu_inicial = int(input("1.Registrarte\n" \
"2. iniciar sesion\n"\
": " ))

if menu_inicial == 1: 
    registrar()
    # Después de registrarse, pedir que inicie sesión
    print("\nAhora inicia sesión con tu nueva cuenta")
    usuario = iniciar_sesion()
    if usuario == "":
        print("No existe un usuario así en nuestro sistema")
        exit()

elif menu_inicial == 2: 
    usuario = iniciar_sesion()
    if usuario == "":
        print("No existe un usuario así en nuestro sistema")
        exit()

# Cargar histórico y jugador
if usuario:
    historico = Historico(usuario)
    historico.cargar_datos()
    jugador = historico.cargar_jugador(usuario)
    if jugador is None:
        print("Error: No se encontró el perfil del jugador")
        exit()




menu_actividad = int(input
("1.Ciclismo\n" \
"2.Correr\n"\
"3.Gimnasio\n"\
"4.Editar métrica\n"\
": "))

if menu_actividad == 1: 
    hora = int(input("Cuando horas enteras has entrenado : "))
    min = int(input("y cuantos mimnutos: "))
    dur = hora*60 + min
    dist = float(input("Cuantos kilometros enteros: "))
    altmax = int(input("Cuanto ha sido la altmura maxima: "))
    altmin = int(input("Y la minima: "))
    desnivel = altmax - altmin
    act = Ciclismo(dur, "2-1-25",dist,desnivel)
    historico.registrar_actividad(act)
    jugador.ganar_exp(40)
    print(jugador.barra_exp())


elif menu_actividad == 2: 
    hora = int(input("Cuando horas enteras has entrenado : "))
    min = int(input("y cuantos mimnutos: "))
    dur = hora*60 + min
    dist = float(input("Cuantos kilometros enteros: "))
    act = Correr(dur,"2-1-25", dist)
    historico.registrar_actividad(act) 
    jugador.ganar_exp(50)
    print(jugador.barra_exp())


elif menu_actividad == 3: 
    hora = int(input("Cuando horas enteras has entrenado : "))
    min = int(input("y cuantos mimnutos: "))
    dur = hora*60 + min
    
    act = Gimnasio(dur, "2-1-25")  
    act.entrenamiento()  # Llamar al método de entrenamiento
    
    historico.registrar_actividad(act)
    jugador.ganar_exp(50)
    print(jugador.barra_exp())
elif menu_actividad == 4:
    input(historico.crear_metrica())
    historico.guardar_metrica()
    historico.cargar_datos_metrica()
    

    


    



historico.guardad_datos()