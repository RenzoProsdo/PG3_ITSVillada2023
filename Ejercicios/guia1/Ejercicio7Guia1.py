def NumeroStep(numero: int):
    cadena = str(numero)

    for i in range(len(cadena) - 1):
        numeroActual = int(cadena[i])
        numeroSiguiente = int(cadena[i+1])

        if abs(numeroActual - numeroSiguiente) != 1:
            return False

    return True

print(123234)
print(NumeroStep(98761787654))