import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="EL-DANZA OneHealth AI",
    layout="wide"
)

st.markdown("### 🟢 Offline-Ready")
st.markdown("# EL-DANZA OneHealth AI")
st.markdown("### One Compound. One Room.")
st.markdown("### One Water Pot. One Health.")
st.markdown("From Danzanfulani, Giwa LGA")
st.markdown("Kaduna, Nigeria - to Africa")
st.error("DEMO - See Doctor / Vet. Photo optional.")

# TOP
c1, c2 = st.columns(2)
with c1:
    lang = st.selectbox(
        "Language",
        ["English", "Hausa", "French"]
    )
with c2:
    level = st.selectbox(
        "Where Are You?",
        ["1. Danzanfulani - Village",
         "2. Giwa LGA",
         "3. Kaduna State",
         "4. Nigeria",
         "5. Entire Africa",
         "6. Inter-Africa"]
    )

if lang == "Hausa":
    st.info("SULEIMAN IBRAHIM | Danzanfulani")
    st.info("Gida daya, Daki daya, Ruwa daya")
elif lang == "French":
    st.info("SULEIMAN IBRAHIM | Danzanfulani")
else:
    st.info("Founder: SULEIMAN IBRAHIM")
    st.info("Danzanfulani, Giwa LGA")
    st.info("Hen, goat and child share room.")
    st.info("Share same water pot.")
    st.info("If all sick in same week, ONE problem.")

# HUMAN LIST
human_list = [
    "Skin sore",
    "Fever + Rash",
    "Diarrhea",
    "Cough",
    "Others"
]
st.divider()
st.header("🧑 HUMAN HEALTH")
human_symptom = st.selectbox(
    "Select Symptom",
    human_list
)
human_other = ""
if human_symptom == "Others":
    human_other = st.text_input(
        "Type human symptom here"
    )
    if human_other:
        st.info(human_other)

st.markdown("**Photo Optional - Not Stored**")
human_img = st.file_uploader(
    "Upload Human Photo",
    type=["jpg", "png"],
    key="human"
)
if human_img:
    st.image(
        human_img,
        caption="Photo Uploaded",
        width=300
    )
    st.caption("Preview only. Not saved.")

if st.button("Analyze Human"):
    fh = human_other
    if fh == "":
        fh = human_symptom
    st.success(f"Human: {fh} - See PHC / Doctor.")
    if human_img:
        st.image(human_img, width=300)

# ANIMAL LIST
animal_list = [
    "Chicken",
    "Goat",
    "Sheep",
    "Cow",
    "Turkey",
    "Duck",
    "Hen",
    "Dog",
    "Others"
]
animal_sym_list = [
    "Skin lumps",
    "Coughing",
    "Diarrhea",
    "Not eating",
    "Others"
]
st.divider()
with st.expander("🐐 ANIMAL HEALTH", expanded=False):
    animal = st.selectbox(
        "Select Animal",
        animal_list
    )
    animal_other_type = ""
    if animal == "Others":
        animal_other_type = st.text_input(
            "Type animal name here"
        )
    animal_symptom = st.selectbox(
        "Select Symptom",
        animal_sym_list
    )
    animal_other = ""
    if animal_symptom == "Others":
        animal_other = st.text_input(
            "Type animal symptom here"
        )
        if animal_other:
            st.info(animal_other)
    st.markdown("**Photo Optional - Not Stored**")
    animal_img = st.file_uploader(
        "Upload Animal Photo",
        type=["jpg", "png"],
        key="animal"
    )
    if animal_img:
        st.image(
            animal_img,
            caption="Animal Photo Uploaded",
            width=300
        )
    if st.button("Analyze Animal"):
        fa = animal_other_type
        if fa == "":
            fa = animal
        fas = animal_other
        if fas == "":
            fas = animal_symptom
        st.success(f"Animal: {fa} - {fas} - Call Vet.")
        if animal_img:
            st.image(animal_img, width=300)

# CROP LIST
crop_list = [
    "Wake / Bean",
    "Dawa / Sorghum",
    "Tomato",
    "Guava",
    "Masara / Maize",
    "Cucumber",
    "Others"
]
crop_sym_list = [
    "Aphids",
    "Tuta",
    "Rot",
    "Yellow leaves",
    "Mold / Aflatoxin",
    "Others"
]
st.divider()
with st.expander("🌱 CROP HEALTH", expanded=False):
    crop = st.selectbox(
        "Select Crop",
        crop_list
    )
    crop_other_type = ""
    if crop == "Others":
        crop_other_type = st.text_input(
            "Type crop name here"
        )
    crop_symptom = st.selectbox(
        "What do you see?",
        crop_sym_list
    )
    crop_other = ""
    if crop_symptom == "Others":
        crop_other = st.text_input(
            "Type crop symptom here"
        )
        if crop_other:
            st.info(crop_other)
    st.markdown("**Photo Optional - Not Stored**")
    crop_img = st.file_uploader(
        "Upload Crop Photo",
        type=["jpg", "png"],
        key="crop"
    )
    if crop_img:
        st.image(
            crop_img,
            caption="Crop Photo Uploaded",
            width=300
        )
    if st.button("Analyze Crop"):
        fc = crop_other_type
        if fc == "":
            fc = crop
        fcs = crop_other
        if fcs == "":
            fcs = crop_symptom
        if fcs == "Aphids":
            st.error(f"{fc} - Aphids - Spray neem.")
        elif fcs == "Tuta":
            st.error(f"{fc} - Tuta - Remove fruits.")
        elif fcs == "Rot":
            st.error(f"{fc} - Rot - Bury far.")
        elif fcs == "Mold / Aflatoxin":
            st.error(f"{fc} - AFLATOXIN - DO NOT EAT.")
        elif fcs == "Others":
            st.warning(f"{fc} - {fcs} - Show Officer.")
        else:
            st.success(f"{fc} - {fcs} - Monitor.")
        if crop_img:
            st.image(crop_img, width=300)

# SAME COMPOUND
st.divider()
st.header("🏠 SAME COMPOUND CHECK")
st.markdown("Gida Daya - Same Compound")
st.caption("Hen, goat, child share room.")
q1 = st.radio(
    "1. Animals sleep in same room?",
    ["No", "Yes"]
)
q2 = st.radio(
    "2. Animals drink same water pot?",
    ["No", "Yes"]
)
q3 = st.radio(
    "3. Dung in compound?",
    ["No", "Yes"]
)
q4 = st.radio(
    "4. Eat Tomato / Guava raw no wash?",
    ["No", "Yes"]
)
q5 = st.radio(
    "5. Use FRESH dung on farm?",
    ["No", "Yes"]
)
compound_yes = 0
for q in [q1, q2, q3, q4, q5]:
    if q == "Yes":
        compound_yes = compound_yes + 1
compound_score = compound_yes * 20

if st.button("Calculate Compound Risk"):
   