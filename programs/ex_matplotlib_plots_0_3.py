import matplotlib.pyplot as plt
from random import *

meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC",]
temperaturas =  [14.3, 14.3, 15.0, 14.7, 14.7, 14.5, 14.3, 14.2, 14.3, 14.3, 14.5, 14.4,]
precipitacion =[]
for i in range(12):
    precipitacion.append(randint(40, 120))

color_fondo = "#333333"
color_temp = "#FFFA5E"
color_pres = "#3388CD"

fig = plt.figure(figsize=(7,4))

ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.set_facecolor(color_fondo)
ax.plot(meses, temperaturas, color_temp , label="temperatura", linestyle="--", marker="s")
ax.set_xlabel("Meses")
ax.set_ylabel("Temperatura", color=color_temp)

ax.set_title("Temperatura y Precipitacion promedio Bogotá, por meses (1970-2000)")

ax2 = ax.twinx()
ax2.plot(meses, precipitacion, color_pres, label="precipitacion", linestyle="-.", marker="o")
ax2.set_ylabel("Precipitacion", color=color_pres)

#ax.legend()
fig.savefig("imagen2.png")
plt.show()
