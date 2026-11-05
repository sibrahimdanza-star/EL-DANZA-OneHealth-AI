import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="EL-DANZA OneHealth AI - One Compound. One Water. One Health.", layout="wide")

# --- PROFESSIONAL HERO ---
st.markdown("### 🟢 Offline-Ready • Works Without Internet • Data Saved Locally")
st.markdown("# EL-DANZA OneHealth AI")
st.markdown("### **One Compound. One Room. One Water Pot. One Health.**")
st.markdown("*From Danzanfulani, Giwa LGA, Kaduna, Nigeria — to Nigeria — to Africa — to Inter-Africa*")
st.error("DEMO VERSION - Rule-Based for Education. Always see Doctor / Vet / Health Worker. Photo is optional and not stored.")

# --- TOP CONTROLS - STAY AT TOP ---
c_top1, c_top2 = st.columns(2)
with c_top1:
    lang = st.selectbox("🌍 Language / Harshe / Langue", ["English", "Hausa", "French"])
with c_top2:
    level = st.selectbox("📍 Where Are You Reporting From?", [
        "1. Danzanfulani (Village) - Where it started",
        "2. Giwa LGA",
        "3. Kaduna State",
        "4. Nigeria",
        "5. Entire Africa",
        "6. Inter-Africa"
    ])

if lang == "Hausa":
    st.info("**SULEIMAN IBRAHIM | Danzanfulani, Giwa.** Gida daya, Daki daya, Tukunyar Ruwa daya, Lafiya daya. Idan yaro, akuya, da gona suka yi rashin lafiya a mako daya, tushe daya ne.")
elif lang == "French":
    st.info("**SULEIMAN IBRAHIM | Danzanfulani, Giwa.** Un même enclos, une même chambre, un même pot d'eau, une même santé.")
else:
    st.info("**Founder: SULEIMAN IBRAHIM | Danzanfulani, Giwa LGA** | In our compound, a hen, a goat and a child sleep in the same room. They share the same water pot. They defecate in the same compound. If they all get sick in the same week, it is ONE problem, not three. This app finds the ROOT.")

if "1." in level:
    st.success("📍 Level 1: Village Pilot - Danzanfulani. This is where we prove it works.")
elif "5." in level or "6." in level:
    st.success("📍 Level: Africa / Inter-Africa Scale - If many villages report same pattern, this is a regional outbreak.")
else:
    st.success(f"📍 Level: {level}")

# --- HUMAN ---
st.divider()
st.header("🧑 HUMAN HEALTH / LAFIYAR MUTANE / SANTÉ HUMAINE")
human_symptom = st.selectbox("Select Symptom", ["Skin sore / Impetigo-like", "Fever + Rash", "Diarrhea / Watery stool", "Cough / Breathing difficulty"])
st.markdown("**📸 Photo (Optional) - Not Stored, For Demo Only**")
human_img = st.file_uploader("Upload Human Skin Photo - Optional", type=["jpg","png"], key="human")
if human_img:
    st.image(human_img, caption="✅ Photo Uploaded - Preview", width=300)
    st.caption("Photo preview only. Not saved to server. Privacy-first.")
if st.button("Analyze Human"):
    st.success(f"Human Result: {human_symptom} - See PHC / Doctor. Wash hands, use clean covered water.")
    if human_img:
        st.image(human_img, caption="Analyzed Human Photo", width=300)

# --- ANIMAL ---
st.divider()
with st.expander("🐐 ANIMAL HEALTH - Click to Open / LAFIYAR DABBOBI", expanded=False):
    animal = st.selectbox("Select Animal", ["Chicken","Goat","Sheep","Cow","Turkey","Duck","Goose","Hen","Dog"])
    animal_symptom = st.selectbox("Select Symptom", ["Skin lumps / Lumpy Skin-like (Cattle)", "Sneezing / Coughing (Poultry)", "Diarrhea / Bloody stool", "Not eating / Weak"])
    st.markdown("**📸 Photo (Optional) - Not Stored, For Demo Only**")
    animal_img = st.file_uploader("Upload Animal Photo - Optional", type=["jpg","png"], key="animal")
    if animal_img:
        st.image(animal_img, caption="✅ Animal Photo Uploaded - Preview", width=300)
        st.caption("Photo preview only. Not saved to server. Privacy-first.")
    if st.button("Analyze Animal"):
        st.success(f"Animal Result: {animal} - {animal_symptom} - Isolate animal, call Vet / Giwa LGA Vet Officer. Do NOT let it drink from human water pot.")
        if animal_img:
            st.image(animal_img, caption="Analyzed Animal Photo", width=300)

