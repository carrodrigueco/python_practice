handle = open("bases_datos/Estado_de_cultivos_Semestrales_2016-2018.csv")
archivo = handle.readlines()
for line in archivo:
    print(line)