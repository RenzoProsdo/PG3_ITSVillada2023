meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

try:
    num_mes = int(input("Ingresa el número de mes (1-12): "))
    
    nombre_mes = meses[num_mes - 1]
    print(f"El mes correspondiente al número {num_mes} es {nombre_mes}.")
    
except IndexError:
    print("El número de mes ingresado es inválido. Debe ser un número entre 1 y 12.")
    

