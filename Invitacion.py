import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Boda de Ismael & Elizabeth", 
    page_icon="💍", 
    layout="centered"
)

# Estilo visual avanzado con CSS (Romántico y Elegante)
st.markdown("""
    <style>
    .main {
        background-color: #faf9f6;
    }
    h1, h2, h3 {
        color: #8c7853;
        font-family: 'Georgia', serif;
        text-align: center;
    }
    .stButton>button {
        background-color: #d4af37;
        color: white;
        border-radius: 20px;
        width: 100%;
        font-weight: bold;
        border: none;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #c19b2e;
        color: white;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado Principal
st.markdown("<h1>💍 ¡Nos Casamos! 💍</h1>", unsafe_allow_html=True)
st.write("### Ismael & Elizabeth")
st.markdown("<p style='text-align: center; color: #555;'>Tenemos el honor de invitarte a celebrar el día más importante de nuestras vidas.</p>", unsafe_allow_html=True)

st.markdown("---")

# Cuenta Regresiva
st.subheader("⏳ Cuenta Regresiva")
fecha_boda = datetime(2026, 12, 18, 19, 0, 0)
tiempo_restante = fecha_boda - datetime.now()

if tiempo_restante.days > 0:
    st.markdown(f"<h3 style='color: #d4af37;'>¡Faltan {tiempo_restante.days} días!</h3>", unsafe_allow_html=True)
else:
    st.markdown("<h3 style='color: #d4af37;'>¡L llegó el gran día!</h3>", unsafe_allow_html=True)

st.markdown("---")

# Detalles del Evento
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📅 Fecha</h3>
        <p>18 de Diciembre de 2026</p>
        <p>Recepción: 19:00 hrs</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>📍 Lugar</h3>
        <p><b>Salón Los Girasoles</b></p>
        <p>Culiacán, Sinaloa</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Itinerario del Día
st.subheader("✨ Itinerario")
st.markdown("""
* **17:00 hrs** - Ceremonia Religiosa / Civil
* **18:30 hrs** - Cóctel de Bienvenida
* **19:30 hrs** - Banquete y Brindis
* **21:00 hrs** - ¡A bailar!
""")

st.markdown("---")

# Mesa de Regalos / Código de Vestimenta
st.subheader("💡 Notas Importantes")
st.info("👗 **Código de Vestimenta:** Rigurosa etiqueta / Formal (Evitar colores blanco o marfil).")
st.success("🎁 **Mesa de Regalos:** Tu presencia es nuestro mejor regalo, pero si deseas tener un detalle con nosotros, puedes consultar nuestra mesa en [Liverpool / Código: 123456] o lluvia de sobres.")

st.markdown("---")

# Formulario de Confirmación (RSVP)
st.subheader("💌 Confirma tu Asistencia")
st.write("Por favor confirma antes del **15 de Noviembre de 2026**.")

with st.form("rsvp_form"):
    nombre = st.text_input("Nombre completo:")
    asistencia = st.radio("¿Asistirás?", ["Sí, ahí estaré", "No podré asistir"])
    acompanantes = st.number_input("Número de acompañantes:", min_value=0, max_value=5, step=1)
    restricciones = st.text_input("¿Tienes alguna alergia o restricción alimentaria?")
    
    submit_button = st.form_submit_button(label="Enviar Confirmación")

    if submit_button:
        if nombre.strip() == "":
            st.error("Por favor, ingresa tu nombre completo.")
        else:
            nuevo_dato = pd.DataFrame([{
                "Fecha_Registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Nombre": nombre,
                "Asistencia": asistencia,
                "Acompañantes": acompanantes,
                "Restricciones": restricciones
            }])
            
            try:
                df = pd.read_csv("asistentes.csv")
                df = pd.concat([df, nuevo_dato], ignore_index=True)
            except FileNotFoundError:
                df = nuevo_dato
            df.to_csv("asistentes.csv", index=False)
            
            st.success(f"¡Muchas gracias, {nombre}! Tu respuesta ha sido guardada con éxito.")

st.markdown("---")

# Panel de Administración (Oculto para invitados comunes, controlado por un PIN opcional)
with st.expander("🔐 Panel de Administración"):
    pin = st.text_input("Ingresa el PIN de administrador:", type="password")
    if pin == "2026": # Puedes cambiar tu PIN aquí
        try:
            df_asistentes = pd.read_csv("asistentes.csv")
            st.dataframe(df_asistentes)
            
            # Botón para descargar el excel/csv de invitados
            csv = df_asistentes.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Descargar lista en CSV",
                data=csv,
                file_name='lista_boda.csv',
                mime='text/csv',
            )
        except FileNotFoundError:
            st.info("Aún no hay confirmaciones registradas.")
    elif pin != "":
        st.error("PIN incorrecto.")
