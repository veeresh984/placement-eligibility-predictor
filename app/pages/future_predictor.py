import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Future Placement Predictor",
    page_icon="🚀",
    layout="wide"
)

# ==========================================
# LOAD MODEL
# ==========================================

@st.cache_resource
def load_model():
    return joblib.load("models/placement_model.pkl")

model = load_model()

# ==========================================
# TITLE
# ==========================================

st.title("🚀 Future Placement Predictor")

st.markdown("""
Simulate future improvements and analyze how your placement eligibility may improve over time.
""")

st.divider()

# ==========================================
# CURRENT PROFILE
# ==========================================

st.header("📌 Current Student Profile")

col1, col2 = st.columns(2)

with col1:

    current_cgpa = st.slider(
        "Current CGPA",
        0.0,
        10.0,
        7.0,
        0.1
    )

    current_attendance = st.slider(
        "Current Attendance",
        0,
        100,
        80
    )

    current_aptitude = st.slider(
        "Current Aptitude Score",
        0,
        100,
        70
    )

    current_communication = st.slider(
        "Current Communication Score",
        0,
        100,
        70
    )

with col2:

    current_internships = st.number_input(
        "Current Internships",
        0,
        10,
        1
    )

    current_certifications = st.number_input(
        "Current Certifications",
        0,
        20,
        2
    )

    current_projects = st.number_input(
        "Current Projects",
        0,
        20,
        3
    )

# ==========================================
# CURRENT PREDICTION
# ==========================================

current_df = pd.DataFrame({
    "cgpa": [current_cgpa],
    "attendance": [current_attendance],
    "aptitude_score": [current_aptitude],
    "communication_score": [current_communication],
    "internships": [current_internships],
    "certifications": [current_certifications],
    "projects": [current_projects]
})

current_probability = (
    model.predict_proba(current_df)[0][1] * 100
)

st.metric(
    "Current Placement Probability",
    f"{current_probability:.2f}%"
)

st.divider()

# ==========================================
# FUTURE PROFILE
# ==========================================

st.header("🎯 Future Improvement Simulator")

col1, col2 = st.columns(2)

with col1:

    future_cgpa = st.slider(
        "Future CGPA",
        current_cgpa,
        10.0,
        min(current_cgpa + 0.5, 10.0),
        0.1
    )

    future_attendance = st.slider(
        "Future Attendance",
        current_attendance,
        100,
        min(current_attendance + 5, 100)
    )

    future_aptitude = st.slider(
        "Future Aptitude",
        current_aptitude,
        100,
        min(current_aptitude + 10, 100)
    )

    future_communication = st.slider(
        "Future Communication",
        current_communication,
        100,
        min(current_communication + 10, 100)
    )

with col2:

    future_internships = st.number_input(
        "Future Internships",
        min_value=current_internships,
        max_value=10,
        value=min(current_internships + 1, 10)
    )

    future_certifications = st.number_input(
        "Future Certifications",
        min_value=current_certifications,
        max_value=20,
        value=min(current_certifications + 2, 20)
    )

    future_projects = st.number_input(
        "Future Projects",
        min_value=current_projects,
        max_value=20,
        value=min(current_projects + 2, 20)
    )

# ==========================================
# FUTURE PREDICTION
# ==========================================

future_df = pd.DataFrame({
    "cgpa": [future_cgpa],
    "attendance": [future_attendance],
    "aptitude_score": [future_aptitude],
    "communication_score": [future_communication],
    "internships": [future_internships],
    "certifications": [future_certifications],
    "projects": [future_projects]
})

future_probability = (
    model.predict_proba(future_df)[0][1] * 100
)

improvement = (
    future_probability - current_probability
)

st.divider()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Current Probability",
    f"{current_probability:.2f}%"
)

col2.metric(
    "Future Probability",
    f"{future_probability:.2f}%"
)

col3.metric(
    "Improvement",
    f"{improvement:.2f}%"
)

# ==========================================
# GAUGE CHART
# ==========================================

