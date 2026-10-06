# 🏛️ Laboratorio de Pensamiento Crítico: Inflación Impulsada por el Fiscal
### Universidad Internacional de las Américas (U.I.A.)
**Escuela de Economía | Curso: Principios de Macroeconomía (Primer Ingreso)**  
**Semana 3: Sesión Sincrónica — Demostración, Simulación y Comprobación de Maestría**

---

## 📌 1. Descripción General del Proyecto y Propósito

Este proyecto consiste en una aplicación web interactiva desarrollada con **Python** y **Streamlit**, diseñada bajo un enfoque de **Ingeniería de Software Educativo y Didáctica Universitaria**. Su propósito primordial es transformar la enseñanza tradicional de la macroeconomía —a menudo atrapada en la memorización pasiva o en el cálculo mecánico de fórmulas— en una experiencia inmersiva orientada al desarrollo del **pensamiento crítico, analítico e inferencial** en estudiantes de primer ingreso universitario.

La plataforma aborda el fenómeno de la **inflación macroeconómica moderna**, sometiendo a contraste empírico y causal la hipótesis de la **inflación impulsada por el déficit fiscal** frente a la inflación generada por la expansión del crédito bancario privado, tomando como eje analítico el marco del ciclo de deuda a largo plazo desarrollado por **Lyn Alden**.

### 🎯 Objetivos de Aprendizaje:
1. **Romper la ilusión de aprendizaje:** Desafiar intuiciones superficiales mediante la manipulación directa de variables macroeconómicas.
2. **Diferenciar regímenes estructurales:** Comprender por qué las recetas monetarias convencionales (como la subida drástica de tasas de interés de Paul Volcker en 1981) generan consecuencias radicalmente distintas cuando el nivel de deuda soberana supera el 100% del PIB (dominancia fiscal).
3. **Fomentar la autonomía cognitiva:** Evitar que la IA o el software resuelvan el dilema por el estudiante; la aplicación actúa como un andamiaje socrático que interpela, exige justificación causal y prepara al alumno para la defensa oral cara a cara con el docente.

---

## 🧠 2. Marco Pedagógico Integrado

La arquitectura didáctica de la plataforma se fundamenta en la articulación cruzada de dos paradigmas pedagógicos contemporáneos:

```
                  ┌────────────────────────────────────────────────────────┐
                  │               THE MASTERY FLIP (J. Bergmann)           │
                  └───────────────────────────┬────────────────────────────┘
                                              │
         ┌────────────────────────────────────┼────────────────────────────────────┐
         ▼                                    ▼                                    ▼
   Pilar 1: AI Engines             Pilar 2: Raíces Analógicas            Pilar 3: Human Checks
 (Preparación Asincrónica)           (Sesión Sincrónica)                (Comprobación de Maestría)
         │                                    │                                    │
         │                                    ▼                                    ▼
         │                         Fase de Demostración                   Fase de Aplicación
         │                        (What-Happens de Merrill)              (Defensa Oral Viva)
         │                                    │                                    │
         └────────────────────────────────────┴────────────────────────────────────┘
```

1. **The Mastery Flip (*Jon Bergmann, 2026*):**
   * **AI Engines:** Utilizados antes de la clase para despejar dudas léxicas iniciales.
   * **Analog Roots (Raíces Analógicas):** Reivindicación del esfuerzo cognitivo sincrónico en vivo mediante la observación atenta de modelos, toma de notas analógicas y experimentación guiada.
   * **Human Checks (Comprobación Humana):** La culminación del aprendizaje no es un cuestionario automatizado, sino la validación del razonamiento del estudiante en un diálogo directo e individual (*Mastery Viva*) con el profesor.

2. **Los 4 Principios del Diseño Didáctico (*David Merrill*):**
   * **Activación:** Conexión con modelos mentales previos sobre deuda y dinero antes de introducir conceptos técnicos.
   * **Demostración (*What-happens*):** Visibilización gráfica y matemática de la dinámica causa-efecto de los choques fiscales e inflación.
   * **Aplicación:** Resolución de dilemas complejos y toma de decisiones en un simulador sin respuestas prefabricadas.
   * **Integración:** Transferencia del conocimiento formulando tesis, respondiendo a contraargumentos y sustentando una postura económica propia.

---

## ✨ 3. Características Principales Implementadas

* **👤 Registro e Identificación del Estudiante:**
  * Formulario persistente para registrar el nombre y carné del alumno en `st.session_state`.
  * Barra de progreso dinámico que monitorea el avance a través de las fases didácticas.

* **🏛️ Sidebar Institucional y Contexto Teórico:**
  * Despliegue del logotipo oficial transparente de la U.I.A.
  * Módulo desplegable con la síntesis de los principios de Merrill y Bergmann.
  * Ficha bibliográfica de las fuentes primarias aplicadas.

