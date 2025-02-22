import streamlit as st
import plotly.express as px
import pandas as pd

# Título de la aplicación
st.title("Panel de Control Streamlit con Plotly (sin seaborn)")

# Cargar datos mpg desde un archivo CSV (debes tener el archivo 'mpg.csv')
# Descarga el archivo CSV desde: https://github.com/mwaskom/seaborn-data/blob/master/mpg.csv
# Y guárdalo en la misma carpeta que tu script.
df = pd.read_csv("mpg.csv") 

# Crear un gráfico de barras (ejemplo: caballos de fuerza promedio por origen)
fig = px.bar(df, x="origin", y="horsepower", title="Caballos de Fuerza Promedio por Origen")

# Mostrar el gráfico de Plotly en Streamlit
st.plotly_chart(fig)
