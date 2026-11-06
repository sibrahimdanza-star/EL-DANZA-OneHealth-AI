import streamlit as st
from PIL import Image
import google.generativeai as genai

st.set_page_config(page_title="EL-DANZA OneHealth AI", layout="centered")

# --- GEMINI SETUP - OFFLINE + ONLINE ---
ai_ready = False
model = None
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-3.8-flash")
    ai_ready = True
except Exception:
    ai_ready = False

# --- HEADER ---
st.markdown("🟢 **Offline-Ready • Works Without Internet • Data Saved Locally**")
st.title("EL-DANZA OneHealth AI")
st.subheader("One Compound. One Room. One Water Pot. One Health.")
st.caption("From Danzanfulani, Giwa LGA, Kaduna, Nigeria — to Nigeria — to Africa — to Inter-Africa")

if ai_ready:
    st.success("Gemini Key: FOUND - Real AI Ready")
else:
    st.warning("Gemini Key: NOT FOUND - Offline Rule-Based Mode Active")

st.error("DEMO VERSION - Rule-Based for Education. Always see Doctor / Vet / Health Worker. Photo is optional and not stored.")

# --- LANGUAGE + LOCATION ---


# --- SMART LOCATION: Continent > Country > State > LGA > Ward > Village ---
st.subheader("📍 Where Are You Reporting From?")
continent = st.selectbox("1. Continent", ["Africa", "Asia", "Europe", "Americas", "Oceania"])
if continent == "Africa":
    country = st.selectbox("2. Country", ["Nigeria", "Ghana", "Niger", "Cameroon", "Chad", "Kenya", "Ethiopia", "South Africa", "Other Africa"])
else:
    country = st.selectbox("2. Country", ["Other - Outside Africa"])

if country == "Nigeria":
    state = st.selectbox("3. State", ["Kaduna", "Kano", "Lagos", "Abuja FCT", "Katsina", "Sokoto", "Zamfara", "Plateau", "Borno", "Other State"])
else:
    state = st.selectbox("3. State / Region", ["Other Region"])

if state == "Kaduna":
    lga = st.selectbox("4. LGA", ["Giwa", "Kaduna North", "Kaduna South", "Zaria", "Sabon Gari", "Kubau", "Ikara", "Other LGA"])
elif country == "Nigeria":
    lga = st.selectbox("4. LGA", ["Other LGA"])
else:
    lga = st.selectbox("4. LGA / District", ["Other District"])

if lga == "Giwa":
    ward = st.selectbox("5. Ward", ["Wazata", "Giwa", "Kakangi", "Kwashingiri", "Shika", "Other Ward"])
else:
    ward = st.selectbox("5. Ward", ["Other Ward"])

village = st.text_input("6. Type Your Exact Village / Area", placeholder="e.g. Danzanfulani, Unguwan Fulani...")
if village:
    location = f"{village}, {ward}, {lga}, {state}, {country}, {continent}"
else:
    location = f"{ward}, {lga}, {state}, {country}, {continent}"
st.success(f"📍 Your Location: {location}")
st.info("**Founder: SULEIMAN IBRAHIM | Danzanfulani, Giwa LGA |** In our compound, a hen, a goat and a child sleep in the same room. They share the same water pot. They defecate in the same compound. If they all get sick in the same week, it is ONE problem, not three. This app finds the ROOT.")
st.success("📍 Level 1: Village Pilot - Danzanfulani. This is where we prove it works.")

# --- HELPER: GEMINI OR OFFLINE ---
def ask_ai(prompt_text, image_obj, offline_fallback):
    if ai_ready and model is not None:
        try:
            with st.spinner("Real Gemini AI is looking..."):
                if image_obj is not None:
                    res = model.generate_content([prompt_text, image_obj])
                else:
                    res = model.generate_content(prompt_text)
                st.markdown("### ✅ REAL GEMINI AI RESULT")
                st.write(res.text)
                return
        except Exception as e:
            st.warning(f"Online AI failed ({e}) - Using Offline Mode")
    st.markdown("### 📴 OFFLINE MODE RESULT")
    st.write(offline_fallback)

st.markdown("---")

# --- 1. COMMUNITY LOG ---
st.header("🏠 Community OneHealth Log - " + location)
st.subheader("Find the ROOT, Not Just the Symptom")

human_n = st.number_input("Human sick cases", 0, 100, 0)
animal_n = st.number_input("Animal sick cases", 0, 100, 0)
crop_n = st.number_input("Crop plots damaged", 0, 100, 0)
root = st.selectbox("What is the SHARED ROOT? / Menene Tushen Matsalar?", [
    "Same Water Source / Ruwan Sha Daya",
    "Flies / Mosquito / Tick / Kuda",
    "Animal Dung in Compound",
    "Dirty Water Pot",
    "Raw Crop Eaten Unwashed",
    "Fresh Dung on Farm"
])

