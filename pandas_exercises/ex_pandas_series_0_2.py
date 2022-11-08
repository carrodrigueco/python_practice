import pandas as pd
df_records = pd.read_csv("bases_datos/Cultivos_semestrales_Departamento_de_Sucre_2018.csv")
lista1 = ['AREA SEMBRADA (ha)','AREA COSECHADA (ha)', 'RENDIMIENTO (t/ha)','PRECIO PAGADO AL PRODUCTOR ($/kg)']
lista2 = ['MUNICIPIOS', 'PRODUCTO', 'SEMESTRE DEL CULTIVO', 'EXPLOTACIONES AGRÍCOLAS' ]
valores = df_records[lista1].copy()
print(valores.sum())
"""
['MUNICIPIOS', 'PRODUCTO', 'SEMESTRE DEL CULTIVO', 'AREA SEMBRADA (ha)',
       'AREA COSECHADA (ha)', 'RENDIMIENTO (t/ha)', 'PRODUCCIÓN (t)',
       'PRECIO PAGADO AL PRODUCTOR ($/kg)', 'EXPLOTACIONES AGRÍCOLAS']
"""