* **1️⃣ Fase de Activación Cognitiva (Módulo 1):**
  * Problematización socrática que contrasta la inyección de \$100B vía crédito bancario comercial (activo/pasivo privado) versus \$100B vía cheques de estímulo fiscal directo.
  * Evaluador heurístico de hipótesis que detecta el nivel de razonamiento estructural del estudiante sin darle la solución.

* **2️⃣ Bloque de Exposición y Demostración Sincrónica (Módulo 2):**
  * **Tarjetas de métricas históricas:** Deuda/PIB y tasas de la Fed en 1940s, 1970s y 2020s.
  * **Gráfica 1 (Comparativa de Regímenes):** Visualización interactiva de deuda soberana, picos de CPI y techos de tasas de interés.
  * **Gráfica 2 (Descomposición de M2):** Desglose del crecimiento de la masa monetaria discriminando entre motores fiscales y préstamos comerciales.
  * **Gráfica 3 (La Trampa de la Transitoriedad):** Demostración visual de la divergencia entre la *tasa interanual de inflación* (velocidad) y el *nivel acumulado del CPI* (escalón permanente de precios).

* **3️⃣ Laboratorio de Decisión Macroeconómica (Módulo 3):**
  * **Simulador interactivo con controles deslizantes (*sliders*):** Deuda Pública/PIB (20%-160%), Déficit Fiscal Anual (0%-20%), Tasa de Política Monetaria (0%-16%) y Choques de Oferta / Petróleo.
  * **Motor causal en tiempo real:** Proyección dinámica de inflación, costo del servicio de deuda soberana y detector de riesgo de **dominancia fiscal** (efecto bumerán de las subidas de tasas).
  * **Ejercicios formativos guiados:**
    * *Ejercicio 1:* Desarticulación matemática del "Momento Volcker" en entornos de deuda hipertrofiada.
    * *Ejercicio 2:* Análisis de la represión financiera y licuación de deuda a costa del ahorro.
    * *Ejercicio 3:* Discriminación rigurosa entre desaceleración de tasas y deflación real.

* **4️⃣ Comprobación de Maestría — Preparación de Defensa Oral (Módulo 4):**
  * Estructuración del guion individual para la evaluación oral presencial (*Mastery Viva*):
    * Enunciación de la tesis central del estudiante.
    * Selección de evidencia cuantitativa/empírica de respaldo.
    * Refutación dialéctica del contraargumento monetarista clásico.

* **5️⃣ Panel de Resultados y Exportación Consolidada (Módulo 5):**
  * Gráfico de perfil de competencias (radar polar) en 4 dimensiones de pensamiento crítico: Interpretación Empírica, Razonamiento Causal, Modelización Macroeconómica y Argumentación Dialéctica.
  * **Botón único de exportación:** Descarga instantánea de un informe completo en formato Markdown (`.md` / `.txt`) con todas las respuestas, retroalimentaciones formativas y rúbrica para revisión docente.

---

## 🛠️ 4. Requisitos Técnicos

* **Sistema Operativo:** Windows 10/11, macOS o Linux.
* **Versión de Python:** Python **3.10**, **3.11** o **3.12+** (verificado en Python 3.13).
* **Dependencias Principales:**
  * `streamlit >= 1.35.0` (Motor de la aplicación web reactiva)
  * `pandas >= 2.0.0` (Estructuración de datos y tablas comparativas)
  * `numpy >= 1.24.0` (Cálculos dinámicos del simulador macroeconómico)
  * `plotly >= 5.18.0` (Visualizaciones y gráficos interactivos de alta definición)
  * `pillow >= 10.0.0` (Gestión y renderizado del logo institucional)

---

## 📦 5. Instrucciones de Instalación Paso a Paso

### Paso 1: Clonar el Repositorio
Abra una terminal (PowerShell, Bash o CMD) y clone el repositorio:
```bash
git clone https://github.com/randallnunezsancho-netizen/semana3OBN.git
cd semana3OBN
```

### Paso 2: Crear y Activar el Entorno Virtual
Se recomienda aislar las dependencias en un entorno virtual (`venv`):

