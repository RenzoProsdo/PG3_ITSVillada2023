strings = ['Que', 'onda', 'profe', 'todo', 'bien', '?', '?']
with open('archivo.txt', 'w') as f:
    for string in strings:
        f.write(string + '\n')
try:
    with open('archivo.txt', 'a') as f:
        f.write(123)
except TypeError:
    print("Error: No se puede escribir un entero en un archivo de texto")
