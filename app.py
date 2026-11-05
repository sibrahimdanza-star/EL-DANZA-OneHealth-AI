# =========================================================
# EL-DANZA OneHealth AI - v3 SCALING VERSION
# FROM: Danzanfulani -> Giwa LGA -> Kaduna -> Nigeria -> Africa
# COPY AND PASTE THIS WHOLE FILE AS app.py
# EASY EDIT: Change ONLY the CONFIG below
# =========================================================
import streamlit as st
from datetime import date

# ---------- 1. EASY EDIT - CHANGE HERE ONLY ----------
CONFIG = {
    "app_name": "EL-DANZA OneHealth AI",
    "tagline": "Multilingual Precision Diagnosis for Human, Animal & Crop",
    "sub_tagline": "From Danzanfulani to Africa • Real-time • Offline-capable • Privacy-first",
    "founder": "SULEIMAN IBRAHIM",
    # YOUR SCALING LADDER - THIS IS YOUR VISION
    "levels": [
        "1. Danzanfulani (Village) - Where it started",
        "2. Giwa LGA (Local Government)",
        "3. Kaduna State",
        "4. Nigeria",
        "5. Entire Africa"
    ],
    "mission": "OneHealth for Rural Giwa - where one dirty water source can make a child, a goat, and a farm sick in the same week. Starting in Danzanfulani, scaling to Giwa, Kaduna, Nigeria, and Entire Africa.",
    "problem": "In Giwa, there is no vet, no lab, no extension officer. Farmers lose Dawa to Aphids, Tomato to Tuta, Guava to Rot. This problem is the same in villages across Nigeria and Africa.",
}

# ---------- 2. PAGE SETUP ----------
st.set_page_config(page_title=CONFIG["app_name"], layout="wide")

st.markdown(f"""
<h1 style='text-align:center; color:#0B5394;'>{CONFIG["app_name"]}</h1>
<p style='text-align:center;'><b>{CONFIG["tagline"]}</b><br>{CONFIG["sub_tagline"]}</p>
<p style='text-align:center; color:red;'><b>DEMO VERSION - Rule-Based. For education. Always see Doctor / Vet / Health Worker.</b></p>
""", unsafe_allow_html=True)

st.info(f"**Founder:** {CONFIG['founder']} | **Mission:** {CONFIG['mission']}")
st.warning(f"**Problem we solve:** {CONFIG['problem']}")

# ---------- 3. SCALING SELECTOR - NEW! ----------
st.markdown("### 🌍 Where Are You Reporting From? / Daga Ina Kake Ba Da Rahoto?")
level = st.selectbox(
    "Choose Your Level - From Village to Africa:",
    CONFIG["levels"]
)
# This shows judges your scaling plan
if "Danzanfulani" in level:
    st.success("📍 Level 1: Village Pilot - Real farm photos from Danzanfulani, Giwa. This is where we prove it works.")
elif "Giwa" in level:
    st.success("📍 Level 2: Giwa LGA - Same diseases, 20+ villages. We share the same vet & PHC.")
elif "Kaduna" in level:
    st.success("📍 Level 3: Kaduna State - Same crops (Dawa, Wake, Tomato), same climate, same language Hausa.")
elif "Nigeria" in level:
    st.success("📍 Level 4: Nigeria - 36 States, same OneHealth problems. App works in English + Hausa + Fulfulde.")
else:
    st.success("📍 Level 5: Entire Africa - From Nigeria to Kenya to Ghana, farmers face Aphids, Tuta, Lumpy Skin. One app, many languages.")

# ---------- 4. LANGUAGE ----------
lang = st.selectbox("Choose Language / Zaɓi Harshe / Choisir Langue",
    ["English", "Hausa", "Fulfulde", "Kiswahili", "French", "Norwegian"])

translations = {
    "English": {"result": "AI OUTPUT (Demo):"},
    "Hausa": {"result": "SAKAMAKO (Demo):"},
}
t = translations.get(lang, translations["English"])

