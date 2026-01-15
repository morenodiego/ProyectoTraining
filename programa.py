from registro import registrar,iniciar_sesion
print("Bienvenido")

menu_inicial = int(input("1.Registrarte\n" \
"2. iniciar sesion\n" ))

if menu_inicial == 1: 
    registrar()
else: 
    iniciar_sesion()