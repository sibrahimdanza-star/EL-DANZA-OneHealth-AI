import streamlit as st
import sqlite3
import datetime
from PIL import Image

st.set_page_config(page_title="EL-DANZA OneHealth AI", layout="centered", page_icon="🟢")

# MULTI-LANGUAGE DICTIONARY
LANG = st.selectbox("Language / Harshe / Harshen", ["English", "Hausa", "Pidgin"])
TEXT = {
    "English": {
        "title": "EL-DANZA OneHealth AI",
        "subtitle": "One Compound. One Room. One Water Pot. One Health.",
        "badge": "Offline-Ready - Azure Ready When Connected - Local SQLite Active",
        "tab_compound": "🏠 Compound Risk & Log",
        "tab_human": "🧒 Human Health",
        "tab_animal": "🐐 Animal Health",
        "tab_crop": "🌱 Crop Health",
        "tab_survey": "🔍 Compound Audit",
        "tab_help": "🏥 Find Help Nearby"
    },
    "Hausa": {
        "title": "EL-DANZA Lafiya Daya",
        "subtitle": "Gida Daya. Daki Daya. Tukunya Daya. Lafiya Daya.",
        "badge": "Yana Aiki Ba Tare da Intanet ba - Azure A Shirye - Ajiya a Na'ura",
        "tab_compound": "🏠 Nazarin Gida da Hadari",
        "tab_human": "🧒 Lafiyar Mutane",
        "tab_animal": "🐐 Lafiyar Dabbobi",
        "tab_crop": "🌱 Lafiyar Gona",
        "tab_survey": "🔍 Binciken Gida",
        "tab_help": "🏥 Nemo Taimako Kusa da Kai"
    },
    "Pidgin": {
        "title": "EL-DANZA OneHealth AI",
        "subtitle": "One Compound. One Room. One Water Pot. One Health.",
        "badge": "E Work Offline - Azure Ready When Connected - Local DB Ready",
        "tab_compound": "🏠 Compound Risk & Log",
        "tab_human": "🧒 Human Health",
        "tab_animal": "🐐 Animal Health",
        "tab_crop": "🌱 Crop Health",
        "tab_survey": "🔍 Compound Check",
        "tab_help": "🏥 Find Help Near You"
    }
}
T = TEXT[LANG]

# AZURE OPENAI SETUP
azure_ready = False
azure_client = None
try:
    from openai import AzureOpenAI
    if "AZURE_OPENAI_API_KEY" in st.secrets and "AZURE_OPENAI_ENDPOINT" in st.secrets:
        azure_client = AzureOpenAI(
            api_key=st.secrets["AZURE_OPENAI_API_KEY"],
            api_version="2024-10-21",
            azure_endpoint=st.secrets["AZURE_OPENAI_ENDPOINT"]
        )
        azure_ready = True
except Exception:
    azure_ready = False

# SQLITE LOCAL DATABASE SETUP
conn = sqlite3.connect("eldanza_reports.db", check_same_thread=False)
conn.execute("""
CREATE TABLE IF NOT EXISTS reports (
    date TEXT,
    location TEXT,
    human INT,
    animal INT,
    crop INT,
    root TEXT,
    risk_score REAL,
    level TEXT
)
""")
conn.commit()

# HEADER
st.markdown(T["badge"])
st.title(T["title"])
st.subheader(T["subtitle"])
st.caption("From Danzanfulani, Giwa LGA, Kaduna, Nigeria - to Nigeria - to Africa - to Inter-Africa")

if azure_ready:
    st.success("Microsoft Azure OpenAI: CONNECTED (Cloud AI Ready)")
else:
    st.warning("Azure AI Key Missing - Running Local Offline Rule-Based Mode")

st.error("DEMO VERSION - Educational Tool. Always consult a certified Doctor, Vet, or Extension Officer.")

st.info("Step 1 Test: Foundation is working. Language, Azure check, SQLite, header all loaded.")

st.markdown("---")
st.caption("© 2026 EL-DANZA OneHealth AI | Built by Suleiman Ibrahim | Designed for Imagine Cup 2027 Startup Championship")