import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Nuestra Boda", page_icon="💍", layout="centered")

# Estilo visual básico con CSS
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
        text-align: center;
    }
    h1 {
        color: #d4af37;
        font-family: 'serif';
    }
    </style>
""", unsafe_allow_html=True)

# Contenido de la invitación
st.markdown("<h1>¡Nos Casamos!</h1>", unsafe_allow_html=True)
st.write("### María & Carlos")
st.write("📅 **Fecha:** 15 de Diciembre de 2026")
st.write("📍 **Lugar:** Salón Los Girasoles, Culiacán")

st.markdown("---")

# Formulario de Confirmación (RSVP)
st.subheader("Confirma tu asistencia")

with st.form("rsvp_form"):
    nombre = st.text_input("Nombre completo:")
    asistencia = st.radio("¿Asistirás?", ["Sí, ahí estaré", "No podré asistir"])
    acompanantes = st.number_input("Número de acompañantes:", min_value=0, max_value=5, step=1)
    restricciones = st.text_input("¿Tienes alguna alergia o restricción alimentaria?")
    
    submit_button = st.form_submit_button(label="Enviar Confirmación")

    if submit_button:
        if nombre.strip() == "":
            st.error("Por favor, ingresa tu nombre.")
        else:
            # Aquí guardamos los datos en un archivo CSV local (o puedes conectarlo a Google Sheets)
            nuevo_dato = pd.DataFrame([{
                "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Nombre": nombre,
                "Asistencia": asistencia,
                "Acompañantes": acompanantes,
                "Restricciones": restricciones
            }])
            
            # Guardar en un archivo CSV
            try:
                df = pd.read_csv("asistentes.csv")
                df = pd.concat([df, nuevo_dato], ignore_index=True)
            except FileNotFoundError:
                df = nuevo_dato
            df.to_csv("asistentes.csv", index=False)
            
            st.success(f"¡Gracias {nombre}! Tu respuesta ha sido guardada con éxito.")

# (Opcional) Si eres el administrador, puedes ver los invitados ocultando esta sección o protegiéndola
if st.checkbox("Ver lista de confirmados (Admin)"):
    try:
        df_asistentes = pd.read_csv("asistentes.csv")
        st.dataframe(df_asistentes)
    except FileNotFoundError:
        st.info("Aún no hay confirmaciones registradas.")