# Escribir un programa que copie el contenido de un archivo en otro.

f1 = open("archivo1.txt", "r")
f2 = open("archivo2.txt", "w+")

content1 = f1.read()

f2.write(str(content1))

f1.close()
f2.close()