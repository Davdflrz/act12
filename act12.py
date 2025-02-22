# Ejemplo 1 con seaborn mpg
import streamlit as st
import plotly.express as px
import seaborn as sns
import pandas as pd

# Título de la aplicación
st.title("Panel de Control Streamlit con Plotly y seaborn mpg")

# Cargar datos de seaborn mpg
df = sns.load_dataset("mpg")

# Crear un gráfico de barras (ejemplo: caballos de fuerza promedio por origen)
fig = px.bar(df, x="origin", y="horsepower", title="Caballos de Fuerza Promedio por Origen")

# Mostrar el gráfico de Plotly en Streamlit
st.plotly_chart(fig)
