import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Placement Eligibility Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.hero-box {
    padding: 2rem;
    border-radius: 15px;
    background: linear-gradient(
        135deg,
        #1f77b4,
        #17becf
    );
    color: white;
    text-align: center;
}

.feature-card {
    padding: 20px;
    border-radius: 12px;
    background-color: #f8f9fa;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
<div class="hero-box">
<h1>🎓 Placement Eligibility Predictor</h1>

<h3>
AI-Powered Student Placement Analytics Platform
</h3>

<p>
Predict placement eligibility, analyze performance,
discover improvement opportunities,
and forecast future placement success.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================
# OVERVIEW
# ==========================================

st.header("📌 Project Overview")

st.markdown("""
This project uses Machine Learning and Data Analytics
to evaluate placement eligibility based on:

- CGPA
- Attendance
- Aptitude Score
- Communication Skills
- Internships
- Certifications
- Projects

The application provides prediction,
analytics dashboards, and future forecasting.
""")

# ==========================================
# FEATURES
# ==========================================

st.header("🚀 Key Features")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    ### 🎯 Placement Predictor

    Predict whether a student is eligible
    for placements using Machine Learning.

    Features:

    ✔ Eligibility Prediction

    ✔ Probability Score

    ✔ Risk Assessment

    ✔ Personalized Recommendations
    """)

with col2:

    st.markdown("""
    ### 📊 Deep Analytics

    Analyze placement trends and patterns.

    Features:

    ✔ CGPA Analysis

    ✔ Internship Impact

    ✔ Certification Impact

    ✔ Correlation Analysis

    ✔ Student Segmentation
    """)

st.write("")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    ### 📈 Future Predictor

    Simulate future improvements.

    Features:

    ✔ What-If Analysis

    ✔ Growth Forecast

    ✔ Future Placement Probability

    ✔ Skill Improvement Impact
    """)

with col2:

    st.markdown("""
    ### 🤖 AI Insights

    Generate smart recommendations.

    Features:

    ✔ Performance Analysis

    ✔ Placement Readiness

    ✔ Improvement Suggestions

    ✔ Career Guidance
    """)

st.divider()

# ==========================================
# MODULES
# ==========================================

st.header("🗂 Application Modules")

module_df = {
    "Module": [
        "Dashboard",
        "Predictor",
        "Analytics",
        "Future Predictor"
    ],
    "Purpose": [
        "Overview of placement statistics",
        "Predict placement eligibility",
        "Deep data analytics",
        "Forecast future placement success"
    ]
}

st.table(module_df)

st.divider()

# ==========================================
# WORKFLOW
# ==========================================

st.header("⚙️ How It Works")

st.markdown("""
### Step 1

Enter student academic information.

⬇️

### Step 2

Machine Learning model evaluates profile.

⬇️

### Step 3

Placement probability is generated.

⬇️

### Step 4

Analytics dashboard provides insights.

⬇️

### Step 5

Future Predictor simulates improvements.
""")

st.divider()

# ==========================================
# MODEL INFO
# ==========================================

st.header("🧠 Machine Learning Model")

st.markdown("""
The prediction engine uses:

- Random Forest Classifier
- Feature Engineering
- Placement Probability Estimation
- Future Growth Forecasting

Input Features:

1. CGPA
2. Attendance
3. Aptitude Score
4. Communication Score
5. Internships
6. Certifications
7. Projects
""")

st.divider()

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("🎓 Navigation")

    st.success(
        "Use the Pages menu above "
        "to navigate through the application."
    )

    st.markdown("---")

    st.markdown("""
    ### Available Pages

    📊 Dashboard

    🎯 Predictor

    📈 Analytics

    🚀 Future Predictor
    """)

    st.markdown("---")

    st.info(
        "Placement Eligibility Predictor "
        "Version 1.0"
    )

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Placement Eligibility Predictor | "
    "Python • Streamlit • Machine Learning"
)
