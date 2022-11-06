import matplotlib.pyplot as plt
from random import *
import matplotlib.ticker as mticker

meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC",]
temps =  []
nombres_ciudades = ["Bogotá", "Barranquilla", "Cali", "Medellín", "Florencia", "Valledupar",]

for i in range(len(nombres_ciudades)):
    temporal = []
    for i in range(len(meses)):
        temporal.append(randint(10,30))
    temps.append(temporal)
    
fig, axes = plt.subplots(2, 3, figsize=(12,8), sharex=True, sharey=True)
num_ciudad = 0
for fila in axes:
    for ax in fila:
        ax.plot(meses, temps[num_ciudad], "r", label="temperatura")

        ticks_loc = ax.get_xticks()
        ax.xaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
        ax.set_xticklabels(meses)
        ax.set_xlabel("Meses")
        ax.set_ylabel("Temperaturas")
        ax.set_title(nombres_ciudades[num_ciudad])
        num_ciudad+=1
plt.tight_layout()
plt.show()