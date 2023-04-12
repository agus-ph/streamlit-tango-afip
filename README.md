# Tango-AFIP Comparador

Este es un programa en Python que compara archivos de AFIP y Tango y muestra las 
diferencias. Utiliza la biblioteca Streamlit para crear una interfaz gráfica de usuario 
y la biblioteca Pandas para leer y manipular datos de Excel.

## Uso
Para ejecutar el programa, simplemente ejecute el siguiente comando en una terminal:


```
streamlit run tango_afip_app.py
```

Esto abrirá la interfaz gráfica de usuario en su navegador web.

El programa le pedirá que cargue dos archivos Excel, uno de AFIP y otro de Tango. 
Una vez que haya cargado los archivos, puede hacer clic en el botón "Comparar Archivos" 
para comparar las facturas en ambos archivos. Las diferencias se mostrarán en una tabla.
También puede descargar un archivo Excel que contiene las diferencias haciendo clic en el enlace 
"Descarga archivo AFIP vs Tango".

## Créditos
El programa utiliza código de ejemplo de la comunidad de Streamlit para agregar la 
funcionalidad de descarga de Excel. El crédito se encuentra dentro del código.
