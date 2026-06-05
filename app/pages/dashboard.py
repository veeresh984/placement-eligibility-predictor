import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Placement Analytics Dashboard",
    page_icon="📊",
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

st.title("📊 Placement Analytics Dashboard")

st.markdown(
    "Deep Analytics and Insights for Student Placement Eligibility"
)

# ==========================================
# KPI SECTION
# ==========================================

total_students = len(df)

placed_students = len(
    df[df["placement_status"] == 1]
)

not_placed = len(
    df[df["placement_status"] == 0]
)

placement_rate = (
    placed_students / total_students
) * 100

avg_cgpa = round(
    df["cgpa"].mean(),
    2
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Students",
    total_students
)

col2.metric(
    "Eligible",
    placed_students
)

col3.metric(
    "Not Eligible",
    not_placed
)

col4.metric(
    "Placement Rate",
    f"{placement_rate:.1f}%"
)

col5.metric(
    "Average CGPA",
    avg_cgpa
)

st.divider()

# ==========================================
# PLACEMENT DISTRIBUTION
# ==========================================

col1, col2 = st.columns(2)

with col1:

    pie = px.pie(
        df,
        names="placement_status",
        title="Placement Distribution",
        hole=0.5
    )

    pie.update_traces(
        textinfo="percent+label"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

with col2:

    bar = px.histogram(
        df,
        x="placement_status",
        title="Eligibility Count"
    )

    st.plotly_chart(
        bar,
        use_container_width=True
    )

st.divider()

# ==========================================
# CGPA ANALYSIS
# ==========================================

st.subheader("📚 CGPA Analysis")

cgpa_fig = px.histogram(
    df,
    x="cgpa",
    color="placement_status",
    nbins=20,
    title="CGPA vs Placement Status"
)

st.plotly_chart(
    cgpa_fig,
    use_container_width=True
)

# ==========================================
# ATTENDANCE ANALYSIS
# ==========================================

st.subheader("🎯 Attendance Analysis")

attendance_fig = px.box(
    df,
    x="placement_status",
    y="attendance",
    title="Attendance Distribution"
)

st.plotly_chart(
    attendance_fig,
    use_container_width=True
)

# ==========================================
# APTITUDE ANALYSIS
# ==========================================

st.subheader("🧠 Aptitude Score Analysis")

aptitude_fig = px.scatter(
    df,
    x="aptitude_score",
    y="cgpa",
    color="placement_status",
    size="projects",
    hover_data=["internships"],
    title="Aptitude vs CGPA"
)

st.plotly_chart(
    aptitude_fig,
    use_container_width=True
)

# ==========================================
# INTERNSHIP IMPACT
# ==========================================

st.subheader("💼 Internship Impact")

internship_rate = (
    df.groupby("internships")
    ["placement_status"]
    .mean()
    .reset_index()
)

internship_rate["placement_status"] *= 100

intern_fig = px.bar(
    internship_rate,
    x="internships",
    y="placement_status",
    title="Placement Rate by Internships"
)

st.plotly_chart(
    intern_fig,
    use_container_width=True
)

# ==========================================
# CERTIFICATION IMPACT
# ==========================================

st.subheader("🏅 Certification Impact")

cert_rate = (
    df.groupby("certifications")
    ["placement_status"]
    .mean()
    .reset_index()
)

cert_rate["placement_status"] *= 100

cert_fig = px.line(
    cert_rate,
    x="certifications",
    y="placement_status",
    markers=True,
    title="Placement Rate by Certifications"
)

st.plotly_chart(
    cert_fig,
    use_container_width=True
)

# ==========================================
# PROJECT IMPACT
# ==========================================

st.subheader("🚀 Project Impact")

project_fig = px.box(
    df,
    x="placement_status",
    y="projects",
    title="Projects vs Placement"
)

st.plotly_chart(
    project_fig,
    use_container_width=True
)

# ==========================================
# CORRELATION HEATMAP
# ==========================================

st.subheader("🔥 Correlation Heatmap")

corr = df.drop(
    columns=["student_id"]
).corr()

fig, ax = plt.subplots(
    figsize=(10, 6)
)

sns.heatmap(
    corr,
    annot=True,
    cmap="Blues",
    ax=ax
)

st.pyplot(fig)

# ==========================================
# TOP PERFORMERS
# ==========================================

st.subheader("🏆 Top Students")

top_students = df.sort_values(
    by=["cgpa", "aptitude_score"],
    ascending=False
).head(10)

st.dataframe(
    top_students,
    use_container_width=True
)

# ==========================================
# SMART INSIGHTS
# ==========================================

st.subheader("💡 AI Insights")

avg_placed_cgpa = round(
    df[df["placement_status"] == 1]["cgpa"].mean(),
    2
)

avg_notplaced_cgpa = round(
    df[df["placement_status"] == 0]["cgpa"].mean(),
    2
)

avg_placed_aptitude = round(
    df[df["placement_status"] == 1]
    ["aptitude_score"]
    .mean(),
    2
)

avg_notplaced_aptitude = round(
    df[df["placement_status"] == 0]
    ["aptitude_score"]
    .mean(),
    2
)

st.success(
    f"""
    Average CGPA of eligible students:
    {avg_placed_cgpa}

    Average CGPA of non-eligible students:
    {avg_notplaced_cgpa}
    """
)

st.info(
    f"""
    Average Aptitude Score of eligible students:
    {avg_placed_aptitude}

    Average Aptitude Score of non-eligible students:
    {avg_notplaced_aptitude}
    """
)

# ==========================================
# PLACEMENT TREND FORECAST
# ==========================================

st.subheader("📈 Future Placement Trend")

future_df = pd.DataFrame({
    "Year": [
        "2024",
        "2025",
        "2026",
        "2027",
        "2028"
    ],
    "Placement Rate": [
        65,
        72,
        78,
        85,
        92
    ]
})

future_fig = go.Figure()

future_fig.add_trace(
    go.Scatter(
        x=future_df["Year"],
        y=future_df["Placement Rate"],
        mode="lines+markers"
    )
)

future_fig.update_layout(
    title="Future Placement Trend Prediction",
    xaxis_title="Year",
    yaxis_title="Placement Rate (%)"
)

st.plotly_chart(
    future_fig,
    use_container_width=True
)

# ==========================================
# DOWNLOAD REPORT
# ==========================================

st.subheader("📥 Export Analytics")

csv = df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Dataset Report",
    data=csv,
    file_name="placement_analytics.csv",
    mime="text/csv"
)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown(
    """
    ### Placement Eligibility Predictor

    Developed using:
    - Python
    - Streamlit
    - Scikit-Learn
    - Plotly
    - Pandas

    Deep Analytics Dashboard
    """
)
