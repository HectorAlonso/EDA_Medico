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

# ! 3- VISUALIZACIONES ---------------------------------------------------------------------

# ? Histograma de presion sistolica ---------------------------------------------------------

sns.histplot(data=datos['Systolic blood pressure'])
plt.xlabel("Presion Sistolica")
plt.ylabel("Cantidad de Personas")
plt.show()

# ? Boxplot de troponina según diagnóstico. -----------------------------------------------

sns.boxplot(x='Result', y='Troponin', data=datos)
plt.title('Distribución de niveles de Troponina según Diagnóstico')
plt.show()

# ? Grafico de barras: numero de positivos y negativos por grupo de edad: <30, 30-50, >50 --

bins = [0,30,51,105]
labels = ['<30','30-50','>50']
datos['AgeGroup'] = pd.cut(datos['Age'], bins=bins, labels=labels, right=False)

CantResultadoXEdad = datos.groupby(['AgeGroup','Result']).size().unstack()
CantResultadoXEdad.plot(kind='bar', stacked=False, figsize=(8,6))

plt.title('Numero de Diagnosticos por Grupo de Edad')
plt.xlabel('Grupos de Edad')
plt.ylabel('Numero de Casos')
plt.grid(color='red',axis='y', linestyle='--', alpha=0.8)
plt.legend(title='Diagnostico')
plt.tight_layout()
plt.xticks(rotation=0)
plt.show()