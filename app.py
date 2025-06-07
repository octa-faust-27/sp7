import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')

if hist_button: #al hacer clic en el botón
    #escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de ventas de coches')
    #crear un histograma
    fig = px.histogram(car_data, x="odometer")
    #mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

#agregar otro botón que al hacer click en él, construya un gráfico
#de dispersión plotly-express. Nuevamente, considera utilizar
#las funciones st.write() y st.plotly_chart()


