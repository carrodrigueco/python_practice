import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#handle = open("bases_datos/Cultivos_semestrales_Departamento_de_Sucre_2018.csv")

serie = pd.Series(np.random.normal(100,20,1000))
serie[100:200] = 0
"""
"""
#Grafica de linea
figure = plt.figure(figsize=(7,4))
ax = figure.add_axes([0.1,0.1,0.8,0.8])
ax.grid(True)
ax.plot(serie)
ax.set_title("Titulo por defecto...")
plt.show()
"""
#Histograma
plt.hist(serie.values, bins=50, edgecolor="black", linewidth=1)
plt.grid(True)
plt.show()
"""
