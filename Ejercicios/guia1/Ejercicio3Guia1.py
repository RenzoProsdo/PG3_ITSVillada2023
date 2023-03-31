def printCuadrado(caracter, ancho, alto):
    for i in range(alto):
        print(caracter * ancho)

def printTriangulo(caracter, altura):
    count = 1
    espacio = " " * altura

    while count <= altura:
        print(espacio + f"{caracter} " * count )
        count += 1
        espacio = espacio[:-1]




caracter = input('Ingrese el caracter caracter para dibujar: ')

print("r - para dibujar rectangulo")
print("t - para dibujar triangulo")
opcion = input()

if opcion == "r":
    ancho = int(input("Ingrese el ancho del rectangulo: "))
    alto = int(input("Ingrese el alto de rectangulo: "))

    printCuadrado(caracter, ancho, alto)
elif opcion == "t":
    alto = int(input("Ingrese el  alto de triangulo: "))
    
    printTriangulo(caracter, alto)
else:
    print("opcion invalida")