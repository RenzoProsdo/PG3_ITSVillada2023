def esAñoBisiesto(año: int):
    return año%4 == 0 and año%400 == 0 and año%100 != 0

año = int(input("Ingrese el año año: "))
if esAñoBisiesto(año):
    print("Año bisiesto")
else:
    print("Año no bisiesto")