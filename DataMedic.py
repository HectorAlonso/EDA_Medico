import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns

# ! 1- CARGA DE DATOS ---------------------------------------------------------------------

datos = pd.read_csv("Medicaldataset.csv")

# ! 2- EXPLORACION GENERAL -----------------------------------------------------------------

# ? Cuál es la edad promedio? --------------------------------------------------------------

edadPromedio = int(datos['Age'].mean())
print(f"El promedio de edad es: {edadPromedio}")

# ? Cuantos Casos hay de cada resultado(positive, negative)? -------------------------------

casos = datos['Result'].value_counts()

colorResulta = ["#e32715","#187919"]
EtiquetasResu = ['Positivo', 'Negativo']

plt.bar(EtiquetasResu,casos, color = colorResulta)

for i, valor in enumerate(casos):
    plt.text(i, valor + 1, str(valor), ha='center')

plt.title('Cantidad de Casos por Resultado')
plt.xlabel('Diagnostico')
plt.ylabel('Cantidad de Casos')
plt.grid(axis='y', color='gray', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.xticks(rotation=0)
plt.show()

# ? Que rango tiene el ritmo Cardiaco ------------------------------------------------------

ritmoExagerado = datos.loc[datos['Heart rate']>200] 
datos.loc[datos['Heart rate']==1111, 'Heart rate'] = 111 

min = datos['Heart rate'].min()
maximo = datos['Heart rate'].max()      
print(f"El rango del ritmo cardiaco es: {min} - {maximo}") 