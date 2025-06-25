
import streamlit as st

st.title("🔑 Bij een groep aansluiten")

code = st.text_input("Voer klascode in")
naam = st.text_input("Jouw naam")

if st.button("Aansluiten"):
    st.success(f"Je bent succesvol aangesloten bij klascode {code} als {naam}!")
