from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Set up the upload folder and allowed file types
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'xls', 'xlsx', 'csv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Static username and password
STATIC_USERNAME = "admin"
STATIC_PASSWORD = "password123"

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == STATIC_USERNAME and password == STATIC_PASSWORD:
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', message="Login Failed! Invalid username or password.")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', message="Login Successful!")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']

    if file.filename == '':
        return "No selected file", 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        try:
            if filename.endswith('.csv'):
                df = pd.read_csv(file_path)
                df = df.head(10)
                os.remove(file_path)
                return render_template('dashboard.html', table=df.to_html(classes='table table-striped'), message="CSV file uploaded successfully!")

            elif filename.endswith('.xlsx') or filename.endswith('.xls'):
                df = pd.read_excel(file_path)
                df = df.head(10)
                os.remove(file_path)
                return render_template('dashboard.html', table=df.to_html(classes='table table-striped'), message="Excel file uploaded successfully!")

            elif filename.endswith('.txt'):
                with open(file_path, 'r') as f:
                    file_content = f.read()
                os.remove(file_path)
                return render_template('dashboard.html', text_content=file_content, message="Text file uploaded successfully!")

            else:
                return "Unsupported file type.", 400

        except Exception as e:
            return str(e), 500

    else:
        return "File type not allowed.", 400


@app.route('/logout')
def logout():
    return redirect(url_for('login_page'))

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
