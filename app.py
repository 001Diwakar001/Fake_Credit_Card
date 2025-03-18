from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load('models/fraud_model.pkl')
scaler = joblib.load('models/scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input from form
        input_data = request.form['features']  
        
        # Convert comma-separated string to a list of floats
        input_list = [float(i) for i in input_data.split(',')]
        
        # Ensure input has exactly 30 features
        if len(input_list) != 30:
            return "Error: Input must have exactly 30 numerical values."

        # Reshape for model
        input_array = np.array(input_list).reshape(1, -1)

        # Standardize input using saved scaler
        scaled_input = scaler.transform(input_array)

        # Predict using model
        prediction = model.predict(scaled_input)[0]

        # Return result
        result = "Fraudulent Transaction" if prediction == 1 else "Legitimate Transaction"
        return f"Prediction: {result}"

    except ValueError:
        return "Error: Please enter valid numerical values separated by commas."

if __name__ == '__main__':
    app.run(debug=True)
