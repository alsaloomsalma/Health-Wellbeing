# app.py

import streamlit as st
import pandas as pd
import joblib

# ✅ Set page config FIRST
st.set_page_config(page_title="Work-Life Balance Predictor", layout="centered")

# ✅ Dark mode styling with light text
st.markdown("""
<style>
/* Set background and text color */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #1e1e1e;
    color: #f5f5f5;
}

/* Text elements */
h1, h2, h3, h4, h5, h6, p, label, div, span {
    color: #f5f5f5 !important;
}

/* Selectbox dropdown options */
div[data-baseweb="select"] {
    background-color: #2b2b2b !important;
    color: #f5f5f5 !important;
}

/* Tooltip (help text) */
[data-testid="stHelpIcon"] svg {
    stroke: #f5f5f5;
}
[data-testid="stMarkdownContainer"] {
    color: #f5f5f5;
}

/* Buttons */
.stButton > button {
    background-color: #74c69d;
    color: white;
    border-radius: 8px;
    padding: 0.5em 1em;
}
.stButton > button:hover {
    background-color: #52b788;
}
</style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("work_life_model.pkl")

# App content
st.title("🌿 Work-Life Balance Predictor")
st.markdown("""
    Enter your lifestyle and wellbeing habits below to predict your **work-life balance category**.
    This tool is based on a machine learning model trained on real wellbeing and lifestyle data.
""")

st.markdown("---")

# ----------------- USER INPUTS -----------------

st.header("🧍 Personal Info")
age = st.selectbox("Age Group", ['less than 20', '20 to 35', '36 to 50', '51 or more'],
                   help="Your age group helps provide context for activity levels and lifestyle expectations.")
gender = st.selectbox("Gender", ['Male', 'Female', 'Other'],
                      help="Used only for trend calibration — your experience matters regardless of gender.")
daily_stress = st.selectbox("Daily Stress Level", ['none', 'low', 'medium', 'high', 'very high'],
                            help="How often you feel mentally or emotionally stressed on a typical day.")

st.header("🍎 Lifestyle Habits")
fruits_veggies = st.slider("Fruit & Veggie Servings per Day", 0, 10, 3,
                           help="How many servings of fruits and vegetables you consume daily.")
daily_steps = st.slider("Daily Steps", 0, 20000, 6000, step=500,
                        help="Your average number of steps walked each day.")
sleep_hours = st.slider("Sleep Hours per Night", 0, 12, 7,
                         help="Your average number of hours of sleep each night.")
weekly_meditation = st.slider("Weekly Meditation Hours", 0, 20, 2,
                               help="Estimated time you spend in mindfulness, meditation, or stillness per week.")
bmi_range = st.selectbox("BMI Range", [1, 2, 3],
                         help="1 = Underweight/Healthy, 2 = Overweight, 3 = Obese (for model calibration only)")

st.header("🧠 Social & Mental Wellbeing")
places_visited = st.slider("Places Visited (per Month)", 0, 10, 2,
                            help="How many distinct places you go outside your home each month.")
core_circle = st.slider("Number of Close Friends", 0, 10, 5,
                        help="People you trust and confide in regularly.")
supporting_others = st.slider("Support Given to Others", 0, 10, 5,
                               help="How much emotional or practical support you offer others.")
social_network = st.slider("Social Network Score", 0, 10, 6,
                            help="Overall strength of your broader social connections (e.g., acquaintances, community).")
live_vision = st.slider("Clarity of Life Vision", 0, 10, 3,
                         help="How clear your goals and long-term purpose feel to you.")
daily_shouting = st.slider("Shouting Episodes per Day", 0, 10, 1,
                            help="Number of times per day you raise your voice due to anger or frustration.")

st.header("💼 Productivity & Finances")
achievement = st.slider("Achievement Score", 0, 10, 4,
                        help="How much you feel you accomplish what matters to you.")
donation = st.slider("Donation Score", 0, 10, 2,
                     help="How much you give back — financially or through volunteering.")
todo_completed = st.slider("Task Completion Score", 0, 10, 4,
                            help="How consistently you complete your daily to-do list.")
flow = st.slider("Flow Score", 0, 10, 3,
                 help="How often you feel fully absorbed and focused in your work or hobbies.")
lost_vacation = st.slider("Days of Vacation Lost", 0, 20, 2,
                          help="Days of entitled vacation you haven't taken this year.")
sufficient_income = st.selectbox("Do You Have Sufficient Income?", [1, 2],
                                  help="1 = Yes, 2 = No — this helps capture financial stress.")
personal_awards = st.slider("Personal Awards Score", 0, 10, 2,
                             help="Recognition you've received for personal or professional efforts.")
time_for_passion = st.slider("Time for Passion Projects", 0, 10, 3,
                              help="How much time you have for hobbies, creative outlets, or learning.")

st.markdown("---")

# ----------------- PREDICTION -----------------

if st.button("🔍 Predict Work-Life Balance Category"):
    input_data = pd.DataFrame({
        'DAILY_STRESS': [daily_stress],
        'AGE': [age],
        'GENDER': [gender],
        'FRUITS_VEGGIES': [fruits_veggies],
        'PLACES_VISITED': [places_visited],
        'CORE_CIRCLE': [core_circle],
        'SUPPORTING_OTHERS': [supporting_others],
        'SOCIAL_NETWORK': [social_network],
        'ACHIEVEMENT': [achievement],
        'DONATION': [donation],
        'BMI_RANGE': [bmi_range],
        'TODO_COMPLETED': [todo_completed],
        'FLOW': [flow],
        'DAILY_STEPS': [daily_steps],
        'LIVE_VISION': [live_vision],
        'SLEEP_HOURS': [sleep_hours],
        'LOST_VACATION': [lost_vacation],
        'DAILY_SHOUTING': [daily_shouting],
        'SUFFICIENT_INCOME': [sufficient_income],
        'PERSONAL_AWARDS': [personal_awards],
        'TIME_FOR_PASSION': [time_for_passion],
        'WEEKLY_MEDITATION': [weekly_meditation],
    })

    prediction = model.predict(input_data)[0]
    st.success(f"🏷️ **Predicted Category:** {prediction}")

    if prediction == "Low":
        st.warning("⚠️ Your work-life balance may be under strain. Consider improving stress levels, sleep, movement, and self-reflection.")
        st.markdown("""
        **Recommendations:**
        - Sleep at least 7–8 hours.
        - Aim for 6,000–10,000 steps per day.
        - Eat more fruits & vegetables.
        - Avoid excessive shouting; manage stress responses.
        - Journal or review your life vision monthly.
        - Try passion projects or meditative hobbies.
        """)

    elif prediction == "Medium":
        st.info("🟨 You're doing okay — but there's room for improvement. Focus on consistency, social support, and mental clarity.")
        st.markdown("""
        **Recommendations:**
        - Maintain sleep & step targets.
        - Grow core friend circle.
        - Celebrate small tasks & wins (achievement).
        - Practice mindfulness & reconnect with life goals.
        - Block time for meaningful work or hobbies.
        """)

    elif prediction == "High":
        st.success("✅ Excellent! Your lifestyle reflects strong balance.")
        st.markdown("""
        **Keep it up:**
        - Sustain strong routines.
        - Support others and spread balance culture.
        - Keep revisiting your passion and personal growth.
        """)

    if hasattr(model.named_steps['classifier'], "predict_proba"):
        proba = model.predict_proba(input_data)[0]
        labels = model.named_steps['classifier'].classes_
        st.markdown("**Prediction Probabilities:**")
        for label, prob in zip(labels, proba):
            st.write(f"- {label}: {prob:.2%}")

    with st.expander("📘 What do these results mean?"):
        st.markdown("""
        The model classifies your **Work-Life Balance** into:

        - 🟥 **Low**: Possible burnout or unmet personal needs.
        - 🟨 **Medium**: Balanced at times, but inconsistent.
        - 🟩 **High**: Strong habits and personal wellbeing alignment.
        """)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Model trained on lifestyle + wellbeing data")