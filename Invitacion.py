import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Boda de María & Carlos 💍", 
    page_icon="💍", 
    layout="centered"
)
st.image("kirina.jpeg", caption="María & Carlos")
# URL de la imagen de fondo (puedes cambiar esta URL por la de tu foto favorita o una local)


# Estilo visual avanzado con CSS (Romántico, Elegante y Adaptable)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Montserrat:wght@300;400;500;600&display=swap');

    /* Fondo principal con overlay oscuro suave para legibilidad */
    [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(255, 255, 255, 0.75), rgba(255, 255, 255, 0.75)), url("{URL_FONDO}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* Ocultar encabezado por defecto de Streamlit */
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}

    /* Fuentes globales */
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

    /* Tarjetas tipo cristal elegante (Glassmorphism) */
    .card {{
        background: rgba(255, 255, 255, 0.88);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.06);
        margin-bottom: 25px;
        text-align: center;
    }}

    /* Foto de perfil / portada de pareja */
    .hero-photo {{
        width: 100%;
        max-width: 320px;
        height: 320px;
        object-fit: cover;
        border-radius: 50%;
        border: 5px solid #ffffff;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        display: block;
        margin: 0 auto 20px auto;
    }}

    /* Estilo para contadores de fecha */
    .countdown-box {{
        background: #8c7853;
        color: white !important;
        padding: 12px 20px;
        border-radius: 30px;
        font-size: 1.3rem;
        font-weight: 600;
        display: inline-block;
        box-shadow: 0 4px 12px rgba(140, 120, 83, 0.3);
    }}

    /* Botones personalizados */
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

    /* Separadores decorativos */
    .divider {{
        text-align: center;
        margin: 25px 0;
        color: #d4af37;
        font-size: 1.5rem;
    }}
    </style>
""", unsafe_allow_html=True)

# ----------------- HERO SECTION -----------------
st.markdown("<br>", unsafe_allow_html=True)

# Foto Principal de los Novios
st.markdown(f'<img src="{URL_FOTO_PAREJA}" class="hero-photo" alt="María & Carlos">', unsafe_allow_html=True)

st.markdown("<h1>María & Carlos</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1rem; font-style: italic; color: #7a6a53;'>¡NOS CASAMOS!</p>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <p style="font-size: 1rem; line-height: 1.6; margin: 0;">
        Hay momentos en la vida que son inolvidables, y compartirlos con las personas que más queremos los hace inolvidables. 
        Queremos que seas parte de esta gran celebración.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)

# ----------------- CUENTA REGRESIVA -----------------
st.markdown("<h2>⏳ Cuenta Regresiva</h2>", unsafe_allow_html=True)
fecha_boda = datetime(2026, 12, 15, 17, 0, 0)
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

# ----------------- DETALLES DEL EVENTO -----------------
st.markdown("<h2>✨ Dónde & Cuándo</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📅 Ceremonia & Fiesta</h3>
        <p style="font-size: 1.1rem; font-weight: 600; color: #8c7853;">15 de Diciembre de 2026</p>
        <p>Recepción: 17:00 hrs</p>
        <p>Misa: 18:00 hrs</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>📍 Lugar</h3>
        <p style="font-size: 1.1rem; font-weight: 600; color: #8c7853;">Salón Los Girasoles</p>
        <p>Culiacán, Sinaloa</p>
        <a href="https://maps.google.com" target="_blank" style="text-decoration: none;">
            <p style="color: #d4af37; font-weight: 600; margin-top: 10px;">🗺️ Ver en Google Maps</p>
        </a>
    </div>
    """, unsafe_allow_html=True)

# ----------------- ITINERARIO -----------------
st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown("<h2>📋 Itinerario</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="card" style="text-align: left; padding-left: 40px;">
    <p><b>17:00 hrs</b> — 🥂 Recepción y Cóctel de Bienvenida</p>
    <p><b>18:00 hrs</b> — 💍 Ceremonia Religiosa / Civil</p>
    <p><b>19:30 hrs</b> — 🍽️ Banquete Real y Brindis</p>
    <p><b>21:00 hrs</b> — 💃 ¡Apertura de Pista y Fiesta!</p>
</div>
""", unsafe_allow_html=True)

# ----------------- GALERÍA DE FOTOS -----------------
st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown("<h2>📸 Nuestra Historia</h2>", unsafe_allow_html=True)

g_col1, g_col2, g_col3 = st.columns(3)
with g_col1:
    st.image("https://images.unsplash.com/photo-1511285560929-80b456fea0bc?q=80&w=400&auto=format&fit=crop", use_container_width=True, caption="Nuestra Promesa")
with g_col2:
    st.image("https://images.unsplash.com/photo-1522673607200-164d1b6ce486?q=80&w=400&auto=format&fit=crop", use_container_width=True, caption="Juntos Siempre")
with g_col3:
    st.image("https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?q=80&w=400&auto=format&fit=crop", use_container_width=True, caption="El Comienzo")

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
                label="📥 Descargar lista en CSV / Excel",
                data=csv,
                file_name='asistentes_boda_maria_carlos.csv',
                mime='text/csv',
            )
        except FileNotFoundError:
            st.info("Aún no hay confirmaciones registradas.")
    elif pin != "":
        st.error("PIN incorrecto.")
```eof

He mejorado el diseño de la invitación en Streamlit. Estas son las principales novedades implementadas:

1. **Foto de fondo con capa protectora**: Agregué una foto de fondo romántica fija que no distrae la lectura gracias a un degradado semi-transparente.
2. **Foto principal circular y Galería**: Incluí una foto central para los novios y un bloque de galería con 3 imágenes para mostrar momentos juntos.
3. **Tipografía elegante**: Se cargaron las fuentes de Google Fonts (*Cormorant Garamond* para títulos y *Montserrat* para textos).
4. **Tarjetas de Cristal (Glassmorphism)**: Todo el contenido está agrupado en tarjetas blancas translúcidas con bordes dorados suaves y sombras elegantes.
5. **Enlace a Google Maps e Itinerario visual**: Añadí enlace interactivo para la ubicación y un diseño ordenado para los tiempos del evento.

Para usar tus propias fotos, únicamente reemplaza los enlaces `URL_FONDO`, `URL_FOTO_PAREJA` o las fotos de la galería por las URLs de tus imágenes o por imágenes alojadas en tu carpeta local. ¡Espero que les encante!
