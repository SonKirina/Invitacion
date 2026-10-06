import base64
from datetime import datetime
import pandas as pd
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Boda de Ismael & Elizabeth 💍",
    page_icon="💍",
    layout="centered",
)


# Función para convertir imágenes locales a Base64
def get_image_base64(file_path):
    try:
        with open(file_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
        return f"data:image/jpeg;base64,{encoded}"
    except FileNotFoundError:
        return ""


# Carga de imágenes locales
fondo_b64 = get_image_base64("Fondo_5.jpg")

# Estilo visual avanzado con CSS (TEXTOS EN COLOR NEGRO / OSCURO) Y EFECTO DE PÉTALOS CAYENDO
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Montserrat:wght@300;400;500;600&display=swap');

    /* Fondo de pantalla directo */
    [data-testid="stAppViewContainer"] {{
        background-image: url({fondo_b64});
        background-size: cover;
        background-position: center 35%;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}

    /* Títulos principales (Negro Intenso) */
    h1, h2, h3 {{
        color: #000000 !important;
        font-family: 'Cormorant Garamond', serif !important;
        text-align: center;
        font-weight: 700 !important;
    }}

    h1 {{
        font-size: 3rem !important;
        letter-spacing: 2px;
        margin-bottom: 0px !important;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8); /* Sombra clara para lectura fácil */
    }}

    /* Párrafos, etiquetas y texto en general (Negro Carbón) */
    p, span, label, div, b, strong {{
        font-family: 'Montserrat', sans-serif !important;
        color: #1a1a1a !important;
    }}

    /* Tarjetas estilo cristal */
    .card {{
        background: rgba(255, 255, 255, 0.92);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 0, 0, 0.15);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
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
        background: #1a1a1a;
        color: #ffffff !important;
        padding: 12px 20px;
        border-radius: 30px;
        font-size: 1.2rem;
        font-weight: 600;
        display: inline-block;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }}

    .stButton>button {{
        background: #000000;
        color: white !important;
        border-radius: 25px;
        width: 100%;
        font-weight: 600;
        border: none;
        padding: 12px;
        font-size: 1rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }}

    .stButton>button:hover {{
        background: #333333;
        transform: translateY(-2px);
    }}

    .divider {{
        text-align: center;
        margin: 25px 0;
        color: #000000;
        font-size: 1.5rem;
    }}

    /* --- ANIMACIÓN DE PÉTALOS CAYENDO --- */
    .petal {{
        position: fixed;
        top: -10px;
        pointer-events: none;
        z-index: 9999;
        animation: fall linear infinite;
        font-size: 1.2rem;
        user-select: none;
    }}

    @keyframes fall {{
        0% {{
            opacity: 1;
            top: -10px;
            transform: translateX(0) rotate(0deg);
        }}
        100% {{
            opacity: 0.2;
            top: 100vh;
            transform: translateX(100px) rotate(360deg);
        }}
    }}

    .petal:nth-child(1) {{ left: 10%; animation-duration: 8s; animation-delay: 0s; }}
    .petal:nth-child(2) {{ left: 25%; animation-duration: 10s; animation-delay: 2s; }}
    .petal:nth-child(3) {{ left: 40%; animation-duration: 7s; animation-delay: 4s; }}
    .petal:nth-child(4) {{ left: 60%; animation-duration: 9s; animation-delay: 1s; }}
    .petal:nth-child(5) {{ left: 75%; animation-duration: 11s; animation-delay: 3s; }}
    .petal:nth-child(6) {{ left: 90%; animation-duration: 8s; animation-delay: 5s; }}
    </style>

    <!-- Contenedor de pétalos -->
    <div class="petal">🌸</div>
    <div class="petal">🌸</div>
    <div class="petal">🌸</div>
    <div class="petal">🌸</div>
    <div class="petal">🌸</div>
    <div class="petal">🌸</div>
""",
    unsafe_allow_html=True,
)

# ----------------- ENCABEZADO -----------------
st.markdown("<br>", unsafe_allow_html=True)


st.markdown("<h1>Ismael & Elizabeth</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 1.1rem; font-style: italic;"
    " color: #000000 !important; font-weight: 600;'>¡NOS CASAMOS!</p>",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="card">
    <p style="font-size: 1rem; line-height: 1.6; margin: 0; color: #000000 !important;">
        Hay momentos en la vida que son inolvidables, y compartirlos con las personas que más queremos los hace aún más especiales. 
        Queremos que seas parte de esta gran celebración.
    </p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)

# ----------------- CUENTA REGRESIVA -----------------
st.markdown("<h2>⏳ Cuenta Regresiva</h2>", unsafe_allow_html=True)
fecha_boda = datetime(2026, 12, 18, 14, 0, 0)
tiempo_restante = fecha_boda - datetime.now()

if tiempo_restante.days > 0:
    st.markdown(
        f"""
    <div style="text-align: center; margin: 20px 0;">
        <span class="countdown-box">¡Faltan {tiempo_restante.days} días para el gran día!</span>
    </div>
    """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
    <div style="text-align: center; margin: 20px 0;">
        <span class="countdown-box">¡Hoy es el gran día! 🎉</span>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)

# ----------------- DETALLES DEL EVENTO (MISA Y FIESTA) -----------------
st.markdown("<h2>✨ Dónde & Cuándo</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
    <div class="card">
        <h3>⛪ Ceremonia Religiosa</h3>
        <p style="font-size: 1.1rem; font-weight: 600; color: #000000 !important;">18 de Diciembre de 2026</p>
        <p style="color: #1a1a1a !important;"><b>Hora:</b> 14:00 hrs</p>
        <p style="color: #1a1a1a !important;"><b>Lugar:</b> Parroquia San Gabriel</p>
        <p style="font-size: 0.9rem; color: #333333 !important;">Culiacán, Sinaloa</p>
        <a href="https://www.google.com/maps/place/Parroquia+de+San+Gabriel/@24.8175739,-107.3979117,16.5z/data=!4m6!3m5!1s0x86bcda0885555555:0xe6e996b30a535946!8m2!3d24.8181119!4d-107.4001306!16s%2Fg%2F11cs9_hkf0?entry=ttu&g_ep=EgoyMDI2MDgxMi4wIKXMDSoASAFQAw%3D%3D" target="_blank" style="text-decoration: none;">
            <p style="color: #000000 !important; font-weight: 700; margin-top: 10px; text-decoration: underline;">🗺️ Ubicación de la Misa</p>
        </a>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
    <div class="card">
        <h3>🎉 Recepción & Fiesta</h3>
        <p style="font-size: 1.1rem; font-weight: 600; color: #000000 !important;">18 de Diciembre de 2026</p>
        <p style="color: #1a1a1a !important;"><b>Hora:</b> 19:00 hrs</p>
        <p style="color: #1a1a1a !important;"><b>Lugar:</b> Salón Metropolitan: Piso 1</p>
        <p style="font-size: 0.9rem; color: #33333
