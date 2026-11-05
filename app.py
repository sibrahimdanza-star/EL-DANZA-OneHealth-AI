import streamlit as st
from PIL import Image
import google.generativeai as genai

st.set_page_config(page_title="EL-DANZA - AI Photo Diagnosis", layout="centered")

st.title("🌾 EL-DANZA")
st.subheader("REAL AI PHOTO DIAGNOSIS")

# --- READ KEY FROM SECRETS ONLY ---
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    st.success("Gemini Key: FOUND - Real AI Ready")
    ai_ready = True
except Exception:
    st.error("Gemini Key: NOT FOUND - Put key in Secrets")
    ai_ready = False

st.markdown("---")
st.markdown("### 📸 Upload Crop Photo")

uploaded = st.file_uploader("Take or Upload Photo", type=["jpg", "jpeg", "png"])

if uploaded is not None:
    image = Image.open(uploaded)
    st.image(image, caption="Your Crop Photo", use_container_width=True)

    if st.button("🔍 DIAGNOSE WITH REAL AI", type="primary", use_container_width=True):
        if not ai_ready:
            st.error("Add your Gemini key in Secrets first.")
        else:
            with st.spinner("Real Gemini AI is looking at your photo..."):
                try:
                    prompt = """
                    You are an expert Nigerian agronomist for EL-DANZA farm in Rivers State.
                    Look at this crop photo carefully.
                    Give answer in simple English + simple Pidgin.
                    1. What crop is this?
                    2. What disease / pest do you see? Or is it healthy?
                    3. How serious? Low / Medium / High
                    4. What to do NOW - name cheap medicine available in Port Harcourt market
                    5. How to prevent next time
                    Keep it short, clear, for a farmer.
                    """
                    response = model.generate_content([prompt, image])
                    st.markdown("### ✅ REAL GEMINI AI RESULT")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"AI Error: {e}")
                    st.info("Check your key in Secrets and Reboot app.")

st.markdown("---")
st.caption("EL-DANZA - SULEIMAN IBRAHIM - Port Harcourt - CROP ONLY")