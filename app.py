import streamlit as st
import pandas as pd
import joblib

# ===== Load Model & Data =====
model = joblib.load("best_model.pkl")
address_freq = joblib.load("address_freq.pkl")
coords = joblib.load("coords.pkl")

address_list = [
    'Shahran', 'Pardis', 'Shahrake Qods', 'Shahrake Gharb', 'North Program Organization',
    'Andisheh', 'West Ferdows Boulevard', 'Narmak', 'Saadat Abad', 'Zafar', 'Islamshahr', 
    'Pirouzi', 'Shahrake Shahid Bagheri', 'Moniriyeh', 'Velenjak', 'Amirieh', 
    'Southern Janatabad', 'Salsabil', 'Zargandeh', 'Feiz Garden', 'Water Organization', 
    'Unknown', 'ShahrAra', 'Gisha', 'Ray', 'Abbasabad', 'Ostad Moein', 'Farmanieh', 
    'Parand', 'Punak', 'Qasr-od-Dasht', 'Aqdasieh', 'Pakdasht', 'Railway', 'Central Janatabad', 
    'East Ferdows Boulevard', 'Pakdasht KhatunAbad', 'Sattarkhan', 'Baghestan', 'Shahryar', 
    'Northern Janatabad', 'Daryan No', 'Southern Program Organization', 'Rudhen', 'West Pars', 
    'Afsarieh', 'Marzdaran', 'Dorous', 'Sadeghieh', 'Chahardangeh', 'Baqershahr', 'Jeyhoon', 
    'Lavizan', 'Shams Abad', 'Fatemi', 'Keshavarz Boulevard', 'Kahrizak', 'Qarchak', 
    'Northren Jamalzadeh', 'Azarbaijan', 'Bahar', 'Persian Gulf Martyrs Lake', 'Beryanak', 
    'Heshmatieh', 'Elm-o-Sanat', 'Golestan', 'Shahr-e-Ziba', 'Pasdaran', 'Chardivari', 
    'Gheitarieh', 'Kamranieh', 'Gholhak', 'Heravi', 'Hashemi', 'Dehkade Olampic', 'Damavand', 
    'Republic', 'Zaferanieh', 'Qazvin Imamzadeh Hassan', 'Niavaran', 'Valiasr', 'Qalandari', 
    'Amir Bahador', 'Ekhtiarieh', 'Ekbatan', 'Absard', 'Haft Tir', 'Mahallati', 'Ozgol', 
    'Tajrish', 'Abazar', 'Koohsar', 'Hekmat', 'Parastar', 'Lavasan', 'Majidieh', 
    'Southern Chitgar', 'Karimkhan', 'Si Metri Ji', 'Karoon', 'Northern Chitgar', 
    'East Pars', 'Kook', 'Air force', 'Sohanak', 'Komeil', 'Azadshahr', 'Zibadasht', 
    'Amirabad', 'Dezashib', 'Elahieh', 'Mirdamad', 'Razi', 'Jordan', 'Mahmoudieh', 
    'Shahedshahr', 'Yaftabad', 'Mehran', 'Nasim Shahr', 'Tenant', 'Chardangeh', 'Fallah', 
    'Eskandari', 'Shahrakeh Naft', 'Ajudaniye', 'Tehransar', 'Nawab', 'Yousef Abad', 
    'Northern Suhrawardi', 'Shahrake Quds', 'Safadasht', 'Khademabad Garden', 'Hassan Abad', 
    'Chidz', 'Khavaran', 'Boloorsazi', 'Mehrabad River River', 'Varamin - Beheshti', 'Shoosh', 
    'Thirteen November', 'Darakeh', 'Aliabad South', 'Alborz Complex', 'Firoozkooh', 
    'Vahidiyeh', 'Shadabad', 'Naziabad', 'Javadiyeh', 'Yakhchiabad'
]

# ===== Custom Page Style =====
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        h1 {
            text-align: center;
            color: #2E86C1;
        }
        .prediction-card {
            padding: 20px;
            background-color: #D4EFDF;
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🏠 Tehran House Price Prediction")

# ===== Input Section =====
st.markdown("### 📏 Property Details")

col1, col2 = st.columns(2)
with col1:
    area = st.number_input("Area (m²)", min_value=1, step=1, value=50)
with col2:
    room = st.number_input("Number of Rooms", min_value=1, step=1, value=2)

# Row for checkboxes
check_col1, check_col2, check_col3 = st.columns(3)
with check_col1:
    parking = 1 if st.checkbox("Parking") else 0
with check_col2:
    warehouse = 1 if st.checkbox("Warehouse") else 0
with check_col3:
    elevator = 1 if st.checkbox("Elevator") else 0

# Row for address selectbox
address = st.selectbox("Select Address", options=address_list)
# ===== Map Section =====
coords_df = pd.DataFrame({
    "lat": [coords.get(addr, (None, None))[0] for addr in address_list if coords.get(addr, (None, None))[0] is not None],
    "lon": [coords.get(addr, (None, None))[1] for addr in address_list if coords.get(addr, (None, None))[1] is not None],
})
if not coords_df.empty:
    st.markdown("### 🗺 Map of Locations")
    st.map(coords_df)

# ===== Prepare Features =====
latitude, longitude = coords.get(address, (None, None))
area_per_room = area / room if room != 0 else 0
total_facilities = parking + warehouse + elevator
address_freq_val = address_freq.get(address, 0)

input_df = pd.DataFrame({
    "Area": [area],
    "Room": [room],
    "Parking": [parking],
    "Warehouse": [warehouse],
    "Elevator": [elevator],
    "Address": [address],
    "Area_per_Room": [area_per_room],
    "Total_Facilities": [total_facilities],
    "Address_Freq": [address_freq_val],
    "Latitude": [latitude],
    "Longitude": [longitude],
})

# ===== Prediction Button =====
if st.button("💰 Predict Price"):
    price_pred = model.predict(input_df)[0]
    st.markdown(f"""
        <div class="prediction-card">
            💵 Estimated Price: <br> <span style="font-size:24px;">${price_pred:,.2f}</span>
        </div>
    """, unsafe_allow_html=True)
