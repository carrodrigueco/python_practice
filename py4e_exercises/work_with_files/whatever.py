import os
handle = open("bases_datos/archivo.txt", mode="r")
file = open("bases_datos/archivo2.txt", mode="w")
for line in handle:
    linea = ""
    for j in line:
        if j == ".":
            linea = linea.lstrip()
            file.write(f"{linea} \n")
            linea = ""
        elif j == "\n":
            file.write("\n")
        else:
            linea+=j

file.close()
handle.close()