# --- CROP ---
st.divider()
with st.expander("🌱 CROP HEALTH - Click to Open - From Giwa Farm Nov 5", expanded=False):
    crop = st.selectbox("Select Crop", ["Wake / Cowpea / Bean", "Dawa / Guinea Corn / Sorghum", "Tomato", "Guava", "Masara / Maize", "Cucumber"])
    crop_symptom = st.selectbox("What do you see? - From Giwa Farm", ["Black small insects / Aphids", "Small round holes / Tuta", "Black dry mummy fruit / Rot", "Yellow leaves / Wilting", "Black mold on stored grain / Aflatoxin"])
    st.markdown("**📸 Photo (Optional) - Not Stored, For Demo Only**")
    crop_img = st.file_uploader("Upload Crop Photo - Optional", type=["jpg","png"], key="crop")
    if crop_img:
        st.image(crop_img, caption="✅ Crop Photo Uploaded - Preview", width=300)
        st.caption("Photo preview only. Not saved to server. Privacy-first.")
    if st.button("Analyze Crop"):
        if "Aphids" in crop_symptom:
            st.error("Crop Result: Black Aphids on Wake - Severe. Spray neem / soapy water, remove infested leaves.")
        elif "Tuta" in crop_symptom:
            st.error("Crop Result: Tuta on Tomato - Severe. Remove infested fruits, use pheromone trap.")
        elif "Rot" in crop_symptom or "mummy" in crop_symptom.lower():
            st.error("Crop Result: Black dry mummy fruit / Guava Rot - Remove mummy fruits, bury them far from house.")
        elif "Aflatoxin" in crop_symptom or "mold" in crop_symptom.lower():
            st.error("Crop Result: AFLATOXIN RISK - Moldy Dawa/Masara - DO NOT EAT, DO NOT FEED TO CHICKEN/GOAT. Poison! Bury it. Dry storage next time.")
        else:
            st.success(f"Crop Result: {crop} - {crop_symptom} - Monitor, improve watering, wash before eating raw.")
        if crop_img:
            st.image(crop_img, caption="Analyzed Crop Photo", width=300)

# --- SAME COMPOUND CHECK ---
st.divider()
st.header("🏠 SAME COMPOUND CHECK - The Innovation Judges Will Remember")
st.markdown("**Gida Daya / Même Enclos / Same Compound** — 30 seconds. Answer honestly. This is what makes EL-DANZA different.")
st.caption("In Danzanfulani, hen, goat and child sleep in same room, share same water pot, defecate in same compound. If YES to 3+, your compound is the root.")

q1 = st.radio("1. Do animals sleep in same room as humans? / Dabbobi suna kwana daki daya da mutane?", ["No", "Yes"])
q2 = st.radio("2. Do animals drink from same water pot as humans? / Dabbobi suna sha ruwa tukunya daya da mutane?", ["No", "Yes"])
q3 = st.radio("3. Do you see animal dung in compound? / Kana ganin kashin dabbobi a gida?", ["No", "Yes"])
q4 = st.radio("4. Do you eat Tomato / Guava raw without washing? / Kana cin Tumatur / Guava ba tare da wankewa ba?", ["No", "Yes"])
q5 = st.radio("5. Do you use FRESH dung on farm? / Kana amfani da sabon taki a gona?", ["No", "Yes"])

compound_yes = sum([1 for q in [q1,q2,q3,q4,q5] if q=="Yes"])
compound_score = compound_yes * 20

if st.button("Calculate Compound Risk"):
    if compound_yes >= 3:
        st.error(f"🔴 HIGH COMPOUND RISK - Score {compound_score}/100 - {compound_yes}/5 YES. BREAK THE CYCLE TODAY: 1) Cover water pot ALWAYS 2) Separate animal bowl 3) Sweep & bury dung far from house 4) Wash tomato/guava with clean water + salt before eating raw 5) Dry dung in sun 2 weeks before using on farm.")
    elif compound_yes >= 1:
        st.warning(f"🟡 MEDIUM COMPOUND RISK - Score {compound_score}/100 - {compound_yes}/5 YES. Fix the YES items today before it becomes HIGH.")
    else:
        st.success(f"🟢 SAFE COMPOUND - Score {compound_score}/100 - 0/5 YES. Keep it safe! Your compound is protecting your family.")

