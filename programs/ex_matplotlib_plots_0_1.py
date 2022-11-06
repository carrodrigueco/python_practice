import matplotlib.pyplot as plt
from random import *

meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC",]
temperaturas =  [14.3, 14.3, 15.0, 14.7, 14.7, 14.5, 14.3, 14.2, 14.3, 14.3, 14.5, 14.4,]
precipitacion =[]
for i in range(12):
    precipitacion.append(randint(40, 120))

"""
plt.figure(figsize=(7,4))
plt.plot(meses, temperaturas, label="temperatura")
plt.xlabel("Meses")
plt.ylabel("Temperaturas")
plt.title("Temperatura promedio Bogotá, por meses (1970-2000)")
plt.legend()
plt.show()
"""
fig = plt.figure(figsize=(7,4))

ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(meses, temperaturas, "r" , label="temperatura")
ax.set_xlabel("Meses")
ax.set_ylabel("Temperatura", color="r")

ax.set_title("Temperatura y Precipitacion promedio Bogotá, por meses (1970-2000)")

ax2 = ax.twinx()
ax2.plot(meses, precipitacion, "b", label="precipitacion")
ax2.set_ylabel("Precipitacion", color="blue")

#ax.legend()
#fig.savefig("imagen.png")
plt.show()