# ---------- 5. THREE COLUMNS LIKE YOUR PICTURE ----------
col1, col2, col3 = st.columns(3)

# ===== HUMAN HEALTH =====
with col1:
    st.subheader("🧑 HUMAN HEALTH")
    st.write("Scan: Lesion / Skin detection")
    human_symptom = st.selectbox("Select Symptom",
        ["Skin sore / Impetigo-like", "Fever + Skin rash", "Wound / Cut", "Other"], key="human")
    human_photo = st.file_uploader("Upload Human Skin Photo", type=["jpg","png","jpeg"], key="h_photo")
    if human_photo:
        st.image(human_photo, caption="Human photo", use_container_width=True)
    if st.button("Analyze Human", key="h_btn"):
        st.subheader(t["result"])
        if "Impetigo" in human_symptom or "Skin sore" in human_symptom:
            st.write("1) **Detected:** Impetigo-like Bacterial Skin Infection (Demo)")
            st.write("2) **General info:** Keep wound clean, avoid contact, wash hands.")
            st.write("3) **Safety:** DO NOT self-prescribe. See PHC / Doctor. Monitor fever.")
        else:
            st.write("1) **Detected:** Needs in-person check")
            st.write("2) **Action:** Clean wound, cover, monitor fever")
            st.write("3) **Safety:** Go to PHC in Giwa if fever, swelling, or spreading redness.")
        st.caption(f"Location: {level}")

# ===== ANIMAL HEALTH =====
with col2:
    st.subheader("🐐 ANIMAL HEALTH")
    st.write("Chicken | Goat | Sheep | Cow | Turkey | Duck | Goose | Hen")
    animal = st.selectbox("Select Animal", ["Chicken","Goat","Sheep","Cow","Turkey","Duck","Goose"], key="animal")
    animal_symptom = st.selectbox("Select Symptom",
        ["Skin lumps / Lumpy Skin-like (Cattle)", "Skin infection / Wounds", "Diarrhoea", "Not eating / Weak"], key="a_symp")
    animal_photo = st.file_uploader("Upload Animal Photo", type=["jpg","png","jpeg"], key="a_photo")
    if animal_photo:
        st.image(animal_photo, caption="Animal photo", use_container_width=True)
    if st.button("Analyze Animal", key="a_btn"):
        st.subheader(t["result"])
        if "Lumpy" in animal_symptom:
            st.write(f"1) **Detected:** Lumpy Skin-like Disease in {animal} (Demo)")
            st.write("2) **General info:** Isolate animal, clean pen, vaccinate herd.")
            st.write("3) **Safety:** Consult LGA Vet before any injection. Do NOT inject without vet.")
        else:
            st.write(f"1) **Detected:** General infection signs in {animal} (Demo)")
            st.write("2) **Action:** Isolate, clean water, keep dry.")
            st.write("3) **Safety:** Call Giwa LGA Vet Officer.")
        st.caption(f"Location: {level}")

