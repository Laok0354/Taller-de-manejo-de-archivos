#Escribir un programa que, dados dos archivos, combine cada línea del primer archivo 
#con la línea correspondiente del segundo. Es decir, concatenar la primera línea de 
#ambos, luego la segunda, luego la tercera, etc. El resultado debe almacenarse en el segundo archivo.

f1 = open("archivo1.txt", "r")
f2 = open("archivo2.txt", "r")
palabras = []
contadorRePiola = 0

for line in f1:
    palabras.append(f2.readline())

f1.close()
f2.close()
f1 = open("archivo1.txt", "r")
f2 = open("archivo2.txt", "a")

for line in f1:
    coso = line[:-1]+palabras[contadorRePiola][:-1]
    f2.write(coso+"\n")
    contadorRePiola+=1

f1.close()
f2.close()