# Credit Card Fraud Detection 💳🔍

This project implements credit card fraud detection using Logistic Regression and Support Vector Machine (SVM) models on a PCA-transformed dataset. The dataset features (`V1` to `V28`) are results of dimensionality reduction applied for privacy protection. 🔒

## Features ✨

- Uses a preprocessed dataset with PCA applied to anonymize features. 🛡️  
- Trains Logistic Regression and SVM models separately using `pickle` for model persistence. 🧠💾  
- Evaluates model performance with metrics including ROC-AUC. 📊  
- Provides a Flask web application for real-time fraud prediction based on user input. 🌐⚡  
- Includes data preprocessing and scaling for consistent input transformation. 🔄  

## Usage 🚀

1. Clone this repository.
    git clone https://github.com/suhanakesharwani/credit-card-fraud-detection.git

2. Install dependencies:
   pip install -r requirements.txt

3. Run the Flask app:
    python app.py

4. Open your browser and go to http://127.0.0.1:5000 to use the prediction interface.

## Future Improvements 🔧

- Use raw data and apply PCA within the app. 🔄  
- Add more algorithms like Random Forest, XGBoost. 🌲⚡  
- Improve UI/UX of the Flask web app. 🎨  
- Deploy the app on cloud platforms. ☁️🚀  

## Author ✍️

Created by Suhana.  

Feel free to reach out if you have any questions or suggestions. 💬🤝