st.subheader("📊 Future Placement Score")

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=future_probability,
    title={"text": "Placement Probability"},
    gauge={
        "axis": {"range": [0, 100]},
        "steps": [
            {"range": [0, 40]},
            {"range": [40, 70]},
            {"range": [70, 100]}
        ]
    }
))

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# FUTURE GROWTH TIMELINE
# ==========================================

st.subheader("📈 Placement Growth Forecast")

months = [
    "Current",
    "3 Months",
    "6 Months",
    "9 Months",
    "12 Months"
]

growth_values = np.linspace(
    current_probability,
    future_probability,
    5
)

timeline_df = pd.DataFrame({
    "Period": months,
    "Probability": growth_values
})

fig = px.line(
    timeline_df,
    x="Period",
    y="Probability",
    markers=True,
    title="Placement Probability Growth"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# IMPROVEMENT CONTRIBUTION
# ==========================================

st.subheader("📌 Improvement Contributions")

contribution_data = pd.DataFrame({
    "Factor": [
        "CGPA",
        "Attendance",
        "Aptitude",
        "Communication",
        "Internships",
        "Certifications",
        "Projects"
    ],
    "Improvement": [
        future_cgpa - current_cgpa,
        future_attendance - current_attendance,
        future_aptitude - current_aptitude,
        future_communication - current_communication,
        future_internships - current_internships,
        future_certifications - current_certifications,
        future_projects - current_projects
    ]
})

fig = px.bar(
    contribution_data,
    x="Factor",
    y="Improvement",
    title="Profile Improvement Areas"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# FUTURE RECOMMENDATIONS
# ==========================================

st.subheader("💡 Personalized Recommendations")

recommendations = []

if future_cgpa < 8:
    recommendations.append(
        "Improve CGPA above 8.0"
    )

if future_aptitude < 80:
    recommendations.append(
        "Increase Aptitude Score above 80"
    )

if future_communication < 80:
    recommendations.append(
        "Improve Communication Skills"
    )

if future_internships < 2:
    recommendations.append(
        "Complete at least 2 internships"
    )

if future_certifications < 3:
    recommendations.append(
        "Earn more certifications"
    )

if future_projects < 4:
    recommendations.append(
        "Build more industry-level projects"
    )

if recommendations:
    for rec in recommendations:
        st.warning(rec)
else:
    st.success(
        "Excellent profile for placement opportunities."
    )

# ==========================================
# FUTURE ELIGIBILITY STATUS
# ==========================================

st.subheader("🏆 Future Eligibility Result")

if future_probability >= 85:
    st.success(
        "High Probability of Placement Success"
    )

elif future_probability >= 65:
    st.info(
        "Good Placement Potential"
    )

else:
    st.error(
        "Further Improvement Recommended"
    )

# ==========================================
# COMPARISON TABLE
# ==========================================

st.subheader("📋 Current vs Future Profile")

comparison_df = pd.DataFrame({
    "Feature": [
        "CGPA",
        "Attendance",
        "Aptitude",
        "Communication",
        "Internships",
        "Certifications",
        "Projects"
    ],
    "Current": [
        current_cgpa,
        current_attendance,
        current_aptitude,
        current_communication,
        current_internships,
        current_certifications,
        current_projects
    ],
    "Future": [
        future_cgpa,
        future_attendance,
        future_aptitude,
        future_communication,
        future_internships,
        future_certifications,
        future_projects
    ]
})

st.dataframe(
    comparison_df,
    use_container_width=True
)

# ==========================================
# DOWNLOAD REPORT
# ==========================================

st.subheader("📥 Download Future Prediction Report")

report_df = pd.DataFrame({
    "Metric": [
        "Current Probability",
        "Future Probability",
        "Improvement"
    ],
    "Value": [
        round(current_probability, 2),
        round(future_probability, 2),
        round(improvement, 2)
    ]
})

csv = report_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Forecast Report",
    data=csv,
    file_name="future_placement_forecast.csv",
    mime="text/csv"
)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Future Placement Predictor | What-If Analysis Engine | Streamlit"
)
