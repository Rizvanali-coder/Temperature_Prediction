from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('temperature_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        humidity = float(request.form['humidity'])
        wind_speed = float(request.form['wind_speed'])
        mean_pressure = float(request.form['mean_pressure'])

        features = np.array([[humidity, wind_speed, mean_pressure]])
        prediction = model.predict(features)[0]

        return render_template('index.html', prediction=f"Predicted Temperature: {prediction:.2f} ")
    except Exception as e:
        return render_terplate('index.html', prediction=f"Error: {str(e)}")

 if __name__ == ' __main__':
     app.run(debug=True)
