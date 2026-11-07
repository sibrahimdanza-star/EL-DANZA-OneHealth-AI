import streamlit as st
import sqlite3
import datetime
from PIL import Image

st.set_page_config(page_title="EL-DANZA OneHealth AI", layout="centered", page_icon="🟢")

# STEP 1 - MULTI-LANGUAGE DICTIONARY - Kept 100%
LANG = st.selectbox("Language / Harshe / Harshen", ["English", "Hausa", "Pidgin"])
TEXT = {
    "English": {
        "title": "EL-DANZA OneHealth AI",
        "subtitle": "One Compound. One Room. One Water Pot. One Health.",
        "badge": "Offline-Ready - Azure Ready When Connected - Local SQLite Active",
        "tab_compound": "🏠 Compound Risk & Log",
        "tab_human": "🧒 Human Health",
        "tab_animal": "🐐 Animal Health",
        "tab_crop": "🌱 Crop Health",
        "tab_survey": "🔍 Compound Audit",
        "tab_help": "🏥 Find Help Nearby"
    },
    "Hausa": {
        "title": "EL-DANZA Lafiya Daya",
        "subtitle": "Gida Daya. Daki Daya. Tukunya Daya. Lafiya Daya.",
        "badge": "Yana Aiki Ba Tare da Intanet ba - Azure A Shirye - Ajiya a Na'ura",
        "tab_compound": "🏠 Nazarin Gida da Hadari",
        "tab_human": "🧒 Lafiyar Mutane",
        "tab_animal": "🐐 Lafiyar Dabbobi",
        "tab_crop": "🌱 Lafiyar Gona",
        "tab_survey": "🔍 Binciken Gida",
        "tab_help": "🏥 Nemo Taimako Kusa da Kai"
    },
    "Pidgin": {
        "title": "EL-DANZA OneHealth AI",
        "subtitle": "One Compound. One Room. One Water Pot. One Health.",
        "badge": "E Work Offline - Azure Ready When Connected - Local DB Ready",
        "tab_compound": "🏠 Compound Risk & Log",
        "tab_human": "🧒 Human Health",
        "tab_animal": "🐐 Animal Health",
        "tab_crop": "🌱 Crop Health",
        "tab_survey": "🔍 Compound Check",
        "tab_help": "🏥 Find Help Near You"
    }
}
T = TEXT[LANG]

# STEP 1 - AZURE OPENAI SETUP - Kept 100%
azure_ready = False
azure_client = None
try:
    from openai import AzureOpenAI
    if "AZURE_OPENAI_API_KEY" in st.secrets and "AZURE_OPENAI_ENDPOINT" in st.secrets:
        azure_client = AzureOpenAI(
            api_key=st.secrets["AZURE_OPENAI_API_KEY"],
            api_version="2024-10-21",
            azure_endpoint=st.secrets["AZURE_OPENAI_ENDPOINT"]
        )
        azure_ready = True
except Exception:
    azure_ready = False

# STEP 1 - SQLITE LOCAL DATABASE SETUP - Kept 100%
conn = sqlite3.connect("eldanza_reports.db", check_same_thread=False)
conn.execute("""
CREATE TABLE IF NOT EXISTS reports (
    date TEXT,
    location TEXT,
    human INT,
    animal INT,
    crop INT,
    root TEXT,
    risk_score REAL,
    level TEXT
)
""")
conn.commit()

# STEP 1 - HEADER - Kept 100%
st.markdown(T["badge"])
st.title(T["title"])
st.subheader(T["subtitle"])
st.caption("From Danzanfulani, Giwa LGA, Kaduna, Nigeria - to Nigeria - to Africa - to Inter-Africa")

if azure_ready:
    st.success("Microsoft Azure OpenAI: CONNECTED (Cloud AI Ready)")
else:
    st.warning("Azure AI Key Missing - Running Local Offline Rule-Based Mode")

st.error("DEMO VERSION - Educational Tool. Always consult a certified Doctor, Vet, or Extension Officer.")

