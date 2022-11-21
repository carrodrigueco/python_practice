import re

handle = open("bases_datos/file3.txt")
suma = 0
for line in handle:
    slot = re.findall("[0-9]+",line)
    if len(slot) != 0:
        for number in slot:
            number = int(number)
            suma += number
print(suma)