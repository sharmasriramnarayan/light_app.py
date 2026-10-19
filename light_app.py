
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ============================================================
# TERA 2.0 — LIGHT EDITION
# Environmental Intelligence & Risk Prioritisation
# ============================================================

st.set_page_config(
    page_title="TERA 2.0 | Light Edition",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------- LIGHT GREEN THEME ---------------------

BG = "#F4F7F0"
SURFACE = "#FFFFFF"
SURFACE_ALT = "#EAF0E5"
BORDER = "#D7E1D2"
TEXT = "#20392A"
MUTED = "#526B59"
GREEN = "#2F6845"
SAGE = "#6E9875"
PALE_GREEN = "#E4EEE1"
AMBER = "#94651D"
PALE_AMBER = "#FBF0D9"
RED = "#A6433D"
PALE_RED = "#F8E7E4"
GRID = "#E1E8DD"

FACTORS = [
    "Hazard",
    "Vulnerability",
    "Population",
    "Exposure",
    "Urgency"
]

WEIGHTS = {
    "Hazard": 0.30,
    "Vulnerability": 0.25,
    "Population": 0.20,
    "Exposure": 0.15,
    "Urgency": 0.10,
}

ZONES = {
    "Forest": [72, 65, 35, 95, 75],
    "Residential Area": [80, 85, 95, 45, 90],
    "Hospital": [75, 90, 90, 30, 95],
    "Smart Farm": [60, 65, 45, 75, 60],
    "River & Dam": [85, 75, 70, 85, 85],
    "Industrial Zone": [82, 70, 75, 65, 80],
}

ACTIONS = {
    "Forest": [
        "Monitor signs of forest fires and unusual heat.",
        "Identify vulnerable wildlife and forest patches.",
        "Maintain firebreaks and safe access routes.",
        "Plan rapid communication with forest personnel.",
    ],
    "Residential Area": [
        "Identify densely populated and vulnerable neighborhoods.",
        "Prepare evacuation routes and public warning messages.",
        "Keep emergency contacts and shelters accessible.",
        "Coordinate with local disaster response teams.",
    ],
    "Hospital": [
        "Protect uninterrupted emergency and medical services.",
        "Check backup power, water, and essential supplies.",
        "Keep patient evacuation and ambulance routes clear.",
        "Prepare a continuity plan for critical care.",
    ],
    "Smart Farm": [
        "Monitor crop stress, soil moisture, and water availability.",
        "Plan efficient irrigation and water conservation.",
        "Protect crops against relevant weather hazards.",
        "Use sustainable farming and soil-management practices.",
    ],
    "River & Dam": [
        "Monitor water levels and official warning bulletins.",
        "Identify low-lying areas that may require evacuation.",
        "Keep drainage and emergency access routes clear.",
        "Coordinate warnings with downstream communities.",
    ],
    "Industrial Zone": [
        "Inspect hazardous-material storage and safety procedures.",
        "Check emergency shutdown and containment plans.",
        "Maintain fire safety and worker evacuation routes.",
        "Prepare pollution-control and incident-response measures.",
    ],
}

# -------------------- LIGHT MODE CSS ------------------------

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {{
        color-scheme: light;
    }}

    html, body, [class*="css"] {{
        font-family: 'Manrope', sans-serif;
        font-size: 17px;
    }}

    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {{
        background: {BG} !important;
        color: {TEXT} !important;
    }}

    [data-testid="stHeader"] {{
        background: {BG} !important;
    }}

    .block-container {{
        max-width: 1600px;
        padding-top: 1.8rem;
        padding-bottom: 2.5rem;
    }}

    h1, h2, h3, h4 {{
        color: {TEXT} !important;
        font-family: 'Manrope', sans-serif !important;
        font-weight: 800 !important;
    }}

    h1 {{
        font-size: 42px !important;
        letter-spacing: -1px;
    }}

    h2 {{
        font-size: 32px !important;
    }}

    h3 {{
        font-size: 25px !important;
    }}

    h4 {{
        font-size: 21px !important;
    }}

    p, li {{
        color: {TEXT};
        font-size: 17px;
        line-height: 1.75;
    }}

    [data-testid="stCaptionContainer"] p {{
        color: {MUTED} !important;
        font-size: 15px !important;
        line-height: 1.65;
    }}

    hr {{
        border-color: {BORDER} !important;
    }}

    /* Hero banner */

    .hero {{
        background: linear-gradient(120deg, #E4EEE0, #FDFEFA 78%);
        border: 1px solid {BORDER};
        border-radius: 22px;
        padding: 32px 34px;
        margin-bottom: 26px;
        box-shadow: 0 5px 20px rgba(36, 74, 53, 0.045);
    }}

    .eyebrow {{
        color: {GREEN};
        font-size: 14px;
        font-weight: 800;
        letter-spacing: 2.2px;
        text-transform: uppercase;
        margin-bottom: 14px;
    }}

    .hero-title {{
        font-size: clamp(36px, 4.5vw, 58px);
        line-height: 1.12;
        font-weight: 800;
        color: {TEXT};
        letter-spacing: -1.5px;
        margin: 0 0 16px 0;
    }}

    .hero-subtitle {{
        color: {MUTED};
        font-size: 18px;
        line-height: 1.8;
        margin: 0;
        max-width: 1000px;
    }}

    /* Metric cards */

    .metric-card {{
        background: {SURFACE};
        border: 1px solid {BORDER};
        border-radius: 17px;
        padding: 22px;
        min-height: 145px;
        box-shadow: 0 4px 14px rgba(36, 74, 53, 0.04);
    }}

    .metric-label {{
        color: {MUTED};
        font-size: 14px;
        font-weight: 800;
        letter-spacing: 1px;
        text-transform: uppercase;
        line-height: 1.5;
    }}

    .metric-value {{
        color: {GREEN};
        font-size: 39px;
        font-weight: 800;
        line-height: 1.45;
        overflow-wrap: anywhere;
    }}

    .metric-note {{
        color: {MUTED};
        font-size: 14px;
        line-height: 1.5;
    }}

    /* General cards */

    .panel {{
        background: {SURFACE};
        border: 1px solid {BORDER};
        border-radius: 16px;
        padding: 21px;
        margin-bottom: 14px;
        box-shadow: 0 4px 14px rgba(36, 74, 53, 0.035);
    }}

    .panel-title {{
        color: {TEXT};
        font-weight: 800;
        font-size: 20px;
        line-height: 1.5;
        margin-bottom: 9px;
    }}

    .panel-text {{
        color: {MUTED};
        font-size: 16px;
        line-height: 1.8;
    }}

    /* Priority labels */

    .priority-pill {{
        display: inline-block;
        padding: 8px 14px;
        border-radius: 22px;
        font-size: 14px;
        font-weight: 800;
        letter-spacing: 0.5px;
        border: 1px solid transparent;
    }}

    .critical {{
        color: {RED};
        background: {PALE_RED};
        border-color: #EAC6C1;
    }}

    .high {{
        color: {AMBER};
        background: {PALE_AMBER};
        border-color: #E9D5A8;
    }}

    .moderate {{
        color: {GREEN};
        background: {PALE_GREEN};
        border-color: #CBDDC7;
    }}

    .lower {{
        color: #386944;
        background: #E7F2E6;
        border-color: #C8DFC6;
    }}

    /* Navigation tabs */

    [data-testid="stTabs"] {{
        margin-top: 15px;
    }}

    [data-testid="stTabs"] button {{
        color: {MUTED} !important;
        font-size: 17px !important;
        font-weight: 800 !important;
        padding: 15px 12px !important;
    }}

    [data-testid="stTabs"] button[aria-selected="true"] {{
        color: {GREEN} !important;
        border-bottom-color: {GREEN} !important;
    }}

    [data-testid="stTabContent"] {{
        padding-top: 24px;
    }}

    /* Selectboxes */

    [data-testid="stSelectbox"] label {{
        color: {TEXT} !important;
        font-size: 17px !important;
        font-weight: 700 !important;
        margin-bottom: 8px;
    }}

    [data-testid="stSelectbox"] div[data-baseweb="select"] > div {{
        background: {SURFACE} !important;
        color: {TEXT} !important;
        border-color: {BORDER} !important;
        border-radius: 11px !important;
        min-height: 50px;
        font-size: 16px !important;
    }}

    [data-baseweb="popover"],
    [data-baseweb="menu"] {{
        background: {SURFACE} !important;
    }}

    [role="option"] {{
        background: {SURFACE} !important;
        color: {TEXT} !important;
        font-size: 16px !important;
    }}

    [role="option"]:hover {{
        background: {PALE_GREEN} !important;
    }}

    /* Sliders */

    [data-testid="stSlider"] label {{
        color: {TEXT} !important;
        font-size: 17px !important;
        font-weight: 700 !important;
    }}

    [data-testid="stSlider"] [role="slider"] {{
        background: {GREEN} !important;
        border-color: {GREEN} !important;
    }}

    /* Buttons */

    .stButton > button {{
        background: {PALE_GREEN};
        color: {GREEN};
        border: 1px solid {BORDER};
        border-radius: 11px;
        font-size: 16px;
        font-weight: 800;
        padding: 10px 18px;
    }}

    .stButton > button:hover {{
        background: #D7E7D2;
        color: {TEXT};
        border-color: {SAGE};
    }}

    /* Dark text on light static tables */

    [data-testid="stTable"] {{
        background: {SURFACE} !important;
        border: 1px solid {BORDER} !important;
        border-radius: 13px !important;
        overflow: hidden;
    }}

    [data-testid="stTable"] table {{
        background: {SURFACE} !important;
        color: {TEXT} !important;
        border-collapse: collapse !important;
        width: 100%;
    }}

    [data-testid="stTable"] thead tr th {{
        background: {PALE_GREEN} !important;
        color: {GREEN} !important;
        border-bottom: 1px solid {BORDER} !important;
        padding: 15px 13px !important;
        font-size: 15px !important;
        font-weight: 800 !important;
        white-space: normal !important;
    }}

    [data-testid="stTable"] tbody tr td {{
        background: {SURFACE} !important;
        color: {TEXT} !important;
        border-bottom: 1px solid #E5EBE1 !important;
        padding: 14px 13px !important;
        font-size: 15px !important;
        line-height: 1.6 !important;
        white-space: normal !important;
    }}

    [data-testid="stTable"] tbody tr:nth-child(even) td {{
        background: #F7F9F4 !important;
    }}

    /* Alerts and expanders */

    [data-testid="stAlert"] {{
        background: {PALE_GREEN} !important;
        border: 1px solid {BORDER} !important;
        border-radius: 12px !important;
        color: {TEXT} !important;
        font-size: 16px !important;
    }}

    [data-testid="stExpander"] {{
        background: {SURFACE} !important;
        border: 1px solid {BORDER} !important;
        border-radius: 12px !important;
    }}

    [data-testid="stExpander"] summary {{
        color: {TEXT} !important;
        font-size: 16px !important;
        font-weight: 700 !important;
    }}

    /* Formula and footer */

    [data-testid="stLatex"] {{
        color: {TEXT} !important;
        font-size: 23px !important;
        overflow-x: auto;
    }}

    .footer {{
        color: {MUTED};
        text-align: center;
        font-size: 14px;
        line-height: 1.8;
        padding: 24px 0 6px 0;
        border-top: 1px solid {BORDER};
        margin-top: 30px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- MODEL FUNCTIONS -----------------------

def calculate_risk(values):
    return round(
        sum(
            values[i] * WEIGHTS[FACTORS[i]]
            for i in range(len(FACTORS))
        ),
        1
    )


def classify_risk(score):
    if score >= 80:
        return "Critical"
    if score >= 65:
        return "High"
    if score >= 45:
        return "Moderate"
    return "Lower"


def priority_color(priority):
    return {
        "Critical": RED,
        "High": AMBER,
        "Moderate": GREEN,
        "Lower": SAGE,
    }.get(priority, GREEN)


def priority_class(priority):
    return {
        "Critical": "critical",
        "High": "high",
        "Moderate": "moderate",
        "Lower": "lower",
    }.get(priority, "moderate")


def build_dataframe():
    rows = []

    for zone, values in ZONES.items():
        score = calculate_risk(values)
        rows.append({
            "Zone": zone,
            "Risk Score": score,
            "Priority": classify_risk(score),
            "Hazard": values[0],
            "Vulnerability": values[1],
            "Population": values[2],
            "Exposure": values[3],
            "Urgency": values[4],
        })

    return pd.DataFrame(rows).sort_values(
        "Risk Score", ascending=False
    ).reset_index(drop=True)


def metric_card(label, value, note):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def show_priority(priority):
    st.markdown(
        f'<span class="priority-pill {priority_class(priority)}">'
        f'{priority.upper()} PRIORITY</span>',
        unsafe_allow_html=True
    )


def make_plot_layout(fig, height=380):
    fig.update_layout(
        height=height,
        paper_bgcolor=SURFACE,
        plot_bgcolor=SURFACE,
        font=dict(
            family="Manrope, sans-serif",
            color=TEXT,
            size=14
        ),
        margin=dict(l=15, r=45, t=35, b=20),
        xaxis=dict(
            gridcolor=GRID,
            zerolinecolor=GRID,
            tickfont=dict(color=MUTED, size=13),
            title_font=dict(color=MUTED, size=14),
        ),
        yaxis=dict(
            gridcolor=GRID,
            zerolinecolor=GRID,
            tickfont=dict(color=TEXT, size=13),
            title_font=dict(color=MUTED, size=14),
        ),
        legend=dict(
            font=dict(color=TEXT, size=13),
            bgcolor="rgba(255,255,255,0)"
        ),
        hoverlabel=dict(
            bgcolor=SURFACE,
            font_color=TEXT,
            bordercolor=BORDER,
            font_size=14
        ),
    )
    return fig


# -------------------- HEADER -------------------------------

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">TERA 2.0 · Light Edition</div>
        <div class="hero-title">Understand the risk.<br>Enable smarter action.</div>
        <p class="hero-subtitle">
            Environmental intelligence through transparent scoring,
            interactive scenario analysis, and structured response planning.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

risk_df = build_dataframe()
highest = risk_df.iloc[0]
average_score = round(risk_df["Risk Score"].mean(), 1)
critical_count = int((risk_df["Priority"] == "Critical").sum())

# -------------------- TABS ---------------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "◈  Command Centre",
    "⌁  Risk Simulator",
    "✚  Response Planner",
    "ⓘ  Methodology & AI"
])

# ============================================================
# TAB 1 — COMMAND CENTRE
# ============================================================

with tab1:
    st.header("Environmental Risk Overview")
    st.caption(
        "Compare illustrative risk-priority scores across six environmental zones."
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("Zones analysed", "06", "Environmental locations")

    with c2:
        metric_card(
            "Highest score",
            f"{highest['Risk Score']:.1f}",
            str(highest["Zone"])
        )

    with c3:
        metric_card(
            "Critical zones",
            f"{critical_count:02d}",
            "Score of 80 or above"
        )

    with c4:
        metric_card(
            "Average score",
            f"{average_score:.1f}",
            "Across all six zones"
        )

    st.write("")
    left, right = st.columns([1.4, 1])

    with left:
        st.subheader("Risk Priority Ranking")
        st.caption("Higher scores indicate higher model-assessed priority.")

        fig = go.Figure(go.Bar(
            x=risk_df["Risk Score"],
            y=risk_df["Zone"],
            orientation="h",
            marker=dict(
                color=[priority_color(p) for p in risk_df["Priority"]],
                line=dict(color=BORDER, width=1)
            ),
            text=[f"{s:.1f}" for s in risk_df["Risk Score"]],
            textposition="outside",
            textfont=dict(color=TEXT, size=14),
            hovertemplate="<b>%{y}</b><br>Score: %{x:.1f}<extra></extra>"
        ))

        fig.update_yaxes(autorange="reversed")
        fig.update_xaxes(
            range=[0, 110],
            title="Weighted risk-priority score",
            dtick=20
        )

        make_plot_layout(fig, 420)
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.subheader("Priority Distribution")

        counts = (
            risk_df["Priority"]
            .value_counts()
            .reindex(
                ["Critical", "High", "Moderate", "Lower"],
                fill_value=0
            )
        )

        fig2 = go.Figure(go.Pie(
            labels=counts.index,
            values=counts.values,
            hole=0.62,
            marker=dict(
                colors=[RED, AMBER, GREEN, SAGE],
                line=dict(color=SURFACE, width=3)
            ),
            textinfo="label+value",
            textfont=dict(color=TEXT, size=14),
            hovertemplate="%{label}: %{value} zone(s)<extra></extra>"
        ))

        fig2.update_layout(
            annotations=[dict(
                text=f"{len(ZONES)}<br>Zones",
                x=0.5,
                y=0.5,
                font=dict(size=25, color=TEXT, family="Manrope"),
                showarrow=False
            )]
        )

        make_plot_layout(fig2, 350)
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-title">Current model leader</div>
                <div style="font-size:27px;font-weight:800;color:{TEXT};margin:10px 0;">
                    {highest['Zone']}
                </div>
                <div style="font-size:19px;color:{MUTED};">
                    Score: {highest['Risk Score']:.1f} / 100
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.subheader("Zone Assessment Table")
    st.caption("Zones are sorted from highest to lowest score.")

    display_df = risk_df[
        [
            "Zone", "Risk Score", "Priority", "Hazard",
            "Vulnerability", "Population", "Exposure", "Urgency"
        ]
    ].copy()

    display_df["Risk Score"] = display_df["Risk Score"].map(
        lambda x: f"{x:.1f}"
    )

    st.table(display_df)

    with st.expander("How should these scores be interpreted?"):
        st.write(
            "These are comparative priority indices calculated from illustrative "
            "factor values and weights. They are not disaster probabilities, "
            "official alerts, or validated real-world forecasts."
        )

# ============================================================
# TAB 2 — RISK SIMULATOR
# ============================================================

with tab2:
    st.header("Risk Scenario Simulator")
    st.caption(
        "Adjust the factor values to see how different scenarios change the score."
    )

    selected_zone = st.selectbox(
        "Choose an environmental zone",
        list(ZONES.keys()),
        key="sim_zone"
    )

    baseline = ZONES[selected_zone]

    st.subheader("Adjust the scenario")
    st.caption("Set each factor from 0 to 100.")

    left, right = st.columns(2)
    values = []

    for i, factor in enumerate(FACTORS):
        column = left if i % 2 == 0 else right

        with column:
            value = st.slider(
                factor,
                min_value=0,
                max_value=100,
                value=int(baseline[i]),
                key=f"slider_{selected_zone}_{factor}",
                help=f"Contribution weight: {WEIGHTS[factor] * 100:.0f}%"
            )
            values.append(value)

    simulated_score = calculate_risk(values)
    simulated_priority = classify_risk(simulated_score)
    base_score = calculate_risk(baseline)
    difference = round(simulated_score - base_score, 1)

    st.write("")
    r1, r2, r3 = st.columns(3)

    with r1:
        metric_card("Simulated score", f"{simulated_score:.1f}", "Out of 100")

    with r2:
        metric_card(
            "Baseline score",
            f"{base_score:.1f}",
            "Original illustrative inputs"
        )

    with r3:
        metric_card(
            "Score change",
            f"{difference:+.1f}",
            "Compared with baseline"
        )

    st.write("")
    show_priority(simulated_priority)

    st.subheader("Factor Contributions")

    contributions = [
        values[i] * WEIGHTS[FACTORS[i]]
        for i in range(len(FACTORS))
    ]

    contribution_df = pd.DataFrame({
        "Factor": FACTORS,
        "Weighted contribution": contributions,
    }).sort_values("Weighted contribution", ascending=True)

    fig3 = go.Figure(go.Bar(
        x=contribution_df["Weighted contribution"],
        y=contribution_df["Factor"],
        orientation="h",
        marker=dict(color=SAGE, line=dict(color=BORDER, width=1)),
        text=[
            f"{v:.1f}"
            for v in contribution_df["Weighted contribution"]
        ],
        textposition="outside",
        textfont=dict(color=TEXT, size=14),
        hovertemplate=(
            "<b>%{y}</b><br>Contribution: %{x:.1f}<extra></extra>"
        )
    ))

    fig3.update_xaxes(
        title="Contribution to total score",
        rangemode="tozero"
    )

    make_plot_layout(fig3, 360)
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Factor Breakdown")

    breakdown = pd.DataFrame({
        "Factor": FACTORS,
        "Input value": values,
        "Weight": [f"{WEIGHTS[f] * 100:.0f}%" for f in FACTORS],
        "Weighted contribution": [round(x, 2) for x in contributions],
    })

    st.table(breakdown)

    st.info(
        "This simulator changes the model inputs, not actual environmental "
        "conditions at a real location."
    )

# ============================================================
# TAB 3 — RESPONSE PLANNER
# ============================================================

with tab3:
    st.header("Environmental Response Planner")
    st.caption(
        "Explore suggested response actions for each zone using its model score."
    )

    selected_response_zone = st.selectbox(
        "Select a zone for response planning",
        list(ZONES.keys()),
        key="response_zone"
    )

    response_score = calculate_risk(ZONES[selected_response_zone])
    response_priority = classify_risk(response_score)

    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.markdown(
            f"""
            <div class="panel">
                <div class="eyebrow">Zone assessment</div>
                <div style="font-size:29px;font-weight:800;color:{TEXT};margin:12px 0;">
                    {selected_response_zone}
                </div>
                <div style="font-size:43px;font-weight:800;color:{priority_color(response_priority)};">
                    {response_score:.1f}
                    <span style="font-size:17px;color:{MUTED};">/ 100</span>
                </div>
                <div style="margin-top:15px;">
                    <span class="priority-pill {priority_class(response_priority)}">
                        {response_priority.upper()} PRIORITY
                    </span>
                </div>
                <p class="panel-text" style="margin-top:18px;">
                    This classification follows the score thresholds defined
                    in the TERA demonstration model.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.subheader("Suggested Response Actions")

        for index, action in enumerate(
            ACTIONS[selected_response_zone], start=1
        ):
            st.markdown(
                f"""
                <div class="panel">
                    <span style="color:{GREEN};font-weight:800;font-size:18px;margin-right:12px;">
                        {index:02d}
                    </span>
                    <span style="color:{TEXT};font-size:17px;line-height:1.7;">
                        {action}
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.subheader("Response Planning Principles")

    p1, p2, p3 = st.columns(3)

    with p1:
        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-title">01 · Assess</div>
                <div class="panel-text">
                    Review hazard, exposure, vulnerability, population,
                    and urgency before deciding on action.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with p2:
        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-title">02 · Prioritise</div>
                <div class="panel-text">
                    Use the score to support discussion about where
                    response resources may be needed first.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with p3:
        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-title">03 · Verify</div>
                <div class="panel-text">
                    Confirm conditions using official warnings, local
                    expertise, and reliable observations.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.warning(
        "These are educational planning suggestions, not live emergency "
        "instructions. Follow official authorities during an actual emergency."
    )

# ============================================================
# TAB 4 — METHODOLOGY & AI
# ============================================================

with tab4:
    st.header("Methodology & Model Transparency")
    st.caption(
        "Explore the formula, weights, priority thresholds, and current limitations."
    )

    st.subheader("Weighted Risk-Priority Formula")
    st.latex(r"R = 0.30H + 0.25V + 0.20P + 0.15E + 0.10U")

    st.markdown(
        f"""
        <div class="panel">
            <div class="panel-title">How the formula works</div>
            <div class="panel-text">
                Each factor is assigned a value from 0 to 100. The model
                multiplies each value by its weight and adds the contributions.
                Hazard contributes 30%, while urgency contributes 10%.
                The final weighted score ranges from 0 to 100.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Factor Weights")

    weights_df = pd.DataFrame({
        "Factor": FACTORS,
        "Weight": [f"{WEIGHTS[f] * 100:.0f}%" for f in FACTORS],
        "Purpose": [
            "Assessed intensity of a hazard.",
            "Susceptibility of a zone to harm.",
            "Population-related dimension of the assessment.",
            "Assessed degree of exposure.",
            "Urgency assigned in the scenario.",
        ]
    })

    st.table(weights_df)

    st.subheader("Priority Thresholds")

    thresholds_df = pd.DataFrame({
        "Priority": ["Critical", "High", "Moderate", "Lower"],
        "Score range": ["80–100", "65–79.9", "45–64.9", "Below 45"],
        "Interpretation": [
            "Highest model-assessed priority",
            "Elevated model-assessed priority",
            "Intermediate model-assessed priority",
            "Lower model-assessed priority",
        ]
    })

    st.table(thresholds_df)

    st.subheader("Technology Stack")

    tech1, tech2, tech3 = st.columns(3)

    with tech1:
        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-title">Python</div>
                <div class="panel-text">
                    Performs weighted calculations and applies priority rules.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with tech2:
        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-title">Pandas</div>
                <div class="panel-text">
                    Organises zone inputs, rankings, and tabular data.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with tech3:
        st.markdown(
            f"""
            <div class="panel">
                <div class="panel-title">Streamlit + Plotly</div>
                <div class="panel-text">
                    Streamlit provides the interface; Plotly renders the charts.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.subheader("Scientific Limitations")

    st.markdown(
        f"""
        <div class="panel">
            <div class="panel-title">What TERA currently does</div>
            <div class="panel-text">
                Calculates and compares illustrative environmental risk-priority
                scores using predefined inputs and transparent weights.
            </div>
            <br>
            <div class="panel-title">What TERA does not currently do</div>
            <div class="panel-text">
                It does not receive live sensor data, verify current environmental
                conditions, or predict the probability of a real disaster.
                The example values and weights are demonstration assumptions,
                not scientifically validated local measurements.
            </div>
            <br>
            <div class="panel-title">Potential future improvements</div>
            <div class="panel-text">
                Incorporate reliable official datasets, expert-reviewed weights,
                measured local indicators, validation against past events,
                and uncertainty analysis.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------- FOOTER -------------------------------

st.markdown(
    """
    <div class="footer">
        TERA 2.0 · Technology for Environmental Risk Analysis<br>
        Light Edition · Educational decision-support prototype<br>
        Scores are illustrative, not live environmental forecasts
    </div>
    """,
    unsafe_allow_html=True
)
