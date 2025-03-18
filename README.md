# Credit Card Fraud Detection 🔍💳

## 📌 Overview  
This project aims to detect fraudulent credit card transactions using machine learning. The model is trained on an imbalanced dataset and applies techniques like feature scaling and classification algorithms to predict fraudulent activities.

## ✅ Features  
✔ Detects fraudulent transactions with high accuracy.  
✔ Uses **Random Forest Classifier** for prediction.  
✔ Standardizes data for better model performance.  
✔ Web-based UI for easy transaction testing.  

---

## 📂 Folder Structure  

CREDIT_CARD_FRAUD_DETECTION/
│── dataset/               # Dataset files (Download from above link)
│── models/                # Trained model & scaler
│── static/                # CSS styles
│   └── styles.css
│── templates/             # HTML templates
│   └── index.html
│── app.py                 # Flask web application
│── download.py            # Script to download dataset (if needed)
│── requirements.txt       # Python dependencies
│── train_model.py         # Model training script



## 📥 Dataset  
Due to GitHub's file size limits, download the dataset manually from Google Drive:  
🔗 [Download from Google Drive](https://drive.google.com/drive/folders/1ZwnJQd_EFIwg8ETmSnjBJadPLDT51WJN?usp=sharing)  

After downloading, place the dataset inside the `dataset/` folder.

## 🚀 How to Run  

1️⃣ Clone the Repository  
```sh
git clone https://github.com/001Diwakar001/Credit_Card_Fraud_Detection.git
cd Credit_Card_Fraud_Detection

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Train the model
python train_model.py

4️⃣ Run the web application
python app.py

5️⃣ Open your browser and go to:
http://127.0.0.1:5000/
