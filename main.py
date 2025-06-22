import streamlit as st
from app.generator import generate_email
from app.data import products
from app.utils import tonalitaets_feedback
from datetime import datetime
import re

# Konfiguration der Seite MUSS als erstes kommen
st.set_page_config(
    page_title="E-Mail Generator",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS einbinden
def load_css():
    with open("static/stil.css") as f:
        return f'<style>{f.read()}</style>'
st.markdown(load_css(), unsafe_allow_html=True)

# Wrapper-Div für Hintergrund und Styling starten
st.markdown('<div class="stApp">', unsafe_allow_html=True)

st.title("ZENLYFE E-Mail Generator")

product_name = st.selectbox("Produkt auswählen", list(products.keys()))
product = products[product_name]

target = st.selectbox("Zielgruppe", ["Neukunden", "Bestandskunden", "Inaktive Nutzer"])
tone = st.selectbox("Tonalität", ["locker", "neutral", "förmlich"])
language = st.selectbox("Sprache", ["Deutsch", "Englisch"])
cta = st.text_input("Call-to-Action", "Jetzt ausprobieren")

if "result" not in st.session_state:
    st.session_state.result = ""

if st.button("E-Mail generieren"):
    st.session_state.result = generate_email(product, target, tone, language, cta)

if st.session_state.result:
    st.markdown("### ✉️ Ergebnis:")
    st.code(st.session_state.result, language="markdown")

    st.text_area("E-Mail Text zum Kopieren", value=st.session_state.result, height=300)

    # Subject line extrahieren
    match = re.search(r"Subject Line:\s*(.+)", st.session_state.result)
    subject_line = match.group(1).strip() if match else "email"

    # Dateiname mit Datum und Subject
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}_{subject_line}.txt"
    # Dateiname safe machen (keine Sonderzeichen)
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)

    st.download_button(
        label="Als Text herunterladen",
        data=st.session_state.result,
        file_name=filename,
        mime="text/plain"
    )

if st.button("A/B Test generieren"):
    if st.session_state.result and "Variante B" not in st.session_state:
        email_a = st.session_state.result
    else:
        email_a = generate_email(product, target, tone, language, cta, version="v1")

    email_b = generate_email(product, target, tone, language, cta, version="v2")

    st.session_state.ab_test_a = email_a
    st.session_state.ab_test_b = email_b

    st.markdown(f"### Variante A ({tone} – Version 1)")
    st.code(email_a)

    st.markdown(f"### Variante B ({tone} – Version 2)")
    st.code(email_b) 


from app.generator import generate_image_prompt

if st.button("Bild-Prompt generieren"):
    image_prompt = generate_image_prompt(product, target)
    st.markdown("### 🖼️ Bild-Prompt")
    st.code(image_prompt)

# Wrapper-Div schließen
st.markdown('</div>', unsafe_allow_html=True)