# Escritura de Archivo de Texto

with open('my_notes.txt', 'w') as file:
    file.write("1. Estudiar para el examen de matemáticas.\n")
    file.write("2. Leer el capítulo 4 del libro de historia.\n")
    file.write("3. Practicar ejercicios de programación en Python.\n")

# Lectura de Archivo de Texto

with open('my_notes.txt', 'r') as file:
    print("Contenido del archivo:")
    linea = file.readline()
    while linea:
        print(linea.strip())
        linea = file.readline()