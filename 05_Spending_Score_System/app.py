from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import pandas as pd
import logging
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session handling

# Setup logging
os.makedirs('logs', exist_ok=True)
logging.basicConfig(filename='logs/app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

# Load model and scaler
model = joblib.load('models/spending_score_model.joblib')
scaler = joblib.load('models/scaler.joblib')

# Dummy user credentials (for demo purposes)
USER_CREDENTIALS = {
    'john': 'password123',
    'samuel':'password456',
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

        # Encode gender
        gender_encoded = 0 if gender == 'Male' else 1

        # Scale age and income
        scaled_features = scaler.transform([[age, income]])
        scaled_df = pd.DataFrame(scaled_features, columns=['Age', 'Annual Income (k$)'])
        scaled_df['Gender'] = gender_encoded

        # Make prediction
        pred = model.predict(scaled_df)
        prediction = round(pred[0], 2)

        logging.info(f'User "{session["username"]}" made prediction: Age={age}, Income={income}, Gender={gender}, Score={prediction}')

    return render_template('predict.html', prediction=prediction)


@app.route('/logout')
def logout():
    username = session.pop('username', None)
    if username:
        logging.info(f'User "{username}" logged out.')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, port=5500)