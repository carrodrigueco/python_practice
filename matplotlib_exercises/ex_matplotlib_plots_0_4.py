import matplotlib.pyplot as plt
from random import *

meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC",]
temperaturas =  [14.3, 14.3, 15.0, 14.7, 14.7, 14.5, 14.3, 14.2, 14.3, 14.3, 14.5, 14.4,]
precipitacion =[]
for i in range(12):
    precipitacion.append(randint(40, 120))

color_fondo = "#242AF1"
color_temp = "#E70F9B"
color_pres = "#1DD4F5"
color_title = "#92A238"

fig = plt.figure(figsize=(7,4))

ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.set_facecolor(color_fondo)
ax.grid(True)

ax.plot(meses, temperaturas, color_temp, label="temperatura", linestyle="--", marker="s")

for label in ax.get_xticklabels():
    label.set_color(color_title)

ax.set_xlabel("Meses", fontweight="bold", color=color_title)
ax.set_ylabel("Temperatura", color=color_temp)

for label in ax.get_yticklabels():
    label.set_color(color_temp)

ax.set_title("Temperatura y Precipitacion promedio Bogotá, por meses (1970-2000)", color=color_title, fontweight="bold")

ax.set_ylim(10,20)

ax2 = ax.twinx()
ax2.plot(meses, precipitacion, color_pres, label="precipitacion", linestyle="-.", marker="o")

ax2.set_ylabel("Precipitacion", color=color_pres)
for label in ax2.get_yticklabels():
    label.set_color(color_pres)

ax2.set_ylim(0,200)

#ax.legend()
fig.savefig("imagen3.png")
plt.show()