# --- COMMUNITY LOG + ROOT + TREND ---
st.divider()
st.header(f"📊 Community OneHealth Log - {level}")
st.markdown("**Find the ROOT, Not Just the Symptom**")

if "history" not in st.session_state:
    st.session_state.history = []

c1, c2, c3 = st.columns(3)
with c1: h = st.number_input("Human sick cases", 0, 100, 0)
with c2: a = st.number_input("Animal sick cases", 0, 100, 0)
with c3: cr = st.number_input("Crop plots damaged", 0, 100, 0)

root = st.selectbox("What is the SHARED ROOT? / Menene Tushen Matsalar?", [
    "Same Water Source / Ruwan Sha Daya",
    "Animal Dung / Manure on Farm / Taki",
    "Moldy Stored Crop / Aflatoxin / Dawa Mai Kwaya",
    "Flies / Mosquito / Tick / Kuda",
    "Sick Soil / Kasa Mara Lafiya",
    "Not Sure / Ban Sani Ba"
])

if st.button("Save Report & Calculate Risk"):
    score = (h + a + cr) * 5.5
    risk = "LOW" if score < 30 else "MEDIUM" if score < 60 else "HIGH"
    st.success(f"Risk Score: {score} - {risk} - Saved for {level} on {date.today()}")
    st.info(f"Root You Selected: {root} - If Human + Animal + Crop are sick, check this root FIRST.")
    if h > 0 and a > 0 and cr > 0:
        st.error("🚨 TRIPLE SIGNAL ALERT - One Compound, One Week! Human + Animal + Crop sick together. This is NOT 3 problems. Check SHARED WATER + DUNG + RAW CROP. Alert PHC + Vet + Extension Officer TOGETHER.")
        if compound_yes >= 3:
            st.error("🔴🔴 DOUBLE RED: Triple Signal + HIGH Compound Risk = BREAK THE CYCLE NOW. Your compound is the root.")
    elif (h > 0 and a > 0) or (a > 0 and cr > 0) or (h > 0 and cr > 0):
        st.warning("⚠️ DOUBLE SIGNAL: Two domains sick together. Check shared water / environment.")
    if "1." in level:
        st.info("Danzanfulani View: Alert village head, PHC, and Giwa LGA. Isolate sick livestock. Cover water pot.")
    elif "5." in level or "6." in level:
        st.info("Africa View: If many villages report same pattern, this is a regional outbreak alert.")
    else:
        st.info(f"{level} View: Alert LGA / State health team and share this log.")
    st.session_state.history.append({"Date": str(date.today()), "Risk Score": score, "Human": h, "Animal": a, "Crop": cr, "Compound YES": compound_yes})
    if st.button("📱 Send SMS Alert to Local PHC (Demo)"):
        st.success(f"SMS Demo Sent to Giwa PHC: Risk {score} - {risk} - Root: {root} - Danzanfulani")
    if len(st.session_state.history) > 0:
        df = pd.DataFrame(st.session_state.history)
        st.download_button("📤 Export Log as CSV", df.to_csv(index=False), "el-danza-log.csv", "text/csv")

if len(st.session_state.history) > 0:
    st.subheader("📈 Trend Visualization - Risk Score Over Time")
    df = pd.DataFrame(st.session_state.history)
    st.line_chart(df.set_index("Date")["Risk Score"])
    st.dataframe(df, use_container_width=True)
    st.caption("This log is your proof for Imagine Cup - real patterns over time from Danzanfulani.")

st.divider()
st.markdown("### The Cycle We Break")
st.markdown("**Sick Goat/Hen in same room → Defecates + Drinks Water → Dirty Water Pot + Dirty Floor + Flies → Child drinks water + eats raw Tomato/Guava → Child + Goat + Crop sick → Dung goes back to farm → CYCLE REPEATS**")
st.markdown("**EL-DANZA breaks the cycle at the ROOT: Cover water, separate animals, sweep dung, wash raw crops, dry dung before farm.**")
st.caption("© 2026 EL-DANZA OneHealth AI - v5.1 Professional | From Danzanfulani, Giwa LGA, Kaduna, Nigeria to Entire Africa & Inter-Africa | Built by SULEIMAN IBRAHIM | Imagine Cup 2026 | Photo Optional - Privacy-First - Not Stored")