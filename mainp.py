import pandas as pd
import streamlit as st

# Crear un DataFrame de ejemplo
df = pd.DataFrame({'Columna1': [1, 2, 3], 'Columna2': ['A', 'B', 'C']})

# Función para descargar el DataFrame como archivo XLSX
def descargar_xlsx():
    # Guardar el DataFrame en un archivo XLSX
    df.to_excel('archivo_excel.xlsx', index=False)
    # Devolver el contenido del archivo como bytes
    with open('archivo_excel.xlsx', 'rb') as f:
        return f.read()

# Botón de descarga
if st.button("Descargar XLSX"):
    archivo_xlsx = descargar_xlsx()
    st.download_button(
        label="Haz clic para descargar",
        data=archivo_xlsx,
        key="archivo_xlsx",
        file_name="archivo_excel.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