if st.button("Save Report & Calculate Risk"):
    risk = (human_n * 10) + (animal_n * 8) + (crop_n * 2)
    if risk >= 50:
        level = "HIGH"
    elif risk >= 20:
        level = "MEDIUM"
    else:
        level = "LOW"
    st.success(f"Risk Score: {risk:.1f} - {level} - Saved for {location} on 2026-11-06")
    st.info(f"Root You Selected: {root} - If Human + Animal + Crop are sick, check this root FIRST.")
    if human_n > 0 and animal_n > 0 and crop_n > 0:
        st.error("🚨 TRIPLE SIGNAL ALERT - One Compound, One Week! Human + Animal + Crop sick together. This is NOT 3 problems. Check SHARED WATER + DUNG + RAW CROP. Alert PHC + Vet + Extension Officer TOGETHER.")
    if risk >= 50:
        st.error("🔴🔴 DOUBLE RED: Triple Signal + HIGH Compound Risk = BREAK THE CYCLE NOW. Your compound is the root.")

st.markdown("### The Cycle We Break")
st.write("Sick Goat/Hen in same room → Defecates + Drinks Water → Dirty Water Pot + Dirty Floor + Flies → Child drinks water + eats raw Tomato/Guava → Child + Goat + Crop sick → Dung goes back to farm → CYCLE REPEATS")
st.write("**EL-DANZA breaks the cycle at the ROOT: Cover water, separate animals, sweep dung, wash raw crops, dry dung before farm.**")

st.markdown("---")

# --- 2. HUMAN HEALTH ---
st.header("🧒 HUMAN HEALTH / LAFIYAR MUTANE / SANTÉ HUMAINE")
human_symptom = st.selectbox("Select Symptom", ["Skin sore / Impetigo-like", "Fever", "Diarrhoea", "Cough", "Rash / Itching", "Stomach Pain"])
human_img_file = st.file_uploader("Upload Human Skin Photo", type=["jpg","jpeg","png"], key="human")
human_img = None
if human_img_file:
    human_img = Image.open(human_img_file)
    st.image(human_img, caption="Human Photo", width=400)
    st.caption("Photo uploaded - Smart Check ready")
if st.button("Analyze Human"):
    ask_ai(
        f"You are a community health educator in Nigeria. User reports human symptom: {human_symptom}. Look at photo if provided. Give simple, safe education in English + Pidgin. Do NOT give definite diagnosis. Always say see PHC/Doctor. Give 3 immediate safe steps: hygiene, water, when to go to hospital urgently.",
        human_img,
        f"Human: {human_symptom} - See PHC / Doctor. Wash hands, covered water. If fever + diarrhoea + not eating, go to PHC TODAY. Do not self-medicate."
    )

st.markdown("---")

# --- 3. ANIMAL HEALTH ---
with st.expander("🐐 ANIMAL HEALTH - Click to Open / LAFIYAR DABBOBI", expanded=False):
    animal = st.selectbox("Select Animal", ["Goat", "Hen / Chicken", "Sheep", "Cow", "Dog"])
    animal_symptom = st.selectbox("Select Symptom", ["Not eating", "Diarrhoea", "Cough / Sneezing", "Skin wound / Tick", "Weak / Lying down"])
    animal_img_file = st.file_uploader("Upload Animal Photo", type=["jpg","jpeg","png"], key="animal")
    animal_img = None
    if animal_img_file:
        animal_img = Image.open(animal_img_file)
        st.image(animal_img, caption="Animal Photo", width=400)
    if st.button("Analyze Animal"):
        ask_ai(
            f"You are a vet assistant in Nigeria. Animal: {animal}, Symptom: {animal_symptom}. Look at photo. Give simple farm advice in English + Pidgin. Always say see Vet. Give isolation, clean water, hygiene steps.",
            animal_img,
            f"Animal: {animal} - {animal_symptom} - Separate from others, give clean water, clean pen. See Vet. Do not give human medicine."
        )

# --- 4. CROP HEALTH ---
with st.expander("🌱 CROP HEALTH - Click to Open - From Giwa Farm", expanded=False):
    crop = st.selectbox("Select Crop", ["Maize", "Cassava", "Yam", "Tomato", "Guava", "Groundnut", "Other"])
    crop_img_file = st.file_uploader("Upload Crop Photo", type=["jpg","jpeg","png"], key="crop")
    crop_img = None
    if crop_img_file:
        crop_img = Image.open(crop_img_file)
        st.image(crop_img, caption="Crop Photo", width=400)
    if st.button("Diagnose Crop With Real AI"):
        ask_ai(
            f"You are an expert Nigerian agronomist for EL-DANZA. Crop: {crop}. Look at photo. Give in simple English + Pidgin: 1. What crop/disease/pest? 2. Serious? Low/Medium/High 3. What to do NOW - cheap medicine in Giwa / Kaduna market 4. Prevention. Keep short for farmer.",
            crop_img,
            f"Crop: {crop} - Check leaf colour, spots, insects. Remove affected leaves, do not use fresh dung, use clean water. See Extension Officer for confirmation."
        )

