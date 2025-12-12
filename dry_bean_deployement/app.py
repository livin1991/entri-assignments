from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load saved objects
model = pickle.load(open("model.pkl","rb"))
scaler = pickle.load(open("scaler.pkl","rb"))
label_map = pickle.load(open("label_map.pkl","rb"))

reverse_label_map = {v:k for k,v in label_map.items()}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get all numeric features
        features = [
            float(request.form['f1']),
            float(request.form['f2']),
            float(request.form['f3']),
            float(request.form['f4']),
            float(request.form['f5']),
            float(request.form['f6']),
            float(request.form['f7']),
            float(request.form['f8']),
            float(request.form['f9']),
            float(request.form['f10']),
            float(request.form['f11']),
            float(request.form['f12']),
            float(request.form['f13']),
            float(request.form['f14']),
            float(request.form['f15']),
            float(request.form['f16'])
        ]

        X = np.array(features).reshape(1, -1)
        X_scaled = scaler.transform(X)

        prediction = model.predict(X_scaled)[0]
        predicted_class = reverse_label_map[prediction]

        return render_template(
            "index.html",
            prediction_text=f"Predicted Bean Class: {predicted_class}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )

if __name__ == "__main__":
    app.run(debug=True)
