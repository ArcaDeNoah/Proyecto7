import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Leer los datos del archivo CSV en la raíz
car_data = pd.read_csv('vehicles_us.csv')

# 2. Encabezado de la aplicación web
st.header('Cuadro de Mandos de Anuncios de Ventas de Coches')

st.write('Selecciona las opciones para visualizar las gráficas interactivas:')

# 3. Casilla de verificación para construir el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    # Mensaje informativo
    st.write('Creación de un histograma para el conjunto de datos de anuncios de coches')
    
    # Crear un histograma utilizando plotly.express
    fig_hist = px.histogram(car_data, x="odometer", title="Distribución del Odómetro")
    
    # Mostrar el gráfico Plotly interactivo en Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)

# 4. Casilla de verificación para construir el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    # Mensaje informativo
    st.write('Creación de un gráfico de dispersión de precio vs odómetro')
    
    # Crear gráfico de dispersión utilizando plotly.express
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relación entre Odómetro y Precio")
    
    # Mostrar el gráfico Plotly interactivo en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)