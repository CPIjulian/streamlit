import os
import streamlit as st
import pandas as pd
import pip
pip.main(["install", "hydralit"])
pip.main(["install", "openpyxl"])
import hydralit_components as hc
import io
from xlsxwriter import ExcelWriter

st.set_page_config(page_title= 'Reformas CPI',
                    page_icon='moneybag:',
                    layout='wide' )



def Inicio():
    st.markdown("<h1 style='text-align: center; background-color: #000045; color: #ece5f6'>Unidad DE PLANIFICACIÓN</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; background-color: #000045; color: #ece5f6'>Sistema de reformas</h4>", unsafe_allow_html=True)
    menu_data = [
    {'id': 1, 'label': "Información", 'key': "md_how_to", 'icon': "fa fa-home"},
    {'id': 2, 'label': "Documentación", 'key': "md_run_analysis"}
    #{'id': 3, 'label': "Document Collection", 'key': "md_document_collection"},
    #{'id': 4, 'label': "Semantic Q&A", 'key': "md_rag"}
    ]

    int(hc.nav_bar(
        menu_definition=menu_data,
        hide_streamlit_markers=False,
        sticky_nav=True,
        sticky_mode='pinned',
        override_theme={'menu_background': '#4c00a5'}
    ))
  
    st.header("**📖 Información general de la Aplicación para realizar reformas**")
    st.markdown("""
                    
                    General:

                    Las reformas al Plan Operativo Anual (POA) del Gobierno Autónomo Descentralizado de la Prefectura de Pichincha (GADPP) consisten en el cambio/modificación a las partidas presupuestarias, proyectos, y metas establecidas
                    por cada una de las Unidades/Unidades del GADPP.
                    Este proceso implica en líneas generales el procesamiento de información disponible en el sistema odoo, así como bases sueltas y el seguimiento a metas en la plataforma
                    de seguimiento, con el propósito de mantener una congruencia de la información para proceder aceptar dichos cambios/modificaciones. 
                    Para llevar a cabo de manera efectiva el proceso y diagnóstico, es crucial tener en cuenta tres elementos esenciales: la normativa, el proceso y las bases. 

                    Este aplicativo web se presenta como una estrategia efectiva para optimizar y agilizar el proceso de gestión de reformas en la institución, al proporcionar una plataforma accesible y dinámica que permitirá a los usuarios
                    navegar a través de los datos, realizar análisis en tiempo real y tomar decisiones informadas de manera eficiente reduciendo el trabajo manual y posibles errores humanos
             
                    Además, el diseño del aplicativo web presenta un panel interactivo y de fácil intuición, garantizando que las diversas Unidades
                    de la institución puedan utilizar la herramienta de manera eficiente
                    """)
        
    st.info("""
                Se describen con más detalle estos componentes en el manual de uso [Documentacion Reformas](https://docs.snowflake.com/). 
                Ademas esta incluida la información del sistema utilizado y sus beneficios.
                """)
        
    st.markdown("""
                    En el caso de tener algun tipo de problema comuniquese con la coordinacion de Planificación. 🚀
                
                    A continuación se detalla cada opción de reforma:

                """)
    
    
    st.header("🔄 Reforma interna", help="Reforma en la misma Unidad")
            
    create_tab, tips_tab = \
        st.tabs(["Resumen", "❄️Pasos"])
    with create_tab:
        st.markdown("""
                    **Interna**

                    En esta sección las reformas/movimientos que se solicitan se realizaran unicamente entre la misma Unidad.
                    Es decir, se puede modificar los proyectos sumando y restando el codificado o cambiar el nombre de las metas en la Unidad seleccionada.
                    Una ves modificado los valores y metas deseadas se procede a guardar la información esto generara automaticamente un archivo pdf con un codigo y con información de las 
                    modificaciones realizadas ya sea solo codificado, metas o los 2.
                    
                    """
                )
                    
    with tips_tab:
        st.markdown("""
                💡 **Pasos para realizar una reforma interna**
                    
                - Selecione la `Unidad` en la cual desea realizar las modificaciones, aparecera 2 tablas con la información de la Unidad: `Presupuesto` y `Metas`. 
                - En la primera tabla `Presupuesto` se puede editar los valores que afectan al `codificado`, con la columna `movimiento` tomando muy en cuenta que se puede restar valores a las partidas unicamente que tengan `saldo diponible` y sumar el valor restado a cualquier partida deseada. 
                - En la segunda tabla `Metas` se pueden realizar modificaciones a la ultima meta registrada, en la columna `nueva meta` se ingresa el nombre de la nueva meta.
                - En los widgets de la parte inferior tiene los totales del `codificado`, `nuevo codificado` y `movimiento`. Esta información permite verificar que la información se a ingresado correctamente ya que el codificado debe tener el mismo valor y el valor de movimiento simpre debe ser cero.
                - El boton de guardar información se activara si todo el proceso se encuentra bien realizado caso contrario no se podra descargar la informacion de los datos modificados.
                - Se descarga un archivo pdf del movimiento del presupuesto y de los cambios de las metas, si el documento se encuentra vacio es decir, que no se a realizado cambios sea en el presupuesto o en las metas.
                """)
                #- Utilize dynamic tables to simplify data transformation and avoid complex pipeline management, making them ideal for materializing query results from multiple base tables in ETL processes.
    st.header("🌀 Reforma Externa", help="Reforma entre Unidades")
            
    create_tab, tips_tab = \
        st.tabs(["Resumen", "❄️Pasos"])
    with create_tab:
        st.markdown("""
                    **Externa**

                    En esta sección las reformas/movimientos que se solicitan se realizaran unicamente entre la misma Unidad.
                    Es decir, se puede modificar los proyectos sumando y restando el codificado o cambiar el nombre de las metas en la Unidad seleccionada.
                    Una ves modificado los valores y metas deseadas se procede a guardar la información esto generara automaticamente un archivo pdf con un codigo y con información de las 
                    modificaciones realizadas ya sea solo codificado, metas o los 2.
                    
                    """
                )
                    
    with tips_tab:
        st.markdown("""
                💡 **Pasos para realizar una reforma externa**
                    
                - Selecione la `Unidad` en la cual desea realizar las modificaciones, aparecera 2 tablas con la información de la Unidad: `Presupuesto` y `Metas`. 
                - En la primera tabla `Presupuesto` se puede editar los valores que afectan al `codificado`, con la columna `movimiento` tomando muy en cuenta que se puede restar valores a las partidas unicamente que tengan `saldo diponible` y sumar el valor restado a cualquier partida deseada. 
                - En la segunda tabla `Metas` se pueden realizar modificaciones a la ultima meta registrada, en la columna `nueva meta` se ingresa el nombre de la nueva meta.
                - En los widgets de la parte inferior tiene los totales del `codificado`, `nuevo codificado` y `movimiento`. Esta información permite verificar que la información se a ingresado correctamente ya que el codificado debe tener el mismo valor y el valor de movimiento simpre debe ser cero.
                - El boton de guardar información se activara si todo el proceso se encuentra bien realizado caso contrario no se podra descargar la informacion de los datos modificados.
                - Se descarga un archivo pdf del movimiento del presupuesto y de los cambios de las metas, si el documento se encuentra vacio es decir, que no se a realizado cambios sea en el presupuesto o en las metas.
                """)
        
    st.header("➖ Liberación ", help="Reforma entre Unidades")
            
    create_tab, tips_tab = \
        st.tabs(["Resumen", "❄️Pasos"])
    with create_tab:
        st.markdown("""
                    **Externa**

                    En esta sección las reformas/movimientos que se solicitan se realizaran unicamente entre la misma Unidad.
                    Es decir, se puede modificar los proyectos sumando y restando el codificado o cambiar el nombre de las metas en la Unidad seleccionada.
                    Una ves modificado los valores y metas deseadas se procede a guardar la información esto generara automaticamente un archivo pdf con un codigo y con información de las 
                    modificaciones realizadas ya sea solo codificado, metas o los 2.
                    
                    """
                )
                    
    with tips_tab:
        st.markdown("""
                💡 **Pasos para realizar una reforma externa**
                    
                - Selecione la `Unidad` en la cual desea realizar las modificaciones, aparecera 2 tablas con la información de la Unidad: `Presupuesto` y `Metas`. 
                - En la primera tabla `Presupuesto` se puede editar los valores que afectan al `codificado`, con la columna `movimiento` tomando muy en cuenta que se puede restar valores a las partidas unicamente que tengan `saldo diponible` y sumar el valor restado a cualquier partida deseada. 
                - En la segunda tabla `Metas` se pueden realizar modificaciones a la ultima meta registrada, en la columna `nueva meta` se ingresa el nombre de la nueva meta.
                - En los widgets de la parte inferior tiene los totales del `codificado`, `nuevo codificado` y `movimiento`. Esta información permite verificar que la información se a ingresado correctamente ya que el codificado debe tener el mismo valor y el valor de movimiento simpre debe ser cero.
                - El boton de guardar información se activara si todo el proceso se encuentra bien realizado caso contrario no se podra descargar la informacion de los datos modificados.
                - Se descarga un archivo pdf del movimiento del presupuesto y de los cambios de las metas, si el documento se encuentra vacio es decir, que no se a realizado cambios sea en el presupuesto o en las metas.
                """)
        
    st.header("➕ Solicitud", help="Reforma entre Unidades")
            
    create_tab, tips_tab = \
        st.tabs(["Resumen", "❄️Pasos"])
    with create_tab:
        st.markdown("""
                    **Externa**

                    En esta sección las reformas/movimientos que se solicitan se realizaran unicamente entre la misma Unidad.
                    Es decir, se puede modificar los proyectos sumando y restando el codificado o cambiar el nombre de las metas en la Unidad seleccionada.
                    Una ves modificado los valores y metas deseadas se procede a guardar la información esto generara automaticamente un archivo pdf con un codigo y con información de las 
                    modificaciones realizadas ya sea solo codificado, metas o los 2.
                    
                    """
                )
                    
    with tips_tab:
        st.markdown("""
                💡 **Pasos para realizar una reforma externa**
                    
                - Selecione la `Unidad` en la cual desea realizar las modificaciones, aparecera 2 tablas con la información de la Unidad: `Presupuesto` y `Metas`. 
                - En la primera tabla `Presupuesto` se puede editar los valores que afectan al `codificado`, con la columna `movimiento` tomando muy en cuenta que se puede restar valores a las partidas unicamente que tengan `saldo diponible` y sumar el valor restado a cualquier partida deseada. 
                - En la segunda tabla `Metas` se pueden realizar modificaciones a la ultima meta registrada, en la columna `nueva meta` se ingresa el nombre de la nueva meta.
                - En los widgets de la parte inferior tiene los totales del `codificado`, `nuevo codificado` y `movimiento`. Esta información permite verificar que la información se a ingresado correctamente ya que el codificado debe tener el mismo valor y el valor de movimiento simpre debe ser cero.
                - El boton de guardar información se activara si todo el proceso se encuentra bien realizado caso contrario no se podra descargar la informacion de los datos modificados.
                - Se descarga un archivo pdf del movimiento del presupuesto y de los cambios de las metas, si el documento se encuentra vacio es decir, que no se a realizado cambios sea en el presupuesto o en las metas.
                """)