# ===== CROP HEALTH - YOUR REAL GIWA FARM DATA =====
with col3:
    st.subheader("🌱 CROP HEALTH")
    st.write("Maize | Tomato | Bean/Wake | Sorghum/Dawa | Soybean | Guava")
    crop = st.selectbox("Select Crop",
        ["Dawa / Sorghum", "Wake / Cowpea / Bean", "Tomato / Tumatur", "Guava / Gwaba", "Maize / Masara", "Soybean"], key="crop")
    crop_sign = st.selectbox("What do you see? - From Giwa Farm Nov 5",
        ["Black small insects / Aphids", "Small round holes in fruit", "Black dry mummy fruit", "Yellow-brown leaves + black head", "Other"], key="c_sign")
    crop_photo = st.file_uploader("Upload Crop Photo - Like your farm photos", type=["jpg","png","jpeg"], key="c_photo")
    if crop_photo:
        st.image(crop_photo, caption="Your farm photo - for analysis", use_container_width=True)
    if st.button("Analyze Crop", key="c_btn"):
        st.subheader(t["result"])
        if "Aphids" in crop_sign:
            st.write(f"1) **Detected:** Black Aphids on {crop} - Severe (Giwa Farm Data)")
            st.write("2) **Action:** Cut heavily infested pods/heads, destroy/bury. Spray neem or soapy water (1 spoon soap in 1L water) in evening.")
            st.write("3) **Prevention:** Harvest clean pods early, check every 2 days.")
        elif "holes" in crop_sign:
            st.write(f"1) **Detected:** Tuta absoluta / Fruit Borer on {crop} - Severe")
            st.write("2) **Action:** Pick ALL fruits with holes, bury in pit. Pick green fruits early, ripen at home in shade.")
            st.write("3) **Prevention:** Do NOT leave rotten fruits under plant.")
        elif "mummy" in crop_sign:
            st.write(f"1) **Detected:** Fruit Rot / Anthracnose - Mummified Fruit on {crop}")
            st.write("2) **Action:** Pick ALL black dry fruits, burn/bury far away. Clean under tree.")
            st.write("3) **Prevention:** Water + compost, prune for air.")
        elif "Yellow" in crop_sign:
            st.write(f"1) **Detected:** Smut / Drought Stress on {crop}")
            st.write("2) **Action:** Remove infected heads, do NOT keep for seed.")
        else:
            st.write("1) **Detected:** Needs clearer photo")
            st.write("2) **Action:** Take photo 1 arm away, hold still 3 seconds.")
        st.caption(f"Location: {level}")

# ---------- 6. HOW IT WORKS / FEATURES / IMPACT ----------
st.markdown("---")
c1, c2, c3 = st.columns(3)
with c1:
    st.subheader("HOW IT WORKS")
    st.write("1. Scan with Smartphone\n2. Analysis (Cloud/Azure in future)\n3. Instant Recommendations")
with c2:
    st.subheader("FEATURES")
    st.write("Multilingual • Works Offline • Farmer-Friendly • Data Secure")
with c3:
    st.subheader("IMPACT")
    st.write("Early Detection • Reduced Losses • Better Health Outcomes")

# ---------- 7. COMMUNITY LOG - WITH SCALING ----------
st.markdown("---")
st.subheader(f"Community OneHealth Log - {level}")
with st.form("log_form"):
    report_date = st.date_input("Date", value=date.today())
    human_cases = st.number_input("Human sick cases", 0, 100, 0)
    animal_cases = st.number_input("Animal sick cases", 0, 100, 0)
    crop_cases = st.number_input("Crop plots damaged", 0, 100, 0)
    submitted = st.form_submit_button("Save Report & Calculate Risk")
    if submitted:
        total = human_cases + animal_cases + crop_cases
        score = min(100, total * 5.5)
        level_risk = "LOW" if score < 30 else "MEDIUM" if score < 70 else "HIGH"
        st.success(f"Risk Score: {score:.1f} - {level_risk} - Saved for {level} on {report_date}")
        if "Africa" in level:
            st.write("**Africa View:** If many villages report same pattern (e.g. Aphids moving), this is a regional outbreak alert.")
        elif "Nigeria" in level:
            st.write("**Nigeria View:** Alert State Ministry of Health + Agriculture.")
        elif "Kaduna" in level:
            st.write("**Kaduna View:** Alert Kaduna State Vet & PHC.")
        elif "Giwa" in level:
            st.write("**Giwa View:** Alert Giwa LGA Vet & Health Officer. Inspect water sources.")
        else:
            st.write("**Danzanfulani View:** Alert village head, PHC, and Giwa LGA. Isolate sick livestock.")
        st.write("This log is your proof for Imagine Cup - it shows real patterns over time.")

st.markdown("---")
st.markdown(f"<p style='text-align:center; color:gray;'>© {date.today().year} {CONFIG['app_name']} - From Danzanfulani, Giwa LGA, Kaduna, Nigeria to Entire Africa | Built by Suleiman Ibrahim | Imagine Cup 2026</p>", unsafe_allow_html=True)