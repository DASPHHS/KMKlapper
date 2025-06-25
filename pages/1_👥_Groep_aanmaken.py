
import streamlit as st
import random
import string

st.title("👥 Groep aanmaken")

def genereer_code():
    return "KLAS-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

groep = st.text_input("Groepsnaam")
beheerder = st.text_input("Naam beheerder")

if st.button("Maak groep aan"):
    code = genereer_code()
    st.success(f"✅ Groep '{groep}' aangemaakt!")
    st.code(f"Klascode: {code}", language="plaintext")