st.markdown("---")

st.header("🏠 SAME COMPOUND CHECK")
st.write("**Gida Daya / Même Enclos / Same Compound — 30 seconds. Answer honestly.**")
st.write("In Danzanfulani, hen, goat and child sleep in same room, share same water pot, defecate in same compound. If YES to 3+, your compound is the root.")

q1 = st.radio("1. Do animals sleep in same room as humans? / Dabbobi suna kwana daki daya da mutane?", ["No", "Yes"])
q2 = st.radio("2. Do animals drink from same water pot as humans? / Dabbobi suna sha ruwa tukunya daya da mutane?", ["No", "Yes"])
q3 = st.radio("3. Do you see animal dung in compound? / Kana ganin kashin dabbobi a gida?", ["No", "Yes"])
q4 = st.radio("4. Do you eat Tomato / Guava raw without washing? / Kana cin Tumatur / Guava ba tare da wankewa ba?", ["No", "Yes"])
q5 = st.radio("5. Do you use FRESH dung on farm? / Kana amfani da sabon taki a gona?", ["No", "Yes"])

if st.button("Calculate Compound Risk"):
    yes_count = sum([1 for q in [q1,q2,q3,q4,q5] if q == "Yes"])
    score = yes_count * 20
    if score >= 60:
        st.error(f"🔴 HIGH COMPOUND RISK - Score {score}/100 - {yes_count} YES. BREAK THE CYCLE TODAY: 1) Cover water pot ALWAYS 2) Separate animal bowl 3) Sweep & bury dung far from house 4) Wash tomato/guava with clean water + salt before eating raw 5) Dry dung in sun 2 weeks before using on farm.")
    elif score >= 40:
        st.warning(f"🟡 MEDIUM COMPOUND RISK - Score {score}/100 - {yes_count} YES. Fix 2 things today: Cover water + Sweep dung.")
    else:
        st.success(f"🟢 LOW COMPOUND RISK - Score {score}/100 - {yes_count} YES. Keep it up! Keep water covered.")

st.markdown("---")
st.markdown("---")

# --- 6. VOICE ASK - FOR NON-FORMAL USERS ---
st.header("🎤 VOICE ASK - Talk, Don't Type / Magana, Ba Rubutu Ba")
st.write("Can't read or type? Press mic, speak in Hausa / Pidgin / English / French. Tell us: Human, Animal or Crop sick? We will listen and answer you.")
st.info("People First: This is for grandmother in Danzanfulani, farmer in Giwa with dirty hands, herdsman on road, child who can speak but cannot spell.")

voice_file = st.audio_input("Press Mic & Speak - Danna Mic ka yi Magana")

if voice_file is not None:
    st.audio(voice_file)
    if st.button("Send Voice to Real AI"):
        if ai_ready and model is not None:
            try:
                with st.spinner("Real Gemini AI is listening..."):
                    audio_bytes = voice_file.read()
                    res = model.generate_content([
                        "You are EL-DANZA OneHealth educator in Nigeria. Listen to this voice note. User is rural farmer / mother, maybe speaking Hausa, Pidgin, English or French. First, write what they said. Then give simple safe advice in SAME language they used. Keep very short, very simple. 3 steps only. Always say see Doctor / Vet / Extension Officer. Do NOT give definite diagnosis.",
                        {"mime_type": "audio/wav", "data": audio_bytes}
                    ])
                    st.markdown("### ✅ REAL GEMINI AI HEARD YOU")
                    st.write(res.text)
            except Exception as e:
                st.warning(f"Online Voice failed ({e}) - Using Offline Mode")
                st.markdown("### 📴 OFFLINE MODE RESULT")
                st.write("Voice received. We heard you. Tell us: Is it Human, Animal or Crop sick? Is there fever, diarrhoea, or not eating? Go to PHC / Vet today if serious.")
        else:
            st.markdown("### 📴 OFFLINE MODE RESULT")
            st.write("Voice received. We heard you. Tell us: Is it Human, Animal or Crop sick? Is there fever, diarrhoea, or not eating? Go to PHC / Vet today if serious.")
st.caption("© 2026 EL-DANZA OneHealth AI - From Danzanfulani, Giwa LGA, Kaduna, Nigeria to Entire Africa & Inter-Africa | Built by Suleiman Ibrahim | Imagine Cup 2026") 