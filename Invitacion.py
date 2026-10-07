import base64
import re
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

def cargar_svg(path_archivo):
    with open(path_archivo, "r", encoding="utf-8") as f:
        return f.read()


# Renderizar en la pantalla
###svg_contenido = cargar_svg("Frame 48.svg")  # pon aquí el nombre de tu archivo

#st.markdown(
#    f"""
#<div style="text-align: center; margin-top: 10px; margin-bottom: 20px;">
#{svg_contenido}
#</div>
#""",
#    unsafe_allow_html=True,
#)


# Carga de imágenes locales
fondo_b64 = get_image_base64("Fondo_5_brillo.jpg")

# Estilo visual avanzado con CSS (TEXTOS EN COLOR NEGRO / OSCURO) Y EFECTO DE PÉTALOS CAYENDO
/* --- ESTILOS DE TARJETA Y SUS TEXTOS --- */
.card {
    background: rgba(0, 0, 0, 0.20) !important;
    backdrop-filter: blur(6px) !important;
    -webkit-backdrop-filter: blur(6px) !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    padding: 24px 20px !important;
    border-radius: 12px !important;
    margin-bottom: 20px !important;
    text-align: center !important;
}

/* Título principal de la tarjeta (Ej. Ceremonia Religiosa) */
.card-title {
    color: #EEE955 !important; /* Amarillo / Dorado destacado */
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 2.2rem !important;
    font-weight: 800 !important;
    margin-bottom: 12px !important;
    display: block !important;
}

/* Fecha destacada */
.card-date {
    color: #FFFFFF !important; /* Blanco destacado */
    font-family: 'Montserrat', sans-serif !important;
    font-size: 1.2rem !important;
    font-weight: 700 !important;
    margin-bottom: 14px !important;
    display: block !important;
}

/* Detalles (Hora, Lugar, Ciudad) */
.card-text {
    color: #E0E0E0 !important; /* Blanco suave / Gris claro */
    font-family: 'Montserrat', sans-serif !important;
    font-size: 1rem !important;
    margin-bottom: 8px !important;
    display: block !important;
}

/* Etiquetas resaltadas (Ej. Hora:, Lugar:) */
.card-label {
    color: #C5A059 !important; /* Tono dorado elegante */
    font-weight: 700 !important;
}

/* Enlaces (Ej. Ubicación de la Misa) */
.card-link {
    color: #FFFFFF !important;
    text-decoration: underline !important;
    font-weight: 600 !important;
    font-family: 'Montserrat', sans-serif !important;
    font-size: 1.05rem !important;
    display: inline-block !important;
    margin-top: 10px !important;
}

