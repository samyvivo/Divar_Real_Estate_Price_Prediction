import streamlit as st
import pandas as pd
import joblib
import pydeck as pdk


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Vazirmatn', sans-serif;
    }

    h1, h2, h3, h4, h5, h6, p, div, span {
        font-family: 'Vazirmatn', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)

# ===== Load Model & Data =====
model = joblib.load("best_model.pkl")
address_freq = joblib.load("address_freq.pkl")
coords = joblib.load("coords.pkl")  # keys must be English names (same as training)

# ===== English address list (the keys used in model/coords/address_freq) =====
address_list_eng = [
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

# ===== Matching Persian labels for display (must be same order) =====
address_list_fa = [
    'شهران', 'پردیس', 'شهرک قدس', 'شهرک غرب', 'سازمان برنامه شمالی',
    'اندیشه', 'بلوار فردوس غرب', 'نارمک', 'سعادت آباد', 'ظفر', 'اسلامشهر',
    'پیروزی', 'شهرک شهید باقری', 'منیریه', 'ولنجک', 'امیریه',
    'جنت آباد جنوبی', 'سلسبیل', 'زرگنده', 'باغ فیض', 'سازمان آب',
    'نامشخص', 'شهرآرا', 'گیشا', 'ری', 'عباس آباد', 'استاد معین', 'فرمانیه',
    'پرند', 'پونک', 'قصرالدشت', 'اقدسیه', 'پاکدشت', 'راه‌آهن', 'جنت آباد مرکزی',
    'بلوار فردوس شرق', 'پاکدشت خاتون‌آباد', 'ستارخان', 'باغستان', 'شهریار',
    'جنت آباد شمالی', 'داریان نو', 'سازمان برنامه جنوبی', 'رودهن', 'پارس غربی',
    'افسریه', 'مرزداران', 'دروس', 'صادقیه', 'چهاردانگه', 'باقرشهر', 'جی',
    'لویزان', 'شمس‌آباد', 'فاطمی', 'بلوار کشاورز', 'کهریزک', 'قرچک',
    'جمالزاده شمالی', 'آذربایجان', 'بهار', 'دریاچه شهدای خلیج فارس', 'بریانک',
    'هشمتیه', 'علم و صنعت', 'گلستان', 'شهر زیبا', 'پاسداران', 'چاردیواری',
    'قیطریه', 'کامرانیه', 'قلهک', 'هروی', 'هاشمی', 'دهکده المپیک', 'دماوند',
    'جمهوری', 'زعفرانیه', 'قزوین امامزاده حسن', 'نیاوران', 'ولیعصر', 'قلندری',
    'امیر بهادر', 'اختیاریه', 'اکباتان', 'آبسرد', 'هفت تیر', 'محلاتی', 'اوجگل',
    'تجریش', 'آذرآز', 'کوهسار', 'حکمت', 'پرستار', 'لواسان', 'مجیدیه',
    'چیتگر جنوبی', 'کریمخان', 'سی‌متری جی', 'کارون', 'چیتگر شمالی',
    'پارس شرقی', 'کوک', 'نیروی هوایی', 'سوهانک', 'کمیل', 'آزادشهر', 'زیبادشت',
    'امیرآباد', 'دزاشیب', 'الهیه', 'میرداماد', 'رازی', 'جردن', 'محمودیه',
    'شاهدشهر', 'یافت‌آباد', 'مهران', 'نسیم‌شهر', 'مستاجر', 'فلاح',
    'اسکندری', 'شهرک نفت', 'اجودانیه', 'تهرانسر', 'نواب', 'یوسف‌آباد',
    'سهروردی شمالی', 'شهرک قدس', 'صفادشت', 'باغ خادم‌آباد', 'حسن‌آباد',
    'چیذر', 'خاوران', 'بلورسازی', 'رودخانه مهرآباد', 'ورامین - بهشتی', 'شوش',
    'سیزده آبان', 'دربند', 'علی‌آباد جنوبی', 'مجتمع البرز', 'فیروزکوه',
    'وحیدیه', 'شادآباد', 'نازی‌آباد', 'جوادیه', 'یاخچی‌آباد'
]

# create mapping (eng -> fa)
eng_to_fa = dict(zip(address_list_eng, address_list_fa))

# ===== Styling RTL =====
st.markdown("""
    <style>
        .main { direction: rtl; }
        .stSelectbox > div { direction: rtl; }  /* try to help selectbox direction */
    </style>
""", unsafe_allow_html=True)

st.title("🏠 پیش‌بینی قیمت خانه در تهران")

# ===== Inputs: area/room defaults & inline checkboxes =====
col1, col2 = st.columns(2)
with col1:
    area = st.number_input("متراژ (متر مربع)", min_value=1, step=1, value=50)
with col2:
    room = st.number_input("تعداد اتاق", min_value=1, step=1, value=2)

chk1, chk2, chk3 = st.columns(3)
with chk1:
    parking = 1 if st.checkbox("پارکینگ") else 0
with chk2:
    warehouse = 1 if st.checkbox("انباری") else 0
with chk3:
    elevator = 1 if st.checkbox("آسانسور") else 0

# ===== Address selectbox: options are EN keys, but show Persian labels =====
address_eng = st.selectbox(
    "انتخاب محله",
    options=address_list_eng,
    format_func=lambda x: "\u200F" + eng_to_fa.get(x, x)  # \u200F = RIGHT-TO-LEFT MARK برای نمایش صحیح
)

# ===== Map: show Persian labels in tooltip (filter out missing coords) =====
map_points = []
for eng in address_list_eng:
    lat, lon = coords.get(eng, (None, None))
    if lat is not None and lon is not None:
        map_points.append({
            "lat": lat,
            "lon": lon,
            "label": eng_to_fa.get(eng, eng)
        })

if map_points:
    df_map = pd.DataFrame(map_points)
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df_map,
        get_position=["lon", "lat"],
        get_fill_color=[75, 0, 130],
        get_radius=100,
        pickable=True
    )
    
