from flask import Flask, render_template, request, redirect, url_for, session, send_file
import joblib
import pandas as pd
import logging
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Setup logging and folders
os.makedirs('logs', exist_ok=True)
os.makedirs('uploads', exist_ok=True)
logging.basicConfig(filename='logs/app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

# Load model and scaler
model = joblib.load('models/spending_score_model.joblib')
scaler = joblib.load('models/scaler.joblib')

# Dummy user credentials
USER_CREDENTIALS = {
    'john': 'password123',
    'samuel': 'password456',
    'james': 'password789'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            session['username'] = username
            logging.info(f'User "{username}" logged in.')
            return redirect(url_for('predict'))
        else:
            return render_template('login.html', error='Invalid credentials.')
    return render_template('login.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'username' not in session:
        return redirect(url_for('login'))

    prediction = None
    if request.method == 'POST':
        gender = request.form['gender']
        age = int(request.form['age'])
        income = int(request.form['income'])
        gender_encoded = 0 if gender == 'Male' else 1

        scaled_features = scaler.transform([[age, income]])
        scaled_df = pd.DataFrame(scaled_features, columns=['Age', 'Annual Income (k$)'])
        scaled_df['Gender'] = gender_encoded

        pred = model.predict(scaled_df)
        prediction = round(pred[0], 2)

        logging.info(f'User "{session["username"]}" made single prediction: Age={age}, Income={income}, Gender={gender}, Score={prediction}')

    return render_template('predict.html', prediction=prediction)

@app.route('/batch_predict', methods=['GET', 'POST'])
def batch_predict():
    if 'username' not in session:
        return redirect(url_for('login'))

    table = None
    download_link = None

    if request.method == 'POST':
        file = request.files['file']
        download = request.form.get('download')

        if file and file.filename.endswith('.csv'):
            filename = secure_filename(file.filename)
            filepath = os.path.join('uploads', filename)
            file.save(filepath)

            # Load CSV
            df = pd.read_csv(filepath)

            # Expecting columns: Gender, Age, Annual Income (k$)
            df['Gender_encoded'] = df['Gender'].map({'Male': 0, 'Female': 1})
            features = df[['Age', 'Annual Income (k$)']]
            scaled_features = scaler.transform(features)
            scaled_df = pd.DataFrame(scaled_features, columns=['Age', 'Annual Income (k$)'])
            scaled_df['Gender'] = df['Gender_encoded']

            # Predict
            predictions = model.predict(scaled_df)
            df['Predicted_Spending_Score'] = predictions

            # Drop Gender_encoded before saving/displaying
            df = df.drop(columns=['Gender_encoded'])

            logging.info(f'User "{session["username"]}" made batch prediction on file "{filename}"')

            # Render table
            table = df.to_html(classes='data', header="true", index=False)

            if download == 'yes':
                output_filename = f'predicted_{filename}'
                output_path = os.path.join('uploads', output_filename)
                df.to_csv(output_path, index=False)
                download_link = url_for('download_file', filename=output_filename)

    return render_template('batch_predict.html', table=table, download_link=download_link)

@app.route('/download/<filename>')
def download_file(filename):
    if 'username' not in session:
        return redirect(url_for('login'))
    filepath = os.path.join('uploads', filename)
    return send_file(filepath, as_attachment=True)

@app.route('/logout')
def logout():
    username = session.pop('username', None)
    if username:
        logging.info(f'User "{username}" logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
