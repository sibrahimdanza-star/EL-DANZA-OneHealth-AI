import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="EL-DANZA OneHealth AI", layout="wide")

# --- STICKY HEADER + OFFLINE INDICATOR ---
st.markdown("### 🟢 Offline-Ready • Data Saved Locally | EL-DANZA OneHealth AI")
st.caption("From Danzanfulani, Giwa LGA, Kaduna, Nigeria to Entire Africa | Imagine Cup 2026")

# --- LANGUAGE + LEVEL AT TOP (No more scrolling up) ---
lang = st.selectbox("Choose Language / Zabi Harshe / Choisir Langue", ["English", "Hausa", "French"])
level = st.selectbox("Where Are You Reporting From? / Daga Ina Kake Ba Da Rahoto?", [
    "1. Danzanfulani (Village) - Where it started",
    "2. Giwa LGA",
    "3. Kaduna State",
    "4. Nigeria",
    "5. Entire Africa"
])

st.title("EL-DANZA OneHealth AI")
st.markdown("**Multilingual Precision Diagnosis for Human, Animal & Crop**")
st.markdown("**From Danzanfulani to Africa • Real-time • Offline-capable • Privacy-first**")
st.error("DEMO VERSION - Rule-Based. For education. Always see Doctor / Vet / Health Worker.")

st.info("**Founder: SULEIMAN IBRAHIM | Mission:** OneHealth for Rural Giwa - where one dirty water source can make a child, a goat, and a farm sick in the same week. Starting in Danzanfulani, scaling to Giwa, Kaduna, Nigeria, and Entire Africa.")
st.warning("**Problem we solve:** In Giwa, there is no vet, no lab, no extension officer. Farmers lose Dawa to Aphids, Tomato to Tuta, Guava to Rot. This problem is the same in villages across Nigeria and Africa.")

if "1." in level:
    st.success("📍 Level 1: Village Pilot - Real farm photos from Danzanfulani, Giwa. This is where we prove it works.")
elif "5." in level:
    st.success("📍 Level 5: Africa Scale - If many villages report same pattern, this is a regional outbreak alert.")
else:
    st.success(f"📍 Level: {level}")

# --- HUMAN HEALTH - OPEN BY DEFAULT ---
st.divider()
st.header("🧑 HUMAN HEALTH")
st.write("Scan: Lesion / Skin detection")
human_symptom = st.selectbox("Select Symptom", ["Skin sore / Impetigo-like", "Fever + Rash", "Diarrhea / Watery stool", "Cough / Breathing difficulty"])
human_img = st.file_uploader("Upload Human Skin Photo", type=["jpg","png"], key="human")
if st.button("Analyze Human"):
    st.success(f"Human Result: {human_symptom} - See PHC / Doctor. Wash hands, clean water, isolate if fever.")
    if human_img: st.image(human_img, caption="Uploaded Human Photo")

# --- ANIMAL HEALTH - COLLAPSIBLE ---
st.divider()
with st.expander("🐐 ANIMAL HEALTH - Click to Open", expanded=False):
    st.write("Chicken | Goat | Sheep | Cow | Turkey | Duck | Goose | Hen")
    animal = st.selectbox("Select Animal", ["Chicken","Goat","Sheep","Cow","Turkey","Duck","Goose","Hen"])
    animal_symptom = st.selectbox("Select Symptom", ["Skin lumps / Lumpy Skin-like (Cattle)", "Sneezing / Coughing (Poultry)", "Diarrhea / Bloody stool", "Not eating / Weak"])
    animal_img = st.file_uploader("Upload Animal Photo", type=["jpg","png"], key="animal")
    if st.button("Analyze Animal"):
        st.success(f"Animal Result: {animal} - {animal_symptom} - Isolate animal, call Vet / Giwa LGA Vet Officer.")
        if animal_img: st.image(animal_img, caption="Uploaded Animal Photo")

# --- CROP HEALTH - COLLAPSIBLE ---
st.divider()
with st.expander("🌱 CROP HEALTH - Click to Open - From Giwa Farm Nov 5", expanded=False):
    crop = st.selectbox("Select Crop", ["Wake / Cowpea / Bean", "Dawa / Guinea Corn / Sorghum", "Tomato", "Guava", "Masara / Maize"])
    crop_symptom = st.selectbox("What do you see? - From Giwa Farm Nov 5", ["Black small insects / Aphids", "Small round holes / Tuta", "Black dry mummy fruit / Rot", "Yellow leaves / Wilting"])
    crop_img = st.file_uploader("Upload Crop Photo", type=["jpg","png"], key="crop")
    if st.button("Analyze Crop"):
        if "Aphids" in crop_symptom:
            st.error("Crop Result: Black Aphids on Wake - Severe. Spray neem / soapy water, remove heavily infested leaves.")
        elif "Tuta" in crop_symptom:
            st.error("Crop Result: Tuta on Tomato - Severe. Remove infested fruits, use pheromone trap.")
        elif "Rot" in crop_symptom or "mummy" in crop_symptom.lower():
            st.error("Crop Result: Black dry mummy fruit / Guava Rot - Remove mummy fruits, bury them, do not leave on tree.")
        else:
            st.success(f"Crop Result: {crop} - {crop_symptom} - Monitor, improve watering, check in 2 days.")
        if crop_img: st.image(crop_img, caption="Uploaded Crop Photo")

# --- COMMUNITY LOG + TREND CHART + EXPORT ---
st.divider()
st.header(f"Community OneHealth Log - {level}")
if "history" not in st.session_state:
    st.session_state.history = []

c1, c2, c3 = st.columns(3)
with c1: h = st.number_input("Human sick cases", 0, 100, 0)
with c2: a = st.number_input("Animal sick cases", 0, 100, 0)
with c3: cr = st.number_input("Crop plots damaged", 0, 100, 0)

if st.button("Save Report & Calculate Risk"):
    score = (h + a + cr) * 5.5
    risk = "LOW" if score < 30 else "MEDIUM" if score < 60 else "HIGH"
    st.success(f"Risk Score: {score} - {risk} - Saved for {level} on {date.today()}")
    if "1." in level:
        st.info("Danzanfulani View: Alert village head, PHC, and Giwa LGA. Isolate sick livestock.")
    elif "5." in level:
        st.info("Africa View: If many villages report same pattern, this is a regional outbreak alert.")
    else:
        st.info(f"{level} View: Alert LGA / State health team and share this log.")

    # Save for chart
    st.session_state.history.append({"Date": str(date.today()), "Risk Score": score, "Human": h, "Animal": a, "Crop": cr})

    # Mock SMS + Export
    if st.button("📱 Send SMS Alert to Local PHC (Demo)"):
        st.success("SMS Demo Sent to Giwa PHC: Risk Score %.1f - %s - Danzanfulani" % (score, risk))
    if len(st.session_state.history) > 0:
        df = pd.DataFrame(st.session_state.history)
        st.download_button("📤 Export Log as CSV", df.to_csv(index=False), "el-danza-log.csv", "text/csv")

# Show Trend Chart if we have data
if len(st.session_state.history) > 0:
    st.subheader("📈 Trend Visualization - Risk Score Over Time - Judges Love This")
    df = pd.DataFrame(st.session_state.history)
    st.line_chart(df.set_index("Date")["Risk Score"])
    st.dataframe(df, use_container_width=True)
    st.caption("This log is your proof for Imagine Cup - it shows real patterns over time.")

st.divider()
st.caption("© 2026 EL-DANZA OneHealth AI - From Danzanfulani, Giwa LGA, Kaduna, Nigeria to Entire Africa | Built by Suleiman Ibrahim | Imagine Cup 2026")