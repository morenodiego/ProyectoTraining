from jugador import Jugador
from historico import Historico

h = Historico("Marcos")
p = Jugador("Marcos", "perro", "dragon", 70, 175, 25)
p2 = Jugador("Hector", "gato", "unicornio", 60, 178, 17)
h.incluir_jugador(p)
h.incluir_jugador(p2)
print(p)
print(p2)
p.ganar_exp(150)
p2.ganar_exp(50)
niveles_subidos = p.ganar_exp(300)
if niveles_subidos > 0:
    print(f"¡Has subido {niveles_subidos} niveles!")
niveles_subidos=p2.ganar_exp(25)
if niveles_subidos > 0:
    print(f"¡Has subido {niveles_subidos} niveles!")
print(p.barra_exp())
print(p2.barra_exp())
print(p)
print(p2)
h.guardar_jugadores()
