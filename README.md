🏠Real Estate Price Prediction

A machine learning project that predicts housing prices in Tehran based on property features and location.
The project includes a Streamlit web app for interactive predictions and a Jupyter Notebook demonstrating the full data analysis, feature engineering, and model training pipeline.

📌 Features

Data preprocessing and feature engineering for real estate listings

Model training with scikit-learn (best model saved as best_model.pkl)

Location-based features (latitude, longitude, address frequency)

Custom engineered features such as:

Area_per_Room

Total_Facilities (Parking + Warehouse + Elevator)

Streamlit web app with:

User-friendly input form

Tehran location map

Price prediction card with styled UI

Getting Started

1️⃣ Clone the Repository

git clone https://github.com/samyvivo/Divar_Real_Estate_Price_Prediction.git
cd Divar_Real_Estate_Price_Prediction

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Streamlit App

streamlit run app.py

The app will launch in your browser at:

👉 http://localhost:8501

Divar_Real_Estate_Price_Prediction/
│── app.py                     # Streamlit web app
│── House_Price_Prediction.ipynb # Jupyter notebook (EDA + model training)
│── requirements.txt           # Python dependencies
│── best_model.pkl             # Trained ML model
│── address_freq.pkl           # Address frequency dictionary
│── coords.pkl                 # Address coordinates (latitude, longitude)


🖥️ Streamlit App Preview

Input property details: Area, Rooms, Parking, Warehouse, Elevator, Address

Map of Tehran addresses

💰 Predicted housing price displayed in a styled card

📊 Model Training (Notebook)

The notebook House_Price_Prediction.ipynb contains:

Data cleaning and preprocessing

Feature engineering (address frequency, geolocation)

Model comparison and selection

Saving the best model with joblib

🛠️ Built With

Streamlit
 - Web app framework

Pandas
 - Data manipulation

Scikit-learn
 - Machine learning

PyDeck
 - Map visualization

 - Future Improvements

Deploy on Streamlit Cloud / Hugging Face Spaces

Add more location-based features (nearby metro, amenities)

Experiment with advanced ML models (XGBoost, LightGBM, CatBoost)

👤 Author

Saman Zeitounian

🔗 LinkedIn : linkedin.com/in/saman-zeitounian-56a0a5164

💻 GitHub : https://github.com/samyvivo

