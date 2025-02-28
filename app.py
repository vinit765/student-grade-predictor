from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib

app = Flask(__name__)
CORS(app)

# Load trained model, scaler, and label encoder
model = joblib.load("student_grade_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    try:
        # Convert input data into array format with correct column names
        features = np.array([
            [
                data['Attendance (%)'],
                data['Midterm_Score'],
                data['Final_Score'],
                data['Assignments_Avg'],
                data['Study_Hours_per_Week'],
                data['Stress_Level (1-10)'],
                data['Sleep_Hours_per_Night']
            ]
        ])

        # Apply the same normalization as in training
        features_scaled = scaler.transform(features)

        # Make prediction (Get the grade index)
        grade_index = model.predict(features_scaled)[0]

        # Convert the numeric grade back to the letter grade (A, B, C, etc.)
        predicted_grade = label_encoder.inverse_transform([grade_index])[0]

        return jsonify({"predicted_grade": predicted_grade})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
