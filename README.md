# 🏠 Real Estate Price Prediction  

A machine learning project that predicts **housing prices in Tehran** based on property features and location.  
Includes a **Streamlit web app** for interactive predictions and a Jupyter Notebook for model training.  

---

## 📌 Features  
- Data preprocessing & feature engineering  
- Location-based features (latitude, longitude, address frequency)  
- Streamlit app with user-friendly inputs and Tehran map  
- Predicts 💰 **house prices**  

---

## 🚀 Getting Started  

### Installation

1. Clone the Repository:
```bash
git clone https://github.com/samyvivo/Real_Estate_Price_Prediction.git 
```

2. Navigate to the Project Directory
```bash
cd Divar_Real_Estate_Price_Prediction
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Run the App
```bash
streamlit run app.py
```

👉 The app will be available at: http://localhost:8501
```bash
Divar_Real_Estate_Price_Prediction/
│── app.py                     # Streamlit web app
│── House_Price_Prediction.ipynb # Jupyter notebook
│── requirements.txt           # Dependencies
│── best_model.pkl             # Trained ML model
│── address_freq.pkl           # Address frequency data
│── coords.pkl                 # Coordinates of addresses
```

🖥️ Streamlit App Preview

• Input property details: Area, Rooms, Parking, Warehouse, Elevator, Address

• Map of Tehran addresses

• Predicted housing price displayed in a styled card


📊 Model Training (Notebook)

• The notebook House_Price_Prediction.ipynb contains:

• Data cleaning and preprocessing

• Feature engineering (address frequency, geolocation)

• Model comparison and selection

• Saving the best model with joblib

🛠️ Built With

• Streamlit - Web app framework

• Pandas - Data manipulation

• Scikit-learn - Machine learning

• PyDeck - Map visualization

📌 Future Improvements
• Deploy on Streamlit Cloud / Hugging Face Spaces

• Add more location-based features (nearby metro, amenities)

• Experiment with advanced ML models (XGBoost, LightGBM, CatBoost)

👤 Author
Saman Zeitounian

• Email: [samanzeitounian@gmail.com]

• LinkedIn : [linkedin.com/in/saman-zeitounian-56a0a5164](https://www.linkedin.com/in/saman-zeitounian-56a0a5164/)

• GitHub : https://github.com/samyvivo

