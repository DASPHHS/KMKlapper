
import streamlit as st
import datetime

st.set_page_config(page_title="Kilometerklapper", layout="wide")

st.title("🚀 Kilometerklapper")

# Groep aanmaken
st.header("1. Maak je groep aan")
groep = st.text_input("Groepsnaam", placeholder="Bijv. 2B of Running Club")
beheerder = st.text_input("Jouw naam (beheerder)")

# Punteninstellingen
st.header("2. Stel je puntensysteem in")
punten_per_km = st.number_input("Aantal punten per kilometer", min_value=0.0, value=1.0)
bonus_drempel = st.number_input("Bonus vanaf hoeveel km?", min_value=0.0, value=5.0)
bonus_per_km = st.number_input("Aantal bonuspunten per extra km", min_value=0.0, value=2.0)

# Periode
st.header("3. Kies de looptijd van de challenge")
start_datum = st.date_input("Startdatum", value=datetime.date.today())
eind_datum = st.date_input("Einddatum", value=datetime.date.today() + datetime.timedelta(days=7))

# Opslaan
if st.button("✅ Start challenge"):
    st.success(f"Challenge gestart voor groep **{groep}** door **{beheerder}**!")
    st.info(f"Punten: {punten_per_km} pt/km | Bonus: vanaf {bonus_drempel} km → +{bonus_per_km}/km")
    st.info(f"Periode: {start_datum} t/m {eind_datum}")

# Afteller
if start_datum and eind_datum:
    resterend = (eind_datum - datetime.date.today()).days
    if resterend >= 0:
        st.subheader(f"⏳ Nog {resterend} dag(en) te gaan!")
    else:
        st.warning("Deze challenge is afgelopen.")
