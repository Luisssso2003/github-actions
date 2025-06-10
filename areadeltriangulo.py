# Archivo de la app

def area(base, altura):
    if base <= 0:
        raise ValueError("La base debe ser mayor que cero")
    if altura < 0:
        raise ValueError("La altura no puede ser negativa")
    return (base * altura) / 2
