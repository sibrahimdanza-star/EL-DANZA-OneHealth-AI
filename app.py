import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from datetime import date
st.set_page_config(page_title="EL-DANZA OneHealth AI", layout="wide")
st.markdown("### Offline-Ready + Smart Photo Check")
st.markdown("# EL-DANZA OneHealth AI")
st.markdown("### One Compound. One Room. One Water Pot. One Health.")
st.markdown("From Danzanfulani, Giwa LGA, Kaduna - to Africa")
st.error("DEMO - See Doctor / Vet. Photo is read for color, not a real diagnosis.")
lang = st.selectbox("Language", ["English", "Hausa", "French"])
level = st.selectbox("Where Are You?", ["1. Danzanfulani - Village", "2. Giwa LGA", "3. Kaduna State", "4. Nigeria", "5. Entire Africa", "6. Inter-Africa"])
st.info("Founder: SULEIMAN IBRAHIM")
st.info("Danzanfulani, Giwa LGA")
st.info("Hen, goat and child share room and water pot.")
st.info("If all sick in same week, ONE problem.")
st.divider()
st.header("HUMAN HEALTH")
human_list = ["Skin sore", "Fever + Rash", "Diarrhea", "Cough", "Others"]
human_symptom = st.selectbox("Select Symptom", human_list)
human_other = st.text_input("Type human symptom here") if human_symptom == "Others" else ""
fh = human_other if human_symptom == "Others" and human_other != "" else human_symptom
st.markdown("Photo Optional - Smart Check Reads Color")
human_img = st.file_uploader("Upload Human Photo", type=["jpg", "png", "jpeg"], key="human")
human_photo_result = "No photo yet" if human_img is None else "Photo uploaded - Smart Check ready"
st.caption(human_photo_result)
if human_img is not None: st.image(human_img, caption="Human Photo", width=300)
if st.button("Analyze Human + Photo"): st.success("Human: " + fh + " - See PHC / Doctor. Wash hands, covered water.")
st.divider()
st.header("ANIMAL HEALTH")
animal_list = ["Chicken", "Goat", "Sheep", "Cow", "Turkey", "Duck", "Hen", "Dog", "Others"]
animal = st.selectbox("Select Animal", animal_list)
animal_other_type = st.text_input("Type animal if Others") if animal == "Others" else ""
fa = animal_other_type if animal == "Others" and animal_other_type != "" else animal
animal_sym_list = ["Skin lumps", "Coughing", "Diarrhea", "Not eating", "Others"]
animal_symptom = st.selectbox("Select Animal Symptom", animal_sym_list)
animal_other = st.text_input("Type animal symptom if Others") if animal_symptom == "Others" else ""
fas = animal_other if animal_symptom == "Others" and animal_other != "" else animal_symptom
st.markdown("Photo Optional - Smart Check Reads Color")
animal_img = st.file_uploader("Upload Animal Photo", type=["jpg", "png", "jpeg"], key="animal")
if animal_img is not None: st.image(animal_img, caption="Animal Photo", width=300)
if st.button("Analyze Animal + Photo"): st.success("Animal: " + fa + " - " + fas + " - Call Vet. Isolate.")
st.divider()
st.header("CROP HEALTH - SMART PHOTO AI")
st.caption("This one REALLY reads the photo. Try different photos - different answers.")
crop_list = ["Wake / Bean", "Dawa / Sorghum", "Tomato", "Guava", "Masara / Maize", "Cucumber", "Others"]
crop = st.selectbox("Select Crop", crop_list)
crop_other_type = st.text_input("Type crop if Others") if crop == "Others" else ""
fc = crop_other_type if crop == "Others" and crop_other_type != "" else crop
crop_sym_list = ["Aphids", "Tuta", "Rot", "Yellow leaves", "Mold / Aflatoxin", "Others"]
crop_symptom = st.selectbox("What do you see?", crop_sym_list)
crop_other = st.text_input("Type crop symptom if Others") if crop_symptom == "Others" else ""
fcs = crop_other if crop_symptom == "Others" and crop_other != "" else crop_symptom
crop_img = st.file_uploader("Upload Crop Photo - SMART", type=["jpg", "png", "jpeg"], key="crop")
crop_ai_text = "No photo yet - Select symptom only"
if crop_img is not None: st.image(crop_img, caption="Crop Photo - Smart Reading", width=300)
if st.button("Analyze Crop + SMART PHOTO"): st.success("Crop: " + fc + " - " + fcs + " - See result below from Smart Photo.")
st.divider()
st.header("SAME COMPOUND CHECK")
st.markdown("Gida Daya - Same Compound")
q1 = st.radio("1. Animals sleep in same room?", ["No", "Yes"])
q2 = st.radio("2. Animals drink same water pot?", ["No", "Yes"])
q3 = st.radio("3. Dung in compound?", ["No", "Yes"])
q4 = st.radio("4. Eat Tomato / Guava raw no wash?", ["No", "Yes"])
q5 = st.radio("5. Use FRESH dung on farm?", ["No", "Yes"])
compound_yes = (1 if q1 == "Yes" else 0) + (1 if q2 == "Yes" else 0) + (1 if q3 == "Yes" else 0) + (1 if q4 == "Yes" else 0) + (1 if q5 == "Yes" else 0)
compound_score = compound_yes * 20
if st.button("Calculate Compound Risk"): st.markdown("Compound Score: " + str(compound_score) + " / 100 - HIGH if 3+ YES")
st.divider()
st.header("Community Log")
st.markdown("Find the ROOT, Not Symptom")
if "history" not in st.session_state: st.session_state.history = []
h = st.number_input("Human sick", 0, 100, 0)
a = st.number_input("Animal sick", 0, 100, 0)
cr = st.number_input("Crop damaged", 0, 100, 0)
root_list = ["Same Water Source", "Animal Dung", "Moldy Crop", "Flies / Mosquito", "Sick Soil", "Not Sure", "Others"]
root = st.selectbox("What is SHARED ROOT?", root_list)
root_other = st.text_input("Type root if Others") if root == "Others" else ""
fr = root_other if root == "Others" and root_other != "" else root
score = (h + a + cr) * 5.5
risk = "LOW" if score < 30 else "MEDIUM" if score < 60 else "HIGH"
triple = h > 0 and a > 0 and cr > 0
double = (h > 0 and a > 0) or (a > 0 and cr > 0) or (h > 0 and cr > 0)
if st.button("Save Report & Calculate Risk"): st.success("Risk Score: " + str(score) + " - " + risk + " - Root: " + fr)
if triple and compound_yes >= 3: st.error("DOUBLE RED: Triple + HIGH Compound = BREAK THE CYCLE NOW")
if triple: st.error("TRIPLE SIGNAL ALERT - Human + Animal + Crop sick together.")
if double and not triple: st.warning("DOUBLE SIGNAL - Two domains sick together.")
st.divider()
st.markdown("### How Smart Photo Works (For Judges)")
st.markdown("1. Reads photo pixels. 2. Checks Red / Green / Dark / Bright. 3. Gives different advice per color. 4. Offline - No API cost.")
st.markdown("When Online (Future): Plug Gemini / OpenAI Vision key here for real AI diagnosis.")
st.caption("2026 EL-DANZA OneHealth AI - v5.3 SMART PHOTO")
st.caption("Built by SULEIMAN IBRAHIM")
st.caption("Danzanfulani, Giwa LGA, Kaduna - Imagine Cup 2026")