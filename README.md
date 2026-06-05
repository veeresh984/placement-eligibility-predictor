# Placement Eligibility Predictor

A Machine Learning-based web application that predicts whether a student is eligible for campus placements based on academic performance, technical skills, internships, projects, and aptitude scores.

---

## Project Overview

The Placement Eligibility Predictor helps students and training departments evaluate placement readiness using historical placement data and machine learning algorithms.

The application provides:

* Placement eligibility prediction
* Interactive dashboard
* Placement analytics
* Future placement trend forecasting
* Data visualization and insights

---

## Features

### Dashboard

* Overview of placement statistics
* Student performance summary
* Interactive charts and graphs

### Placement Predictor

* Input student details
* Predict placement eligibility
* Instant prediction results

### Analytics

* Placement trends analysis
* Skill-based insights
* Academic performance analysis
* Visual reports

### Future Predictor

* Future placement forecasting
* Trend prediction
* Placement probability analysis

---

## Project Structure

```text
placement-eligibility-predictor/
│
├── data/
│   └── placement_data.csv
│
├── models/
│   └── placement_model.pkl
│
├── app/
│   ├── pages/
│   │   ├── dashboard.py
│   │   ├── predictor.py
│   │   ├── analytics.py
│   │   └── future_predictor.py
│   │
│   ├── utils/
│   │   ├── charts.py
│   │   └── preprocessing.py
│   │
│   └── app.py
│
├── notebooks/
│   └── model_training.ipynb
│
├── requirements.txt
├── README.md
└── train_model.py
```

---

## Machine Learning Workflow

```text
Placement Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Save Model
        │
        ▼
Placement Prediction
```

---

## Dataset Description

The dataset contains student-related attributes used for placement prediction.

Example features:

| Feature             | Description                     |
| ------------------- | ------------------------------- |
| CGPA                | Academic performance            |
| Internships         | Number of internships completed |
| Projects            | Number of projects completed    |
| AptitudeScore       | Aptitude test score             |
| CommunicationSkills | Communication skill rating      |
| TechnicalSkills     | Technical skill rating          |
| Backlogs            | Number of active backlogs       |
| PlacementStatus     | Target variable                 |

Example:

| CGPA | Internships | Projects | AptitudeScore | CommunicationSkills | TechnicalSkills | Backlogs | PlacementStatus |
| ---- | ----------- | -------- | ------------- | ------------------- | --------------- | -------- | --------------- |
| 8.5  | 2           | 4        | 85            | 8                   | 9               | 0        | Placed          |
| 6.7  | 0           | 1        | 55            | 5                   | 6               | 2        | Not Placed      |

---

## Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn

### Data Processing

* Pandas
* NumPy

### Visualization

* Matplotlib
* Plotly

### Web Application

* Streamlit

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/placement-eligibility-predictor.git

cd placement-eligibility-predictor
```

### Create Virtual Environment

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Training the Model

Run:

```bash
python train_model.py
```

The script will:

1. Load dataset
2. Clean data
3. Preprocess features
4. Train model
5. Evaluate performance
6. Save trained model

Saved model:

```text
models/placement_model.pkl
```

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app/app.py
```

Application URL:

```text
http://localhost:8501
```

---

## Model Evaluation Metrics

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

Example output:

```text
Accuracy: 92.5%

Precision: 0.93
Recall: 0.91
F1 Score: 0.92
```

---

## Screenshots

### Dashboard

Add dashboard screenshot here.

### Predictor

Add prediction page screenshot here.

### Analytics

Add analytics page screenshot here.

### Future Predictor

Add future prediction screenshot here.

---

## Future Enhancements

* Deep Learning models
* Resume analysis
* Placement recommendation engine
* Company-specific eligibility prediction
* Student performance tracking
* PDF report generation
* Real-time analytics

---

## Requirements

Example `requirements.txt`

```text
streamlit
pandas
numpy
scikit-learn
matplotlib
plotly
joblib
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Author

Name: Your Name

GitHub: https://github.com/your-username

LinkedIn: https://linkedin.com/in/your-profile

---

## License

This project is licensed under the MIT License.

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files to deal in the Software without restriction.