tooltip = {
    "html": """
        <div style='
            direction: rtl;
            text-align: right;
            font-weight: 600;
            font-family: Vazirmatn, sans-serif;
            white-space: nowrap;
        '>{label}</div>
    """,
    "style": {"backgroundColor": "white"}
}

    
map_points.append({
    "lat": lat,
    "lon": lon,
    "label": eng_to_fa.get(eng, eng)  # Convert to Persian for display
})
    
coords_df = pd.DataFrame({
    "lat": [coords.get(addr, (None, None))[0] for addr in address_list_eng if coords.get(addr, (None, None))[0] is not None],
    "lon": [coords.get(addr, (None, None))[1] for addr in address_list_eng if coords.get(addr, (None, None))[1] is not None],
})
if not coords_df.empty:
    st.markdown("نقشه‌ی موقعیت‌ها 🗺")
    st.map(coords_df)

# ===== Prepare features (use eng key for Address so it matches model) =====
latitude, longitude = coords.get(address_eng, (None, None))
area_per_room = area / room if room else 0
total_facilities = parking + warehouse + elevator
address_freq_val = address_freq.get(address_eng, 0)

input_df = pd.DataFrame({
    "Area": [area],
    "Room": [room],
    "Parking": [parking],
    "Warehouse": [warehouse],
    "Elevator": [elevator],
    "Address": [address_eng],   # <-- ENGLISH key, matches training
    "Area_per_Room": [area_per_room],
    "Total_Facilities": [total_facilities],
    "Address_Freq": [address_freq_val],
    "Latitude": [latitude],
    "Longitude": [longitude],
})

# ===== Predict =====
if st.button("💰 پیش‌بینی قیمت"):
    pred = model.predict(input_df)[0] * 98000
    st.success(f"💵 قیمت تقریبی: {pred:,.0f} تومان")