# ----------------- ENCABEZADO -----------------
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<h1>Ismael & Elizabeth</h1>", unsafe_allow_html=True)
st.markdown(
    "<h4 style='text-align: center; font-size: 1.1rem; font-style: italic; color: #FFFFFF !important; font-weight: 600;'>¡NOS CASAMOS!</h4>",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="card">
    <p style="font-size: 1rem; line-height: 1.6; margin: 0; color: #000000 !important;">
        !NOS CASAMOS! Hay momentos en la vida que son inolvidables, y compartirlos con las personas que más queremos los hace aún más especiales. 
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
        <h3>🎉 Fiesta</h3>
        <p style="font-size: 1.1rem; font-weight: 600; color: #000000 !important;">18 de Diciembre de 2026</p>
        <p style="color: #1a1a1a !important;"><b>Hora:</b> 19:00 hrs</p>
        <p style="color: #1a1a1a !important;"><b>Lugar:</b> Salón Metropolitan: Piso 1</p>
        <p style="font-size: 0.9rem; color: #333333 !important;">Culiacán, Sinaloa</p>
        <a href="https://www.google.com/maps/place/Sal%C3%B3n+Metropolitan/@24.7943447,-107.4047708,16.67z/data=!4m6!3m5!1s0x86bcd0beee3643ff:0xf86e169e6767365b!8m2!3d24.7953022!4d-107.4048423!16s%2Fg%2F1tg7sg73?entry=ttu&g_ep=EgoyMDI2MDgxMi4wIKXMDSoASAFQAw%3D%3D" target="_blank" style="text-decoration: none;">
            <p style="color: #000000 !important; font-weight: 700; margin-top: 10px; text-decoration: underline;">🗺️ Ubicación de la Fiesta</p>
        </a>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ----------------- NOTAS IMPORTANTES -----------------
st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown("<h2>💡 Información Importante</h2>", unsafe_allow_html=True)

st.markdown(
    """
<div class="card">
    <h3 style="font-size: 1.3rem;">🎁 Mesa de Regalos</h3>
    <p style="color: #000000 !important;">Tu presencia es nuestro mejor regalo. Si deseas tener un detalle adicional:</p>
    <p style="color: #000000 !important;">
        • <b>Liverpool:</b>
        <a href="https://mesaderegalos.liverpool.com.mx/milistaderegalos/60030339" target="_blank" style="color: #1a0dab; font-weight: 600; text-decoration: underline;">Ver mesa de regalos aquí</a>
    </p>
    <p style="color: #000000 !important;">• Contaremos con lluvia de sobres en la recepción.</p>
</div>
""",
    unsafe_allow_html=True,
)

# ----------------- GALERÍA DE FOTOS LOCALES -----------------
st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown("<h2>📸 Nuestra Historia</h2>", unsafe_allow_html=True)

g_col1, g_col2, g_col3 = st.columns(3)
with g_col1:
    try:
        st.image("Kirina.jpeg", use_container_width=True)
    except Exception:
        st.write("📷 Foto 1")
with g_col2:
    try:
        st.image("foto2.jpg", use_container_width=True)
    except Exception:
        st.write("📷 Foto 2")
with g_col3:
    try:
        st.image("foto3.jpg", use_container_width=True)
    except Exception:
        st.write("📷 Foto 3")


# ----------------- FORMULARIO RSVP -----------------

st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown("<h2>💌 Confirmación de Asistencia</h2>", unsafe_allow_html=True)

st.markdown(
    """
<div class="card">
    <p style="color: #000000 !important;">Por favor confirma tu asistencia antes del <b>15 de Noviembre de 2026</b>.</p>
</div>
""",
    unsafe_allow_html=True,
)

# Creamos un contenedor reactivo que mantendrá la tarjeta transparente
with st.container():
    # 1. Nombre principal
    nombre = st.text_input("Nombre completo del invitado(a) principal:")

    # 2. Teléfono celular
    telefono = st.text_input(
        "Teléfono celular (10 dígitos):",
        max_chars=10,
        placeholder="Ej. 6671234567",
    )

    # 3. Número de acompañantes
    acompanantes = st.number_input(
        "Número de acompañantes adicionales:",
        min_value=0,
        max_value=5,
        step=1,
        value=0,
    )

    # 4. Campos dinámicos para nombres de acompañantes
    nombres_acompanantes = []
    if acompanantes > 0:
        st.markdown(
            "<p style='color: #FFFFFF !important; font-weight: 600; margin-top: 15px; margin-bottom: 5px;'>Nombres de tus acompañantes:</p>",
            unsafe_allow_html=True,
        )
        for i in range(int(acompanantes)):
            nombre_acomp = st.text_input(
                f"Nombre completo del acompañante {i+1}:", key=f"acomp_{i}"
            )
            nombres_acompanantes.append(nombre_acomp)

    # 5. Asistencia y Restricciones
    asistencia = st.radio(
        "¿Nos acompañarás?",
        [
            "Sí, ahí estaré con mucho gusto 🥂",
            "Lamentablemente no podré asistir ❤️",
        ],
    )

    restricciones = st.text_input("Alergias o restricciones alimentarias:")

    # Botón normal
    enviar = st.button("Enviar Confirmación ✨", use_container_width=True)

    if enviar:
        nombre_clean = nombre.strip()
        telefono_clean = re.sub(r"\D", "", telefono.strip())  # Solo dígitos
        lista_nombres_acomp = [
            n.strip() for n in nombres_acompanantes if n.strip() != ""
        ]

        # Validaciones
        if not nombre_clean:
            st.error(
                "Por favor, ingresa tu nombre completo antes de enviar la confirmación."
            )

        elif len(telefono_clean) != 10:
            st.error(
                "Por favor, ingresa un número de teléfono celular válido a 10 dígitos (ej. 6671234567)."
            )

        elif acompanantes > 0 and len(lista_nombres_acomp) < acompanantes:
            st.error(
                "Por favor, completa los nombres de todos tus acompañantes."
            )

        else:
            try:
                df = pd.read_csv("asistentes.csv")
            except FileNotFoundError:
                df = pd.DataFrame(
                    columns=[
                        "Fecha_Registro",
                        "Nombre",
                        "Telefono",
                        "Asistencia",
                        "Acompañantes",
                        "Nombres_Acompañantes",
                        "Restricciones",
                        "Mesa",
                    ]
                )

            # Asegurar que la columna 'Telefono' exista si el CSV ya se había creado previamente sin ella
            if "Telefono" not in df.columns:
                df["Telefono"] = ""

            cadena_acompanantes = (
                ", ".join(lista_nombres_acomp)
                if lista_nombres_acomp
                else "Ninguno"
            )

            nuevo_dato = pd.DataFrame([
                {
                    "Fecha_Registro": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                    "Nombre": nombre_clean,
                    "Telefono": telefono_clean,
                    "Asistencia": asistencia,
                    "Acompañantes": acompanantes,
                    "Nombres_Acompañantes": cadena_acompanantes,
                    "Restricciones": restricciones,
                    "Mesa": "Por asignar",
                }
            ])

            df = pd.concat([df, nuevo_dato], ignore_index=True)
            df.to_csv("asistentes.csv", index=False)

            st.balloons()
            st.markdown(
                f"""
                <div style="
                    background-color: #FFFFFF; 
                    padding: 16px; 
                    border-radius: 8px; 
                    border: 1px solid #E0E0E0;
                    box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
                    margin: 10px 0px;">
                    <span style="font-size: 18px; margin-right: 8px;">✅</span>
                    <span style="color: #262730; font-weight: 500;">
                        ¡Muchas gracias <strong>{nombre_clean}</strong>! Hemos recibido tu confirmación.
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

# ----------------- BUSCADOR DE MESA PARA INVITADOS -----------------
st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown("<h2>🍽️ Consulta tu Mesa</h2>", unsafe_allow_html=True)

st.markdown(
    """
<div class="card">
    <p style="color: #000000 !important;">Ingresa tu nombre tal como lo registraste para consultar tu mesa asignada.</p>
</div>
""",
    unsafe_allow_html=True,
)

nombre_buscar = st.text_input("Escribe tu nombre:", key="buscar_mesa")

if nombre_buscar.strip() != "":
    try:
        df_mesas = pd.read_csv("asistentes.csv")
        if "Mesa" in df_mesas.columns:
            resultado = df_mesas[
                df_mesas["Nombre"].str.contains(
                    nombre_buscar, case=False, na=False
                )
            ]

            if not resultado.empty:
                for idx, row in resultado.iterrows():
                    mesa_asignada = row.get("Mesa", "Aún no asignada")
                    if (
                        pd.isna(mesa_asignada)
                        or str(mesa_asignada).strip() == ""
                    ):
                        mesa_asignada = "Por asignar"

                    st.info(
                        f"👤 **{row['Nombre']}**: Tu mesa asignada es la **Mesa"
                        f" {mesa_asignada}** 🥂"
                    )
            else:
                st.warning(
                    "No encontramos ninguna confirmación con ese nombre."
                )
        else:
            st.info("La asignación de mesas aún no está disponible.")
    except FileNotFoundError:
        st.info("Aún no hay confirmaciones registradas.")
        
# ----------------- BUSCADOR DE MESA PARA INVITADOS -----------------
st.markdown('<div class="divider">❦ ❦ ❦</div>', unsafe_allow_html=True)
st.markdown("<h2>🍽️ Consulta tu Mesa</h2>", unsafe_allow_html=True)

st.markdown(
    """
<div class="card">
    <p style="color: #000000 !important;">Ingresa tu nombre tal como lo registraste para consultar tu mesa asignada.</p>
</div>
""",
    unsafe_allow_html=True,
)

nombre_buscar = st.text_input("Escribe tu nombre:", key="buscar_mesa")

if nombre_buscar.strip() != "":
    try:
        df_mesas = pd.read_csv("asistentes.csv")
        if "Mesa" in df_mesas.columns:
            resultado = df_mesas[
                df_mesas["Nombre"].str.contains(
                    nombre_buscar, case=False, na=False
                )
            ]

            if not resultado.empty:
                for idx, row in resultado.iterrows():
                    mesa_asignada = row.get("Mesa", "Aún no asignada")
                    if (
                        pd.isna(mesa_asignada)
                        or str(mesa_asignada).strip() == ""
                    ):
                        mesa_asignada = "Por asignar"

                    st.info(
                        f"👤 **{row['Nombre']}**: Tu mesa asignada es la **Mesa"
                        f" {mesa_asignada}** 🥂"
                    )
            else:
                st.warning(
                    "No encontramos ninguna confirmación con ese nombre."
                )
        else:
            st.info("La asignación de mesas aún no está disponible.")
    except FileNotFoundError:
        st.info("Aún no hay confirmaciones registradas.")

# ----------------- PANEL DE ADMINISTRACIÓN -----------------
st.markdown("<br><br>", unsafe_allow_html=True)
with st.expander("🔐 Panel de Administración (Novios)"):
    pin = st.text_input("Ingresa el PIN de administrador:", type="password")
    if pin == "1812":
        try:
            df_asistentes = pd.read_csv("asistentes.csv")

            if "Mesa" not in df_asistentes.columns:
                df_asistentes["Mesa"] = "Por asignar"

            st.dataframe(df_asistentes)
        except FileNotFoundError:
            st.info("No hay lista de asistentes creada aún.")