# STEP 2 - LOCATION HIERARCHY - CORRECTED, 100% DATA MAINTAINED
st.subheader("Location Setup / Wurin Da Kake")
continent = st.selectbox("Continent", ["Africa", "Asia", "Europe", "North America", "South America", "Oceania"])

AFRICA_COUNTRIES = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Cote d'Ivoire", "DR Congo", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Republic of Congo", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]

if continent == "Africa":
    country = st.selectbox("Country", AFRICA_COUNTRIES, index=AFRICA_COUNTRIES.index("Nigeria"))
else:
    country = st.text_input("Country", "Nigeria")

# Full Nigeria - 36 States + FCT with LGAs - Maintained 100%
NIGERIA_DATA = {
    "Abia": ["Aba North", "Aba South", "Arochukwu", "Bende", "Ikwuano", "Isiala Ngwa North", "Isiala Ngwa South", "Isuikwuato", "Obi Ngwa", "Ohafia", "Osisioma Ngwa", "Ugwunagbo", "Ukwa East", "Ukwa West", "Umuahia North", "Umuahia South", "Umunneochi"],
    "Adamawa": ["Demsa", "Fufore", "Ganye", "Girei", "Gombi", "Guyuk", "Hong", "Jada", "Lamurde", "Madagali", "Maiha", "Mayo-Belwa", "Michika", "Mubi North", "Mubi South", "Numan", "Shelleng", "Song", "Toungo", "Yola North", "Yola South"],
    "Akwa Ibom": ["Abak", "Eastern Obolo", "Eket", "Esit Eket", "Essien Udim", "Etim Ekpo", "Etinan", "Ibeno", "Ibesikpo Asutan", "Ibiono Ibom", "Ika", "Ikono", "Ikot Abasi", "Ikot Ekpene", "Ini", "Itu", "Mbo", "Mkpat Enin", "Nsit Atai", "Nsit Ibom", "Nsit Ubium", "Obot Akara", "Okobo", "Onna", "Oron", "Oruk Anam", "Udung Uko", "Ukanafun", "Uruan", "Urue-Offong/Oruko", "Uyo"],
    "Anambra": ["Aguata", "Anambra East", "Anambra West", "Anaocha", "Awka North", "Awka South", "Ayamelum", "Dunukofia", "Ekwusigo", "Idemili North", "Idemili South", "Ihiala", "Njikoka", "Nnewi North", "Nnewi South", "Ogbaru", "Onitsha North", "Onitsha South", "Orumba North", "Orumba South", "Oyi"],
    "Bauchi": ["Alkaleri", "Bauchi", "Bogoro", "Damban", "Darazo", "Dass", "Ganjuwa", "Giade", "Itas/Gadau", "Jama'are", "Katagum", "Kirfi", "Misau", "Ningi", "Shira", "Tafawa Balewa", "Toro", "Warji", "Zaki"],
    "Bayelsa": ["Brass", "Ekeremor", "Kolokuma/Opokuma", "Nembe", "Ogbia", "Sagbama", "Southern Ijaw", "Yenagoa"],
    "Benue": ["Ado", "Agatu", "Apa", "Buruku", "Gboko", "Guma", "Gwer East", "Gwer West", "Katsina-Ala", "Konshisha", "Kwande", "Logo", "Makurdi", "Obi", "Ogbadibo", "Oju", "Okpokwu", "Ohimini", "Oturkpo", "Tarka", "Ukum", "Ushongo", "Vandeikya"],
    "Borno": ["Abadam", "Askira/Uba", "Bama", "Bayo", "Biu", "Chibok", "Damboa", "Dikwa", "Gubio", "Guzamala", "Gwoza", "Hawul", "Jere", "Kaga", "Kala/Balge", "Konduga", "Kukawa", "Kwaya Kusar", "Mafa", "Magumeri", "Maiduguri", "Marte", "Mobbar", "Monguno", "Ngala", "Nganzai", "Shani"],
    "Cross River": ["Abi", "Akamkpa", "Akpabuyo", "Bakassi", "Bekwarra", "Biase", "Boki", "Calabar Municipal", "Calabar South", "Etung", "Ikom", "Obanliku", "Obubra", "Obudu", "Odukpani", "Ogoja", "Yakurr", "Yala"],
    "Delta": ["Aniocha North", "Aniocha South", "Bomadi", "Burutu", "Ethiope East", "Ethiope West", "Ika North East", "Ika South", "Isoko North", "Isoko South", "Ndokwa East", "Ndokwa West", "Okpe", "Oshimili North", "Oshimili South", "Patani", "Sapele", "Udu", "Ughelli North", "Ughelli South", "Ukwuani", "Uvwie", "Warri North", "Warri South", "Warri South West"],
    "Ebonyi": ["Abakaliki", "Afikpo North", "Afikpo South", "Ebonyi", "Ezza North", "Ezza South", "Ikwo", "Ishielu", "Ivo", "Izzi", "Ohaozara", "Ohaukwu", "Onicha"],
    "Edo": ["Akoko-Edo", "Egor", "Esan Central", "Esan North-East", "Esan South-East", "Esan West", "Etsako Central", "Etsako East", "Etsako West", "Igueben", "Ikpoba-Okha", "Oredo", "Orhionmwon", "Ovia North-East", "Ovia South-West", "Owan East", "Owan West", "Uhunmwonde"],
    "Ekiti": ["Ado Ekiti", "Efon", "Ekiti East", "Ekiti South-West", "Ekiti West", "Emure", "Gbonyin", "Ido-Osi", "Ijero", "Ikere", "Ikole", "Ilejemeje", "Irepodun/Ifelodun", "Ise/Orun", "Moba", "Oye"],
    "Enugu": ["Aninri", "Awgu", "Enugu East", "Enugu North", "Enugu South", "Ezeagu", "Igbo Etiti", "Igbo Eze North", "Igbo Eze South", "Isi Uzo", "Nkanu East", "Nkanu West", "Nsukka", "Oji River", "Udenu", "Udi", "Uzo-Uwani"],
    "FCT": ["Abaji", "Bwari", "Gwagwalada", "Kuje", "Kwali", "Abuja Municipal"],
    "Gombe": ["Akko", "Balanga", "Billiri", "Dukku", "Funakaye", "Gombe", "Kaltungo", "Kwami", "Nafada", "Shongom", "Yamaltu/Deba"],
    "Imo": ["Aboh Mbaise", "Ahiazu Mbaise", "Ehime Mbano", "Ezinihitte", "Ideato North", "Ideato South", "Ihitte/Uboma", "Ikeduru", "Isiala Mbano", "Isu", "Mbaitoli", "Ngor Okpala", "Njaba", "Nkwerre", "Nwangele", "Obowo", "Oguta", "Ohaji/Egbema", "Okigwe", "Onuimo", "Orlu", "Orsu", "Oru East", "Oru West", "Owerri Municipal", "Owerri North", "Owerri West"],
    "Jigawa": ["Auyo", "Babura", "Biriniwa", "Birnin Kudu", "Buji", "Dutse", "Gagarawa", "Garki", "Gumel", "Guri", "Gwaram", "Gwiwa", "Hadejia", "Jahun", "Kafin Hausa", "Kaugama", "Kazaure", "Kiri Kasama", "Kiyawa", "Maigatari", "Malam Madori", "Miga", "Ringim", "Roni", "Sule Tankarkar", "Taura", "Yankwashi"],
    "Kaduna": ["Birnin Gwari", "Chikun", "Giwa", "Igabi", "Ikara", "Jaba", "Jema'a", "Kachia", "Kaduna North", "Kaduna South", "Kagarko", "Kajuru", "Kaura", "Kauru", "Kubau", "Kudan", "Lere", "Makarfi", "Sabon Gari", "Sanga", "Soba", "Zangon Kataf", "Zaria"],
    "Kano": ["Ajingi", "Albasu", "Bagwai", "Bebeji", "Bichi", "Bunkure", "Dala", "Dambatta", "Dawakin Kudu", "Dawakin Tofa", "Doguwa", "Fagge", "Gabasawa", "Garko", "Garun Mallam", "Gaya", "Gezawa", "Gwale", "Gwarzo", "Kabo", "Kano Municipal", "Karaye", "Kibiya", "Kiru", "Kumbotso", "Kunchi", "Kura", "Madobi", "Makoda", "Minjibir", "Nasarawa", "Rano", "Rimin Gado", "Rogo", "Shanono", "Sumaila", "Takai", "Tarauni", "Tofa", "Tsanyawa", "Tudun Wada", "Ungogo", "Warawa", "Wudil"],
    "Katsina": ["Bakori", "Batagarawa", "Batsari", "Baure", "Bindawa", "Charanchi", "Dan Musa", "Dandume", "Danja", "Daura", "Dutsi", "Dutsin-Ma", "Faskari", "Funtua", "Ingawa", "Jibia", "Kafur", "Kaita", "Kankara", "Kankia", "Katsina", "Kurfi", "Kusada", "Mai'Adua", "Malumfashi", "Mani", "Mashi", "Matazu", "Musawa", "Rimi", "Sabuwa", "Safana", "Sandamu", "Zango"],
    "Kebbi": ["Aleiro", "Arewa Dandi", "Argungu", "Augie", "Bagudo", "Birnin Kebbi", "Bunza", "Dandi", "Fakai", "Gwandu", "Jega", "Kalgo", "Koko/Besse", "Maiyama", "Ngaski", "Sakaba", "Shanga", "Suru", "Wasagu/Danko", "Yauri", "Zuru"],
    "Kogi": ["Adavi", "Ajaokuta", "Ankpa", "Bassa", "Dekina", "Ibaji", "Idah", "Igalamela-Odolu", "Ijumu", "Kabba/Bunu", "Kogi", "Lokoja", "Mopa-Muro", "Ofu", "Ogori/Magongo", "Okehi", "Okene", "Olamaboro", "Omala", "Yagba East", "Yagba West"],
    "Kwara": ["Asa", "Baruten", "Edu", "Ekiti", "Ifelodun", "Ilorin East", "Ilorin South", "Ilorin West", "Irepodun", "Isin", "Kaiama", "Moro", "Offa", "Oke Ero", "Oyun", "Pategi"],
    "Lagos": ["Agege", "Ajeromi-Ifelodun", "Alimosho", "Amuwo-Odofin", "Apapa", "Badagry", "Epe", "Eti-Osa", "Ibeju-Lekki", "Ifako-Ijaiye", "Ikeja", "Ikorodu", "Kosofe", "Lagos Island", "Lagos Mainland", "Mushin", "Ojo", "Oshodi-Isolo", "Shomolu", "Surulere"],
    "Nasarawa": ["Akwanga", "Awe", "Doma", "Karu", "Keana", "Keffi", "Kokona", "Lafia", "Nasarawa", "Nasarawa Egon", "Obi", "Toto", "Wamba"],
    "Niger": ["Agaie", "Agwara", "Bida", "Borgu", "Bosso", "Chanchaga", "Edati", "Gbako", "Gurara", "Katcha", "Kontagora", "Lapai", "Lavun", "Magama", "Mariga", "Mashegu", "Mokwa", "Munya", "Paikoro", "Rafi", "Rijau", "Shiroro", "Suleja", "Tafa", "Wushishi"],
    "Ogun": ["Abeokuta North", "Abeokuta South", "Ado-Odo/Ota", "Egbado North", "Egbado South", "Ewekoro", "Ifo", "Ijebu East", "Ijebu North", "Ijebu North East", "Ijebu Ode", "Ikenne", "Imeko Afon", "Ipokia", "Obafemi Owode", "Odeda", "Odogbolu", "Ogun Waterside", "Remo North", "Shagamu"],
    "Ondo": ["Akoko North-East", "Akoko North-West", "Akoko South-East", "Akoko South-West", "Akure North", "Akure South", "Ese Odo", "Idanre", "Ifedore", "Ilaje", "Irele", "Ile Oluji/Okeigbo", "Odigbo", "Okitipupa", "Ondo East", "Ondo West", "Ose", "Owo"],
    "Osun": ["Atakunmosa East", "Atakunmosa West", "Ayedaade", "Ayedire", "Boluwaduro", "Boripe", "Ede North", "Ede South", "Egbedore", "Ejigbo", "Ife Central", "Ife East", "Ife North", "Ife South", "Ifedayo", "Ifelodun", "Ila", "Ilesa East", "Ilesa West", "Irepodun", "Irewole", "Isokan", "Iwo", "Obokun", "Odo Otin", "Ola Oluwa", "Olorunda", "Oriade", "Orolu", "Osogbo"],
    "Oyo": ["Afijio", "Akinyele", "Atiba", "Atisbo", "Egbeda", "Ibadan North", "Ibadan North-East", "Ibadan North-West", "Ibadan South-East", "Ibadan South-West", "Ibarapa Central", "Ibarapa East", "Ibarapa North", "Ido", "Irepo", "Iseyin", "Itesiwaju", "Iwajowa", "Kajola", "Lagelu", "Ogbomosho North", "Ogbomosho South", "Ogo Oluwa", "Olorunsogo", "Ona Ara", "Oorelope", "Ori Ire", "Oyo", "Oyo East", "Saki East", "Saki West", "Surulere"],
    "Plateau": ["Barkin Ladi", "Bassa", "Bokkos", "Jos East", "Jos North", "Jos South", "Kanam", "Kanke", "Langtang North", "Langtang South", "Mangu", "Mikang", "Pankshin", "Qua'an Pan", "Riyom", "Shendam", "Wase"],
    "Rivers": ["Abua/Odual", "Ahoada East", "Ahoada West", "Akuku-Toru", "Andoni", "Asari-Toru", "Bonny", "Degema", "Eleme", "Emuoha", "Etche", "Gokana", "Ikwerre", "Khana", "Obio/Akpor", "Ogba/Egbema/Ndoni", "Ogu/Bolo", "Okrika", "Omuma", "Opobo/Nkoro", "Oyigbo", "Port Harcourt", "Tai"],
    "Sokoto": ["Binji", "Bodinga", "Dange Shuni", "Gada", "Goronyo", "Gudu", "Gwadabawa", "Illela", "Isa", "Kebbe", "Kware", "Rabah", "Sabon Birni", "Shagari", "Silame", "Sokoto North", "Sokoto South", "Tambuwal", "Tangaza", "Tureta", "Wamako", "Wurno", "Yabo"],
    "Taraba": ["Ardo Kola", "Bali", "Donga", "Gashaka", "Gassol", "Ibi", "Jalingo", "Karim Lamido", "Kurmi", "Lau", "Sardauna", "Takum", "Ussa", "Wukari", "Yorro", "Zing"],
    "Yobe": ["Bade", "Bursari", "Damaturu", "Fika", "Fune", "Geidam", "Gujba", "Gulani", "Jakusko", "Karasuwa", "Machina", "Nangere", "Nguru", "Potiskum", "Tarmuwa", "Yunusari", "Yusufari"],
    "Zamfara": ["Anka", "Bakura", "Birnin Magaji", "Bukkuyum", "Bungudu", "Chafe", "Gummi", "Gusau", "Kaura Namoda", "Maradun", "Maru", "Shinkafi", "Talata Mafara", "Zurmi"]
}

