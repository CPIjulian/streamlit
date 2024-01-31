import os
import streamlit as st
import pandas as pd
import pip
pip.main(["install", "hydralit"])
pip.main(["install", "openpyxl"])
import hydralit_components as hc
import io
from io import BytesIO
st.set_page_config(page_title= 'Reformas CPI',
                    page_icon='moneybag:',
                    layout='wide' )

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

# Para la seccion 1 y 2
def agregar_columnas(df):
    df['Movimiento'] = 0
    df['TOTAL'] = df['Codificado'] + df['Movimiento']
    return df
# Para la seccion 2 segunda tabla
def agregar_column(dfd):
    dfd['Movimiento'] = 0
    dfd['TOTAL'] = dfd['Codificado'] + dfd['Movimiento']
    return dfd

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

    def main():
        #CARGAMOS LAS BASES
        odoo = pd.read_excel("tabla_presupuesto.xlsx")
        metas = pd.read_excel("tabla_metas.xlsx")
        df_odoo = pd.DataFrame(odoo)
        df_mt = pd.DataFrame(metas)
        #ENCABEZADO
        st.markdown("<h1 style='text-align:center;background-color: #000045; color: #ffffff'>🔄 REFORMA INTERNA </h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; background-color: #f0efeb; color: #080200'>(En la misma Unidad)</h4>", unsafe_allow_html=True)
        st.markdown("---")
        #reload---
        reload_data = False
        #FILTRAMOS SOLO PAI
        df_odoo= df_odoo.loc[df_odoo['PAI/NO PAI'] == 'PAI']
        df_odoo['Codificado'] = df_odoo['Codificado'].round(2)
        #AGRUPAMOS LAS UNIDADES
        direc = st.selectbox('Escoja la Unidad', options=df_odoo['Unidad'].unique())
        #FILTRAMOS COLUMNAS 
        df_od= df_odoo.loc[df_odoo.Unidad == direc].groupby(['Unidad','PROYECTO','Código','Estructura'], as_index= False)[['Codificado', 'Saldo Disponible']].sum()##.agg({'Codificado':'sum'},{'Saldo_Disponible':'sum'}) #
        df_od.rename(columns = {'Saldo Disponible': 'Saldo_Disponible'}, inplace= True)
        df_mt= df_mt.loc[df_mt.Unidad == direc]
        df = pd.DataFrame(df_od)
        df = agregar_columnas(df)
        #SUBTITULOS
        st.markdown(f"<h2 style='text-align:center;'> {direc} </h2>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("<h3 style='text-align: center; background-color: #DDDDDD;'> 🗄 Tabla de Presupuesto</h3>", unsafe_allow_html=True, help="Se realiza cambios en la columna Movimientos, tomar encuenta el saldo disponible para restar un valor caso contrario no se tomara encuenta la reforma.")
        #FORMATO DE COLUMNAS
        gb = GridOptionsBuilder.from_dataframe(df) 
        gb.configure_column('Unidad', hide=True)#, rowGroup=True, cellRenderer= "agGroupCellRenderer", )
        gb.configure_column('PROYECTO',header_name="PROYECTO", hide=True, rowGroup=True)
        gb.configure_column('Estructura')
        gb.configure_column(field ='Codificado', maxWidth=150, aggFunc="sum", valueFormatter="data.Codificado.toLocaleString('en-US');")
        gb.configure_column('Saldo_Disponible', maxWidth=150, valueFormatter="data.Saldo_Disponible.toLocaleString('en-US');", aggFunc='sum' )
        cellsytle_jscode = JsCode("""
            function(params) {
                if (params.value > '0') {
                    return {
                        'color': 'white',
                        'backgroundColor': 'green'
                    }
                } 
                else if (params.value < '0'){
                    return {
                        'color': 'white',
                        'backgroundColor': 'darkred'
                    }
                }                 
                else {
                    return {
                        'color': 'black',
                        'backgroundColor': 'white'
                    }
                }
            };
        """)
          
        gb.configure_column('Movimiento', header_name='Increm/Dismi' , editable= True ,type=['numericColumn'], cellStyle=cellsytle_jscode, maxWidth=150, valueFormatter="data.Movimiento.toLocaleString('en-US');")
        
        gb.configure_column('Nuevo Codificado',header_name='Nuevo Cod' , valueGetter='Number(data.Codificado) + Number(data.Movimiento)', cellRenderer='agAnimateShowChangeCellRenderer',
                            type=['numericColumn'],maxWidth=150, valueFormatter="data.Nuevo Codificado.toLocaleString('en-US');", aggFunc='sum', enableValue=True)
        gb.configure_column('TOTAL', hide=True)

        go = gb.build()
        go['alwaysShowHorizontalScroll'] = True
        go['scrollbarWidth'] = 1
        reload_data = False

        edited_df = AgGrid(
            df,
            editable= True,
            gridOptions=go,
            width=1000, 
            height=400, 
            fit_columns_on_grid_load=True,
            theme="streamlit",
            #data_return_mode=return_mode_value, 
            #update_mode=update_mode_value,
            allow_unsafe_jscode=True, 
            #key='an_unique_key_xZs151',
            reload_data=reload_data,
            #no agregar cambia la columna de float a str
            #try_to_convert_back_to_original_types=False
        )
       
        # Si se detectan cambios, actualiza el DataFrame
        if edited_df is not None:
            # Convierte el objeto AgGridReturn a DataFrame
            edited_df = pd.DataFrame(edited_df['data'])
            edited_df['TOTAL'] = edited_df['Codificado'] + edited_df['Movimiento']
            #st.write('Tabla editada:', edited_df)
            #st.write(f'<div style="width: 100%; margin: auto;">{df.to_html(index=False)}</div>',unsafe_allow_html=True)
        #AGREGAR NUEVA PARTIDA
        st.markdown(
            '''
            <style>
            .streamlit-expanderHeader {
                background-color: blue;
                color: black; # Adjust this for expander header color
            }
            .streamlit-expanderContent {
                background-color: blue;
                color: black; # Expander content color
            }
            </style>
            ''',
            unsafe_allow_html=True
        )
        with st.expander("🆕  Crear una partida nueva", expanded=False): 
            st.markdown("<p style='text-align: center; background-color: #B5E6FC;'> Agregar nueva partida </p>", unsafe_allow_html=True)
            dfnuevop = pd.DataFrame(columns=['Proyecto','Estructura','Incremento'])
            #colors = st.selectbox('Escoja la Unidad', options=df_odoo['Unidad'].unique())
            config = {
                'Proyecto' : st.column_config.SelectboxColumn('Proyecto',width='large', options=df_od['PROYECTO'].unique()),
                'Estructura' : st.column_config.TextColumn('Estructura', width='large', required=True),
                'Incremento' : st.column_config.NumberColumn('Incremento', min_value=0)
            }

            result = st.data_editor(dfnuevop, column_config = config, num_rows='dynamic')

            if st.button('Crear partida:'):
                st.write(result)
        #TOTALES
        total_cod = int(edited_df['Codificado'].sum())
        total_mov = int(edited_df['Movimiento'].sum())
        total_tot = int(edited_df['TOTAL'].sum())
        nuevo_p = int(result['Incremento'].sum())

        #DIVIDIMOS EL TABLERO EN 3 SECCIONES
        left_column, center_column, right_column = st.columns(3)
        with left_column:
            st.subheader("Total Codificado: ")
            st.subheader(f"US $ {total_cod:,}")
            #st.dataframe(df_od.stack())
            #st.write(df_od)
        
        with center_column:
            st.subheader("Nuevo Codificado: ")
            st.subheader(f"US $ {total_tot+nuevo_p:,}")

        with right_column:
            st.subheader("Total Increm/Dismi(): ")
            st.subheader(f"US $ {total_mov+nuevo_p:,}")


        st.markdown(f"<h3 style='text-align: center; background-color: #DDDDDD;'> 🗄 Tabla de Metas </h3>", unsafe_allow_html=True, help="En la columna Nueva Meta se puede agregar la modificación a la meta actual")
        # Mostrar la tabla con la extensión st_aggrid
        with st.expander("🆕  Modificar metas de los proyectos", expanded=False): 
            edit_df = AgGrid(df_mt, editable=True)
                            #reload_data=reload_data,)
            edit_df = pd.DataFrame(edit_df['data'])

        if total_cod != total_tot+nuevo_p:
            st.markdown('<div style="max-width: 900px; margin: 0 auto; background-color:#ffcccc; padding:10px; text-align: center;"><h4 style="color:#ff0000;">El valor total del codificado y nuevo codificado son diferentes</h3></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="max-width: 900px; margin: 0 auto; background-color:#F1FFEF; padding:10px; text-align: center;"><h4 style="color:#008000;">El valor total del codificado y nuevo codificado son iguales</h3></div>', unsafe_allow_html=True)


        try:
            edited_rows = edited_df[edited_df['Movimiento'] != 0]
            edit_rows = edit_df[edit_df['Nueva Meta'] != '-']
        except:
            st.write('No se realizaron cambios en de la información')

           
        def descargar_xlsx(edited_rows, edit_rows):
              # Guardar los DataFrames en dos hojas de un archivo XLSX en memoria
              output = BytesIO()
              with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                  edited_rows.to_excel(writer, sheet_name='Hoja1', index=False)
                  edit_rows.to_excel(writer, sheet_name='Hoja2', index=False)
              output.seek(0)
              return output

        if st.button("Descargar XLSX con Dos Hojas"):
              archivo_xlsx = descargar_xlsx(edited_rows, edit_rows)
              st.download_button(
                  label="Haz clic para descargar",
                  data=archivo_xlsx.read(),
                  key="archivo_xlsx",
                  file_name="archivo_excel.xlsx",
                  mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
              )
              st.success("¡Descarga exitosa!")
        
    
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
