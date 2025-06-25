
import streamlit as st
import datetime

st.title("🎯 Challenge instellen")

activiteiten = ["Wandelen", "Fietsen", "Hardlopen"]
activiteit = st.selectbox("Kies een activiteit", activiteiten)
start = st.date_input("Startdatum", value=datetime.date.today())
einde = st.date_input("Einddatum", value=datetime.date.today() + datetime.timedelta(days=7))
punten = st.number_input("Punten per km", value=1.0)
bonus_drempel = st.number_input("Bonus vanaf (km)", value=5.0)
bonus = st.number_input("Bonuspunten per extra km", value=2.0)

if st.button("✅ Challenge opslaan"):
    st.success(f"Challenge ingesteld: {activiteit} van {start} t/m {einde}")
    st.info(f"🏅 {punten} pt/km — bonus vanaf {bonus_drempel}km → +{bonus}/km")
