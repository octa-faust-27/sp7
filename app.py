import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
car_data = car_data.dropna(subset=['odometer'])

st.header('Proyecto 7 Sprint: Contrucción de una aplicación web')

if st.button('Mostrar tabla de datos'):
    st.subheader('Vista del DataFrame')
    st.write(car_data)

 

if st.checkbox('Histograma: Condición vs. Año del modelo'):
    st.subheader('Histograma: Condición vs Año del Modelo')
    fig_hist = px.histogram(car_data, x='model_year', color='condition', barmode='group', nbins=10, title ='Condición por Año del modelo')
    st.plotly_chart(fig_hist, use_container_width=True)

if st.checkbox('Gráfico de dispersión: Precio por fabricante'):
    st.subheader('Gráfico de dispersión de precios por fabricante')
    car_data['manufacturer'] = car_data['model'].apply(lambda x: x.split()[0])
    fig_scatter = px.scatter(car_data, x= 'model_year', y= 'price', color='manufacturer', size='odometer', hover_data=['model'], title='Distribución de precios por fabricante')
    st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("---")
st.caption('App creada con Streamlit y Plotly Express')
st.write('Despliegue del dataframe.')



#st.write('Aún debo agregar ciertas cosas. En construcción')

#if hist_button: #al hacer clic en el botón
    #escribir un mensaje
#    st.write('Creación de un histograma para el conjunto de datos de anuncios de ventas de coches')
    #crear un histograma
 #   fig = px.histogram(car_data, x="odometer")
    #mostrar un gráfico Plotly interactivo
  #  st.plotly_chart(fig, use_container_width=True)

#agregar otro botón que al hacer click en él, construya un gráfico
#de dispersión plotly-express. Nuevamente, considera utilizar
#las funciones st.write() y st.plotly_chart()


