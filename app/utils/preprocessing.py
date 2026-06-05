import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib

# =====================================================
# LOAD DATASET
# =====================================================

def load_dataset(file_path):
    """
    Load placement dataset
    """

    try:
        df = pd.read_csv(file_path)
        return df

    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


# =====================================================
# BASIC CLEANING
# =====================================================

def clean_data(df):
    """
    Remove duplicates and null values
    """

    df = df.copy()

    df.drop_duplicates(inplace=True)

    df.fillna(0, inplace=True)

    return df


# =====================================================
# FEATURE ENGINEERING
# =====================================================

def create_performance_score(df):
    """
    Create composite performance score
    """

    df = df.copy()

    df["performance_score"] = (
        df["cgpa"] * 10
        + df["aptitude_score"] * 0.30
        + df["communication_score"] * 0.20
        + df["internships"] * 5
        + df["certifications"] * 3
        + df["projects"] * 2
    )

    return df


# =====================================================
# STUDENT SEGMENTATION
# =====================================================

def assign_student_segment(cgpa):
    """
    Categorize student based on CGPA
    """

    if cgpa >= 8.5:
        return "High Performer"

    elif cgpa >= 7.0:
        return "Average Performer"

    else:
        return "Needs Improvement"


def create_segments(df):

    df = df.copy()

    df["segment"] = df["cgpa"].apply(
        assign_student_segment
    )

    return df


# =====================================================
# PREPARE FEATURES
# =====================================================

def prepare_features(df):
    """
    Separate X and y
    """

    features = [
        "cgpa",
        "attendance",
        "aptitude_score",
        "communication_score",
        "internships",
        "certifications",
        "projects"
    ]

    X = df[features]

    y = df["placement_status"]

    return X, y


# =====================================================
# TRAIN TEST SPLIT
# =====================================================

def split_data(X, y):

    return train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )


# =====================================================
# SCALE FEATURES
# =====================================================

def scale_features(
        X_train,
        X_test,
        save_scaler=True
):

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(
        X_train
    )

    X_test_scaled = scaler.transform(
        X_test
    )

    if save_scaler:

        joblib.dump(
            scaler,
            "models/scaler.pkl"
        )

    return (
        X_train_scaled,
        X_test_scaled,
        scaler
    )


# =====================================================
# LOAD SAVED SCALER
# =====================================================

def load_scaler():

    try:

        scaler = joblib.load(
            "models/scaler.pkl"
        )

        return scaler

    except:

        return None


# =====================================================
# TRANSFORM SINGLE INPUT
# =====================================================

def preprocess_student_input(
        cgpa,
        attendance,
        aptitude_score,
        communication_score,
        internships,
        certifications,
        projects
):

    input_df = pd.DataFrame({
        "cgpa": [cgpa],
        "attendance": [attendance],
        "aptitude_score": [aptitude_score],
        "communication_score": [communication_score],
        "internships": [internships],
        "certifications": [certifications],
        "projects": [projects]
    })

    scaler = load_scaler()

    if scaler is not None:

        scaled_data = scaler.transform(
            input_df
        )

        return scaled_data

    return input_df


# =====================================================
# GENERATE PROFILE SCORE
# =====================================================

def calculate_profile_strength(
        cgpa,
        aptitude,
        communication,
        internships,
        certifications,
        projects
):

    score = (
        cgpa * 10
        + aptitude * 0.30
        + communication * 0.20
        + internships * 5
        + certifications * 3
        + projects * 2
    )

    return round(score, 2)


# =====================================================
# ELIGIBILITY LEVEL
# =====================================================

def get_eligibility_level(probability):

    if probability >= 85:
        return "Excellent"

    elif probability >= 70:
        return "Good"

    elif probability >= 50:
        return "Moderate"

    else:
        return "Needs Improvement"


# =====================================================
# IMPROVEMENT RECOMMENDATIONS
# =====================================================

def generate_recommendations(
        cgpa,
        aptitude,
        communication,
        internships,
        certifications,
        projects
):

    recommendations = []

    if cgpa < 8:
        recommendations.append(
            "Improve CGPA above 8.0"
        )

    if aptitude < 80:
        recommendations.append(
            "Practice aptitude regularly"
        )

    if communication < 80:
        recommendations.append(
            "Improve communication skills"
        )

    if internships < 2:
        recommendations.append(
            "Complete more internships"
        )

    if certifications < 3:
        recommendations.append(
            "Earn additional certifications"
        )

    if projects < 4:
        recommendations.append(
            "Build industry-level projects"
        )

    return recommendations


# =====================================================
# FUTURE PROBABILITY SIMULATION
# =====================================================

def simulate_future_growth(
        current_probability,
        future_probability
):

    growth = []

    periods = [
        "Current",
        "3 Months",
        "6 Months",
        "9 Months",
        "12 Months"
    ]

    values = np.linspace(
        current_probability,
        future_probability,
        len(periods)
    )

    for period, value in zip(
            periods,
            values):

        growth.append({
            "Period": period,
            "Probability": round(value, 2)
        })

    return pd.DataFrame(growth)


# =====================================================
# SUMMARY REPORT
# =====================================================

def generate_summary_report(df):

    report = {
        "Total Students": len(df),

        "Eligible Students":
        len(df[df["placement_status"] == 1]),

        "Non Eligible Students":
        len(df[df["placement_status"] == 0]),

        "Average CGPA":
        round(df["cgpa"].mean(), 2),

        "Average Aptitude":
        round(df["aptitude_score"].mean(), 2),

        "Average Communication":
        round(df["communication_score"].mean(), 2)
    }

    return report


# =====================================================
# TOP STUDENTS
# =====================================================

def get_top_students(
        df,
        top_n=10
):

    temp = create_performance_score(df)

    return temp.sort_values(
        by="performance_score",
        ascending=False
    ).head(top_n)


# =====================================================
# SAVE FEATURE LIST
# =====================================================

def save_feature_names():

    features = [
        "cgpa",
        "attendance",
        "aptitude_score",
        "communication_score",
        "internships",
        "certifications",
        "projects"
    ]

    joblib.dump(
        features,
        "models/features.pkl"
    )

    return features


# =====================================================
# LOAD FEATURE LIST
# =====================================================

def load_feature_names():

    try:

        return joblib.load(
            "models/features.pkl"
        )

    except:

        return [
            "cgpa",
            "attendance",
            "aptitude_score",
            "communication_score",
            "internships",
            "certifications",
            "projects"
        ]
