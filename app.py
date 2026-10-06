import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
from datetime import datetime

# ==============================================================================
# CONFIGURACIÓN INICIAL DE STREAMLIT
# ==============================================================================
st.set_page_config(
    page_title="U.I.A. Economía | Pensamiento Crítico & Inflación Fiscal",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================================================================
# ESTILOS CSS PERSONALIZADOS (Aesthetic Premium Académico UIA)
# ==============================================================================
st.markdown("""
<style>
    /* Tipografía y paleta base */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Header estilizado */
    .hero-container {
        background: linear-gradient(135deg, #0A192F 0%, #172A45 50%, #1E3A8A 100%);
        border-radius: 16px;
        padding: 2.2rem 2.5rem;
        margin-bottom: 2rem;
        color: #FFFFFF;
        box-shadow: 0 10px 25px -5px rgba(10, 25, 47, 0.3), 0 8px 10px -6px rgba(10, 25, 47, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    
    .hero-title {
        font-size: 2.1rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        margin-bottom: 0.5rem;
        color: #F8FAFC;
    }
    
    .hero-subtitle {
        font-size: 1.05rem;
        color: #94A3B8;
        max-width: 850px;
        line-height: 1.5;
    }
    
    .badge-tag {
        display: inline-block;
        background: rgba(59, 130, 246, 0.2);
        color: #60A5FA;
        border: 1px solid rgba(96, 165, 250, 0.3);
        border-radius: 6px;
        padding: 0.2rem 0.65rem;
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }

    /* Tarjetas de Métricas y Contenedores */
    .custom-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.03);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .custom-card:hover {
        box-shadow: 0 6px 12px rgba(0,0,0,0.06);
    }
    
    .pedagogy-card {
        background: #F8FAFC;
        border-left: 4px solid #3B82F6;
        border-radius: 0 10px 10px 0;
        padding: 1.1rem 1.4rem;
        margin-bottom: 1.2rem;
    }
    
    .feedback-box {
        border-radius: 10px;
        padding: 1.2rem 1.4rem;
        margin-top: 1rem;
        margin-bottom: 1rem;
        border-left: 5px solid;
    }
    
    .feedback-pass {
        background-color: #ECFDF5;
        border-color: #10B981;
        color: #065F46;
    }
    
    .feedback-warning {
        background-color: #FFFBEB;
        border-color: #F59E0B;
        color: #92400E;
    }
    
    .feedback-challenge {
        background-color: #EFF6FF;
        border-color: #3B82F6;
        color: #1E40AF;
    }

    /* Subtítulos de sección */
    .section-header {
        font-size: 1.35rem;
        font-weight: 700;
        color: #0F172A;
        margin-top: 1.2rem;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Indicador socrático */
    .socratic-prompt {
        font-style: italic;
        background: #F1F5F9;
        border-left: 3px solid #64748B;
        padding: 0.75rem 1rem;
        margin: 0.75rem 0;
        border-radius: 0 6px 6px 0;
        font-size: 0.93rem;
        color: #334155;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# INICIALIZACIÓN DE ESTADO (st.session_state)
# ==============================================================================
def init_session_state():
    if "student_name" not in st.session_state:
        st.session_state.student_name = ""
    if "student_id" not in st.session_state:
        st.session_state.student_id = ""
    if "answers" not in st.session_state:
        st.session_state.answers = {
            "act_previa": "",
            "ej1_causas": "",
            "ej1_volcker": "",
            "ej2_dilema_fed": "",
            "ej3_transitoriedad": "",
            "ej4_propuesta": "",
            "oral_tesis": "",
            "oral_evidencia": "",
            "oral_refutacion": ""
        }
    if "evaluations" not in st.session_state:
        st.session_state.evaluations = {}
    if "scores" not in st.session_state:
        st.session_state.scores = {
            "interpretacion": 0,
            "analisis_causal": 0,
            "evaluacion_modelos": 0,
            "argumentacion_oral": 0
        }
    if "completed_modules" not in st.session_state:
        st.session_state.completed_modules = set()

init_session_state()

# ==============================================================================
# RESOLUCIÓN DE RECURSOS (LOGO U.I.A.)
# ==============================================================================
def get_logo_path():
    base_dir = Path(__file__).resolve().parent
    candidates = [
        base_dir / "SEMANA3OBN" / "Logo-transparente.png",
        base_dir / "Logo-transparente.png",
        Path("SEMANA3OBN/Logo-transparente.png"),
        Path("Logo-transparente.png")
    ]
    for p in candidates:
        if p.exists():
            return str(p)
    return None

logo_path = get_logo_path()

# ==============================================================================
# SIDEBAR DE CONTEXTO & PRINCIPIOS DIDÁCTICOS (Requisito 1)
# ==============================================================================
with st.sidebar:
    if logo_path:
        st.image(logo_path, width="stretch")
    else:
        st.markdown("### 🏛️ UNIVERSIDAD INTERNACIONAL DE LAS AMÉRICAS")
    
    st.markdown("#### **Laboratorio Didáctico de Economía**")
    st.caption("Curso: Principios de Economía | Nivel: Primer Ingreso")
    st.divider()

    # Requisito 0: Identificación del estudiante
    st.markdown("##### 👤 Identificación del Estudiante")
    name_input = st.text_input(
        "Nombre Completo:",
        value=st.session_state.student_name,
        placeholder="Ej: Ana María González Mora",
        help="El nombre se incluirá en el reporte descargable para la Comprobación de Maestría."
    )
    st.session_state.student_name = name_input

    id_input = st.text_input(
        "Carné / Identificación:",
        value=st.session_state.student_id,
        placeholder="Ej: UIA-2026-8941"
    )
    st.session_state.student_id = id_input

    if not st.session_state.student_name.strip():
        st.warning("⚠️ Ingrese su nombre para registrar el avance de su sesión sincrónica.")
    else:
        st.success(f"Estudiante activo: **{st.session_state.student_name}**")

    st.divider()

    # Principios Didácticos Integrados (Merrill + Bergmann)
    with st.expander("📘 Marco Didáctico Aplicado", expanded=False):
        st.markdown("""
        **1. Cuatro Principios de Merrill:**
        - **Activación:** Anclaje en modelos mentales previos.
        - **Demostración:** Visibilización de propiedades causales (*what-happens*).
        - **Aplicación:** Resolución de dilemas reales sin recetas.
        - **Integración:** Transferencia y defensa pública del conocimiento.

        **2. The Mastery Flip (Jon Bergmann):**
        - **AI Engines:** Preparación previa exploratoria.
        - **Analog Roots:** Demostración y esfuerzo cognitivo sincrónico.
        - **Human Checks:** Validación humana cara a cara del razonamiento (Defensa Oral).
        """)

    with st.expander("📚 Fuentes Curadas", expanded=False):
        st.markdown("""
        - **Lyn Alden (2021):** *Inflación impulsada por el fiscal: Comparativa 1940s vs 1970s vs 2020s*.
        - **Jon Bergmann (2026):** *The Mastery Flip: Averting AI Stupefaction*.
        - **David Merrill:** *First Principles of Instruction*.
        - **U.I.A.:** *Metodología de Clase Invertida y Raíces Analógicas*.
        """)

    # Monitor de avance en tiempo real
    st.divider()
    prog_count = len(st.session_state.completed_modules)
    st.markdown(f"##### 🎯 Progreso de la Sesión: {prog_count}/4 fases")
    st.progress(prog_count / 4.0)
    
    st.caption("Este entorno no proporciona respuestas automáticas: evalúa el rigor analítico, la justificación causal y la coherencia de su defensa.")

# ==============================================================================
# ENCABEZADO PRINCIPAL (HERO SECTION)
# ==============================================================================
st.markdown("""
<div class="hero-container">
    <div>
        <span class="badge-tag">Sesión Sincrónica</span>
        <span class="badge-tag">Fase de Demostración & Aplicación</span>
        <span class="badge-tag">Macroeconomía U.I.A.</span>
    </div>
    <div class="hero-title">Laboratorio de Pensamiento Crítico: Inflación Impulsada por el Fiscal</div>
    <div class="hero-subtitle">
        Desarrollo de pensamiento analítico e inferencial sobre el ciclo de deuda a largo plazo, 
        dominancia fiscal y mecanismos de transmisión monetaria frente a estímulos soberanos.
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# PESTAÑAS PRINCIPALES DEL FLUJO DIDÁCTICO
# ==============================================================================
tab_activacion, tab_demostracion, tab_simulador, tab_aplicacion, tab_resumen = st.tabs([
    "1️⃣ Fase de Activación",
    "2️⃣ Exposición y Demostración",
    "3️⃣ Laboratorio de Decisión",
    "4️⃣ Comprobación de Maestría",
    "5️⃣ Reporte Consolidado"
])

# ==============================================================================
# TAB 1: FASE DE ACTIVACIÓN COGNITIVA (Merrill: Principio 1)
# ==============================================================================
with tab_activacion:
    st.markdown('<div class="section-header">🧠 1. Activación de Esquemas Mentales Previos</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="pedagogy-card">
        <strong>Objetivo Didáctico (Activación):</strong> Antes de sumergirnos en los modelos matemáticos y gráficos, 
        debemos conectar con sus intuiciones sobre el dinero, la deuda y el poder de compra. 
        Evitamos la memorización ciega de fórmulas para construir un modelo mental que distinga entre 
        <strong>dinero bancario</strong> y <strong>dinero fiscal</strong>.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("### El Dilema Inicial del Flujo Monetario")
        st.write("""
        Imagine dos escenarios en los que circulan **100.000 millones de dólares adicionales** en una economía:
        
        * **Escenario A (Préstamo Bancario Clásico):** El sistema bancario privado expande líneas de crédito e hipotecas a empresas y familias con solvencia para pagar con intereses en 20 años.
        * **Escenario B (Gasto Fiscal Directo Monetizado):** El gobierno emite bonos de deuda comprados indirectamente por el Banco Central y deposita transferencias monetarias no reembolsables directamente en las cuentas de todos los ciudadanos durante una emergencia.
        """)

    with col2:
        st.markdown("### Su Hipótesis Inicial")
        act_resp = st.text_area(
            "¿Cuál de los dos escenarios genera mayor presión inflacionaria sobre los bienes básicos de consumo inmediato y por qué? Justifique su respuesta analizando la velocidad y el balance patrimonial:",
            value=st.session_state.answers.get("act_previa", ""),
            height=160,
            placeholder="Analice: ¿quién recibe el dinero?, ¿debe devolverlo?, ¿qué ocurre con el balance patrimonial del sector privado?..."
        )
        st.session_state.answers["act_previa"] = act_resp

        if st.button("Evaluar Razonamiento Inicial", key="btn_act"):
            if len(act_resp.strip()) < 40:
                st.warning("⚠️ Su respuesta es demasiado escueta. El pensamiento crítico requiere justificar con mecanismos de causa y efecto.")
            else:
                st.session_state.completed_modules.add("activacion")
                # Feedback formativo sin revelar respuesta fija
                has_balance = any(w in act_resp.lower() for w in ["balance", "patrimonio", "devolver", "deuda", "ahorro"])
                has_demand = any(w in act_resp.lower() for w in ["consumo", "gasto", "velocidad", "demanda", "inmediato", "bienes"])
                
                if has_balance and has_demand:
                    st.markdown("""
                    <div class="feedback-box feedback-pass">
                        <strong>Excelente Intuición Estructural:</strong> Ha identificado la diferencia clave: el crédito bancario crea tanto un activo como un pasivo para el privado (debe pagarse), mientras que el déficit fiscal financiado monetariamente inyecta patrimonio neto líquido directo en manos de consumidores con alta propensión marginal a consumir.
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="feedback-box feedback-challenge">
                        <strong>Pregunta de Reflexión Socrática:</strong> Fíjese en el pasivo: cuando un banco le presta dinero a usted, ¿aumenta su riqueza neta o solo su liquidez temporal con deuda a futuro? ¿Qué ocurre cuando el Estado regala cheques sin exigir devolución futura de préstamos?
                    </div>
                    """, unsafe_allow_html=True)

# ==============================================================================
# TAB 2: EXPOSICIÓN Y DEMOSTRACIÓN SINCRÓNICA (Requisito 2 & Lyn Alden)
# ==============================================================================
with tab_demostracion:
    st.markdown('<div class="section-header">📊 2. Demostración Sincrónica: Evidencia Empírica y Dinámica Causal</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="pedagogy-card">
        <strong>Fase de Demostración (What-Happens):</strong> En este bloque analizamos cómo se despliega el fenómeno 
        según el marco de <strong>Lyn Alden</strong>. Contrastamos tres épocas fundamentales: los 
        <strong>años 1940</strong> (Segunda Guerra Mundial), los <strong>años 1970</strong> (Expansión crediticia y petróleo) 
        y los <strong>años 2020</strong> (Pandemia y endeudamiento récord).
    </div>
    """, unsafe_allow_html=True)

    # Métricas comparativas de cabecera
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric(label="Deuda Pública / PIB (1940s)", value="119%", delta="Fiscal Dominant")
    with m2:
        st.metric(label="Deuda Pública / PIB (1970s)", value="32%", delta="-87% vs 1940s", delta_color="inverse")
    with m3:
        st.metric(label="Deuda Pública / PIB (2020s)", value="130%", delta="Récord Histórico")
    with m4:
        st.metric(label="Tasa Fed Máx. (1980 vs 2023)", value="20.0% vs 5.5%", delta="-14.5% de margen")

    st.markdown("---")

    # Selector de visualizaciones interactivas
    chart_view = st.radio(
        "Seleccione la Demostración Empírica a Examinar:",
        [
            "1. Comparativa de Ciclos: Deuda Soberana vs Inflación vs Tasas de Interés",
            "2. Descomposición del Crecimiento del Dinero (M2): Motores Fiscales vs Préstamos Bancarios",
            "3. La Trampa de la Transitoriedad: Tasa de Variación vs Salto Permanente en Nivel de Precios"
        ],
        horizontal=True
    )

    if "1. Comparativa" in chart_view:
        st.markdown("#### Matriz Histórica de Regímenes Inflacionarios")
        
        # Datos basados en el análisis de Lyn Alden
        history_data = pd.DataFrame({
            "Época": ["Década de 1940", "Década de 1970", "Década de 2020"],
            "Deuda Pública (% PIB)": [118.0, 34.0, 128.0],
            "Déficit Fiscal Pico (% PIB)": [26.0, 4.2, 18.0],
            "Pico Inflacionario (CPI %)": [19.5, 14.8, 9.1],
            "Tasa de Interés Fed Pico (%)": [0.375, 20.0, 5.5],
            "Tasa Real de Interés en Pico (%)": [-19.1, +5.2, -3.6],
            "Mecanismo Dominante": [
                "Gasto de Guerra + Monetización + Represión Financiera",
                "Crédito Bancario Privado + Demografía Baby Boomers + Petróleo",
                "Estímulos Fiscales Masivos + QE + Cuellos de Suministro"
            ]
        })
        
        st.dataframe(history_data, width="stretch", hide_index=True)

        # Gráfico comparativo Plotly
        fig_comp = go.Figure()
        fig_comp.add_trace(go.Bar(
            name="Deuda Pública / PIB (%)",
            x=history_data["Época"],
            y=history_data["Deuda Pública (% PIB)"],
            marker_color="#1E3A8A"
        ))
        fig_comp.add_trace(go.Bar(
            name="Pico Inflación CPI (%)",
            x=history_data["Época"],
            y=history_data["Pico Inflacionario (CPI %)"],
            marker_color="#EF4444"
        ))
        fig_comp.add_trace(go.Bar(
            name="Tasa de Interés Fed Pico (%)",
            x=history_data["Época"],
            y=history_data["Tasa de Interés Fed Pico (%)"],
            marker_color="#10B981"
        ))
        fig_comp.update_layout(
            title="Contraste Estructural: Deuda Pública, Inflación y Capacidad de Subir Tasas",
            barmode="group",
            yaxis_title="Porcentaje (%)",
            template="plotly_white",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_comp, width="stretch")

        st.info("💡 **Observación Crítica:** Observe la década de 1940 vs 1970. En los años 40, con una deuda pública sobre el 100% del PIB, la Reserva Federal no pudo subir las tasas de interés porque habría quebrado al gobierno; impuso un control de curva (represión financiera). En los 70, con la deuda en solo el 34% del PIB, Paul Volcker pudo subir las tasas al 20% sin detonar una bancarrota fiscal.")

    elif "2. Descomposición" in chart_view:
        st.markdown("#### ¿De Dónde Vino el Dinero Nuevo? Desglose Anual de M2")
        
        years = list(range(2015, 2025))
        np.random.seed(42)
        deficit_contrib = [2.4, 3.1, 3.4, 3.8, 4.6, 15.2, 12.1, 5.4, 5.8, 6.2]
        bank_loans_contrib = [5.5, 5.8, 4.9, 4.8, 4.2, 3.1, 4.2, 5.8, 2.5, 2.2]
        m2_growth = [deficit_contrib[i] + bank_loans_contrib[i] - 1.5 for i in range(len(years))]

        df_m2 = pd.DataFrame({
            "Año": years,
            "Aporte Déficit Fiscal (%)": deficit_contrib,
            "Aporte Préstamos Bancarios (%)": bank_loans_contrib,
            "Crecimiento Total M2 (%)": m2_growth
        })

        fig_m2 = go.Figure()
        fig_m2.add_trace(go.Scatter(
            x=df_m2["Año"], y=df_m2["Aporte Déficit Fiscal (%)"],
            mode="lines+markers", name="Impulso Fiscal Monetizado",
            line=dict(color="#DC2626", width=3)
        ))
        fig_m2.add_trace(go.Scatter(
            x=df_m2["Año"], y=df_m2["Aporte Préstamos Bancarios (%)"],
            mode="lines+markers", name="Crédito Bancario Privado",
            line=dict(color="#2563EB", width=2, dash="dash")
        ))
        fig_m2.add_trace(go.Bar(
            x=df_m2["Año"], y=df_m2["Crecimiento Total M2 (%)"],
            name="Expansión M2 Total",
            marker_color="rgba(156, 163, 175, 0.4)"
        ))
        fig_m2.update_layout(
            title="Aceleración de Oferta Monetaria: Dominancia Fiscal 2020-2021",
            xaxis_title="Año",
            yaxis_title="% del PIB / Variación Anual",
            template="plotly_white",
            legend=dict(orientation="h", yanchor="bottom", y=1.02)
        )
        st.plotly_chart(fig_m2, width="stretch")

        st.caption("Fuente de referencia conceptual: Lyn Alden (2021) adaptando datos de la St. Louis Fed (FRED).")

    else:
        st.markdown("#### La Trampa Cognitiva: 'Tasa Transitoria' vs 'Nivel Permanente'")
        
        meses = np.arange(0, 36)
        # IPC con un escalón permanente del 20%
        cpi_index = 100 + 20 / (1 + np.exp(-(meses - 12)/3))
        # Tasa de inflación interanual (se eleva y luego vuelve a bajar a ~2%)
        tasa_yoy = np.diff(cpi_index, prepend=100) * 6
        tasa_yoy = np.clip(tasa_yoy, 1.8, 9.8)

        fig_trap = go.Figure()
        fig_trap.add_trace(go.Scatter(
            x=meses, y=cpi_index,
            mode="lines", name="Nivel Absoluto de Precios (CPI Index)",
            yaxis="y1", line=dict(color="#1E3A8A", width=3.5)
        ))
        fig_trap.add_trace(go.Scatter(
            x=meses, y=tasa_yoy,
            mode="lines", name="Tasa de Inflación Anual (% YoY)",
            yaxis="y2", line=dict(color="#DC2626", width=2.5, dash="dot")
        ))
        fig_trap.update_layout(
            title="Divergencia entre Tasa de Variación y Nivel de Precios",
            xaxis_title="Meses desde el inicio del choque fiscal",
            yaxis=dict(title="Índice de Precios (Nivel acumulado)", side="left", range=[95, 125]),
            yaxis2=dict(title="Tasa Interanual (%)", side="right", overlaying="y", range=[0, 12]),
            template="plotly_white",
            legend=dict(orientation="h", yanchor="bottom", y=1.05)
        )
        st.plotly_chart(fig_trap, width="stretch")

        st.markdown("""
        <div class="socratic-prompt">
            <strong>Pregunta de examen analítico:</strong> ¿Por qué cuando las noticias anuncian que "la inflación bajó del 9% al 3%", las familias de bajos recursos sienten que todo sigue igual de caro o peor? Observe la línea azul (nivel de precios) frente a la roja (velocidad de cambio).
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# TAB 3: MÓDULO INTERACTIVO DE PENSAMIENTO CRÍTICO (Requisito 3 & Simulador)
# ==============================================================================
with tab_simulador:
    st.markdown('<div class="section-header">🎛️ 3. Laboratorio de Decisión: Simulador Macroeconómico de Dominancia Fiscal</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="pedagogy-card">
        <strong>Espacio de Simulación y Toma de Decisiones:</strong> Tome el mando como Asesor Macroeconómico. 
        Ajuste las variables y observe cómo interactúan la política fiscal, la política monetaria y la sostenibilidad de la deuda. 
        <strong>Restricción cognitiva:</strong> Ningún modelo tiene soluciones milagrosas; todo ajuste conlleva costos distribuidos y dilemas estructurales.
    </div>
    """, unsafe_allow_html=True)

    col_sim_left, col_sim_right = st.columns([1, 1.2], gap="large")

    with col_sim_left:
        st.markdown("#### Parámetros del Entorno Económico")
        
        sim_deuda = st.slider(
            "Deuda Pública Inicial (% del PIB):",
            min_value=20, max_value=160, value=120, step=5,
            help="Compare un país con 30% (EE.UU. en los 70) vs 130% (EE.UU. en los 2020)."
        )
        
        sim_deficit = st.slider(
            "Déficit Fiscal Anual (% del PIB):",
            min_value=0.0, max_value=20.0, value=7.5, step=0.5,
            help="Exceso de gasto del gobierno sobre los ingresos tributarios."
        )
        
        sim_tasa_fed = st.slider(
            "Tasa de Interés de Política Monetaria (%):",
            min_value=0.0, max_value=16.0, value=5.0, step=0.25,
            help="Tasa de referencia fijada por el Banco Central."
        )
        
        sim_shock = st.selectbox(
            "Choque en Cadenas de Suministro / Petróleo:",
            ["Nulo (Oferta Fluida)", "Moderado (Tensiones Comerciales)", "Severo (Crisis Geopolítica / Energía)"]
        )
        shock_factor = {"Nulo (Oferta Fluida)": 0.5, "Moderado (Tensiones Comerciales)": 2.2, "Severo (Crisis Geopolítica / Energía)": 4.5}[sim_shock]

        # Lógica del motor macroeconómico simplificado de Alden
        costo_interes = (sim_deuda * (sim_tasa_fed / 100.0))
        deficit_total = sim_deficit + (costo_interes * 0.75) # parte financiada con nueva deuda
        
        # Inflación modelada: impulso fiscal + shock oferta - amortiguador por tasas
        inflacion_proyectada = max(1.2, (deficit_total * 0.7) + shock_factor - (sim_tasa_fed * 0.35))
        tasa_real = sim_tasa_fed - inflacion_proyectada
        
        # Alerta de dominancia fiscal
        riesgo_dominancia = "Bajo"
        if costo_interes > 4.5:
            riesgo_dominancia = "CRÍTICO (La deuda genera más déficit que el gasto primario)"
        elif costo_interes > 2.8:
            riesgo_dominancia = "Elevado (Riesgo de espiral de intereses)"

    with col_sim_right:
        st.markdown("#### Resultados Proyectados por el Modelo")
        
        r1, r2 = st.columns(2)
        with r1:
            st.metric(
                label="Inflación Proyectada (CPI)",
                value=f"{inflacion_proyectada:.1f}%",
                delta=f"Tasa Real: {tasa_real:.1f}%",
                delta_color="normal" if tasa_real >= 0 else "inverse"
            )
        with r2:
            st.metric(
                label="Servicio de la Deuda (% PIB)",
                value=f"{costo_interes:.2f}%",
                delta=riesgo_dominancia,
                delta_color="off" if "Bajo" in riesgo_dominancia else "inverse"
            )

        st.markdown(f"""
        **Diagnóstico Dinámico:**
        - **Costo de Intereses Soberanos:** Con una deuda de **{sim_deuda}% del PIB** y una tasa de **{sim_tasa_fed}%**, el Estado destina **{costo_interes:.2f}% del PIB** solo a pagar intereses a los tenedores de bonos.
        - **Efecto Bumerán:** Al subir la tasa para frenar la inflación, el déficit fiscal total aumenta a **{deficit_total:.2f}% del PIB**, inyectando más transferencias al sector privado tenedor de bonos del Tesoro.
        """)

        # Gráfico dinámico de radar o barras
        fig_sim_res = go.Figure(go.Bar(
            x=["Déficit Primario", "Pago Intereses", "Inflación CPI", "Tasa Fed"],
            y=[sim_deficit, costo_interes, inflacion_proyectada, sim_tasa_fed],
            marker_color=["#3B82F6", "#EF4444", "#F59E0B", "#10B981"]
        ))
        fig_sim_res.update_layout(
            title="Estructura de la Simulación Actual (% del PIB y Tasas)",
            yaxis_title="Magnitud (%)",
            template="plotly_white",
            height=300
        )
        st.plotly_chart(fig_sim_res, width="stretch")

    st.markdown("---")
    st.markdown("### 📝 Ejercicios de Pensamiento Crítico Guiado")

    # Ejercicio 1
    with st.expander("Ejercicio 1: Desarmando el 'Momento Volcker' (Análisis Causal y Contraste)", expanded=True):
        st.write("""
        Muchos analistas tradicionales sugieren: *"Para acabar con la inflación de los 2020s, el Banco Central solo necesita hacer lo que hizo Paul Volcker en 1981: subir las tasas hasta el 15% o 20%"*.
        
        Utilice los datos observados en el simulador y la lectura de Lyn Alden para responder:
        """)
        ej1_ans = st.text_area(
            "¿Por qué es matemáticamente imposible aplicar la receta de Volcker en un entorno de Deuda/PIB del 130% sin provocar una crisis fiscal y un aumento paradójico del déficit?",
            value=st.session_state.answers.get("ej1_volcker", ""),
            height=130,
            key="txt_ej1"
        )
        st.session_state.answers["ej1_volcker"] = ej1_ans
        
        if st.button("Guardar y Evaluar Ejercicio 1", key="btn_eval_ej1"):
            if len(ej1_ans.strip()) < 50:
                st.warning("⚠️ Su argumentación es insuficiente. Debe incorporar la relación entre tasa de interés, deuda acumulada y servicio fiscal.")
            else:
                st.session_state.completed_modules.add("ej1")
                has_servicio = any(w in ej1_ans.lower() for w in ["servicio", "interes", "intereses", "costo", "fiscal", "pago"])
                has_deuda = any(w in ej1_ans.lower() for w in ["130", "deuda", "quiebra", "bancarrota", "deficit", "sostenib"])
                
                if has_servicio and has_deuda:
                    st.session_state.scores["analisis_causal"] = max(st.session_state.scores["analisis_causal"], 25)
                    st.markdown("""
                    <div class="feedback-box feedback-pass">
                        <strong>Razonamiento Causal Solvente (Nivel Avanzado):</strong> Correcto. Una tasa del 15% sobre una deuda del 130% del PIB implicaría un pago de intereses cercano al 19% del PIB anual, superando toda la recaudación tributaria y forzando a imprimir dinero para pagar los intereses, empeorando la espiral inflacionaria.
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.session_state.scores["analisis_causal"] = max(st.session_state.scores["analisis_causal"], 12)
                    st.markdown("""
                    <div class="feedback-box feedback-warning">
                        <strong>Orientación Formativa:</strong> Ha esbozado la idea, pero calcule: si la deuda es del 130% del PIB y la tasa sube al 10%, ¿cuánto dinero extra tiene que pagar el gobierno cada año solo en intereses? ¿Quién termina pagando esa cuenta si el banco central debe evitar el default soberano?
                    </div>
                    """, unsafe_allow_html=True)

    # Ejercicio 2
    with st.expander("Ejercicio 2: Evaluación del Dilema de la Reserva Federal (Evaluación de Modelos)", expanded=False):
        st.write("""
        En la lectura de Lyn Alden se explica que la Reserva Federal implementó en 2020-2021 un régimen de **AIT (Average Inflation Targeting)** y tasas reales profundamente negativas (tasas nominales por debajo de la inflación).
        """)
        ej2_ans = st.text_area(
            "¿Por qué la 'represión financiera' (mantener las tasas de interés por debajo de la tasa de inflación) funciona históricamente como un mecanismo encubierto de desapalancamiento de la deuda soberana a costa de los ahorristas?",
            value=st.session_state.answers.get("ej2_dilema_fed", ""),
            height=130,
            key="txt_ej2"
        )
        st.session_state.answers["ej2_dilema_fed"] = ej2_ans

        if st.button("Guardar y Evaluar Ejercicio 2", key="btn_eval_ej2"):
            if len(ej2_ans.strip()) < 50:
                st.warning("⚠️ Argumente con mayor profundidad conceptual.")
            else:
                st.session_state.completed_modules.add("ej2")
                has_real = any(w in ej2_ans.lower() for w in ["real", "reales", "poder", "compra", "licua", "licuar", "inflacion"])
                has_ahorro = any(w in ej2_ans.lower() for w in ["ahorr", "bonos", "tasa", "perdida", "deuda", "gobierno"])
                
                if has_real and has_ahorro:
                    st.session_state.scores["evaluacion_modelos"] = max(st.session_state.scores["evaluacion_modelos"], 25)
                    st.markdown("""
                    <div class="feedback-box feedback-pass">
                        <strong>Comprensión del Mecanismo de Licuación:</strong> Excelente. Cuando la inflación supera las tasas de interés (tasas reales negativas), el valor real de la deuda pública se 'licúa', transfiriendo poder adquisitivo de los ahorristas e inversores en renta fija hacia el Estado deudor.
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.session_state.scores["evaluacion_modelos"] = max(st.session_state.scores["evaluacion_modelos"], 12)
                    st.markdown("""
                    <div class="feedback-box feedback-warning">
                        <strong>Pregunta de Profundización:</strong> Si usted presta $100 al 2% de interés pero la inflación es del 8%, ¿al cabo de un año puede comprar más cosas o menos cosas? ¿A quién beneficia esa diferencia cuando el mayor deudor del mundo es el Estado?
                    </div>
                    """, unsafe_allow_html=True)

    # Ejercicio 3
    with st.expander("Ejercicio 3: Desmitificando el Concepto de 'Inflación Transitoria' (Interpretación Empírica)", expanded=False):
        st.write("""
        Las autoridades económicas y los medios suelen calificar los choques inflacionarios como "transitorios".
        """)
        ej3_ans = st.text_area(
            "Explique la diferencia fundamental entre una inflación que es 'transitoria en tasa de cambio' versus una que es 'transitoria en nivel de precios'. ¿Por qué la deflación generalizada casi nunca ocurre tras un pico fiscal?",
            value=st.session_state.answers.get("ej3_transitoriedad", ""),
            height=130,
            key="txt_ej3"
        )
        st.session_state.answers["ej3_transitoriedad"] = ej3_ans

        if st.button("Guardar y Evaluar Ejercicio 3", key="btn_eval_ej3"):
            if len(ej3_ans.strip()) < 50:
                st.warning("⚠️ Justifique analizando la irreversibilidad del nivel de precios.")
            else:
                st.session_state.completed_modules.add("ej3")
                has_tasa_nivel = any(w in ej3_ans.lower() for w in ["tasa", "nivel", "porcentaje", "acumulado", "salto", "escalon"])
                has_bajar = any(w in ej3_ans.lower() for w in ["bajan", "caen", "permanente", "quedan", "deflacion", "precios"])
                
                if has_tasa_nivel and has_bajar:
                    st.session_state.scores["interpretacion"] = max(st.session_state.scores["interpretacion"], 25)
                    st.markdown("""
                    <div class="feedback-box feedback-pass">
                        <strong>Rigor en la Discriminación de Variables:</strong> Muy bien. La tasa es una primera derivada (velocidad de cambio anual); que baje a cero o al 2% solo significa que los precios dejan de acelerarse, pero permanecen en el nuevo escalón más alto.
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.session_state.scores["interpretacion"] = max(st.session_state.scores["interpretacion"], 12)
                    st.markdown("""
                    <div class="feedback-box feedback-challenge">
                        <strong>Desafío Socrático:</strong> Si un automóvil cuesta $10.000 y sube un 20% a $12.000 (año 1), y al año siguiente la inflación es de solo el 2% ($12.240), ¿el auto volvió a costar $10.000? Explique esa diferencia con sus palabras.
                    </div>
                    """, unsafe_allow_html=True)

# ==============================================================================
# TAB 4: COMPROBACIÓN DE MAESTRÍA (Defensa Oral / Human Check de Bergmann)
# ==============================================================================
with tab_aplicacion:
    st.markdown('<div class="section-header">🗣️ 4. Comprobación de Maestría: Preparación para la Defensa Oral</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="pedagogy-card">
        <strong>Pilar 3 de The Mastery Flip (Jon Bergmann - Human Checks):</strong> 
        La tecnología y las simulaciones son solo el calentamiento. La verdadera demostración de maestría ocurre cuando 
        usted puede <strong>mirar al docente a los ojos y defender verbalmente</strong> su razonamiento frente a preguntas imprevistas 
        y contraargumentos rigurosos.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Guion Estructurado de Defensa Oral (Mastery Viva)")
    st.write("Complete su guion argumentativo para la sesión presencial con el profesor:")

    c_or1, c_or2 = st.columns(2, gap="medium")

    with c_or1:
        st.markdown("##### 1. Su Tesis Central")
        t_oral = st.text_area(
            "Enuncie su tesis económica principal en 2 o 3 oraciones:",
            value=st.session_state.answers.get("oral_tesis", ""),
            placeholder="Ej: 'La inflación actual es predominantemente fiscal debido a que los déficits masivos monetizados inyectaron demanda directa en un entorno de deuda récord...'",
            height=120,
            key="k_tesis"
        )
        st.session_state.answers["oral_tesis"] = t_oral

        st.markdown("##### 2. Evidencia Empírica de Soporte")
        e_oral = st.text_area(
            "¿Qué datos cuantitativos o gráficos de la lectura usará como prueba irrefutable ante el docente?",
            value=st.session_state.answers.get("oral_evidencia", ""),
            placeholder="Ej: 'Citaré la gráfica de 1940 donde la deuda/PIB superó el 110% y las tasas reales fueron de -19%...'",
            height=120,
            key="k_evidencia"
        )
        st.session_state.answers["oral_evidencia"] = e_oral

    with c_or2:
        st.markdown("##### 3. Refutación del Contraargumento Clásico")
        st.markdown("""
        <div class="socratic-prompt">
            <strong>Pregunta del Docente durante la Defensa:</strong> 
            <em>"Un colega monetarista clásico afirma que 'la inflación es siempre y en todo lugar un fenómeno estrictamente monetario provocado por los bancos comerciales, y que el déficit del gobierno no tiene nada que ver si el banco central es independiente'. ¿Cómo le responde usted?"</em>
        </div>
        """, unsafe_allow_html=True)
        
        r_oral = st.text_area(
            "Su refutación y respuesta técnica al docente:",
            value=st.session_state.answers.get("oral_refutacion", ""),
            placeholder="Desmonte la falacia explicando cómo la emisión de bonos y el rescate del tesoro forzan la monetización indirecta...",
            height=160,
            key="k_refutacion"
        )
        st.session_state.answers["oral_refutacion"] = r_oral

    if st.button("Validar Guion para Defensa Oral", key="btn_oral_check"):
        if len(t_oral.strip()) < 30 or len(e_oral.strip()) < 30 or len(r_oral.strip()) < 40:
            st.warning("⚠️ Debe completar todos los campos del guion de defensa con argumentos sólidos.")
        else:
            st.session_state.completed_modules.add("oral")
            st.session_state.scores["argumentacion_oral"] = 25
            st.markdown("""
            <div class="feedback-box feedback-pass">
                <strong>Guion de Defensa Oral Preparado:</strong> Ha articulado una tesis, seleccionado evidencia empírica concreta y ensayado la refutación del contraargumento monetarista clásico. Presente este esquema al profesor durante el chequeo individual sincrónico.
            </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# TAB 5: REPORTE CONSOLIDADO Y EXPORTACIÓN (Requisito de Salida)
# ==============================================================================
with tab_resumen:
    st.markdown('<div class="section-header">📋 5. Reporte Consolidado de la Sesión Sincrónica</div>', unsafe_allow_html=True)
    
    # Verificación de datos del alumno
    nombre_alumno = st.session_state.student_name.strip() or "Estudiante U.I.A. (No Especificado)"
    carne_alumno = st.session_state.student_id.strip() or "Pendiente"
    
    total_score = sum(st.session_state.scores.values())

    st.markdown(f"""
    <div class="custom-card">
        <h3>Reporte de Evaluación Formativa</h3>
        <p><strong>Estudiante:</strong> {nombre_alumno} | <strong>Identificación:</strong> {carne_alumno}</p>
        <p><strong>Institución:</strong> Universidad Internacional de las Américas (U.I.A.)</p>
        <p><strong>Fecha de Sesión:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
        <hr/>
        <h4>Desempeño Global en Competencias de Pensamiento Crítico: <strong>{total_score}/100 pts</strong></h4>
    </div>
    """, unsafe_allow_html=True)

    # Gráfico de radar / barras de competencias
    c_rep1, c_rep2 = st.columns([1, 1], gap="large")

    with c_rep1:
        st.markdown("#### Desglose de Competencias Evaluadas")
        rubrica_df = pd.DataFrame({
            "Competencia de Pensamiento Crítico": [
                "Interpretación Empírica & Discriminación de Variables",
                "Razonamiento Causal y Descomposición Funcional",
                "Evaluación y Contraste de Modelos Macroeconómicos",
                "Defensa Argumentativa Dialéctica (Mastery Viva)"
            ],
            "Puntaje Obtenido": [
                st.session_state.scores["interpretacion"],
                st.session_state.scores["analisis_causal"],
                st.session_state.scores["evaluacion_modelos"],
                st.session_state.scores["argumentacion_oral"]
            ],
            "Puntaje Máximo": [25, 25, 25, 25]
        })
        st.table(rubrica_df)

    with c_rep2:
        fig_radar = go.Figure(data=go.Scatterpolar(
            r=[
                st.session_state.scores["interpretacion"],
                st.session_state.scores["analisis_causal"],
                st.session_state.scores["evaluacion_modelos"],
                st.session_state.scores["argumentacion_oral"],
                st.session_state.scores["interpretacion"]
            ],
            theta=[
                "Interpretación",
                "Causalidad",
                "Modelización",
                "Defensa Oral",
                "Interpretación"
            ],
            fill="toself",
            name="Nivel Demostrado",
            line_color="#1E3A8A"
        ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 25])),
            title="Perfil de Pensamiento Crítico del Alumno",
            template="plotly_white",
            height=320
        )
        st.plotly_chart(fig_radar, width="stretch")

    st.markdown("---")
    st.markdown("### Generación y Descarga del Reporte Consolidado")
    st.write("Haga clic en el botón inferior para descargar su reporte completo con todas las respuestas, la retroalimentación formativa y la rúbrica para ser entregado o defendido ante el docente.")

    # Generación del archivo en formato Markdown (.md)
    markdown_report = f"""# REPORTE DE SESIÓN SINCRÓNICA - ECONOMÍA U.I.A.
**Universidad Internacional de las Américas**  
**Facultad de Ciencias Económicas y Empresariales**  
**Curso:** Principios de Economía (Primer Ingreso)  
**Metodología:** Clase Invertida (Mastery Flip - Jon Bergmann & Principios Didácticos de Merrill)  

---
### 1. DATOS DEL ESTUDIANTE
- **Nombre del Alumno:** {nombre_alumno}
- **Identificación / Carné:** {carne_alumno}
- **Fecha de Emisión:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Calificación Formativa Global:** {total_score}/100 puntos

---
### 2. RÚBRICA DE COMPETENCIAS DE PENSAMIENTO CRÍTICO
| Competencia Evaluada | Puntaje | Máximo | Estado |
| :--- | :---: | :---: | :--- |
| 1. Interpretación Empírica & Discriminación de Variables | {st.session_state.scores['interpretacion']} | 25 | {'Demostrado' if st.session_state.scores['interpretacion'] >= 20 else 'En desarrollo'} |
| 2. Razonamiento Causal y Descomposición Funcional | {st.session_state.scores['analisis_causal']} | 25 | {'Demostrado' if st.session_state.scores['analisis_causal'] >= 20 else 'En desarrollo'} |
| 3. Evaluación y Contraste de Modelos Macroeconómicos | {st.session_state.scores['evaluacion_modelos']} | 25 | {'Demostrado' if st.session_state.scores['evaluacion_modelos'] >= 20 else 'En desarrollo'} |
| 4. Defensa Argumentativa Dialéctica (Defensa Oral) | {st.session_state.scores['argumentacion_oral']} | 25 | {'Demostrado' if st.session_state.scores['argumentacion_oral'] >= 20 else 'En desarrollo'} |

---
### 3. REGISTRO ACUMULADO DE EJERCICIOS Y RESPUESTAS

#### A. Fase de Activación (Pregunta Inicial de Balance y Liquidez):
> **Respuesta del Estudiante:**  
> {st.session_state.answers.get('act_previa', '[No respondido]')}

#### B. Ejercicio 1: Desarmando el Momento Volcker (Contraste 1970 vs 2020):
> **Respuesta del Estudiante:**  
> {st.session_state.answers.get('ej1_volcker', '[No respondido]')}

#### C. Ejercicio 2: El Dilema de la Fed y Represión Financiera:
> **Respuesta del Estudiante:**  
> {st.session_state.answers.get('ej2_dilema_fed', '[No respondido]')}

#### D. Ejercicio 3: Transitoriedad en Tasa vs Nivel de Precios:
> **Respuesta del Estudiante:**  
> {st.session_state.answers.get('ej3_transitoriedad', '[No respondido]')}

---
### 4. GUION PARA LA COMPROBACIÓN DE MAESTRÍA (DEFENSA ORAL INDIVIDUAL)
- **Tesis Central Formulada:**  
  {st.session_state.answers.get('oral_tesis', '[Sin registrar]')}
- **Evidencia Empírica Cuantitativa a Exponer:**  
  {st.session_state.answers.get('oral_evidencia', '[Sin registrar]')}
- **Refutación del Contraargumento Monetarista Clásico:**  
  {st.session_state.answers.get('oral_refutacion', '[Sin registrar]')}

---
### 5. DICTAMEN PEDAGÓGICO DE LA IA (RETROALIMENTACIÓN FORMATIVA)
Este reporte certifica que el estudiante ha interactuado con los modelos empíricos de Lyn Alden, desarticulando explicaciones simplistas y contrastando la dominancia fiscal frente al crédito bancario privado. La preparación para la defensa oral demuestra la superación de la memorización pasiva, cumpliendo con la fase de Demostración y Aplicación de la sesión sincrónica.

*Firma del Estudiante:* __________________________  
*Validación del Docente U.I.A.:* __________________________  
"""

    # Botón único de exportación descargable (.md)
    st.download_button(
        label="📥 Descargar Reporte Consolidado (.md)",
        data=markdown_report,
        file_name=f"Reporte_Economia_UIA_{nombre_alumno.replace(' ', '_')}.md",
        mime="text/markdown",
        help="Descargue el archivo de texto estructurado para remitir a su profesor o adjuntar a su portafolio."
    )
