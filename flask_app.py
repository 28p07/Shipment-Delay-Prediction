from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

scaler = joblib.load('scaler.pkl')
label_encoders = joblib.load('label_encoders.pkl')
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input data from HTML form
        data = {
            'Origin': request.form['Origin'],
            'Destination': request.form['Destination'],
            'Vehicle Type': request.form['Vehicle Type'],
            'Distance (km)': float(request.form['Distance']),
            'Weather Conditions': request.form['Weather Conditions'],
            'Traffic Conditions': request.form['Traffic Conditions']
        }

        # Convert input data to DataFrame
        df = pd.DataFrame([data])

        # Label encode categorical columns
        categorical_columns = ['Origin', 'Destination','Weather Conditions','Traffic Conditions','Vehicle Type']
        for col in categorical_columns:
            df[col] = label_encoders[col].transform(df[col])

        # Select input features for the model
        input_features = ['Origin', 'Destination', 'Vehicle Type', 'Distance (km)',
                          'Weather Conditions', 'Traffic Conditions']
        input_data = df[input_features]
        input_data = scaler.transform(input_data)

        # Predict using the loaded model
        prediction = model.predict(input_data)

        # Convert prediction to "Delayed" or "On Time"
        result = "Delayed" if prediction[0] > 0.5 else "On Time"

        return render_template('form.html', prediction=result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)