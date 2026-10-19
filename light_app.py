
import streamlit as st

# ============================================================
# TERA 2.0 | CLIMATE INTELLIGENCE EDITION
# Technology for Environmental Risk Analysis
# No Plotly or Pandas required
# ============================================================

st.set_page_config(
    page_title="TERA 2.0 | Climate Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- COLOUR SYSTEM --------------------

BG = "#F3F7F5"
WHITE = "#FFFFFF"
FOREST = "#163A32"
FOREST_DARK = "#102D27"
TEAL = "#0D9488"
TEAL_PALE = "#DDF5EF"
TEXT = "#203B35"
MUTED = "#61756E"
BORDER = "#D9E5DF"
PANEL = "#F8FBF9"

CRITICAL = "#B91C1C"
HIGH = "#C2410C"
MODERATE = "#A16207"
LOWER = "#15803D"

RISK_COLOURS = {
    "CRITICAL": CRITICAL,
    "HIGH": HIGH,
    "MODERATE": MODERATE,
    "LOWER": LOWER,
}

# -------------------- PAGE STYLING --------------------

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {{
    font-family: 'Manrope', sans-serif;
}}

.stApp {{
    background: {BG};
    color: {TEXT};
}}

[data-testid="stHeader"] {{
    background: rgba(243,247,245,0.96);
}}

[data-testid="stSidebar"] {{
    background: {FOREST_DARK};
    border-right: 1px solid #285348;
}}

[data-testid="stSidebar"] * {{
    color: #E8F5EE !important;
}}

[data-testid="stSidebar"] [data-testid="stRadio"] label {{
    background: transparent;
    border-radius: 8px;
    padding: 5px;
}}

[data-testid="stSidebar"] hr {{
    border-color: #35574D;
}}

h1, h2, h3 {{
    color: {FOREST} !important;
    font-weight: 800 !important;
    letter-spacing: -0.5px;
}}

p, li, label {{
    color: {MUTED};
}}

[data-testid="stMarkdownContainer"] p {{
    line-height: 1.65;
}}

.hero {{
    background: linear-gradient(120deg, {FOREST_DARK} 0%, {FOREST} 68%, #176B5B 100%);
    border: 1px solid #285348;
    border-radius: 22px;
    padding: 30px;
    margin-bottom: 24px;
    box-shadow: 0 8px 24px rgba(22,58,50,0.10);
}}

.eyebrow {{
    color: #8DE2C8;
    font-size: 11px;
    letter-spacing: 2.5px;
    font-weight: 800;
}}

.hero-title {{
    color: #FFFFFF;
    font-size: clamp(36px, 5vw, 54px);
    line-height: 1.08;
    font-weight: 800;
    margin: 12px 0;
}}

.hero-copy {{
    color: #D8EEE5;
    font-size: 15px;
    line-height: 1.8;
    max-width: 760px;
}}

.hero-tag {{
    display: inline-block;
    border: 1px solid #4B8172;
    background: rgba(255,255,255,0.07);
    color: #C8F5E5;
    border-radius: 30px;
    padding: 6px 11px;
    font-size: 11px;
    font-weight: 700;
    margin-top: 14px;
}}

.metric {{
    background: {WHITE};
    border: 1px solid {BORDER};
    border-top: 4px solid {TEAL};
    border-radius: 15px;
    padding: 18px;
    min-height: 115px;
    box-shadow: 0 3px 12px rgba(22,58,50,0.035);
}}

.metric-label {{
    color: {MUTED};
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1px;
}}

.metric-value {{
    color: {FOREST};
    font-size: 31px;
    font-weight: 800;
    margin-top: 10px;
}}

.panel {{
    background: {WHITE};
    border: 1px solid {BORDER};
    border-radius: 16px;
    padding: 21px;
    margin: 8px 0 16px 0;
}}

.section-kicker {{
    color: {TEAL};
    font-size: 11px;
    letter-spacing: 1.8px;
    font-weight: 800;
}}

.small-note {{
    background: {TEAL_PALE};
    border-left: 4px solid {TEAL};
    padding: 13px 15px;
    border-radius: 8px;
    color: {FOREST};
    font-size: 13px;
    line-height: 1.7;
    margin: 12px 0;
}}

.risk-badge {{
    display: inline-block;
    border-radius: 7px;
    padding: 6px 9px;
    font-size: 11px;
    letter-spacing: 0.5px;
    font-weight: 800;
}}

div.stButton > button {{
    background: {FOREST};
    color: #FFFFFF;
    border: 1px solid {FOREST};
    border-radius: 10px;
    font-weight: 700;
    min-height: 43px;
    transition: 0.2s ease;
}}

div.stButton > button:hover {{
    background: {TEAL};
    border-color: {TEAL};
    color: #FFFFFF;
}}

[data-testid="stMetric"] {{
    background: {WHITE};
    border: 1px solid {BORDER};
    border-radius: 13px;
    padding: 15px;
}}

[data-testid="stMetricLabel"] {{
    color: {MUTED};
}}

[data-testid="stMetricValue"] {{
    color: {FOREST};
    font-weight: 800;
}}

.stTabs [data-baseweb="tab-list"] {{
    gap: 8px;
}}

.stTabs [data-baseweb="tab"] {{
    background: {WHITE};
    border-radius: 8px;
    padding: 10px 15px;
}}

.stTabs [aria-selected="true"] {{
    color: {TEAL} !important;
    border-bottom: 3px solid {TEAL} !important;
}}

input, textarea {{
    border-radius: 9px !important;
}}

hr {{
    border-color: {BORDER};
}}

footer {{
    visibility: hidden;
}}

#MainMenu {{
    visibility: hidden;
}}

