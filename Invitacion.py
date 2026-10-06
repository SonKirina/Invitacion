import base64
import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="Invitación de Boda",
    page_icon="💍",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# Función para convertir imágenes locales a Base64 para usarlas en CSS
def cargar_imagen_base64(ruta_archivo):
    try:
        with open(ruta_archivo, "rb") as archivo:
            return f"data:image/jpeg;base64,{base64.b64encode(archivo.read()).decode()}"
    except FileNotFoundError:
        # Retorna una cadena vacía o una imagen por defecto si no se encuentra el archivo
        return ""


# Cargar imagen de fondo (reemplaza 'fondo.jpg' por la ruta de tu imagen)
fondo_b64 = cargar_imagen_base64("fondo.jpg")

# CSS personalizado optimizado
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

    /* 1. Estilo base para textos generales */
    p, span, label, b, strong, .stMarkdown p {{
        font-family: 'Montserrat', sans-serif !important;
        color: #000000 !important;
    }}

    /* 2. Estilo para el título principal (h1) */
    h1, div h1, .titulo-principal {{
        color: #FFFFFF !important;
        font-family: 'Cormorant Garamond', serif !important;
        font-weight: 600;
        font-size: 3.5rem !important;
        letter-spacing: 2px;
        text-align: center;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.65);
    }}

    /* 3. Estilo para títulos secundarios (h2 y h3) */
    h2, h3, div h2, div h3 {{
        color: #000000 !important;
        font-family: 'Cormorant Garamond', serif !important;
        text-align: center;
        font-weight: 600;
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
    .petal:nth-child(4) {{ left: 60%; animation-duration: 1s; animation-delay: 1s; }}
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

# Encabezado principal
st.markdown("<h1>NUESTRA BODA</h1>", unsafe_allow_html=True)

# Tarjeta principal: Foto y Nombres
st.markdown(
    """
    <div class="card">
        <img src="https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=600&q=80" class="hero-photo" alt="Novios">
        <h2>Ana & Carlos</h2>
        <p>¡Nos casamos y nos encantaría compartir este día tan especial contigo!</p>
        <div class="countdown-box">Sábado, 15 de Noviembre</div>
    </div>
""",
    unsafe_allow_html=True,
)

# Tarjeta de Detalles del Evento
st.markdown(
    """
    <div class="card">
        <h3>Detalles del Evento</h3>
        <p><b>Misa / Ceremonia:</b> 17:00 hrs</p>
        <p>Parroquia de San Francisco</p>
        <div class="divider">❖</div>
        <p><b>Recepción:</b> 19:30 hrs</p>
        <p>Jardín Las Rosas</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Formulario de Confirmación (RSVP)
with st.container():
    st.markdown(
        """
        <div class="card">
            <h3>Confirmación de Asistencia</h3>
            <p>Por favor, confirma tu asistencia antes del 15 de Octubre.</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    with st.form("rsvp_form"):
        nombre = st.text_input("Nombre completo")
        asistencia = st.radio(
            "¿Nos acompañarás?", ["Sí, ahí estaré 🥂", "Lamentablemente no podré ir 😔"]
        )
        pases = st.number_input("Número de pases", min_value=1, max_value=5, value=1)
        mensaje = st.text_area("Mensaje para los novios (opcional)")

        btn_enviar = st.form_submit_button("Enviar Confirmación")

        if btn_enviar:
            if nombre.strip() != "":
                st.success(
                    f"¡Gracias {nombre}! Hemos recibido tu confirmación correctamente."
                )
            else:
                st.warning("Por favor, ingresa tu nombre antes de enviar.")
