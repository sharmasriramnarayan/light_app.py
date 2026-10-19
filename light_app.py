
import streamlit as st

# ============================================================
# TERA 2.0 — LIGHT EDITION
# Technology for Environmental Risk Analysis
# Uses Streamlit only: no Plotly or Pandas required.
# ============================================================

st.set_page_config(
    page_title="TERA 2.0 | Environmental Command Centre",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- THEME --------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Manrope', sans-serif;
}
.stApp {
    background: #F4F7F0;
    color: #20392A;
}
[data-testid="stHeader"] {
    background: rgba(244,247,240,0.95);
}
[data-testid="stSidebar"] {
    background: #E7EFE2;
    border-right: 1px solid #D7E1D2;
}
h1, h2, h3 {
    color: #20392A !important;
    font-weight: 800 !important;
}
p, label, li {
    color: #526B59;
}
.hero {
    background: linear-gradient(120deg, #FFFFFF, #E7F1E4);
    border: 1px solid #D7E1D2;
    border-radius: 22px;
    padding: 28px 30px;
    margin-bottom: 22px;
}
.eyebrow {
    color: #2F6845;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 800;
}
.hero-title {
    color: #20392A;
    font-size: clamp(30px, 4vw, 46px);
    line-height: 1.12;
    font-weight: 800;
    margin: 10px 0;
}
.hero-copy {
    font-size: 16px;
    line-height: 1.7;
    color: #526B59;
}
.metric {
    background: #FFFFFF;
    border: 1px solid #D7E1D2;
    border-radius: 16px;
    padding: 19px;
    min-height: 115px;
}
.metric-label {
    color: #526B59;
    font-size: 13px;
    font-weight: 700;
}
.metric-value {
    color: #2F6845;
    font-size: 30px;
    font-weight: 800;
    margin-top: 8px;
}
.panel {
    background: #FFFFFF;
    border: 1px solid #D7E1D2;
    border-radius: 16px;
    padding: 20px;
    margin: 8px 0 16px 0;
}
.small-note {
    background: #EAF0E5;
    border-left: 4px solid #6E9875;
    padding: 12px 15px;
    border-radius: 7px;
    color: #526B59;
    font-size: 13px;
}
div.stButton > button {
    background: #2F6845;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    min-height: 44px;
}
div.stButton > button:hover {
    background: #234F35;
    color: white;
    border: none;
}
[data-testid="stMetric"] {
    background: white;
    border: 1px solid #D7E1D2;
    border-radius: 14px;
    padding: 15px;
}
hr {
    border-color: #D7E1D2;
}
</style>
""", unsafe_allow_html=True)

# -------------------- MODEL --------------------

FACTORS = ["Hazard", "Vulnerability", "Population", "Exposure", "Urgency"]

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
        "Check crop conditions and weather-related vulnerabilities",
        "Prepare water-conservation and crop-protection measures",
    ],
    "River & Dam": [
        "Inspect monitoring and warning procedures",
        "Review downstream communication and evacuation routes",
        "Check drainage and emergency response arrangements",
    ],
    "Industrial Zone": [
        "Inspect hazardous-material storage and safety procedures",
        "Review emergency shutdown and spill-response plans",
        "Check worker alerts and emergency access",
    ],
}


def calculate_risk(values):
    return round(sum(values[i] * WEIGHTS[FACTORS[i]]
                     for i in range(len(FACTORS))), 1)


def risk_level(score):
    if score >= 80:
        return "CRITICAL"
    if score >= 65:
        return "HIGH"
    if score >= 45:
        return "MODERATE"
    return "LOWER"


def risk_colour(level):
    return {
        "CRITICAL": "#B83D3D",
        "HIGH": "#B66A18",
        "MODERATE": "#8A791E",
        "LOWER": "#2F6845",
    }.get(level, "#2F6845")


def progress_bar(label, score, colour="#2F6845"):
    score = max(0, min(100, score))
    st.markdown(f"""
    <div style="margin:12px 0">
      <div style="display:flex;justify-content:space-between;
                  gap:12px;margin-bottom:6px">
        <span style="font-weight:700;color:#20392A">{label}</span>
        <span style="font-weight:800;color:{colour}">{score:.1f}/100</span>
      </div>
      <div style="height:10px;background:#E7EFE2;border-radius:20px;
                  overflow:hidden">
        <div style="height:10px;width:{score}%;background:{colour};
                    border-radius:20px"></div>
      </div>
    </div>
    """, unsafe_allow_html=True)


# -------------------- SIDEBAR --------------------

st.sidebar.markdown("## 🌿 TERA 2.0")
st.sidebar.caption("ENVIRONMENTAL INTELLIGENCE")
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
st.sidebar.markdown("### MODEL STATUS")
st.sidebar.success("Weighted scoring engine ready")
st.sidebar.info("Illustrative demonstration data")
st.sidebar.caption("No live sensors are connected.")

# -------------------- COMPUTE ALL ZONES --------------------

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
critical_count = sum(1 for r in results if r["Level"] == "CRITICAL")
high_count = sum(1 for r in results if r["Level"] == "HIGH")
average_score = round(sum(r["Score"] for r in results) / len(results), 1)
top_zone = results[0]

# -------------------- HERO --------------------

st.markdown("""
<div class="hero">
    <div class="eyebrow">AI-ASSISTED ENVIRONMENTAL DECISION SUPPORT</div>
    <div class="hero-title">TERA 2.0</div>
    <div class="hero-copy">
        Turning environmental risk indicators into clearer priorities
        and actionable response plans.
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------- COMMAND CENTRE --------------------

if page == "Command Centre":

    st.subheader("Environmental Command Centre")
    st.write("A comparative overview of the six demonstration zones.")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f'<div class="metric"><div class="metric-label">ZONES ANALYSED</div>'
            f'<div class="metric-value">{len(results)}</div></div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f'<div class="metric"><div class="metric-label">CRITICAL PRIORITIES</div>'
            f'<div class="metric-value" style="color:#B83D3D">{critical_count}</div></div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            f'<div class="metric"><div class="metric-label">HIGH PRIORITIES</div>'
            f'<div class="metric-value" style="color:#B66A18">{high_count}</div></div>',
            unsafe_allow_html=True,
        )
    with c4:
        st.markdown(
            f'<div class="metric"><div class="metric-label">AVERAGE INDEX</div>'
            f'<div class="metric-value">{average_score}</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown("### Priority ranking")
    st.caption("Higher index values indicate higher relative priority in this demonstration model.")

    for rank, item in enumerate(results, start=1):
        colour = risk_colour(item["Level"])
        with st.container(border=True):
            left, middle, right = st.columns([1, 5, 1.4])
            with left:
                st.markdown(f"### #{rank}")
            with middle:
                st.markdown(f"**{item['Zone']}**")
                progress_bar(item["Level"], item["Score"], colour)
            with right:
                st.markdown(
                    f"<div style='padding-top:8px;color:{colour};"
                    f"font-weight:800'>{item['Level']}</div>",
                    unsafe_allow_html=True,
                )

    st.markdown("### Highest-priority zone")
    st.markdown(
        f"<div class='panel'><div style='font-size:12px;letter-spacing:1px;"
        f"font-weight:800;color:#526B59'>CURRENT MODEL RESULT</div>"
        f"<div style='font-size:27px;font-weight:800;color:#20392A;"
        f"margin:8px 0'>{top_zone['Zone']}</div>"
        f"<div style='font-size:17px;color:{risk_colour(top_zone['Level'])};"
        f"font-weight:800'>{top_zone['Score']}/100 — {top_zone['Level']}</div>"
        f"<p>Review this zone first under the assumptions used in this model.</p>"
        f"</div>",
        unsafe_allow_html=True,
    )

    st.markdown("### Priority distribution")
    distribution = {}
    for item in results:
        distribution[item["Level"]] = distribution.get(item["Level"], 0) + 1

    for level in ["CRITICAL", "HIGH", "MODERATE", "LOWER"]:
        count = distribution.get(level, 0)
        st.write(f"**{level.title()}** — {count} zone(s)")
        progress_bar(level.title(), count / len(results) * 100,
                     risk_colour(level))

    st.markdown("""
    <div class="small-note">
    IMPORTANT: These values are illustrative weighted priority indices,
    not real disaster probabilities, validated forecasts, or live measurements.
    </div>
    """, unsafe_allow_html=True)

# -------------------- RISK SIMULATOR --------------------

elif page == "Risk Simulator":

    st.subheader("Interactive Risk Simulator")
    st.write(
        "Change the factor scores to see how the weighted priority index changes."
    )

    selected_zone = st.selectbox("Choose a zone", list(ZONES.keys()))
    baseline = ZONES[selected_zone]

    st.markdown("### Adjust indicators")
    changed = []

    for i, factor in enumerate(FACTORS):
        changed.append(
            st.slider(
                factor,
                min_value=0,
                max_value=100,
                value=int(baseline[i]),
                key=f"sim_{selected_zone}_{factor}",
                help=f"Weight in model: {WEIGHTS[factor] * 100:.0f}%",
            )
        )

    baseline_score = calculate_risk(baseline)
    new_score = calculate_risk(changed)
    difference = round(new_score - baseline_score, 1)
    level = risk_level(new_score)

    st.markdown("---")
    a, b, c = st.columns(3)

    a.metric("Original index", f"{baseline_score}/100")
    b.metric("Simulated index", f"{new_score}/100", delta=f"{difference:+.1f}")
    c.metric("Priority category", level)

    st.markdown("### Factor contribution")
    for i, factor in enumerate(FACTORS):
        contribution = changed[i] * WEIGHTS[factor]
        progress_bar(
            f"{factor} · {WEIGHTS[factor] * 100:.0f}% weight",
            contribution / WEIGHTS[factor] if WEIGHTS[factor] else 0,
        )

    st.markdown("### Interpretation")
    if new_score >= 80:
        st.error(
            "The simulated index is in the critical band. "
            "Under this model, this zone should receive the earliest review."
        )
    elif new_score >= 65:
        st.warning(
            "The simulated index is in the high-priority band. "
            "Review mitigation and preparedness measures."
        )
    elif new_score >= 45:
        st.info(
            "The simulated index is in the moderate band. "
            "Continue monitoring and review appropriate preventive actions."
        )
    else:
        st.success(
            "The simulated index is in the lower band. "
            "Continue routine monitoring and preparedness."
        )

    st.caption(
        "This simulator changes model inputs only. It does not measure actual "
        "environmental conditions or predict the probability of a disaster."
    )

# -------------------- RESPONSE PLANNER --------------------

elif page == "Response Planner":

    st.subheader("Response Planning Desk")
    st.write(
        "Use the demonstration model's ranking to organise a review of possible "
        "preparedness and mitigation actions."
    )

    selected_zone = st.selectbox(
        "Select a zone to plan for",
        [item["Zone"] for item in results],
        key="planner_zone",
    )

    item = next(r for r in results if r["Zone"] == selected_zone)
    colour = risk_colour(item["Level"])

    st.markdown(
        f"<div class='panel'><div style='font-size:12px;font-weight:800;"
        f"letter-spacing:1px;color:#526B59'>MODEL PRIORITY</div>"
        f"<div style='font-size:27px;font-weight:800;margin:8px 0;"
        f"color:#20392A'>{selected_zone}</div>"
        f"<div style='font-size:18px;font-weight:800;color:{colour}'>"
        f"{item['Score']}/100 · {item['Level']}</div></div>",
        unsafe_allow_html=True,
    )

    st.markdown("### Suggested review checklist")
    st.caption(
        "These are general preparedness suggestions, not automatically "
        "generated or verified emergency instructions."
    )

    for action in ACTIONS[selected_zone]:
        st.checkbox(action, key=f"action_{selected_zone}_{action}")

    st.markdown("### Planning notes")
    notes = st.text_area(
        "Record observations, responsible persons, or next steps",
        placeholder="Example: Verify the evacuation map with the responsible authority...",
        height=120,
    )

    if st.button("Prepare planning summary", key="prepare_summary"):
        st.markdown("#### Planning summary")
        st.write(f"**Zone:** {selected_zone}")
        st.write(f"**Model index:** {item['Score']}/100")
        st.write(f"**Priority band:** {item['Level']}")
        st.write("**Review actions:**")
        for action in ACTIONS[selected_zone]:
            st.write(f"- {action}")
        st.write("**Notes:**")
        st.write(notes if notes.strip() else "No additional notes entered.")

# -------------------- METHODOLOGY --------------------

elif page == "Methodology & AI":

    st.subheader("Methodology & AI")
    st.write(
        "TERA demonstrates how a transparent weighted scoring model can "
        "organise environmental indicators into a comparative priority index."
    )

    st.markdown("### 1. Weighted scoring formula")
    st.latex(
        r"R = 0.30H + 0.25V + 0.20P + 0.15E + 0.10U"
    )

    st.markdown("### 2. Indicator definitions")
    definitions = [
        ("Hazard", "30%", "Illustrative severity or likelihood-related indicator."),
        ("Vulnerability", "25%", "Illustrative susceptibility to harm."),
        ("Population", "20%", "Illustrative number or concentration of people affected."),
        ("Exposure", "15%", "Illustrative extent of people or assets in harm's way."),
        ("Urgency", "10%", "Illustrative need for timely review or response."),
    ]

    for factor, weight, description in definitions:
        with st.container(border=True):
            left, middle, right = st.columns([2, 1, 5])
            left.markdown(f"**{factor}**")
            middle.markdown(f"**{weight}**")
            right.write(description)

    st.markdown("### 3. Priority bands")
    for name, rule, colour in [
        ("CRITICAL", "80–100", "#B83D3D"),
        ("HIGH", "65–79.9", "#B66A18"),
        ("MODERATE", "45–64.9", "#8A791E"),
        ("LOWER", "Below 45", "#2F6845"),
    ]:
        st.markdown(
            f"<div style='display:flex;justify-content:space-between;"
            f"padding:12px 15px;margin:8px 0;background:white;"
            f"border:1px solid #D7E1D2;border-left:5px solid {colour};"
            f"border-radius:10px'>"
            f"<span style='font-weight:800;color:{colour}'>{name}</span>"
            f"<span style='color:#526B59'>{rule}</span></div>",
            unsafe_allow_html=True,
        )

    st.markdown("### 4. How TERA uses an AI-inspired workflow")
    st.markdown("""
    1. **Input:** Demonstration environmental indicators are provided for each zone.
    2. **Processing:** A weighted mathematical formula calculates a score.
    3. **Prioritisation:** Scores are grouped into predefined priority bands.
    4. **Decision support:** Suggested actions help organise a human review.
    5. **Human oversight:** Authorities must verify information before acting.
    """)

    st.markdown("### 5. Scientific limitations")
    st.warning("""
    This prototype uses manually supplied illustrative data and a
    rule-based weighted formula. It does not currently train a machine-learning
    model, connect to live sensors, use live satellite data, or predict actual
    disasters. The score is not a probability. Real-world deployment would
    require validated data, justified weights, expert review, and field testing.
    """)

# -------------------- FOOTER --------------------

st.markdown("---")
st.markdown("""
<div style="text-align:center;padding:12px 0">
    <div style="font-size:18px;font-weight:800;color:#2F6845">
        TERA 2.0
    </div>
    <div style="font-size:12px;color:#526B59;margin-top:5px">
        Technology for Environmental Risk Analysis · Student Prototype
    </div>
</div>
""", unsafe_allow_html=True)
