def contar_vocales(frase):
    vocales = 'aeiouAEIOU'
    cant_vocales = 0
    for letra in frase:
        if letra in vocales:
            cant_vocales += 1
    return cant_vocales
frase = "Viejo y Glorioso Talleres"
cant_vocales = contar_vocales(frase)
print(cant_vocales)