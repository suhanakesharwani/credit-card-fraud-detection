from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__)

with open('models/svm_model.pkl','rb') as f:
    model=pickle.load(f)
with open('models/scaler.pkl','rb') as f:
    scaler=pickle.load(f)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def predict():
    time = float(request.form['Time'].replace(',', '.'))
    amount = float(request.form['Amount'].replace(',', '.'))
    v_features = [float(request.form[f'V{i}'].replace(',', '.')) for i in range(1, 29)]


    input_data = np.array([time] + v_features + [amount]).reshape(1, -1)

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_scaled)[0][1]
    else:
        probability = "N/A"

    result = "Fraudulent Transaction ⚠️" if prediction == 1 else "Legitimate Transaction ✅"
    
    return render_template('index.html', prediction=result, probability=probability)

if __name__ == '__main__':
    app.run(debug=True)



