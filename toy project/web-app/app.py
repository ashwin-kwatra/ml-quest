from flask import Flask, request, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the model and scaler
# Since we are running from 'toy project/web-app', we need to go one level up to find the pkl files if they are there
# Or we can assume they are in the same directory as app.py if we copy them later.
# For now, let's look for them in the parent directory relative to this file.
base_path = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_path, '..', 'model.pkl')
scaler_path = os.path.join(base_path, '..', 'scaler.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        cgpa = float(request.form.get('cgpa'))
        iq = float(request.form.get('iq'))
        
        # Transform input data
        input_data = np.array([[cgpa, iq]])
        input_scaled = scaler.transform(input_data)
        
        # Predict
        prediction = model.predict(input_scaled)
        
        result = "Placed" if prediction[0] == 1 else "Not Placed"
        
        return render_template('index.html', prediction_text=f'Prediction: {result}', cgpa=cgpa, iq=iq)
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