def Interna():
    st.markdown("<h1 style='text-align: center; background-color: #000045; color: #ece5f6'>Unidad DE PLANIFICACIÓN</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; background-color: #000045; color: #ece5f6'>Sistema de reformas</h4>", unsafe_allow_html=True)
    menu_data = [
    {'id': 1, 'label': "Información", 'key': "md_how_to", 'icon': "fa fa-home"},
    {'id': 2, 'label': "Documentación", 'key': "md_run_analysis"}
    #{'id': 3, 'label': "Document Collection", 'key': "md_document_collection"},
    #{'id': 4, 'label': "Semantic Q&A", 'key': "md_rag"}
    ]

    int(hc.nav_bar(
        menu_definition=menu_data,
        hide_streamlit_markers=False,
        sticky_nav=True,
        sticky_mode='pinned',
        override_theme={'menu_background': '#4c00a5'}
    ))

    def main():
        st.title("Cargar Archivo Excel en Streamlit")
        df = pd.read_excel("tabla_presupuesto.xlsx", engine='openpyxl')
        st.write("Datos del archivo:")
        st.write(df)
        
      
        
        
        # buffer to use for excel writer
        buffer = io.BytesIO()
        
        data = {
            "calories": [420, 380, 390],
            "duration": [50, 40, 45],
            "random1": [5, 12, 1],
            "random2": [230, 23, 1]
        }
        df = pd.DataFrame(data)
        
        @st.cache
        def convert_to_csv(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv(index=False).encode('utf-8')
        
        csv = convert_to_csv(df)
        
        # display the dataframe on streamlit app
        st.write(df)
        
        # download button 1 to download dataframe as csv
        download1 = st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='large_df.csv',
            mime='text/csv'
        )
        
        # download button 2 to download dataframe as xlsx
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            # Write each dataframe to a different worksheet.
            df.to_excel(writer, sheet_name='Sheet1', index=False)
        
            download2 = st.download_button(
                label="Download data as Excel",
                data=buffer,
                file_name='large_df.xlsx',
                mime='application/vnd.ms-excel'
            )
      
    
    if __name__ == "__main__":
        main()


    


page_names_to_funcs = {
    "Inicio": Inicio,   
    "Interna": Interna
}


st.sidebar.image('logo GadPP.png', caption='Unidad de Planificación')
st.sidebar.title("Reformas:")

demo_name = st.sidebar.selectbox('Escoja el tipo de Reforma', page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()

with st.sidebar.expander("🗺 Datos", expanded=True):
    st.markdown(f"""
    - La información del `presupuesto` se actualiza cada día a las 10 de la mañana.
    - Fecha actual de la información presupuestaria: (dd/mm/aa) 
        """)

contrasena_correcta = "CPI"

# Configuración de la aplicación
st.sidebar.title("ADMIN")

# Entrada de contraseña
contrasena = st.sidebar.text_input("contraseña:", type="password")

# Verificar si la contraseña es correcta
if contrasena == contrasena_correcta:

    st.sidebar.success("Contraseña correcta. ¡Bienvenido!")
else:
    st.sidebar.error("Contraseña incorrecta. Acceso denegado.")