@media (max-width: 700px) {{
    .hero {{
        padding: 22px;
    }}
    .metric {{
        padding: 13px;
    }}
    .metric-value {{
        font-size: 25px;
    }}
}}
</style>
""", unsafe_allow_html=True)


# -------------------- MODEL DATA --------------------

FACTORS = [
    "Hazard",
    "Vulnerability",
    "Population",
    "Exposure",
    "Urgency",
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
        "Inspect firebreaks and forest access routes",
        "Monitor dry vegetation and possible ignition sources",
        "Prepare trained response teams and evacuation routes",
    ],
    "Residential Area": [
        "Review evacuation routes and public alert procedures",
        "Check emergency access and vulnerable households",
        "Prepare local response teams and public information",
    ],
    "Hospital": [
        "Verify backup power and emergency supplies",
        "Review patient evacuation and continuity plans",
        "Keep emergency access routes clear",
    ],
    "Smart Farm": [
        "Inspect irrigation and water-storage systems",
        "Review crop conditions and weather-related vulnerabilities",
        "Prepare water-conservation and crop-protection measures",
    ],
    "River & Dam": [
        "Review water-level monitoring and warning procedures",
        "Check downstream communication and evacuation plans",
        "Review drainage and emergency response arrangements",
    ],
    "Industrial Zone": [
        "Inspect hazardous-material storage and safety procedures",
        "Review emergency shutdown and spill-response plans",
        "Check worker alerts and emergency access",
    ],
}


# -------------------- CALCULATIONS --------------------

def calculate_risk(values):
    return round(
        sum(values[i] * WEIGHTS[FACTORS[i]]
            for i in range(len(FACTORS))),
        1,
    )


def risk_level(score):
    if score >= 80:
        return "CRITICAL"
    if score >= 65:
        return "HIGH"
    if score >= 45:
        return "MODERATE"
    return "LOWER"


def risk_colour(level):
    return RISK_COLOURS.get(level, FOREST)


def progress_bar(label, score, colour=TEAL):
    score = max(0, min(100, float(score)))
    st.markdown(f"""
    <div style="margin:12px 0">
      <div style="display:flex;justify-content:space-between;
                  align-items:center;gap:10px;margin-bottom:7px">
        <span style="font-weight:700;color:{TEXT}">{label}</span>
        <span style="font-weight:800;color:{colour}">{score:.1f}</span>
      </div>
      <div style="height:10px;background:#E3ECE7;border-radius:20px;
                  overflow:hidden">
        <div style="height:10px;width:{score}%;background:{colour};
                    border-radius:20px"></div>
      </div>
    </div>
    """, unsafe_allow_html=True)


def risk_badge(level):
    colour = risk_colour(level)
    backgrounds = {
        "CRITICAL": "#FCE8E8",
        "HIGH": "#FFF0E5",
        "MODERATE": "#FFF7D6",
        "LOWER": "#E3F6E8",
    }
    background = backgrounds[level]
    st.markdown(
        f'<span class="risk-badge" style="color:{colour};'
        f'background:{background}">{level}</span>',
        unsafe_allow_html=True,
    )


def section_header(kicker, heading, description=None):
    st.markdown(
        f'<div class="section-kicker">{kicker}</div>',
        unsafe_allow_html=True,
    )
    st.subheader(heading)
    if description:
        st.caption(description)


# -------------------- SIDEBAR --------------------

st.sidebar.markdown(
    f"""
    <div style="padding:12px 2px 18px 2px">
      <div style="font-size:27px;font-weight:800;color:#FFFFFF">
        🌿 TERA<span style="color:#72D9BC">.2</span>
      </div>
      <div style="font-size:10px;letter-spacing:2px;font-weight:800;
                  color:#8DE2C8;margin-top:5px">
        CLIMATE INTELLIGENCE
      </div>
      <div style="font-size:12px;color:#B9D7CC;margin-top:10px">
        Environmental Risk Analysis
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Command Centre",
        "Risk Simulator",
        "Response Planner",
        "Methodology & AI",
    ],
)

