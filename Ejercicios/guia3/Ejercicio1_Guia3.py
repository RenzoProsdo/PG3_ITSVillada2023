while True:
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print(f"el resultado de la suma es: {num1+num2}")
    except ValueError:
        print("Debe ingresar solo números enteros.")
    respuesta = input("¿Desea seguir sumando valores? (si/no): ")
    if respuesta.lower() != "si":
        break
