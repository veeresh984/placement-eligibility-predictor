import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Advanced Analytics",
    page_icon="📈",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

@st.cache_data
def load_data():
    return pd.read_csv("data/placement_data.csv")

df = load_data()

# ==========================================
# TITLE
# ==========================================

st.title("📈 Advanced Placement Analytics")

st.markdown("""
Deep Analytics Dashboard for Placement Eligibility Analysis
""")

st.divider()

# ==========================================
# FILTERS
# ==========================================

st.sidebar.header("Filters")

cgpa_filter = st.sidebar.slider(
    "Minimum CGPA",
    0.0,
    10.0,
    0.0
)

attendance_filter = st.sidebar.slider(
    "Minimum Attendance",
    0,
    100,
    0
)

filtered_df = df[
    (df["cgpa"] >= cgpa_filter)
    &
    (df["attendance"] >= attendance_filter)
]

# ==========================================
# KPI SECTION
# ==========================================

total_students = len(filtered_df)

placed = len(
    filtered_df[
        filtered_df["placement_status"] == 1
    ]
)

placement_rate = (
    placed / total_students * 100
    if total_students > 0 else 0
)

avg_cgpa = round(
    filtered_df["cgpa"].mean(),
    2
)

avg_aptitude = round(
    filtered_df["aptitude_score"].mean(),
    2
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Students",
    total_students
)

col2.metric(
    "Eligible",
    placed
)

col3.metric(
    "Placement Rate",
    f"{placement_rate:.2f}%"
)

col4.metric(
    "Avg CGPA",
    avg_cgpa
)

st.divider()

# ==========================================
# ELIGIBILITY DISTRIBUTION
# ==========================================

col1, col2 = st.columns(2)

with col1:

    fig = px.pie(
        filtered_df,
        names="placement_status",
        title="Placement Distribution",
        hole=0.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    fig = px.histogram(
        filtered_df,
        x="cgpa",
        color="placement_status",
        nbins=20,
        title="CGPA Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================
# CGPA VS APTITUDE
# ==========================================

st.subheader("📊 CGPA vs Aptitude Analysis")

fig = px.scatter(
    filtered_df,
    x="cgpa",
    y="aptitude_score",
    color="placement_status",
    size="projects",
    hover_data=[
        "internships",
        "certifications"
    ],
    title="CGPA vs Aptitude Score"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# INTERNSHIP IMPACT
# ==========================================

st.subheader("💼 Internship Impact")

internship_analysis = (
    filtered_df
    .groupby("internships")
    ["placement_status"]
    .mean()
    .reset_index()
)

internship_analysis[
    "placement_status"
] *= 100

fig = px.bar(
    internship_analysis,
    x="internships",
    y="placement_status",
    title="Placement Rate by Internship Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# CERTIFICATION IMPACT
# ==========================================

st.subheader("🏅 Certification Impact")

cert_analysis = (
    filtered_df
    .groupby("certifications")
    ["placement_status"]
    .mean()
    .reset_index()
)

cert_analysis[
    "placement_status"
] *= 100

fig = px.line(
    cert_analysis,
    x="certifications",
    y="placement_status",
    markers=True,
    title="Placement Rate by Certifications"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# COMMUNICATION ANALYSIS
# ==========================================

st.subheader("🗣 Communication Skills Analysis")

fig = px.box(
    filtered_df,
    x="placement_status",
    y="communication_score",
    title="Communication Score Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# ATTENDANCE ANALYSIS
# ==========================================

st.subheader("🎯 Attendance Analysis")

fig = px.violin(
    filtered_df,
    y="attendance",
    x="placement_status",
    box=True,
    title="Attendance Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# CORRELATION MATRIX
# ==========================================

st.subheader("🔥 Feature Correlation Matrix")

corr = filtered_df.drop(
    columns=["student_id"]
).corr()

fig = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    title="Correlation Heatmap"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# STUDENT SEGMENTATION
# ==========================================

st.subheader("🎓 Student Segmentation")

conditions = [
    filtered_df["cgpa"] >= 8.5,
    (filtered_df["cgpa"] >= 7.0)
    & (filtered_df["cgpa"] < 8.5),
    filtered_df["cgpa"] < 7.0
]

labels = [
    "High Performer",
    "Average Performer",
    "Needs Improvement"
]

filtered_df["segment"] = np.select(
    conditions,
    labels,
    default="Unknown"
)

segment_count = (
    filtered_df["segment"]
    .value_counts()
    .reset_index()
)

segment_count.columns = [
    "Segment",
    "Count"
]

fig = px.bar(
    segment_count,
    x="Segment",
    y="Count",
    title="Student Segmentation"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# PERFORMANCE SCORE
# ==========================================

st.subheader("⭐ Composite Performance Score")

filtered_df["performance_score"] = (
    filtered_df["cgpa"] * 10
    + filtered_df["aptitude_score"] * 0.3
    + filtered_df["communication_score"] * 0.2
    + filtered_df["internships"] * 5
    + filtered_df["certifications"] * 3
    + filtered_df["projects"] * 2
)

fig = px.histogram(
    filtered_df,
    x="performance_score",
    nbins=25,
    title="Performance Score Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# TOP STUDENTS
# ==========================================

st.subheader("🏆 Top 20 Students")

top_students = filtered_df.sort_values(
    by="performance_score",
    ascending=False
).head(20)

st.dataframe(
    top_students,
    use_container_width=True
)

# ==========================================
# AI INSIGHTS
# ==========================================

st.subheader("🤖 Smart Insights")

best_cgpa = round(
    filtered_df[
        filtered_df["placement_status"] == 1
    ]["cgpa"].mean(),
    2
)

best_aptitude = round(
    filtered_df[
        filtered_df["placement_status"] == 1
    ]["aptitude_score"].mean(),
    2
)

best_comm = round(
    filtered_df[
        filtered_df["placement_status"] == 1
    ]["communication_score"].mean(),
    2
)

st.success(
    f"""
    Students who are eligible typically have:

    • Average CGPA: {best_cgpa}

    • Average Aptitude Score: {best_aptitude}

    • Average Communication Score: {best_comm}
    """
)

# ==========================================
# EXECUTIVE SUMMARY
# ==========================================

st.subheader("📑 Executive Summary")

summary = pd.DataFrame({
    "Metric": [
        "Total Students",
        "Eligible Students",
        "Placement Rate",
        "Average CGPA",
        "Average Aptitude"
    ],
    "Value": [
        total_students,
        placed,
        f"{placement_rate:.2f}%",
        avg_cgpa,
        avg_aptitude
    ]
})

st.table(summary)

# ==========================================
# DOWNLOAD REPORT
# ==========================================

st.subheader("📥 Download Analytics Report")

csv = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Analytics Data",
    data=csv,
    file_name="placement_analytics_report.csv",
    mime="text/csv"
)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Advanced Placement Analytics Dashboard | Streamlit + Machine Learning"
)
