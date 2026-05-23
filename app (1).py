"""
=============================================================
  El Acero bajo la Lupa — Panel Educativo Interactivo
  Ciencia de Materiales: Aceros al Carbono
=============================================================
  Requisitos:
      pip install streamlit pandas plotly
  Ejecución:
      streamlit run app.py
=============================================================
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# ─────────────────────────────────────────────────────────────
#  CONFIGURACIÓN DE PÁGINA  (debe ser la primera llamada a st)
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="El Acero bajo la Lupa",
    page_icon="assets/favicon.ico" if False else None,
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────
#  ESTILOS GLOBALES (CSS inyectado)
# ─────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ── Google Fonts ── */
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&display=swap');

    /* ── Variables ── */
    :root {
        --navy:      #1a1a2e;
        --navy-mid:  #16213e;
        --navy-deep: #0f3460;
        --gold:      #c8a96e;
        --gold-soft: #e8ddd0;
        --cream:     #faf7f4;
        --border:    #e0d8ce;
        --muted:     #6b6b6b;
        --blue:      #4a90d9;
        --red:       #e05c5c;
        --green:     #5cbf8a;
        --purple:    #9b59b6;
    }

    /* ── Fondo general ── */
    .stApp { background-color: var(--cream); }

    /* ── Eliminar padding superior excesivo de Streamlit ── */
    .block-container { padding-top: 2rem !important; padding-bottom: 4rem !important; }

    /* ── Tipografía base ── */
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        color: var(--navy);
    }

    h1, h2, h3 {
        font-family: 'DM Serif Display', serif !important;
    }

    /* ── Ocultar menú hamburguesa de Streamlit ── */
    #MainMenu, footer, header { visibility: hidden; }

    /* ═══════════════════ HEADER ═══════════════════ */
    .main-header {
        background: linear-gradient(140deg, var(--navy) 0%, var(--navy-mid) 55%, var(--navy-deep) 100%);
        padding: 3.5rem 3rem 3rem;
        border-radius: 18px;
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
    }

    /* Decoración radial de fondo */
    .main-header::before {
        content: '';
        position: absolute;
        top: -40%;
        right: -10%;
        width: 520px;
        height: 520px;
        background: radial-gradient(circle, rgba(200,169,110,.18) 0%, transparent 68%);
        pointer-events: none;
    }

    /* Línea dorada decorativa */
    .accent-bar {
        width: 52px;
        height: 3px;
        background: var(--gold);
        border-radius: 2px;
        margin-bottom: 1.4rem;
    }

    .main-header h1 {
        font-family: 'DM Serif Display', serif !important;
        font-size: 2.8rem;
        color: #fff !important;
        line-height: 1.18;
        margin: 0 0 1rem;
    }

    .main-header .intro-text {
        font-size: 1.05rem;
        color: #c4b49e;
        line-height: 1.75;
        max-width: 720px;
        margin-bottom: 2rem;
    }

    /* ─── Glosario ─── */
    .glossary-label {
        font-size: 0.72rem;
        letter-spacing: .12em;
        text-transform: uppercase;
        color: var(--gold);
        margin-bottom: 1rem;
        font-weight: 600;
    }

    .glossary-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
        gap: .9rem;
    }

    .glossary-card {
        background: rgba(255,255,255,.07);
        border: 1px solid rgba(200,169,110,.25);
        border-radius: 10px;
        padding: 1.1rem 1.3rem;
        backdrop-filter: blur(8px);
        transition: border-color .2s;
    }

    .glossary-card:hover { border-color: rgba(200,169,110,.55); }

    .glossary-card .term {
        font-family: 'DM Serif Display', serif;
        font-size: 1rem;
        color: var(--gold);
        margin-bottom: .35rem;
    }

    .glossary-card .definition {
        font-size: .82rem;
        color: #c4b49e;
        line-height: 1.55;
    }

    /* ═══════════════════ SECCIONES ═══════════════════ */
    .section-header {
        margin-bottom: 1.8rem;
    }

    .section-tag {
        font-size: .7rem;
        font-weight: 600;
        letter-spacing: .14em;
        text-transform: uppercase;
        color: var(--gold);
        margin-bottom: .5rem;
    }

    .section-title {
        font-family: 'DM Serif Display', serif !important;
        font-size: 1.85rem;
        color: var(--navy) !important;
        margin: 0 0 .6rem;
        line-height: 1.2;
    }

    .section-subtitle {
        font-size: .95rem;
        color: var(--muted);
        line-height: 1.65;
        max-width: 740px;
    }

    .section-divider {
        border: none;
        border-top: 1px solid var(--border);
        margin: 3.5rem 0;
    }

    /* ═══════════════════ MÉTRICAS ═══════════════════ */
    .metric-card {
        background: #fff;
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 1.4rem 1rem;
        text-align: center;
        box-shadow: 0 2px 14px rgba(0,0,0,.04);
        height: 100%;
    }

    .metric-value {
        font-family: 'DM Serif Display', serif;
        font-size: 2.2rem;
        color: var(--navy);
        line-height: 1;
        margin-bottom: .4rem;
    }

    .metric-label {
        font-size: .72rem;
        font-weight: 600;
        letter-spacing: .1em;
        text-transform: uppercase;
        color: var(--muted);
    }

    /* ═══════════════════ INSIGHT BOX ═══════════════════ */
    .insight-box {
        background: linear-gradient(135deg, var(--navy), var(--navy-mid));
        border-left: 4px solid var(--gold);
        padding: 1.2rem 1.6rem;
        border-radius: 0 12px 12px 0;
        margin: 1.8rem 0 0;
    }

    .insight-box p {
        color: #e8ddd0;
        margin: 0;
        font-size: .93rem;
        line-height: 1.7;
    }

    .insight-box strong { color: var(--gold); font-weight: 600; }

    /* ═══════════════════ LEYENDA COLORES ═══════════════════ */
    .legend-row {
        display: flex;
        flex-wrap: wrap;
        gap: .6rem;
        margin-bottom: 1rem;
    }

    .legend-chip {
        display: inline-flex;
        align-items: center;
        gap: .4rem;
        font-size: .78rem;
        padding: .25rem .7rem;
        border-radius: 20px;
        background: #fff;
        border: 1px solid var(--border);
        color: var(--navy);
    }

    .chip-dot {
        width: 9px;
        height: 9px;
        border-radius: 50%;
        flex-shrink: 0;
    }

    /* ═══════════════════ TABLAS STREAMLIT ═══════════════════ */
    [data-testid="stDataFrame"] {
        border: 1px solid var(--border) !important;
        border-radius: 12px !important;
        overflow: hidden !important;
    }

    /* ═══════════════════ SELECTOR ═══════════════════ */
    [data-testid="stSelectbox"] label {
        font-size: .82rem !important;
        font-weight: 500 !important;
        letter-spacing: .05em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ─────────────────────────────────────────────────────────────
#  FASE 1 ─ PREPROCESAMIENTO DE DATOS
# ─────────────────────────────────────────────────────────────

@st.cache_data(show_spinner="Cargando y limpiando datos...")
def load_and_preprocess(filepath: str) -> pd.DataFrame:
    """
    Carga el archivo CSV y aplica todas las transformaciones de limpieza
    y enriquecimiento requeridas.

    Pasos aplicados
    ---------------
    1. Lectura con sep=',' y encoding='utf-8'; SAE Grade forzado a str.
    2. Limpieza de Conditions: espacios dobles → sencillo, Title Case.
    3. Cálculo de %C como promedio exacto de C (Min) y C (Max).
    4. Conversión de propiedades mecánicas a float (errores → NaN).
    5. Clasificación de Condition_simple por palabras clave.
    """

    # ── 1. Lectura con tipos explícitos ────────────────────────
    df = pd.read_csv(
        filepath,
        sep=",",
        encoding="utf-8",
        dtype={"SAE Grade": str},   # SAE Grade siempre como texto
    )

    # ── 2. Limpiar columna Conditions ──────────────────────────
    df["Conditions"] = (
        df["Conditions"]
        .str.replace(r"\s{2,}", " ", regex=True)  # colapsar espacios múltiples
        .str.strip()
        .str.title()                                # Formato Title Case
    )

    # ── 3. Calcular %C (promedio exacto C Min / C Max) ─────────
    df["%C"] = (df["C (Min)"] + df["C (Max)"]) / 2

    # ── 4. Convertir propiedades mecánicas a float ─────────────
    mechanical_cols = ["UTS (MPa)", "YS (MPa)", "Hardness (HB)", "Elongation (%)"]
    for col in mechanical_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # ── 5. Clasificación de tratamientos por palabras clave ─────
    def _classify(condition: str) -> str:
        """Agrupa el tratamiento ignorando temperaturas específicas."""
        if pd.isna(condition):
            return "Other"
        c = condition.lower()
        if "anneal" in c:
            return "Annealed"
        if "normaliz" in c:
            return "Normalized"
        if "hot roll" in c or "hot-roll" in c:
            return "Hot Rolled"
        if "cold draw" in c or "cold-draw" in c:
            return "Cold Drawn"
        if "quench" in c:
            return "Quenched"
        return "Other"

    df["Condition_simple"] = df["Conditions"].apply(_classify)

    return df


# ─────────────────────────────────────────────────────────────
#  PALETAS Y CONSTANTES GLOBALES
# ─────────────────────────────────────────────────────────────

# Colores por propiedad mecánica
PROP_COLORS: dict[str, str] = {
    "UTS (MPa)":          "#c8a96e",   # dorado
    "YS (MPa)":           "#4a90d9",   # azul
    "Hardness (HB)":      "#e05c5c",   # rojo
    "Elongation (%) x10": "#5cbf8a",   # verde
}

# Colores por tratamiento
COND_COLORS: dict[str, str] = {
    "Annealed":   "#4a90d9",
    "Normalized": "#5cbf8a",
    "Hot Rolled": "#c8a96e",
    "Cold Drawn": "#e05c5c",
    "Quenched":   "#9b59b6",
    "Other":      "#95a5a6",
}

# Config de estilo Plotly reutilizable
PLOTLY_LAYOUT: dict = dict(
    plot_bgcolor="#ffffff",
    paper_bgcolor="#ffffff",
    font=dict(family="DM Sans, sans-serif", size=12, color="#1a1a2e"),
    margin=dict(l=10, r=10, t=48, b=10),
)


# ─────────────────────────────────────────────────────────────
#  FASE 2 ─ SECCIONES DE LA INTERFAZ
# ─────────────────────────────────────────────────────────────

def render_header() -> None:
    """Encabezado principal + miniglosario educativo."""

    st.markdown(
        """
        <div class="main-header">
            <div class="accent-bar"></div>
            <h1>El Acero bajo la Lupa</h1>
            <p class="intro-text">
                El acero es uno de los materiales más usados del mundo, pero ¿sabías que
                añadir un poco más de carbono o calentar el metal puede cambiar completamente
                su comportamiento? En este panel explorarás esas relaciones con datos reales,
                sin necesitar ningún conocimiento previo de ingeniería.
            </p>
            <div class="glossary-label">Glosario rapido — lo que miden los datos</div>
            <div class="glossary-grid">
                <div class="glossary-card">
                    <div class="term">Resistencia maxima (UTS)</div>
                    <div class="definition">
                        La fuerza más grande que puede soportar el acero justo antes de romperse.
                        Se expresa en Megapascales (MPa). Mayor UTS = más difícil de romper.
                    </div>
                </div>
                <div class="glossary-card">
                    <div class="term">Limite elastico (YS)</div>
                    <div class="definition">
                        La fuerza a partir de la cual el acero empieza a deformarse de forma
                        permanente, como cuando doblas un clip y ya no regresa a su forma original.
                    </div>
                </div>
                <div class="glossary-card">
                    <div class="term">Elongacion (%)</div>
                    <div class="definition">
                        Cuanto puede estirarse el acero antes de romperse. Un valor alto
                        indica un material dúctil: flexible y que avisa antes de fallar.
                    </div>
                </div>
                <div class="glossary-card">
                    <div class="term">Dureza (HB)</div>
                    <div class="definition">
                        Que tan resistente es a ser rayado o abollado. Se mide con la escala
                        Brinell (HB). Más duro significa más resistente al desgaste.
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_data_section(df: pd.DataFrame) -> None:
    """Sección 1 — Descripción general del conjunto de datos."""

    st.markdown(
        """
        <div class="section-header">
            <div class="section-tag">Seccion 01</div>
            <div class="section-title">Nuestros Datos</div>
            <p class="section-subtitle">
                Antes de buscar patrones, conviene conocer con qué datos contamos.
                Aquí se muestran cuántos registros hay por grado de acero y por tipo
                de tratamiento térmico.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Métricas generales ─────────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)

    pct_range = f"{df['%C'].min():.2f} – {df['%C'].max():.2f}"

    for col, value, label in [
        (c1, len(df),                        "Registros totales"),
        (c2, df["SAE Grade"].nunique(),      "Grados SAE"),
        (c3, df["Condition_simple"].nunique(),"Tratamientos"),
        (c4, pct_range,                      "Rango de %C"),
    ]:
        with col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-value">{value}</div>
                    <div class="metric-label">{label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Tablas de conteo ───────────────────────────────────────
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown(
            "<p style='font-size:.85rem; font-weight:600; margin-bottom:.5rem;'>"
            "Registros por grado SAE</p>",
            unsafe_allow_html=True,
        )
        grade_counts = (
            df.groupby("SAE Grade")
            .size()
            .reset_index(name="Registros")
            .sort_values("SAE Grade")
        )
        st.dataframe(grade_counts, use_container_width=True, hide_index=True, height=280)

    with col_right:
        st.markdown(
            "<p style='font-size:.85rem; font-weight:600; margin-bottom:.5rem;'>"
            "Registros por tratamiento termico</p>",
            unsafe_allow_html=True,
        )
        cond_counts = (
            df.groupby("Condition_simple")
            .size()
            .reset_index(name="Registros")
            .sort_values("Registros", ascending=False)
        )
        st.dataframe(cond_counts, use_container_width=True, hide_index=True, height=280)


def render_carbon_section(df: pd.DataFrame) -> None:
    """Sección 2 — Efecto del porcentaje de carbono en las propiedades mecánicas."""

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="section-header">
            <div class="section-tag">Seccion 02</div>
            <div class="section-title">El Efecto del Carbono</div>
            <p class="section-subtitle">
                Cada punto en la gráfica representa un grado de acero con un tratamiento
                específico. Observa cómo cambian las propiedades a medida que el porcentaje
                de carbono crece de izquierda a derecha. Puedes filtrar por tratamiento
                para ver el efecto de forma aislada.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Filtro interactivo ─────────────────────────────────────
    conditions = ["Todos"] + sorted(df["Condition_simple"].unique().tolist())
    col_filter, _ = st.columns([2, 5])
    with col_filter:
        selected = st.selectbox("Filtrar por tratamiento:", conditions, index=0)

    # ── Preparar datos ─────────────────────────────────────────
    plot_df = df if selected == "Todos" else df[df["Condition_simple"] == selected]
    plot_df = plot_df.dropna(
        subset=["%C", "UTS (MPa)", "YS (MPa)", "Hardness (HB)", "Elongation (%)"]
    ).copy()
    plot_df["Elongation (%) x10"] = plot_df["Elongation (%)"] * 10

    # ── Construir figura ───────────────────────────────────────
    fig = go.Figure()

    prop_labels = {
        "UTS (MPa)":          "Resistencia Maxima (UTS)",
        "YS (MPa)":           "Limite Elastico (YS)",
        "Hardness (HB)":      "Dureza (HB)",
        "Elongation (%) x10": "Elongacion x10",
    }

    for col, label in prop_labels.items():
        fig.add_trace(
            go.Scatter(
                x=plot_df["%C"],
                y=plot_df[col],
                mode="markers",
                name=label,
                marker=dict(
                    size=10,
                    color=PROP_COLORS[col],
                    opacity=0.82,
                    line=dict(width=1, color="#ffffff"),
                ),
                hovertemplate=(
                    f"<b>{label}</b><br>"
                    "Carbono: %{x:.3f} %%<br>"
                    "Valor: %{y:.1f}<extra></extra>"
                ),
            )
        )

    fig.update_layout(
        **PLOTLY_LAYOUT,
        height=460,
        xaxis=dict(
            title="Contenido de Carbono (%C)",
            showgrid=True, gridcolor="#f0ebe4",
            linecolor="#e0d8ce", zeroline=False,
        ),
        yaxis=dict(
            title="Valor de la propiedad (unidades mixtas)",
            showgrid=True, gridcolor="#f0ebe4",
            linecolor="#e0d8ce", zeroline=False,
        ),
        legend=dict(
            orientation="h", yanchor="bottom", y=1.02,
            xanchor="right", x=1, bgcolor="rgba(0,0,0,0)",
        ),
    )

    st.plotly_chart(fig, use_container_width=True)

    # ── Texto explicativo automático con correlaciones ─────────
    corr_uts   = plot_df[["%C", "UTS (MPa)"]].corr().iloc[0, 1]
    corr_elong = plot_df[["%C", "Elongation (%)"]].corr().iloc[0, 1]

    dir_uts   = "aumenta" if corr_uts   > 0 else "disminuye"
    dir_elong = "aumenta" if corr_elong > 0 else "disminuye"

    abs_uts   = abs(corr_uts)
    abs_elong = abs(corr_elong)

    strength_word = (
        "muy fuerte" if abs_uts > 0.8 else
        "moderada"   if abs_uts > 0.5 else
        "débil"
    )

    st.markdown(
        f"""
        <div class="insight-box">
            <p>
                <strong>Lo que muestra la grafica:</strong>
                con el filtro seleccionado, a medida que el carbono aumenta,
                la resistencia maxima <em>{dir_uts}</em>
                (correlacion = {corr_uts:.2f}, relacion {strength_word}),
                mientras que la elongacion <em>{dir_elong}</em>
                (correlacion = {corr_elong:.2f}).
                <strong>Esto refleja un principio fundamental:</strong>
                mas carbono hace al acero mas duro y resistente,
                pero también mas fragil y menos capaz de estirarse sin romperse.
                La Elongacion se multiplico por 10 para que sea
                visible en la misma escala que las otras propiedades.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_treatment_section(df: pd.DataFrame) -> None:
    """Sección 3 — Efecto del tratamiento térmico (boxplots interactivos)."""

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="section-header">
            <div class="section-tag">Seccion 03</div>
            <div class="section-title">El Efecto del Tratamiento Termico</div>
            <p class="section-subtitle">
                El mismo acero puede comportarse de forma completamente distinta según
                cómo se procese. Estos gráficos de caja muestran la variabilidad de
                cada propiedad para cada tratamiento. La línea central es el valor típico;
                las cajas, la mitad central de los datos; los bigotes, los valores extremos.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Leyenda de colores ─────────────────────────────────────
    chips = "".join(
        f'<span class="legend-chip">'
        f'<span class="chip-dot" style="background:{color}"></span>{cond}'
        f'</span>'
        for cond, color in COND_COLORS.items()
        if cond != "Other"
    )
    st.markdown(f'<div class="legend-row">{chips}</div>', unsafe_allow_html=True)

    # ── Cuatro propiedades en grid 2×2 ─────────────────────────
    properties = [
        ("UTS (MPa)",     "Resistencia Maxima (UTS)"),
        ("YS (MPa)",      "Limite Elastico (YS)"),
        ("Hardness (HB)", "Dureza (HB)"),
        ("Elongation (%)","Elongacion (%)"),
    ]

    col_a, col_b = st.columns(2)
    columns = [col_a, col_b, col_a, col_b]

    for (prop, label), col in zip(properties, columns):
        data_clean = df.dropna(subset=[prop, "Condition_simple"])

        fig = go.Figure()

        for cond in sorted(data_clean["Condition_simple"].unique()):
            subset = data_clean.loc[data_clean["Condition_simple"] == cond, prop]
            fig.add_trace(
                go.Box(
                    y=subset,
                    name=cond,
                    marker_color=COND_COLORS.get(cond, "#aaa"),
                    boxmean=True,           # muestra la media como línea punteada
                    line=dict(width=1.6),
                    fillcolor=COND_COLORS.get(cond, "#aaa"),
                    opacity=0.82,
                )
            )

        fig.update_layout(
            **PLOTLY_LAYOUT,
            height=340,
            showlegend=False,
            title=dict(
                text=label,
                font=dict(family="DM Serif Display, serif", size=15, color="#1a1a2e"),
                x=0.04,
            ),
            yaxis=dict(
                title=prop,
                showgrid=True, gridcolor="#f0ebe4",
                linecolor="#e0d8ce", zeroline=False,
            ),
            xaxis=dict(linecolor="#e0d8ce"),
        )

        with col:
            st.plotly_chart(fig, use_container_width=True)

    # ── Insight explicativo ────────────────────────────────────
    # Calculamos qué tratamiento tiene mayor UTS promedio
    avg_uts = (
        df.dropna(subset=["UTS (MPa)"])
        .groupby("Condition_simple")["UTS (MPa)"]
        .mean()
        .sort_values(ascending=False)
    )
    top_cond  = avg_uts.index[0]
    low_cond  = avg_uts.index[-1]

    st.markdown(
        f"""
        <div class="insight-box">
            <p>
                <strong>Como leer estos graficos:</strong>
                la linea central de cada caja es la mediana (el valor que divide
                exactamente la mitad de los datos). La linea punteada es el promedio.
                En este conjunto de datos, el tratamiento
                <strong>{top_cond}</strong> produce la mayor resistencia promedio,
                mientras que <strong>{low_cond}</strong> da los valores mas bajos.
                Esto muestra que el proceso de fabricacion puede alterar las propiedades
                del acero tanto como su composicion quimica.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer() -> None:
    """Pie de página."""

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.markdown(
        """
        <p style="text-align:center; color:#a0a0a0; font-size:.82rem; padding-bottom:2rem;">
            Panel educativo de Ciencia de Materiales &mdash;
            Datos: aceros.csv &mdash;
            Desarrollado con Streamlit y Plotly
        </p>
        """,
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────────────────────
#  PUNTO DE ENTRADA
# ─────────────────────────────────────────────────────────────

def main() -> None:
    # Carga y preprocesamiento (con caché para evitar recargas)
    try:
        df = load_and_preprocess("aceros.csv")
    except FileNotFoundError:
        st.error(
            "No se encontro el archivo 'aceros.csv'. "
            "Asegurate de que este en la misma carpeta que app.py."
        )
        st.stop()
    except Exception as exc:
        st.error(f"Error al procesar los datos: {exc}")
        st.stop()

    # Renderizar cada sección en orden
    render_header()
    render_data_section(df)
    render_carbon_section(df)
    render_treatment_section(df)
    render_footer()


if __name__ == "__main__":
    main()
