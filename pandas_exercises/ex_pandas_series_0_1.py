import pandas as pd
import random
def subir_notas(notas:pd.Series)->pd.Series:
    media = notas.mean()
    if media > 2.5 :
        notas += round(notas.std(), 2)
    for i in range(notas.size):
        if notas.iloc[i] > 5 :
            notas.iloc[i] = 5.0
    return notas

notas = []
for i in range(15):
    nota_generada = random.normalvariate(3.5, 0.98)
    nota_generada = round(nota_generada, 2)
    while True:
        if nota_generada >= 1.5 and nota_generada <= 5 :
            notas.append(nota_generada)
            break
        else:
            nota_generada = random.normalvariate(3.5, 0.98)
            nota_generada = round(nota_generada, 2)
serie_notas = pd.Series(notas)
print("Serie notas")
print("-"*15)
print(serie_notas)
print("Serie notas")
print("-"*15)
print(subir_notas(serie_notas))

        