# Detailed pilot wards - CORRECTED: Danzanfulani is Village, NOT Ward. Wazata is Ward.
WARD_DATA = {
    "Kaduna": {
        "Giwa": ["Wazata", "Giwa", "Kakangi", "Kidandan", "Shika", "Idasu", "Panhauya", "Gangara", "Galadimawa", "Yakawada", "Danmahawayi"],
        "Sabon Gari": ["Sabon Gari", "Zabi", "Bomo", "Basawa"],
        "Zaria": ["Tudun Wada", "Wusasa", "Pangaskia", "Kofan Doka"]
    },
    "Kano": {
        "Kano Municipal": ["Sharada", "Cikin Gari", "Kano City"],
        "Nasarawa": ["Giginyu", "Kaura Goje", "Dakata"]
    }
}

if country == "Nigeria":
    state_list = list(NIGERIA_DATA.keys())
    state = st.selectbox("State", state_list, index=state_list.index("Kaduna"))
    lga_options = NIGERIA_DATA[state]
    lga = st.selectbox("LGA", lga_options, index=lga_options.index("Giwa") if state == "Kaduna" and "Giwa" in lga_options else 0)
    if state in WARD_DATA and lga in WARD_DATA[state]:
        ward_options = WARD_DATA[state][lga]
        ward = st.selectbox("Ward", ward_options, index=ward_options.index("Wazata") if "Wazata" in ward_options else 0)
    else:
        ward = st.text_input("Ward", "")
    village = st.text_input("Village / Area", "Danzanfulani" if state == "Kaduna" and lga == "Giwa" else "")
