import streamlit as st
import pandas as pd

def main():
    st.title("Plantilla de Streamlit con Tabla")

    # Datos de ejemplo para la tabla
    data = {
        'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
        'Edad': [25, 30, 22, 28],
        'Ciudad': ['Ciudad A', 'Ciudad B', 'Ciudad C', 'Ciudad D'],
    }
    df = pd.DataFrame(data)

    # Mostrar la tabla en la aplicación
    st.write("Datos de ejemplo:")
    st.table(df)

if __name__ == '__main__':
    main()
