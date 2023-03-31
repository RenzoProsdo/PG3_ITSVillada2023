def buscar_elemento(lista, numero):
    try:
        indice = lista.index(numero)
        return indice
    except ValueError:
        return None

lista = [5, 77, 20, 145]
print(lista.index(int(input('Ingresar numero: '))))

indice = buscar_elemento(lista, lista.index)

if indice is not None:
    print(f"El elemento {lista.index} está en lista.")
else:
    print(f"El elemento {lista.index} no está en la lista.")