else:
    state = st.text_input("State / Region", "")
    lga = st.text_input("LGA / District", "")
    ward = st.text_input("Ward", "")
    village = st.text_input("Village / Area", "")

location = f"{village}, {ward} Ward, {lga}, {state}, {country}"
st.info(f"Active Location: {location} | Founder: Suleiman Ibrahim (Danzanfulani)")


# STEP 3 - TAB 1: COMPOUND LOG & RISK SCORING - ADDED BY EDIT, STEP 1 AND 2 KEPT
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    T["tab_compound"],
    T["tab_human"],
    T["tab_animal"],
    T["tab_crop"],
    T["tab_survey"],
    T["tab_help"]
])

with tab1:
    st.header("Community OneHealth Compound Log")
    st.write("In our compound, a hen, a goat and a child share the same room, water pot, and soil. If they get sick together, it is ONE root cause.")
    human_n = st.number_input("Human sick cases in compound", 0, 50, 0)
    animal_n = st.number_input("Animal sick cases in compound", 0, 50, 0)
    crop_n = st.number_input("Crop plots damaged / wilting", 0, 50, 0)
    root = st.selectbox("Identified Shared Root Cause / Tushen Matsalar:", [
        "Same Water Source / Ruwan Sha Daya",
        "Flies / Mosquito / Tick / Kuda da Sauro",
        "Animal Dung on Compound Soil / Kashin Dabbobi",
        "Dirty Shared Water Pot / Tukunyar Ruwa Mai Datti",
        "Raw Crop Eaten Unwashed / Cin Abinci Ba Wankewa"
    ])
    if st.button("Save Report & Calculate Compound Risk", type="primary"):
        risk = (human_n * 10) + (animal_n * 8) + (crop_n * 2)
        level = "HIGH" if risk >= 50 else ("MEDIUM" if risk >= 20 else "LOW")
        conn.execute("INSERT INTO reports VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (str(datetime.date.today()), location, human_n, animal_n, crop_n, root, risk, level))
        conn.commit()
        st.success(f"Risk Score: {risk:.1f} - Level: {level} - Saved to Local DB!")
        if human_n > 0 and animal_n > 0 and crop_n > 0:
            st.error("TRIPLE SIGNAL ALERT: Human + Animal + Crop sick simultaneously in one compound! Check Shared Water + Dung + Raw Crops immediately. Alert PHC and Vet together.")
        elif risk >= 50:
            st.error("HIGH COMPOUND RISK: Break the cycle today. Separate water sources and clean animal pens.")
        st.caption("For education only. This score is a community signal, not a medical diagnosis. See Doctor / Vet.")
    st.info("Step 3 Test: Tab 1 Compound Log is working. Try Human=2, Animal=2, Crop=1 and press Save.")

with tab2:
    st.header("Human Health Check")
    st.write("Check one person at a time. This is guidance only, not a diagnosis.")
    h_symptom = st.selectbox("Main Symptom / Babban Alamun:", ["Fever / Zazzabi", "Diarrhoea / Gudawa", "Vomiting / Amai", "Cough / Difficulty Breathing / Tari", "Skin Rash / Itching / Kaikayi", "Stomach Pain / Ciwon Ciki"])
    h_age = st.number_input("Age of Person", 0, 120, 5)
    h_photo = st.file_uploader("Upload Photo of Symptom (Optional) - Human", type=["jpg", "jpeg", "png"], key="human_photo")
    if h_photo is not None:
        st.image(h_photo, caption="Human symptom photo uploaded", width=250)
    if st.button("Get Human Guidance"):
        if h_age < 5 and h_symptom in ["Fever / Zazzabi", "Diarrhoea / Gudawa", "Vomiting / Amai", "Cough / Difficulty Breathing / Tari"]:
            st.error("URGENT: Child Under 5 - Go to PHC immediately. Do not wait. Give clean water, keep child warm, do not give adult medicine.")
        elif h_symptom == "Fever / Zazzabi":
            st.warning("Fever Guidance: Rest, drink clean boiled water, use mosquito net. Go to PHC if fever lasts more than 2 days or child is weak.")
        elif h_symptom == "Diarrhoea / Gudawa":
            st.warning("Diarrhoea Guidance: Give ORS / clean water often. Wash hands. Go to PHC if blood in stool or child is very weak.")
        elif h_symptom == "Vomiting / Amai":
            st.warning("Vomiting Guidance: Give small sips of clean water. Do not force food. Go to PHC if vomiting continues.")
        elif h_symptom == "Cough / Difficulty Breathing / Tari":
            st.warning("Cough Guidance: Keep away from smoke. Drink warm water. Go to PHC urgently if breathing is difficult.")
        elif h_symptom == "Skin Rash / Itching / Kaikayi":
            st.warning("Skin Guidance: Wash with clean water, keep area dry. Do not scratch. Go to PHC if spreading fast.")
        else:
            st.warning("Stomach Pain Guidance: Drink clean water, rest. Go to PHC if pain is severe or with fever.")
        st.caption("For education only. Always see a certified Doctor / PHC.")

with tab3:
    st.header("Animal Health Check")
    st.write("Check one animal at a time. Separate sick animal from healthy ones.")
    a_type = st.selectbox("Animal Type / Nau'in Dabba:", ["Goat / Akuya", "Sheep / Tumaki", "Cow / Saniya", "Chicken / Hen / Kaza", "Dog / Kare"])
    a_symptom = st.selectbox("Animal Symptom / Alamun Dabba:", ["Fever / Zazzabi", "Diarrhoea / Gudawa", "Not Eating / Baya Ci", "Cough / Tari", "Skin Sores / Rauni a Fata"])
    a_photo = st.file_uploader("Upload Photo of Animal (Optional) - Animal", type=["jpg", "jpeg", "png"], key="animal_photo")
    if a_photo is not None:
        st.image(a_photo, caption="Animal photo uploaded", width=250)
    if st.button("Get Animal Guidance"):
        st.warning(f"Isolate the {a_type} immediately. Do not mix with healthy animals. Clean pen, give clean water.")
        if a_symptom == "Fever / Zazzabi":
            st.warning("Fever in animal: Keep in shade, give clean water. Call Vet urgently, do not give human medicine.")
        elif a_symptom == "Diarrhoea / Gudawa":
            st.warning("Diarrhoea in animal: Give clean water, clean pen. Call Vet if blood or animal is weak.")
        elif a_symptom == "Not Eating / Baya Ci":
            st.warning("Not eating: Check teeth, water, and pen. Call Vet if more than 1 day.")
        elif a_symptom == "Cough / Tari":
            st.warning("Cough in animal: Separate from others, keep dry. Call Vet.")
        else:
            st.warning("Skin sores: Wash with clean water, keep flies away. Call Vet, do not use dirty herbs on open wound.")
        st.caption("For education only. Always see a certified Vet.")

with tab4:
    st.header("Crop Health Check")
    st.write("Check one crop plot at a time. Do not eat unwashed raw crop from sick plot.")
    c_type = st.selectbox("Crop Type / Nau'in Gona:", ["Maize / Masara", "Millet / Gero", "Sorghum / Dawa", "Groundnut / Gyada", "Rice / Shinkafa", "Vegetables / Kayan Lambu"])
    c_photo = st.file_uploader("Upload Photo of Crop (Optional) - Crop", type=["jpg", "jpeg", "png"], key="crop_photo")
    if c_photo is not None:
        st.image(c_photo, caption="Crop photo uploaded", width=250)
    if st.button("Get Crop Guidance"):
        st.warning(f"For {c_type}: Check water, soil, and pests. Remove damaged leaves, do not spray near water pot or animal pen.")
        st.warning("Guidance: Wash hands after farm work. Wash crop well before eating. Ask Extension Officer before using any chemical. Keep children and animals away from sprayed plot for 2 days.")
        st.caption("For education only. Always see a certified Extension Officer / Agro Dealer.")
with tab5:
    st.header("Compound Audit - Check Your Compound")
    st.write("Answer honestly. This audit shows where your compound is strong and where to fix today.")
    q1 = st.checkbox("1. Clean drinking water is covered and separate from animals?")
    q2 = st.checkbox("2. Animal pen is separate from sleeping room?")
    q3 = st.checkbox("3. Family washes hands with soap after toilet / farm?")
    q4 = st.checkbox("4. Compound has clean latrine / toilet?")
    q5 = st.checkbox("5. Children sleep under mosquito net?")
    q6 = st.checkbox("6. Animal dung is removed from compound daily?")
    if st.button("Calculate Compound Audit Score", type="primary"):
        score = sum([q1, q2, q3, q4, q5, q6])
        percent = (score / 6) * 100
        st.success(f"Audit Score: {score} / 6 = {percent:.0f}%")
        if percent >= 80:
            st.success("EXCELLENT COMPOUND: Keep doing this. Your compound is protecting Human, Animal and Crop together.")
        elif percent >= 50:
            st.warning("MEDIUM COMPOUND: Good start, but fix the missing items today. Start with clean water and dung removal.")
        else:
            st.error("NEEDS URGENT ACTION: Many risks in one compound. Start with 1. Clean water, 2. Separate animal pen, 3. Handwashing.")
        if not q1:
            st.info("Fix: Cover water pot. Do not let animals drink from same pot as people.")
        if not q2:
            st.info("Fix: Move animal pen away from sleeping room. Animals and children must not share same room at night.")
        if not q3:
            st.info("Fix: Wash hands with soap after toilet, after farm, before cooking.")
        if not q4:
            st.info("Fix: Use latrine always. Do not defecate in open compound / farm near water.")
        if not q5:
            st.info("Fix: Use mosquito net every night, especially for children under 5.")
        if not q6:
            st.info("Fix: Remove dung daily. Dung on soil spreads disease to children, animals and crops.")
        st.caption("For education only. This audit is a community signal, not a medical diagnosis.")
    with tab6:
with tab6:
    st.header("Find Help Nearby - Giwa, Kaduna")
    st.write("Do not wait if it is urgent.")
    help_type = st.selectbox("What Help Do You Need?", ["PHC - For People", "Vet - For Animals", "Extension - For Crops", "Emergency"])
    if help_type == "PHC - For People":
        st.success("GO TO: Wazata Ward PHC / Giwa General Hospital")
        st.write("Take patient, age, symptom, when it started.")
    elif help_type == "Vet - For Animals":
        st.success("GO TO: Giwa LGA Vet Clinic / Ward Vet Officer")
        st.write("Separate sick animal. Do not give human medicine.")
    elif help_type == "Extension - For Crops":
        st.success("GO TO: Giwa Agriculture Office / Extension Officer")
        st.write("Take photo of crop. Ask before using chemical.")
    else:
        st.error("EMERGENCY: Go to Giwa General Hospital NOW.")
        st.write("If person cannot breathe, is very weak, bleeding.")
    st.divider()
    st.write("1. Human -> PHC / Doctor")
    st.write("2. Animal -> Vet")
    st.write("3. Crop -> Extension Officer")
    if st.button("I Have Found Help - Finish Check"):
        st.balloons()
        st.success("Alhamdulillah! You completed a full OneHealth check: Human + Animal + Crop + Compound + Help. Share EL-DANZA with one neighbour today.")
st.info("Step 2 Test: Location is working. Check that Kaduna > Giwa > Wazata Ward > Danzanfulani Village shows correctly.")

st.markdown("---")
st.caption("© 2026 EL-DANZA OneHealth AI | Built by Suleiman Ibrahim | Designed for Imagine Cup 2027 Startup Championship")