* **En Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
  *(Si PowerShell restringe scripts, ejecute previamente: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*

* **En macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Paso 3: Instalar las Dependencias
Con el entorno virtual activo, instale las librerías requeridas mediante `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## 🚀 6. Guía de Uso con Ejemplos Básicos

### Ejecutar la Aplicación:
Desde la raíz del proyecto, ejecute:
```powershell
streamlit run app.py
```
La aplicación se abrirá automáticamente en su navegador predeterminado en `http://localhost:8501`.

### Flujo de Trabajo Recomendado para el Estudiante:
1. **Identificación Inicial:** En la barra lateral izquierda, escriba su nombre completo y carné de estudiante.
2. **Fase 1 (Activación):** Lea el dilema del flujo monetario e ingrese su razonamiento sobre balances y consumo. Presione *Evaluar Razonamiento Inicial* para recibir retroalimentación formativa.
3. **Fase 2 (Demostración):** Explore las 3 visualizaciones empíricas. Analice la matriz de datos de Lyn Alden y observe cómo la deuda pública condiciona la respuesta de los bancos centrales.
4. **Fase 3 (Laboratorio de Decisión):**
   * Mueva el deslizador de **Deuda Pública** a `130%` y el de **Tasa de Interés** a `10%`.
   * Observe el indicador de **Servicio de la Deuda**: notará que supera el 10% del PIB, disparando la alerta de **Riesgo Crítico de Dominancia Fiscal**.
   * Responda los 3 ejercicios de pensamiento crítico y haga clic en los botones de evaluación de cada uno.
5. **Fase 4 (Defensa Oral):** Complete su guion de defensa (Tesis, Evidencia Cuantitativa y Refutación al contraargumento monetarista clásico).
6. **Fase 5 (Exportación):** Diríjase a la pestaña *Reporte Consolidado* y presione **📥 Descargar Reporte Consolidado (.md)** para obtener el archivo que entregará a su profesor.

---

## 📁 7. Estructura del Proyecto

```text
semana3OBN/
│
├── app.py                                                # Aplicación principal de Streamlit (raíz)
├── requirements.txt                                      # Lista de dependencias del entorno Python
├── .gitignore                                            # Filtro de exclusión para Git (venv, cachés)
├── README.md                                             # Documentación técnica y pedagógica completa
│
└── SEMANA3OBN/                                           # Carpeta de recursos curriculares y fuentes
    ├── Logo-transparente.png                             # Logo oficial de la Universidad Internacional de las Américas
    ├── funcionalidades.txt                               # Requisitos técnicos y didácticos del proyecto
    ├── 2021 05 - Inflación impulsada por el fiscal.pdf   # Lectura macroeconómica central (Lyn Alden)
    ├── MasteryFlip-A_Guide_to_the_Future_of_Educcation.pdf# Marco pedagógico de Jon Bergmann (Mastery Flip)
    ├── Método de estudio sugerido.pdf                    # Guía didáctica institucional de la U.I.A.
    └── substack.com-Los 4 principios del diseño didáctico.pdf # Principios de David Merrill
```

---

## 📊 8. Interpretación Pedagógica de Resultados

El modelo implementado en la aplicación no califica a través del acierto binario (correcto/incorrecto), sino a través de la **madurez argumentativa y el rigor causal**.

### Rúbrica de Pensamiento Crítico (100 Puntos):

| Dimensión de Pensamiento | Criterio de Logro Superior (20 - 25 pts) | Alerta de Razonamiento Superficial (< 15 pts) |
| :--- | :--- | :--- |
| **1. Interpretación Empírica** | Discrimina entre la tasa de inflación (% de variación) y el nivel acumulado del índice de precios (CPI). Entiende por qué el fin de la inflación no es deflación. | Confunde la reducción de la tasa de inflación con una rebaja en los precios del supermercado. |
| **2. Análisis Causal y Descomposición** | Identifica el canal de transmisión de la deuda soberana: cómo las tasas altas incrementan el gasto en intereses del Estado y agravan el déficit. | Asume de forma ingenua que subir las tasas al 20% siempre cura la inflación sin efectos secundarios en las cuentas públicas. |
| **3. Evaluación de Modelos** | Explica la represión financiera como una tasa de interés real negativa que traslada riqueza del acreedor al deudor soberano para licuar la deuda. | Considera que las decisiones del banco central son puramente técnicas y neutrales para los ahorristas. |
| **4. Argumentación Dialéctica (Oral)** | Sustenta una tesis propia articulada con datos cuantitativos y refuta con solvencia teórica la premisa monetarista reduccionista. | Repite definiciones de memoria sin conectar datos ni formular una postura justificada. |

---

## ⚖️ 9. Licencia y Nota Educativa

### 📄 Licencia
Este proyecto se distribuye bajo la licencia **MIT**, permitiendo su uso, estudio y adaptación con fines académicos e investigativos.

### 🎓 Nota Didáctica Institucional
> **Aviso Importante:** Este software y sus materiales asociados han sido desarrollados **exclusivamente con fines didácticos y pedagógicos** para el curso de Principios de Economía de la **Universidad Internacional de las Américas (U.I.A.)**. 
>
> Los simuladores y proyecciones representan simplificaciones analíticas destinadas a entrenar el discernimiento conceptual y no deben ser interpretados como asesoría financiera, proyecciones econométricas oficiales ni recomendaciones de inversión.
