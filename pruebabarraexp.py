def barra_exp(exp_actual, exp_max, longitud=175):
    # Proporción de progreso
    porcentaje = exp_actual / exp_max

    # Número de bloques llenos
    llenos = int(longitud * porcentaje)
    vacios = longitud - llenos

    # Construcción de la barra
    barra = "█" * llenos + "░" * vacios

    # Mostrar barra con porcentaje
    return f"[{barra}] {porcentaje*100:.0f} %"

# Ejemplo de uso
exp_actual = 50
exp_max = 100

print(barra_exp(exp_actual, exp_max))


