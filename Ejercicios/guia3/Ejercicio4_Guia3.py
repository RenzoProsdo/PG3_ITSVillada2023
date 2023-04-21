try:
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))

    resultado = num1 / num2
    print(f"El resultado de la division es: {resultado}.")

except ZeroDivisionError:
    print("Error: no es posible dividir entre cero.")

except ValueError:
    print("Error: ingresaste un valor inválido. Debe ingresar un número entero.")
