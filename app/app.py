import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Title
st.set_page_config(page_title="AI Life Copilot", layout="centered")

st.title("AI Life Copilot")
st.markdown("### Predict student performance & get AI-powered suggestions")

# Inputs
st.subheader("Enter Student Details")

col1, col2 = st.columns(2)

with col1:
    studytime = st.slider("Study Time (1-4)", 1, 4)
    absences = st.slider("Absences", 0, 30)

with col2:
    sleep_hours = st.slider("Sleep Hours", 4, 9)
    goout = st.slider("Social Activity (1-5)", 1, 5)

# Dummy model training (same logic as notebook)
# Load data
try:
    df = pd.read_csv("data/student_data.csv")
    st.write(" Data loaded successfully")
except Exception as e:
    st.error(f"Error loading data: {e}")

df['performance'] = df['G3'].apply(lambda x: 1 if x >= 10 else 0)

df['sleep_hours'] = np.random.randint(4, 9, size=len(df))
df['screen_time'] = np.random.randint(2, 8, size=len(df))
df['stress_level'] = np.random.randint(1, 10, size=len(df))

features = [
    'studytime','failures','absences','goout',
    'Dalc','Walc','health',
    'sleep_hours','screen_time','stress_level'
]

X = df[features]
y = df['performance']

model = RandomForestClassifier()
model.fit(X, y)

# Prediction
if st.button(" Predict Performance"):

    input_data = [[studytime, 0, absences, goout, 1, 1, 5, sleep_hours, 3, 5]]

    prediction = model.predict(input_data)[0]

    st.subheader(" Prediction Result")

    if prediction == 1:
        st.success(" Student is likely to perform well")
    else:
        st.error(" Student is at risk")

    st.subheader(" AI Suggestions")

    suggestions = []

    if studytime < 2:
        suggestions.append("Increase study time")

    if absences > 10:
        suggestions.append("Reduce absences")

    if sleep_hours < 6:
        suggestions.append("Improve sleep schedule")

    if goout > 3:
        suggestions.append("Reduce social outings")

    if suggestions:
        for s in suggestions:
            st.write("•", s)
    else:
        st.write("No major issues detected ")

    # Suggestions
    st.subheader("AI Suggestions")

    if studytime < 2:
        st.write("- Increase study time")

    if absences > 10:
        st.write("- Reduce absences")

    if sleep_hours < 6:
        st.write("- Improve sleep schedule")

    if goout > 3:
        st.write("- Reduce social outings")