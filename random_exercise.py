import streamlit as st
import random

chest_exercises = ["Pec Deck", "Bench Press", "Incline Bench Press"]
tricep_exercises = ["Tricep Pressdown", "Overhead Extensions", "Tricep Kickback", "Dips"]
back_exercises = ["Pull Ups", "T-Bar Row", "Lat Pull Down", "Isolateral Rows"]
bicep_exercises = ["Hammer Curls", "Preacher Curls", "Bayesian Cable curls", "Bicep Curls", "Inclined Dumbell Curl"]
leg_exercises = ["Leg Press", "Hamstring Curls", "Leg Extensions", "Calf Raises", "Walking Lunge", ]
shoulder_exercises = ["Machine Shoulder Press", "Inclined Dumbell Y Raise", "Upright Row", "Cable Lateral Raise", "Dumbell Shrugs", "Reverse Cable Crossovers"]
cardio_exercises = ["Cycling", "Rowing", "Elliptical", "Treadmill"]

st.title("Workout Randomizer")

day = st.selectbox("Choose workout day:", ["push", "pull", "legs and shoulder", "cardio"])

if st.button("Generate Workout"):
    if day == "push":
        st.write("Chest:", random.sample(chest_exercises, 2))
        st.write("Triceps:", random.sample(tricep_exercises, 2))
    elif day == "pull":
        st.write("Back:", random.sample(back_exercises, 2))
        st.write("Biceps:", random.sample(bicep_exercises, 2))
    elif day == "legs and shoulder":
        st.write("Shoulders:", random.sample(shoulder_exercises, 2))
        st.write("Legs:", random.sample(leg_exercises, 2))
    elif day == "cardio": 
        st.write("Cardio:", random.sample(cardio_exercises, 3))
