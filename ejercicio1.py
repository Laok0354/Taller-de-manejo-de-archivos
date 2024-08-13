# Escribir un programa que cuente la cantidad de líneas en un archivo.
with open("archivo1.txt", "r") as f:
    count = 0

    for line in f:
        count+=1

    print("El archivo tiene " + str(count) + " lineas")