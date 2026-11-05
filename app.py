import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="EL-DANZA OneHealth AI", layout="wide")

st.markdown("### 🟢 Offline-Ready • Works Without Internet")
st.markdown("# EL-DANZA OneHealth AI")
st.markdown("### **One Compound. One Room. One Water Pot. One Health.**")
st.markdown("*From Danzanfulani, Giwa LGA, Kaduna, Nigeria - to Nigeria - to Africa - to Inter-Africa*")
st.error("DEMO VERSION - Rule-Based. Always see Doctor / Vet. Photo is optional and not stored.")

c_top1, c_top2 = st.columns(2)
with c_top1:
    lang = st.selectbox("Language / Harshe / Langue", ["English", "Hausa", "French"])
with c_top2:
    level = st.selectbox("Where Are You Reporting From?", [
        "1. Danzanfulani (Village) - Where it started",
        "2. Giwa LGA",
        "3. Kaduna State",
        "4. Nigeria",
        "5. Entire Africa",
        "6. Inter-Africa"
    ])

if lang == "Hausa":
    st.info("SULEIMAN IBRAHIM | Danzanfulani, Giwa. Gida daya, Daki daya, Tukunyar Ruwa daya, Lafiya daya.")
elif lang == "French":
    st.info("SULEIMAN IBRAHIM | Danzanfulani, Giwa. Un meme enclos, une meme chambre, un meme pot d eau, une meme sante.")
else:
    st.info("Founder: SULEIMAN IBRAHIM | Danzanfulani, Giwa LGA | Hen, goat and child sleep in same room. Share same water pot. If all sick in same week, it is ONE problem. This app finds the ROOT.")

if "1." in level:
    st.success("Level 1: Village Pilot - Danzanfulani. This is where we prove it works.")
elif "5." in level or "6." in level:
    st.success("Level: Africa / Inter-Africa Scale - Regional outbreak if many villages report same pattern.")
else:
    st.success(level)

# HUMAN
st.divider()
st.header("🧑 HUMAN HEALTH")
human_symptom = st.selectbox("Select Symptom", [
    "Skin sore / Impetigo-like",
    "Fever + Rash",
    "Diarrhea / Watery stool",
    "Cough / Breathing difficulty",
    "Others - Type Your Own Symptom"
])
human_other = ""
if "Others" in human_symptom:
    human_other = st.text_input("Type the exact human symptom here", placeholder="e.g. headache, vomiting")
    if human_other:
        st.info(f"You typed: {human_other}")
st.markdown("**📸 Photo (Optional) - Not Stored**")
human_img = st.file_uploader("Upload Human Photo - Optional", type=["jpg", "png"], key="human")
if human_img:
    st.image(human_img, caption="Photo Uploaded - Preview", width=300)
    st.caption("Preview only. Not saved. Privacy-first.")
if st.button("Analyze Human"):
    final_human = human_other if "Others" in human_symptom and human_other else human_symptom
    st.success(f"Human Result: {final_human} - See PHC / Doctor. Wash hands, use clean covered water.")
    if human_img:
        st.image(human_img, caption="Analyzed Human Photo", width=300)

# ANIMAL
st.divider()
with st.expander("🐐 ANIMAL HEALTH - Click to Open", expanded=False):
    animal = st.selectbox("Select Animal", ["Chicken", "Goat", "Sheep", "Cow", "Turkey", "Duck", "Goose", "Hen", "Dog", "Others - Other Animal"])
    animal_other_type = ""
    if "Others" in animal:
        animal_other_type = st.text_input("Type animal name here", placeholder="e.g. rabbit, pig")
    animal_symptom = st.selectbox("Select Symptom", [
        "Skin lumps / Lumpy Skin-like",
        "Sneezing / Coughing",
        "Diarrhea / Bloody stool",
        "Not eating / Weak",
        "Others - Type Your Own Symptom"
    ])
    animal_other = ""
    if "Others" in animal_symptom:
        animal_other = st.text_input("Type the exact animal symptom here", placeholder="e.g. leg swelling")
        if animal_other:
            st.info(f"You typed: {animal_other}")
    st.markdown("**📸 Photo (Optional) - Not Stored**")
    animal_img = st.file_uploader("Upload Animal Photo - Optional", type=["jpg", "png"], key="animal")
    if animal_img:
        st.image(animal_img, caption="Animal Photo Uploaded", width=300)
        st.caption("Preview only. Not saved. Privacy-first.")
    if st.button("Analyze Animal"):
        final_animal = animal_other_type if "Others" in animal and animal_other_type else animal
        final_as = animal_other if "Others" in animal_symptom and animal_other else animal_symptom
        st.success(f"Animal Result: {final_animal} - {final_as} - Isolate animal, call Vet. Do NOT let it drink from human water pot.")
        if animal_img:
            st.image(animal_img, caption="Analyzed Animal Photo", width=300)

