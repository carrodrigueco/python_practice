import random
import matplotlib.pyplot as plt

dict = {}
color_fondo = "#242AF1"


for i in range(30):
    nota_generada = random.normalvariate(3.5, 0.98)
    nota_generada = round(nota_generada, 2)
    while True:
        id_estudiante = str(random.randint(20000, 20100))
        if id_estudiante not in dict.keys():
            dict[id_estudiante] = nota_generada
            break

"""
#Figure 
fig = plt.figure(figsize=(10,10))
ax = fig.add_axes([0.1, 0.1, 0.8,0.8])

ax.set_facecolor(color_fondo)
ax.grid(True)

ax.plot(dict.keys(), dict.values(), color="#FFFFFF", marker="s")
ax.set_xlabel("Estudiantes")
ax.set_ylabel("Notas")

ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.show()

hist = plt.hist(dict.values(), bins=4)
plt.scatter()
"""