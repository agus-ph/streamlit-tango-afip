import streamlit as st
import pandas as pd
import plotly.express as px
import base64
from io import StringIO, BytesIO

def generate_excel_download_link(df):
    # Credit Excel: https://discuss.streamlit.io/t/how-to-add-a-download-excel-csv-function-to-a-button/4474/5
    towrite = BytesIO()
    df.to_excel(towrite, encoding="utf-8", index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="AFIP vs Tango.xlsx">Download Excel File</a>'
    return st.markdown(href, unsafe_allow_html=True)


st.set_page_config(page_title = "Tango-AFIP")
st.title("Comparador Tango-AFIP")
st.subheader("Cargue el archivo de AFIP")

upload_afip_file = st.file_uploader("Elige un archivo AFIP", type=["xlsx", "xls"])
if upload_afip_file:
    st.markdown("---")
    df = pd.read_excel(upload_afip_file, header=1)
    st.dataframe(df)

st.subheader("Cargue el archivo de Tango")

upload_tango_file = st.file_uploader("Elige un archivo Tango", type=["xlsx", "xls"])
if upload_tango_file:
    st.markdown("---")
    df2 = pd.read_excel(upload_tango_file)
    st.dataframe(df2)

st.subheader("Comparación facturas en AFIP vs Tango")


comparar_tango_afip = st.button("Comparar Archivos")

if comparar_tango_afip:
    df_afip = df

    df_afip["Fecha"] = pd.to_datetime(df_afip["Fecha"], format="%d/%m/%Y")
    df_afip_filt = df_afip[["Fecha", "Nro. Doc. Emisor", "Denominación Emisor", "Tipo", "Punto de Venta", "Número Desde"]]
    df_afip_sorted = df_afip_filt.sort_values(by=["Nro. Doc. Emisor", "Punto de Venta", "Número Desde"])
    df_afip_sorted["Codigo"] = df_afip_sorted["Fecha"].astype(str)+"-"+df_afip_sorted["Nro. Doc. Emisor"].astype(str)+"-"+df_afip_sorted["Número Desde"].astype(str).str[-2:]

    df_tango = df2

    df_tango["IDENTIFTRI"] = df_tango["IDENTIFTRI"].str.replace("-","")
    df_tango_filt = df_tango[["FECHA_EMI", "IDENTIFTRI", "NOM_PROVE", "T_COMP", "N_COMP"]]
    df_tango_sorted = df_tango_filt.sort_values(by=["IDENTIFTRI", "N_COMP"])
    df_tango_sorted["Codigo"] = df_tango_sorted["FECHA_EMI"].astype(str)+"-"+df_tango_sorted["IDENTIFTRI"].astype(str)+"-"+df_tango_sorted["N_COMP"].astype(str).str[-2:]

    df_afip_tango = pd.merge(df_afip_sorted, df_tango_sorted, how="left", on="Codigo")


    st.dataframe(df_afip_tango)

    st.subheader("Descarga archivo AFIP vs Tango")
    download_file = generate_excel_download_link(df_afip_tango)