# CROP
st.divider()
with st.expander("🌱 CROP HEALTH - Click to Open", expanded=False):
    crop = st.selectbox("Select Crop", ["Wake / Cowpea / Bean", "Dawa / Sorghum", "Tomato", "Guava", "Masara / Maize", "Cucumber", "Others - Other Crop"])
    crop_other_type = ""
    if "Others" in crop:
        crop_other_type = st.text_input("Type crop name here", placeholder="e.g. pepper, okra")
    crop_symptom = st.selectbox("What do you see?", [
        "Black small insects / Aphids",
        "Small round holes / Tuta",
        "Black dry mummy fruit / Rot",
        "Yellow leaves / Wilting",
        "Black mold on stored grain / Aflatoxin",
        "Others - Type Your Own Symptom"
    ])
    crop_other = ""
    if "Others" in crop_symptom:
        crop_other = st.text_input("Type the exact crop symptom here", placeholder="e.g. white spots")
        if crop_other:
            st.info(f"You typed: {crop_other}")
    st.markdown("**📸 Photo (Optional) - Not Stored**")
    crop_img = st.file_uploader("Upload Crop Photo - Optional", type=["jpg", "png"], key="crop")
    if crop_img:
        st.image(crop_img, caption="Crop Photo Uploaded", width=300)
        st.caption("Preview only. Not saved. Privacy-first.")
    if st.button("Analyze Crop"):
        final_crop = crop_other_type if "Others" in crop and crop_other_type else crop
        final_cs = crop_other if "Others" in crop_symptom and crop_other else crop_symptom
        if "Aphids" in final_cs:
            st.error(f"Crop Result: {final_crop} - Black Aphids - Severe. Spray neem / soapy water.")
        elif "Tuta" in final_cs:
            st.error(f"Crop Result: {final_crop} - Tuta - Severe. Remove infested fruits.")
        elif "Rot" in final_cs or "mummy" in final_cs.lower():
            st.error(f"Crop Result: {final_crop} - Mummy fruit / Rot - Remove and bury far from house.")
        elif "Aflatoxin" in final_cs or "mold" in final_cs.lower():
            st.error(f"Crop Result: {final_crop} - AFLATOXIN RISK - DO NOT EAT, DO NOT FEED TO ANIMALS. Bury it.")
        elif "Others" in crop_symptom:
            st.warning(f"Crop Result: {final_crop} - You typed: {final_cs} - Show to Extension Officer.")
        else:
            st.success(f"Crop Result: {final_crop} - {final_cs} - Monitor, wash before eating raw.")
        if crop_img:
            st.image(crop_img, caption="Analyzed Crop Photo", width=300)

# SAME COMPOUND CHECK
st.divider()
st.header("🏠 SAME COMPOUND CHECK - The Innovation")
st.markdown("**Gida Daya / Meme Enclos / Same Compound** - 30 seconds.")
st.caption("In Danzanfulani, hen, goat and child sleep in same room, share same water pot.")

q1 = st.radio("1. Do animals sleep in same room as humans?", ["No", "Yes"])
q2 = st.radio("2. Do animals drink from same water pot as humans?", ["No", "Yes"])
q3 = st.radio("3. Do you see animal dung in compound?", ["No", "Yes"])
q4 = st.radio("4. Do you eat Tomato / Guava raw without washing?", ["No", "Yes"])
q5 = st.radio("5. Do you use FRESH dung on farm?", ["No", "Yes"])

compound_yes = sum([1 for q in [q1, q2, q3, q4, q5] if q == "Yes"])
compound_score = compound_yes * 20

if st.button("Calculate Compound Risk"):
    if compound_yes >= 3:
        st.error(f"🔴 HIGH COMPOUND RISK - Score {compound_score}/100 - {compound_yes}/5 YES. BREAK THE CYCLE: 1) Cover water pot 2) Separate animal bowl 3) Sweep and bury dung far 4) Wash tomato/guava with clean water + salt 5) Dry dung 2 weeks before farm.")
    elif compound_yes >= 1:
        st.warning(f"🟡 MEDIUM COMPOUND RISK - Score {compound_score}/100 - {compound_yes}/5 YES. Fix the YES items today.")
    else:
        st.success(f"🟢 SAFE COMPOUND - Score {compound_score}/100 - 0/5 YES. Keep it safe!")

# COMMUNITY LOG
st.divider()
st.header(f"📊 Community OneHealth Log - {level}")
st.markdown("**Find the ROOT, Not Just the Symptom**")

if "history" not in st.session_state:
    st.session_state.history = []

c1, c2, c3 = st.columns(3)
with c1:
    h = st.number_input("Human sick cases", 0, 100, 0)
with c2:
    a = st.number_input("Animal sick cases", 0, 100, 0)
with c3:
    cr = st.number_input("Crop plots damaged", 0, 100, 0)

root = st.selectbox("What is the SHARED ROOT?", [
    "Same Water Source",
    "Animal Dung / Manure on Farm",
    "Moldy Stored Crop / Aflatoxin",
    "Flies / Mosquito / Tick",
    "Sick Soil",
    "Not Sure",
    "Others - Type Your Own Root"
])
root_other = ""
if "Others" in root:
    root_other = st.text_input("Type the exact shared root here", placeholder="e.g. dirty well water")
    if root_other:
        st.info(f"You typed root: {root_other}")

if st.button("Save Report & Calculate Risk"):
    final_root = root_other if "Others" in root and root_other else root
    score = (h + a + cr) * 5.5
    risk = "LOW" if score < 30 else "MEDIUM" if score < 60 else "HIGH"
    st.success(f"Risk Score: {score} - {risk} - Saved for {level} on {date.today()}")
    st.info(f"Root