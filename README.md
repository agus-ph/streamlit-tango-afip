[Esañol](#Tango-AFIP-Comparador)

[English](#Tango-AFIP-Comparator)


# Tango-AFIP Comparador

Este es un programa en Python que compara archivos Excel de AFIP y Tango y muestra, eu un nuevo archivo,
las diferencias en el listado de facturas que figuran en cada uno. Utiliza la biblioteca Streamlit 
para crear una interfaz gráfica de usuario y la biblioteca Pandas para leer y manipular datos de Excel.

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




# Tango-AFIP Comparator
This is a Python program that compares AFIP (Argentinian IRS) and Tango (a popular ERP to process invoices) 
Excel files and displays, in a new file, the differences in the list of invoices that appear in each file.
It uses the Streamlit library to create a graphical user interface and the Pandas library
to read and manipulate Excel data.

## Usage
To run the program, simply execute the following command in a terminal:

```
streamlit run tango_afip_app.py
```

This will open the graphical user interface in your web browser.

The program will prompt you to load two Excel files, one from AFIP and one from Tango.
Once you have loaded the files, you can click the "Compare Files" button to compare the invoices
in both files. The differences will be displayed in a table. You can also download an Excel file
that contains the differences by clicking on the link "Download AFIP vs Tango file".

## Credits
The program uses sample code from the Streamlit community to add Excel download functionality.
The credit is included within the code.
