import streamlit as st
import pandas as pd
from datetime import datetime
import base64

# Configuración de la página
st.set_page_config(
    page_title="Boda de Ismael & Elizabeth 💍", 
    page_icon="💍", 
    layout="centered"
)

# Función para convertir imágenes locales a Base64 y usarlas en CSS/HTML
def get_image_base64(file_path):
    try:
        with open(file_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
        return f"data:image/jpeg;base64,{encoded}"
    except FileNotFoundError:
        return ""

# Carga de imágenes locales
fondo_b64 = get_image_base64("Kirina.jpeg")
novios_b64 = get_image_base64("Kirina.jpeg")

# Estilo visual avanzado con CSS
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Montserrat:wght@300;400;500;600&display=swap');

    /* Fondo de pantalla usando la foto local Kirina.jpeg con overlay transparente */
    [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.78), rgba(255, 255, 255, 0.78)), url("{fondo_b64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}

    h1, h2, h3 {{
        color: #6b5b45 !important;
        font-family: 'Cormorant Garamond', serif !important;
        text-align: center;
        font-weight: 600;
    }}

    h1 {{
        font-size: 3rem !important;
        letter-spacing: 2px;
        margin-bottom: 0px !important;
    }}

    p, span, label, div {{
        font-family: 'Montserrat', sans-serif !important;
        color: #4a4a4a;
    }}

    /* Tarjetas estilo cristal (Glassmorphism) */
    .card {{
        background: rgba(255, 255, 255, 0.90);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.06);
        margin-bottom: 25px;
        text-align: center;
    }}

    /* Foto circular principal de los novios */
    .hero-photo {{
        width: 100%;
        max-width: 300px;
        height: 300px;
        object-fit: cover;
        border-radius: 50%;
        border: 5px solid #ffffff;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        display: block;
        margin: 0 auto 20px auto;
    }}

    .countdown-box {{
        background: #8c7853;
        color: white !important;
        padding: 12px 20px;
        border-radius: 30px;
        font-size: 1.2rem;
        font-weight: 600;
        display: inline-block;
        box-shadow: 0 4px 12px rgba(140, 120, 83, 0.3);
    }}

    .stButton>button {{
        background: linear-gradient(135deg, #d4af37 0%, #b89228 100%);
        color: white !important;
        border-radius: 25px;
        width: 100%;
        font-weight: 600;
        border: none;
        padding: 12px;
        font-size: 1rem;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
        transition: all 0.3s ease;
    }}

    .stButton>button:hover {{
        background: linear-gradient(135deg, #b89228 0%, #a07d1c 100%);
        transform: translateY(-2px);
    }}

    .divider {{
        text-align: center;
        margin: 25px 0;
        color: #d4af37;
        font-size: 1.5rem;
    }}
    </style>
""", unsafe_allow_html=True)

# ----------------- ENCABEZADO -----------------
st.markdown("<br>", unsafe_allow_html=True)

# Muestra la foto de novios local
if novios_b64:
    st.markdown(f'<img src="{novios_b64}" class="hero-photo" alt="Ismael & Elizabeth">', unsafe_allow_html=True)
else:
    st.image("Kirina.jpeg", use_container_width=True)

st.markdown("<h1>Ismael & Elizabeth</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1rem; font-style: italic; color: #7a6a53;'>¡NOS CASAMOS!</p>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <p style="font-size: 1rem; line-height: 1.6; margin: 0;">
        Hay momentos en la vida que son inolvidables, y compartirlos con las personas que más queremos los hace aún más especiales. 
        Queremos que seas parte de esta gran celebración.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)

# ----------------- CUENTA REGRESIVA -----------------
st.markdown("<h2>⏳ Cuenta Regresiva</h2>", unsafe_allow_html=True)
fecha_boda = datetime(2026, 12, 18, 14, 0, 0)
tiempo_restante = fecha_boda - datetime.now()

if tiempo_restante.days > 0:
    st.markdown(f"""
    <div style="text-align: center; margin: 20px 0;">
        <span class="countdown-box">¡Faltan {tiempo_restante.days} días para el gran día!</span>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style="text-align: center; margin: 20px 0;">
        <span class="countdown-box">¡Hoy es el gran día! 🎉</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)

# ----------------- DETALLES DEL EVENTO (MISA Y FIESTA) -----------------
st.markdown("<h2>✨ Dónde & Cuándo</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>⛪ Ceremonia Religiosa</h3>
        <p style="font-size: 1.1rem; font-weight: 600; color: #8c7853;">18 de Diciembre de 2026</p>
        <p><b>Hora:</b> 14:00 hrs</p>
        <p><b>Lugar:</b> Parroquia San Gabriel</p>
        <p style="font-size: 0.9rem; color: #777;">Culiacán, Sinaloa</p>
        <a href="https://www.google.com/maps/place/Parroquia+de+San+Gabriel/@24.8192977,-107.3993506,16.46z/data=!4m6!3m5!1s0x86bcda0885555555:0xe6e996b30a535946!8m2!3d24.8181119!4d-107.4001306!16s%2Fg%2F11cs9_hkf0?entry=ttu&g_ep=EgoyMDI2MDgxMi4wIKXMDSoASAFQAw%3D%3D" "Culiacán Rosales, Sin." target="_blank" style="text-decoration: none;">
            <p style="color: #d4af37; font-weight: 600; margin-top: 10px;">🗺️ Ubicación de la Misa</p>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🎉 Recepción & Fiesta</h3>
        <p style="font-size: 1.1rem; font-weight: 600; color: #8c7853;">18 de Diciembre de 2026</p>
        <p><b>Hora:</b> 19:00 hrs</p>
        <p><b>Lugar:</b> Salón Metropolitan (Piso 1)</p>
        <p style="font-size: 0.9rem; color: #777;">Culiacán, Sinaloa</p>
        <a href="https://www.google.com/maps/place/Sal%C3%B3n+Metropolitan/@24.7950842,-107.4044858,19z/data=!4m6!3m5!1s0x86bcd0beee3643ff:0xf86e169e6767365b!8m2!3d24.7953022!4d-107.4048423!16s%2Fg%2F1tg7sg73?entry=ttu&g_ep=EgoyMDI2MDgxMi4wIKXMDSoASAFQAw%3D%3D" "Culiacán Rosales, Sin." target="_blank" style="text-decoration: none;">
            <p style="color: #d4af37; font-weight: 600; margin-top: 10px;">🗺️ Ubicación de la Fiesta</p>
        </a>
    </div>
    """, unsafe_allow_html=True)

# ----------------- ITINERARIO -----------------
st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown("<h2>📋 Itinerario</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="card" style="text-align: left; padding-left: 30px;">
    <p><b>14:00 hrs</b> — 💍 Misa / Ceremonia Religiosa</p>
    <p><b>19:00 hrs</b> — 🥂 Recepción y Cóctel de Bienvenida</p>
    <p><b>20:30 hrs</b> — 🍽️ Banquete y Brindis</p>
    <p><b>21:30 hrs</b> — 💃 ¡Apertura de Pista y Fiesta!</p>
</div>
""", unsafe_allow_html=True)

# ----------------- GALERÍA DE FOTOS LOCALES -----------------
st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown("<h2>📸 Nuestra Historia</h2>", unsafe_allow_html=True)

g_col1, g_col2, g_col3 = st.columns(3)
with g_col1:
    try:
        st.image("Kirina.jpeg", use_container_width=True)
    except:
        st.write("📷 Foto 1")
with g_col2:
    try:
        st.image("foto2.jpg", use_container_width=True)
    except:
        st.write("📷 Foto 2")
with g_col3:
    try:
        st.image("foto3.jpg", use_container_width=True)
    except:
        st.write("📷 Foto 3")

# ----------------- NOTAS IMPORTANTES -----------------
st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown("<h2>💡 Información Importante</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3 style="font-size: 1.3rem;">👗 Código de Vestimenta</h3>
    <p><b>Formal / Rigurosa Etiqueta</b></p>
    <p style="font-size: 0.9rem; color: #777;">Les pedimos amablemente reservar los tonos blanco, marfil y crema para la novia.</p>
    <hr style="border: 0; border-top: 1px solid #eee; margin: 15px 0;">
    <h3 style="font-size: 1.3rem;">🎁 Mesa de Regalos</h3>
    <p>Tu presencia es nuestro mejor regalo. Si deseas tener un detalle adicional:</p>
    <p>• <b>Liverpool:</b> Evento No. 123456</p>
    <p>• Contaremos con lluvia de sobres en la recepción.</p>
</div>
""", unsafe_allow_html=True)

# ----------------- FORMULARIO RSVP -----------------
st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown("<h2>💌 Confirmación de Asistencia</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <p>Por favor confirma tu asistencia antes del <b>15 de Noviembre de 2026</b>.</p>
</div>
""", unsafe_allow_html=True)

with st.form("rsvp_form"):
    nombre = st.text_input("Nombre completo del invitado(a):")
    asistencia = st.radio("¿Nos acompañarás?", ["Sí, ahí estaré con mucho gusto 🥂", "Lamentablemente no podré asistir ❤️"])
    acompanantes = st.number_input("Número de acompañantes adicionales:", min_value=0, max_value=5, step=1)
    restricciones = st.text_input("Alergias o restricciones alimentarias:")
    
    submit_button = st.form_submit_button(label="Enviar Confirmación ✨")

    if submit_button:
        if nombre.strip() == "":
            st.error("Por favor, ingresa tu nombre completo antes de enviar.")
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
            
            st.balloons()
            st.success(f"¡Muchas gracias {nombre}! Hemos recibido tu confirmación.")

# ----------------- PANEL DE ADMINISTRACIÓN -----------------
st.markdown("<br><br>", unsafe_allow_html=True)
with st.expander("🔐 Panel de Administración (Novios)"):
    pin = st.text_input("Ingresa el PIN de administrador:", type="password")
    if pin == "2026":
        try:
            df_asistentes = pd.read_csv("asistentes.csv")
            st.subheader("Lista de Confirmados")
            st.dataframe(df_asistentes, use_container_width=True)
            
            csv = df_asistentes.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Descargar lista en CSV",
                data=csv,
                file_name='asistentes_boda_Ismael_Elizabeth.csv',
                mime='text/csv',
            )
        except FileNotFoundError:
            st.info("Aún no hay confirmaciones registradas.")
    elif pin != "":
        st.error("PIN incorrecto.")
