# EL-DANZA OneHealth AI - Imagine Cup 2026

From Danzanfulani, Giwa LGA, Kaduna, Nigeria to Entire Africa.

One app for Human, Animal & Crop health. Where one dirty water source can make a child, a goat, and a farm sick in the same week.

Live App: https://el-danza-onehealth-ai.streamlit.app

## Features:
- Multilingual (English / Hausa / French)
- Offline-Ready
- Human, Animal, Crop Diagnosis
- Community OneHealth Log + Risk Score + Trend Chart
- Export Log as CSV + SMS Alert Demo

## What It Does
- Asks for Location: Village, Ward, LGA, State, Country
- Asks Who: Human or Animal, Age, Sex
- Asks Symptoms: Fever, Cough, Diarrhoea, Vomiting, Rash, Headache, Difficulty breathing, Loss of appetite, Weakness
- Asks Duration: Today, 1-3 days, 4-7 days, More than 1 week
- Gives Guidance: URGENT or Monitor at home

## URGENT Rule
Go to nearest Health Facility TODAY if:
- Difficulty breathing, OR
- Child under 5 with Fever + Diarrhoea + Vomiting together

Do NOT wait 48 hours.

## How To Use
1. Open the App link
2. Fill Village, Ward, LGA, State, Country
3. Choose Human or Animal
4. Enter Age and Sex
5. Select all symptoms
6. Select how long
7. Optional: Upload photo (not stored)
8. Press **Get Guidance**
9. Follow the guidance

## Home Care (If NOT Urgent)
1. Rest, clean water, light food
2. Wash hands with soap
3. If worse, go to facility immediately

> DEMO - For Education Only. Always see Doctor / Vet.

## Tech
- Python
- Streamlit
- GitHub + Streamlit Cloud

## Run Locally
```bash
pip install streamlit
streamlit run app.py