st.sidebar.markdown("---")
st.sidebar.markdown("### SYSTEM STATUS")
st.sidebar.success("Scoring engine ready")
st.sidebar.info("Demonstration dataset")
st.sidebar.caption(
    "Prototype mode · No live sensors connected"
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    '<div style="font-size:11px;color:#A9C8BD">'
    'BUILT FOR ENVIRONMENTAL AWARENESS<br><br>'
    'TERA 2.0 · Student prototype'
    '</div>',
    unsafe_allow_html=True,
)


# -------------------- COMPUTE ZONE RESULTS --------------------

results = []

for zone, values in ZONES.items():
    score = calculate_risk(values)
    results.append({
        "Zone": zone,
        "Score": score,
        "Level": risk_level(score),
        "Values": values,
    })

results.sort(key=lambda item: item["Score"], reverse=True)

critical_count = sum(
    1 for item in results if item["Level"] == "CRITICAL"
)
high_count = sum(
    1 for item in results if item["Level"] == "HIGH"
)
average_score = round(
    sum(item["Score"] for item in results) / len(results), 1
)
top_zone = results[0]


# -------------------- HERO BANNER --------------------

st.markdown("""
<div class="hero">
    <div class="eyebrow">ENVIRONMENTAL DECISION SUPPORT SYSTEM</div>
    <div class="hero-title">TERA 2.0</div>
    <div class="hero-copy">
        See the signals. Understand the risks. Prioritise the response.
        A transparent, data-driven prototype for comparing environmental
        risk indicators across different zones.
    </div>
    <div class="hero-tag">● CLIMATE INTELLIGENCE EDITION</div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# PAGE 1 — COMMAND CENTRE
# ============================================================

if page == "Command Centre":

    section_header(
        "LIVE MODEL OVERVIEW",
        "Environmental Command Centre",
        "A comparative overview of six demonstration zones.",
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f'<div class="metric"><div class="metric-label">'
            f'ZONES ANALYSED</div><div class="metric-value">'
            f'{len(results)}</div></div>',
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f'<div class="metric" style="border-top-color:{CRITICAL}">'
            f'<div class="metric-label">CRITICAL PRIORITIES</div>'
            f'<div class="metric-value" style="color:{CRITICAL}">'
            f'{critical_count}</div></div>',
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            f'<div class="metric" style="border-top-color:{HIGH}">'
            f'<div class="metric-label">HIGH PRIORITIES</div>'
            f'<div class="metric-value" style="color:{HIGH}">'
            f'{high_count}</div></div>',
            unsafe_allow_html=True,
        )

    with c4:
        st.markdown(
            f'<div class="metric"><div class="metric-label">'
            f'AVERAGE INDEX</div><div class="metric-value">'
            f'{average_score}</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown("")
    section_header(
        "RANKING ENGINE",
        "Zone Priority Ranking",
        "Rankings are based on the weighted scores in the current dataset.",
    )

    for rank, item in enumerate(results, start=1):
        colour = risk_colour(item["Level"])

        with st.container(border=True):
            left, middle, right = st.columns([0.8, 5, 1.5])

            with left:
                st.markdown(
                    f"<div style='font-size:25px;font-weight:800;"
                    f"color:{TEAL};padding-top:8px'>"
                    f"{rank:02d}</div>",
                    unsafe_allow_html=True,
                )

            with middle:
                st.markdown(f"**{item['Zone']}**")
                progress_bar(
                    "Priority index",
                    item["Score"],
                    colour,
                )

            with right:
                st.markdown("<div style='height:10px'></div>",
                            unsafe_allow_html=True)
                risk_badge(item["Level"])
                st.caption(f"{item['Score']}/100")

    st.markdown("")
    section_header(
        "TOP MODEL RESULT",
        "Highest-Priority Zone",
        "The zone with the highest score under the current model assumptions.",
    )

    st.markdown(
        f"""
        <div class="panel" style="border-left:5px solid {risk_colour(top_zone['Level'])}">
          <div class="section-kicker">MODEL PRIORITY #01</div>
          <div style="font-size:29px;font-weight:800;color:{FOREST};
                      margin:9px 0">{top_zone['Zone']}</div>
          <div style="font-size:25px;font-weight:800;
                      color:{risk_colour(top_zone['Level'])}">
              {top_zone['Score']} / 100
          </div>
          <div style="margin-top:9px;color:{MUTED}">
            Review this zone first within the assumptions and limitations
            of this demonstration model.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_header(
        "DISTRIBUTION",
        "Priority Band Distribution",
        "Number of zones in each predefined band.",
    )

    distribution = {}
    for item in results:
        level = item["Level"]
        distribution[level] = distribution.get(level, 0) + 1

    for level in ["CRITICAL", "HIGH", "MODERATE", "LOWER"]:
        count = distribution.get(level, 0)
        share = count / len(results) * 100
        progress_bar(
            f"{level.title()} · {count} zone(s)",
            share,
            risk_colour(level),
        )

    st.markdown(
        """
        <div class="small-note">
        <b>MODEL NOTE:</b> These are illustrative weighted priority
        indices, not real disaster probabilities, validated forecasts,
        or live environmental measurements.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# PAGE 2 — RISK SIMULATOR
# ============================================================

elif page == "Risk Simulator":

    section_header(
        "INTERACTIVE LAB",
        "Risk Simulator",
        "Change the indicators and observe their effect on the weighted index.",
    )

    st.markdown(
        """
        <div class="small-note">
        <b>Experiment:</b> Adjust one or more indicators. The model
        recalculates the score instantly using the displayed weights.
        </div>
        """,
        unsafe_allow_html=True,
    )

    selected_zone = st.selectbox(
        "SELECT ZONE",
        list(ZONES.keys()),
    )

    baseline = ZONES[selected_zone]

    st.markdown("### Indicator Controls")

    left, right = st.columns(2)
    changed = []

    for i, factor in enumerate(FACTORS):
        target_col = left if i % 2 == 0 else right

        with target_col:
            value = st.slider(
                factor,
                min_value=0,
                max_value=100,
                value=int(baseline[i]),
                key=f"sim_{selected_zone}_{factor}",
                help=f"This factor has a {WEIGHTS[factor] * 100:.0f}% model weight.",
            )
            st.caption(
                f"Model weight: {WEIGHTS[factor] * 100:.0f}%"
            )
            changed.append(value)

    baseline_score = calculate_risk(baseline)
    new_score = calculate_risk(changed)
    difference = round(new_score - baseline_score, 1)
    level = risk_level(new_score)
    colour = risk_colour(level)

    st.markdown("---")
    section_header("SIMULATION OUTPUT", "Your Results")

    a, b, c = st.columns(3)

    a.metric("Original index", f"{baseline_score}/100")
    b.metric(
        "Simulated index",
        f"{new_score}/100",
        delta=f"{difference:+.1f}",
    )

    with c:
        st.markdown(
            f"<div class='metric' style='border-top-color:{colour}'>"
            f"<div class='metric-label'>PRIORITY BAND</div>"
            f"<div style='font-size:22px;font-weight:800;color:{colour};"
            f"margin-top:13px'>{level}</div></div>",
            unsafe_allow_html=True,
        )

    st.markdown("### Indicator Profile")

    for i, factor in enumerate(FACTORS):
        progress_bar(
            f"{factor} · {WEIGHTS[factor] * 100:.0f}% weight",
            changed[i],
            TEAL if changed[i] == baseline[i] else FOREST,
        )

    st.markdown("### Interpretation")

    if new_score >= 80:
        st.error(
            "CRITICAL BAND — the simulated score is in the highest "
            "priority category. Review preparedness and mitigation needs."
        )
    elif new_score >= 65:
        st.warning(
            "HIGH PRIORITY — review preventive measures and preparedness."
        )
    elif new_score >= 45:
        st.info(
            "MODERATE PRIORITY — continue monitoring and review "
            "appropriate preventive actions."
        )
    else:
        st.success(
            "LOWER PRIORITY BAND — maintain routine monitoring and "
            "preparedness appropriate to local conditions."
        )

    st.caption(
        "Changing these sliders changes model inputs only. It does not "
        "measure real conditions or predict the probability of a disaster."
    )


# ============================================================
# PAGE 3 — RESPONSE PLANNER
# ============================================================

elif page == "Response Planner":

    section_header(
        "ACTION WORKSPACE",
        "Response Planning Desk",
        "Use the model ranking to organise a review of preparedness actions.",
    )

    selected_zone = st.selectbox(
        "SELECT ZONE FOR PLANNING",
        [item["Zone"] for item in results],
        key="planner_zone",
    )

    item = next(
        result for result in results
        if result["Zone"] == selected_zone
    )

    colour = risk_colour(item["Level"])

    st.markdown(
        f"""
        <div class="panel" style="border-left:5px solid {colour}">
          <div class="section-kicker">SELECTED ZONE</div>
          <div style="font-size:27px;font-weight:800;color:{FOREST};
                      margin:8px 0">{selected_zone}</div>
          <div style="font-size:23px;font-weight:800;color:{colour}">
            {item['Score']} / 100
          </div>
          <div style="margin-top:8px">{item['Level']} PRIORITY</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Preparedness Checklist")
    st.caption(
        "Tick items to track your planning discussion. These are general "
        "suggestions, not verified emergency instructions."
    )

    for index, action in enumerate(ACTIONS[selected_zone]):
        st.checkbox(
            action,
            key=f"action_{selected_zone}_{index}",
        )

    st.markdown("### Planning Notes")

    notes = st.text_area(
        "Observations and next steps",
        placeholder=(
            "Record observations, responsible persons, or measures "
            "that need expert verification..."
        ),
        height=120,
    )

    if st.button("Prepare Planning Summary"):
        st.markdown("---")
        st.markdown("### Planning Summary")
        st.write(f"**Zone:** {selected_zone}")
        st.write(f"**Model index:** {item['Score']}/100")
        st.write(f"**Priority band:** {item['Level']}")
        st.write("**Suggested review actions:**")

        for index, action in enumerate(ACTIONS[selected_zone]):
            completed = st.session_state.get(
                f"action_{selected_zone}_{index}", False
            )
            status = "✓ Reviewed" if completed else "○ Pending review"
            st.write(f"- {status}: {action}")

        st.write("**Planning notes:**")
        st.write(
            notes.strip() if notes.strip()
            else "No additional notes entered."
        )

        st.caption(
            "This summary supports planning discussion; it does not "
            "replace instructions from emergency management authorities."
        )


# ============================================================
# PAGE 4 — METHODOLOGY & AI
# ============================================================

elif page == "Methodology & AI":

    section_header(
        "TRANSPARENCY & SCIENCE",
        "Methodology & AI",
        "Understand how TERA transforms illustrative indicators into a score.",
    )

    st.markdown(
        """
        <div class="panel">
          <div class="section-kicker">THE CORE EQUATION</div>
          <div style="font-size:14px;color:#61756E;margin:8px 0">
            Weighted Environmental Priority Index
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.latex(
        r"R = 0.30H + 0.25V + 0.20P + 0.15E + 0.10U"
    )

    st.markdown("### Indicator Definitions")

    definitions = [
        (
            "Hazard",
            "30%",
            "An illustrative indicator related to hazard severity.",
        ),
        (
            "Vulnerability",
            "25%",
            "An illustrative indicator of susceptibility to harm.",
        ),
        (
            "Population",
            "20%",
            "An illustrative indicator of people potentially affected.",
        ),
        (
            "Exposure",
            "15%",
            "An illustrative indicator of people or assets in harm's way.",
        ),
        (
            "Urgency",
            "10%",
            "An illustrative indicator of the need for timely review.",
        ),
    ]

    for factor, weight, description in definitions:
        with st.container(border=True):
            left, middle, right = st.columns([2, 1, 5])

            with left:
                st.markdown(f"**{factor}**")

            with middle:
                st.markdown(
                    f"<span style='color:{TEAL};font-weight:800'>"
                    f"{weight}</span>",
                    unsafe_allow_html=True,
                )

            with right:
                st.write(description)

    st.markdown("### Priority Classification")

    bands = [
        ("CRITICAL", "80–100", CRITICAL, "#FCE8E8"),
        ("HIGH", "65–79.9", HIGH, "#FFF0E5"),
        ("MODERATE", "45–64.9", MODERATE, "#FFF7D6"),
        ("LOWER", "Below 45", LOWER, "#E3F6E8"),
    ]

    for name, rule, colour, pale in bands:
        st.markdown(
            f"""
            <div style="display:flex;justify-content:space-between;
                        align-items:center;padding:13px 15px;
                        margin:8px 0;background:{WHITE};
                        border:1px solid {BORDER};
                        border-left:5px solid {colour};
                        border-radius:10px">
                <span style="font-weight:800;color:{colour}">
                    {name}
                </span>
                <span style="background:{pale};color:{colour};
                             padding:5px 9px;border-radius:6px;
                             font-size:12px;font-weight:800">
                    {rule}
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### How TERA Works")

    steps = [
        (
            "01",
            "INPUT",
            "Demonstration environmental indicators are supplied for each zone.",
        ),
        (
            "02",
            "CALCULATE",
            "A weighted mathematical formula calculates the index.",
        ),
        (
            "03",
            "CLASSIFY",
            "The result is assigned to a predefined priority band.",
        ),
        (
            "04",
            "PLAN",
            "Suggested actions help organise a human review.",
        ),
        (
            "05",
            "VERIFY",
            "Experts must validate the information before real-world use.",
        ),
    ]

    for number, title, description in steps:
        with st.container(border=True):
            left, right = st.columns([0.7, 5])

            with left:
                st.markdown(
                    f"<div style='font-size:22px;font-weight:800;"
                    f"color:{TEAL}'>{number}</div>",
                    unsafe_allow_html=True,
                )

            with right:
                st.markdown(f"**{title}**")
                st.caption(description)

    st.markdown("### Scientific Limitations")

    st.warning(
        "This prototype uses manually supplied illustrative data and "
        "a rule-based weighted scoring formula. It does not currently "
        "train a machine-learning model, connect to live sensors, use "
        "live satellite data, or predict actual disasters. The index is "
        "not a probability. Real-world use would require validated data, "
        "justified weights, expert review, testing, and calibration."
    )


# -------------------- FOOTER --------------------

st.markdown("---")

st.markdown(
    f"""
    <div style="text-align:center;padding:18px 0 8px 0">
      <div style="font-size:22px;font-weight:800;color:{FOREST}">
        TERA<span style="color:{TEAL}"> 2.0</span>
      </div>
      <div style="font-size:11px;font-weight:800;letter-spacing:1.8px;
                  color:{MUTED};margin-top:6px">
        TECHNOLOGY FOR ENVIRONMENTAL RISK ANALYSIS
      </div>
      <div style="font-size:11px;color:{MUTED};margin-top:10px">
        Climate Intelligence Edition · Student Prototype
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
