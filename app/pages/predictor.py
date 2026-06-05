import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
from datetime import datetime

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Placement Predictor",
    page_icon="🎯",
    layout="wide"
)

# =====================================
# LOAD MODEL
# =====================================

@st.cache_resource
def load_model():
    return joblib.load("models/placement_model.pkl")

model = load_model()

# =====================================
# TITLE
# =====================================

st.title("🎯 Placement Eligibility Predictor")

st.markdown("""
Predict whether a student is eligible for placements using Machine Learning.
""")

st.divider()

# =====================================
# INPUT SECTION
# =====================================

col1, col2 = st.columns(2)

with col1:

    cgpa = st.slider(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        value=7.5,
        step=0.1
    )

    attendance = st.slider(
        "Attendance (%)",
        0,
        100,
        80
    )

    aptitude_score = st.slider(
        "Aptitude Score",
        0,
        100,
        70
    )

    communication_score = st.slider(
        "Communication Score",
        0,
        100,
        70
    )

with col2:

    internships = st.number_input(
        "Internships",
        min_value=0,
        max_value=10,
        value=1
    )

    certifications = st.number_input(
        "Certifications",
        min_value=0,
        max_value=20,
        value=2
    )

    projects = st.number_input(
        "Projects",
        min_value=0,
        max_value=20,
        value=3
    )

st.divider()

# =====================================
# PREDICTION BUTTON
# =====================================

predict_btn = st.button(
    "🚀 Predict Placement Eligibility",
    use_container_width=True
)

# =====================================
# PREDICTION
# =====================================

if predict_btn:

    input_df = pd.DataFrame({
        "cgpa": [cgpa],
        "attendance": [attendance],
        "aptitude_score": [aptitude_score],
        "communication_score": [communication_score],
        "internships": [internships],
        "certifications": [certifications],
        "projects": [projects]
    })

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    probability_percent = round(
        probability * 100,
        2
    )

    st.divider()

    # ===============================
    # RESULT HEADER
    # ===============================

    col1, col2 = st.columns([1, 1])

    with col1:

        if prediction == 1:
            st.success(
                "✅ Eligible for Placement"
            )
        else:
            st.error(
                "❌ Not Eligible for Placement"
            )

        st.metric(
            "Placement Probability",
            f"{probability_percent}%"
        )

    # ===============================
    # GAUGE CHART
    # ===============================

    with col2:

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=probability_percent,
                title={
                    "text":
                    "Placement Probability"
                },
                gauge={
                    "axis": {
                        "range": [0, 100]
                    },
                    "bar": {
                        "thickness": 0.3
                    },
                    "steps": [
                        {
                            "range": [0, 40],
                            "color": "lightgray"
                        },
                        {
                            "range": [40, 70],
                            "color": "gray"
                        },
                        {
                            "range": [70, 100],
                            "color": "darkgray"
                        }
                    ]
                }
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # ===============================
    # RISK ANALYSIS
    # ===============================

    st.subheader("📊 Eligibility Analysis")

    if probability_percent >= 80:
        st.success(
            "Excellent Placement Potential"
        )

    elif probability_percent >= 60:
        st.warning(
            "Moderate Placement Potential"
        )

    else:
        st.error(
            "High Risk Category"
        )

    # ===============================
    # INPUT SUMMARY
    # ===============================

    st.subheader("📋 Student Profile")

    summary = pd.DataFrame({
        "Feature": [
            "CGPA",
            "Attendance",
            "Aptitude Score",
            "Communication Score",
            "Internships",
            "Certifications",
            "Projects"
        ],
        "Value": [
            cgpa,
            attendance,
            aptitude_score,
            communication_score,
            internships,
            certifications,
            projects
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True
    )

    # ===============================
    # STRENGTHS
    # ===============================

    st.subheader("💪 Strength Analysis")

    strengths = []

    if cgpa >= 8:
        strengths.append("Strong Academic Record")

    if aptitude_score >= 80:
        strengths.append("Excellent Aptitude")

    if communication_score >= 80:
        strengths.append("Strong Communication Skills")

    if internships >= 2:
        strengths.append("Good Industry Exposure")

    if certifications >= 3:
        strengths.append("Well Certified")

    if projects >= 4:
        strengths.append("Good Project Experience")

    if strengths:
        for item in strengths:
            st.success(item)
    else:
        st.info("No major strengths detected")

    # ===============================
    # IMPROVEMENT AREAS
    # ===============================

    st.subheader("📈 Areas for Improvement")

    improvements = []

    if cgpa < 7.5:
        improvements.append(
            "Improve CGPA"
        )

    if aptitude_score < 75:
        improvements.append(
            "Practice Aptitude Tests"
        )

    if communication_score < 75:
        improvements.append(
            "Improve Communication Skills"
        )

    if internships < 1:
        improvements.append(
            "Complete Internships"
        )

    if certifications < 2:
        improvements.append(
            "Earn Certifications"
        )

    if projects < 3:
        improvements.append(
            "Build More Projects"
        )

    if improvements:

        for item in improvements:
            st.warning(item)

    else:
        st.success(
            "Profile looks strong"
        )

    # ===============================
    # RECOMMENDATION
    # ===============================

    st.subheader("🎯 Recommendation")

    if probability_percent >= 85:

        recommendation = """
        Your profile is highly competitive.

        Continue:
        • Practicing coding
        • Mock interviews
        • Resume building

        You have excellent placement chances.
        """

    elif probability_percent >= 60:

        recommendation = """
        Your placement chances are good.

        Focus on:
        • Aptitude preparation
        • Additional certifications
        • More projects

        These can significantly improve your chances.
        """

    else:

        recommendation = """
        Immediate improvement required.

        Focus on:
        • CGPA improvement
        • Aptitude training
        • Internship experience
        • Communication skills

        This can substantially increase eligibility.
        """

    st.info(recommendation)

    # ===============================
    # REPORT DOWNLOAD
    # ===============================

    st.subheader("📥 Download Prediction Report")

    report = pd.DataFrame({
        "Metric": [
            "Prediction",
            "Probability (%)",
            "CGPA",
            "Attendance",
            "Aptitude",
            "Communication",
            "Internships",
            "Certifications",
            "Projects",
            "Generated At"
        ],
        "Value": [
            "Eligible"
            if prediction == 1
            else "Not Eligible",
            probability_percent,
            cgpa,
            attendance,
            aptitude_score,
            communication_score,
            internships,
            certifications,
            projects,
            datetime.now()
        ]
    })

    csv = report.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Report",
        data=csv,
        file_name="placement_prediction_report.csv",
        mime="text/csv"
    )

# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.caption(
    "Placement Eligibility Predictor | Streamlit + Machine Learning"
)
