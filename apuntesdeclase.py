#read
#append
#write
#create

#read
#error - el archivo no existe
#error - si no se abrio primero}

f = open("archivo1.txt", "r")

# .read() se puede mandar un número como variable para printear
# cierta cantidad de caracteres
# si ya se hizo un read completo antes no se puede leer por caracteres
# esto es porque python mantiene referencia de lo ultimo que leyo
# print(f.read()) lee todo el archivo

# print(f.read(4))

# .readline() lee una linea del archivo. si se pone 2 veces lee primero la primera y luego la segunda

#print(f.readline())

# con for por cada linea printea esa linea
for line in f:
    print(line)

try:
    f = open("archivo2.txt")
    print(f.read())
except:
    print("El archivo no existe :'v")
finally:

#siempre cerrar el archivo al final
    f.close()

#append

f = open("archivo1.txt", "a")

# en modo a, write escribe en la ultima linea
f.write("\n hambra")

f.close

f = open("archivo1.txt", "r")
print(f.read())
f.close

#write

#si se usa open y w y el archivo no existe se crea uno nuevo
f = open("archivo1.txt", "w")

#en modo w, write sobreescribe todo el archivo
f.write("borre todo lol")

f = open("archivo1.txt", "r")
print(f.read())
f.close

