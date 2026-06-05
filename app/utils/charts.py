import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# ==================================================
# KPI GAUGE CHART
# ==================================================

def create_gauge_chart(value, title):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={"text": title},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"thickness": 0.25},
                "steps": [
                    {
                        "range": [0, 40],
                        "color": "#ff6b6b"
                    },
                    {
                        "range": [40, 70],
                        "color": "#ffd93d"
                    },
                    {
                        "range": [70, 100],
                        "color": "#6bcB77"
                    }
                ]
            }
        )
    )

    fig.update_layout(
        height=350
    )

    return fig


# ==================================================
# PLACEMENT PIE CHART
# ==================================================

def placement_distribution(df):

    fig = px.pie(
        df,
        names="placement_status",
        hole=0.5,
        title="Placement Distribution"
    )

    fig.update_traces(
        textinfo="percent+label"
    )

    return fig


# ==================================================
# CGPA HISTOGRAM
# ==================================================

def cgpa_histogram(df):

    fig = px.histogram(
        df,
        x="cgpa",
        color="placement_status",
        nbins=20,
        title="CGPA Distribution"
    )

    return fig


# ==================================================
# APTITUDE HISTOGRAM
# ==================================================

def aptitude_histogram(df):

    fig = px.histogram(
        df,
        x="aptitude_score",
        color="placement_status",
        nbins=20,
        title="Aptitude Score Distribution"
    )

    return fig


# ==================================================
# ATTENDANCE HISTOGRAM
# ==================================================

def attendance_histogram(df):

    fig = px.histogram(
        df,
        x="attendance",
        color="placement_status",
        nbins=20,
        title="Attendance Analysis"
    )

    return fig


# ==================================================
# SCATTER ANALYSIS
# ==================================================

def cgpa_vs_aptitude(df):

    fig = px.scatter(
        df,
        x="cgpa",
        y="aptitude_score",
        color="placement_status",
        size="projects",
        hover_data=[
            "internships",
            "certifications"
        ],
        title="CGPA vs Aptitude"
    )

    return fig


# ==================================================
# INTERNSHIP IMPACT
# ==================================================

def internship_impact(df):

    data = (
        df.groupby("internships")
        ["placement_status"]
        .mean()
        .reset_index()
    )

    data["placement_status"] *= 100

    fig = px.bar(
        data,
        x="internships",
        y="placement_status",
        title="Placement Rate by Internship Count"
    )

    return fig


# ==================================================
# CERTIFICATION IMPACT
# ==================================================

def certification_impact(df):

    data = (
        df.groupby("certifications")
        ["placement_status"]
        .mean()
        .reset_index()
    )

    data["placement_status"] *= 100

    fig = px.line(
        data,
        x="certifications",
        y="placement_status",
        markers=True,
        title="Certification Impact"
    )

    return fig


# ==================================================
# PROJECT IMPACT
# ==================================================

def project_impact(df):

    fig = px.box(
        df,
        x="placement_status",
        y="projects",
        title="Projects vs Placement"
    )

    return fig


# ==================================================
# COMMUNICATION ANALYSIS
# ==================================================

def communication_analysis(df):

    fig = px.box(
        df,
        x="placement_status",
        y="communication_score",
        title="Communication Skill Analysis"
    )

    return fig


# ==================================================
# CORRELATION HEATMAP
# ==================================================

def correlation_heatmap(df):

    corr = df.drop(
        columns=["student_id"],
        errors="ignore"
    ).corr(numeric_only=True)

    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        title="Correlation Matrix"
    )

    return fig


# ==================================================
# STUDENT SEGMENTATION
# ==================================================

def student_segmentation(df):

    segmented_df = df.copy()

    segmented_df["segment"] = pd.cut(
        segmented_df["cgpa"],
        bins=[0, 7, 8.5, 10],
        labels=[
            "Needs Improvement",
            "Average",
            "High Performer"
        ]
    )

    segment_data = (
        segmented_df["segment"]
        .value_counts()
        .reset_index()
    )

    segment_data.columns = [
        "Segment",
        "Count"
    ]

    fig = px.bar(
        segment_data,
        x="Segment",
        y="Count",
        title="Student Segmentation"
    )

    return fig


# ==================================================
# PERFORMANCE SCORE DISTRIBUTION
# ==================================================

def performance_distribution(df):

    temp = df.copy()

    temp["performance_score"] = (
        temp["cgpa"] * 10
        + temp["aptitude_score"] * 0.3
        + temp["communication_score"] * 0.2
        + temp["internships"] * 5
        + temp["certifications"] * 3
        + temp["projects"] * 2
    )

    fig = px.histogram(
        temp,
        x="performance_score",
        nbins=25,
        title="Performance Score Distribution"
    )

    return fig


# ==================================================
# FUTURE GROWTH CHART
# ==================================================

def future_growth_chart(
        current_probability,
        future_probability
):

    periods = [
        "Current",
        "3 Months",
        "6 Months",
        "9 Months",
        "12 Months"
    ]

    growth = [
        current_probability,
        current_probability +
        ((future_probability -
          current_probability) * 0.25),

        current_probability +
        ((future_probability -
          current_probability) * 0.50),

        current_probability +
        ((future_probability -
          current_probability) * 0.75),

        future_probability
    ]

    fig = px.line(
        x=periods,
        y=growth,
        markers=True,
        title="Future Placement Growth Forecast"
    )

    fig.update_layout(
        xaxis_title="Timeline",
        yaxis_title="Probability (%)"
    )

    return fig


# ==================================================
# FEATURE IMPORTANCE CHART
# ==================================================

def feature_importance_chart(
        feature_names,
        importance_values
):

    imp_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importance_values
    })

    imp_df = imp_df.sort_values(
        by="Importance",
        ascending=False
    )

    fig = px.bar(
        imp_df,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Feature Importance"
    )

    return fig


# ==================================================
# IMPROVEMENT CONTRIBUTION
# ==================================================

def improvement_chart(df):

    fig = px.bar(
        df,
        x="Factor",
        y="Improvement",
        title="Improvement Contribution"
    )

    return fig
