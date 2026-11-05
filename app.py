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

# --- TOP CONTROLS ---
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
human_symptom = st.selectbox("Select Symptom", ["Skin sore / Impetigo-like", "Fever + Rash", "Diarrhea / Watery stool", "Cough / Breathing difficulty", "Others - Type Your Own Symptom / Sauran - Rubuta Naka"])
human_other = ""
if "Others" in human_symptom:
    human_other = st.text_input("✍️ Type the exact human symptom here (e.g. headache, vomiting, eye redness)", placeholder="Type symptom here...")
    if human_other:
        st.info(f"You typed: {human_other}")
st.markdown("**📸 Photo (Optional) - Not Stored, For Demo Only**")
human_img = st.file_uploader("Upload Human Skin Photo - Optional", type=["jpg","png"], key="human")
if human_img:
    st.image(human_img, caption="✅ Photo Uploaded - Preview", width=300)
    st.caption("Photo preview only. Not saved to server. Privacy-first.")
if st.button("Analyze Human"):
    final_human = human_other if "Others" in human_symptom and human_other else human_symptom
    st.success(f"Human Result: {final_human} - See PHC / Doctor. Wash hands, use clean covered water.")
    if human_img:
        st.image(human_img, caption="Analyzed Human Photo", width=300)

# --- ANIMAL ---
st.divider()
with st.expander("🐐 ANIMAL HEALTH - Click to Open / LAFIYAR DABBOBI", expanded=False):
    animal = st.selectbox("Select Animal", ["Chicken","Goat","Sheep","Cow","Turkey","Duck","Goose","Hen","Dog", "Others - Other Animal"])
    animal_other_type = ""
    if "Others" in animal:
        animal_other_type = st.text_input("✍️ Type animal name here (e.g. rabbit, pig)", placeholder="Type animal here...")
    animal_symptom = st.selectbox("Select Symptom", ["Skin lumps / Lumpy Skin-like (Cattle)", "Sneezing / Coughing (Poultry)", "Diarrhea / Bloody stool", "Not eating / Weak", "Others - Type Your Own Symptom / Sauran - Rubuta Naka"])
    animal_other = ""
    if "Others" in animal_symptom:
        animal_other = st.text_input("✍️ Type the exact animal symptom here (e.g. leg swelling, not laying eggs)", placeholder="Type animal symptom here...")
        if animal_other:
            st.info(f"You typed: {animal_other}")
    st.markdown("**📸 Photo (Optional) - Not Stored, For Demo Only**")
    animal_img = st.file_uploader("Upload Animal Photo - Optional", type=["jpg","png"], key="animal")
    if animal_img:
        st.image(animal_img, caption="✅ Animal Photo Uploaded - Preview", width=300)
        st.caption("Photo preview only. Not saved to server. Privacy-first.")
    if st.button("Analyze Animal"):
        final_animal = animal_other_type if "Others" in animal and animal_other_type else animal
        final_animal_symptom = animal_other if "Others" in animal_symptom and animal_other else animal_symptom
        st.success(f"Animal Result: {final_animal} - {final_animal_symptom} - Isolate animal, call Vet / Giwa LGA Vet Officer. Do NOT let it drink from human water pot.")
        if animal_img:
            st.image(animal_img, caption="Analyzed Animal Photo", width=300)

# --- CROP ---
st.divider()
with st.expander("🌱 CROP HEALTH - Click to Open - From Giwa Farm Nov 5", expanded=False):
    crop = st.selectbox("Select Crop", ["Wake / Cowpea / Bean", "Dawa / Guinea Corn / Sorghum", "Tomato", "Guava", "Masara / Maize", "Cucumber", "Others - Other Crop"])
    crop_other_type = ""
    if "Others" in crop:
        crop_other_type = st.text_input("✍️ Type crop name here (e.g. pepper, okra)", placeholder="Type crop here...")
    crop_symptom = st.selectbox("What do you see? - From Giwa Farm", ["Black small insects