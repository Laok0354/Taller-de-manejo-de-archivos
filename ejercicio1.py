f = open("archivo1.txt", "r")
count = 0

for line in f:
    count+=1

print("El archivo tiene " + str(count) + " lineas")