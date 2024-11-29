def gran_llista(llista):
    """Retorna el valor més gran de la llista de números."""
    if not llista:  # Comprovar si la llista està buida
        return None  # Retorna None si la llista és buida
    max_num = llista[0]  # Assumeix que el primer element és el més gran
    for num in llista:
        if num > max_num:
            max_num = num  # Actualitza el més gran
    return max_num

# Proves de la funció
print(gran_llista([3, 4, 2, 3, 10]))  # Retorna 10
print(gran_llista([-1, -5, -3]))       # Retorna -1
print(gran_llista([1, 2, 3, 4]))       # Retorna 4
print(gran_llista([]))                  # Retorna None
