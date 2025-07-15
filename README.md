# Data-Science-and-ML-Engineering-Deployment-with-Flask

Welcome! This repository is designed for learners all over the world who want to master the deployment of Data Science and Machine Learning solutions using Flask. Whether you are a beginner or looking to deepen your practical skills, this repository will guide you step-by-step from Flask basics to deploying a real ML model as a web app.

---

## Project Structure

```
.
├── 01_Flask_Basic/
│   ├── 01_flask_hello_world.py
│   ├── 02_routes_and_urls.py
│   ├── 03_GET_and_POST_requests.py
│   ├── 04_to_do_and_return_custom_response.py
│   ├── 05_Template_and_HTML.py
│   ├── 06_Template_and_HTML_2.py
│   ├── 07_Template_inheritance.py
│   ├── 08_Inheritance_and_filters.py
│   └── templates/
│       ├── base.html
│       ├── filter.html
│       ├── index.html
│       ├── index1.html
│       ├── index2.html
│       ├── students.html
│       └── ...
├── 02_Dynamic_URLs/
│   ├── Dynamic_url.py
│   └── templates/
│       ├── base.html
│       ├── dynamic_index.html
│       ├── dynamic_student_detail.html
│       └── dynamic_student_prompt.html
├── 03_URL_Building_and_Redirection/
│   ├── app.py
│   └── templates/
│       ├── base.html
│       ├── glossary_detail.html
│       ├── glossary_prompt.html
│       └── index.html
├── 04_Forms_POST_Files/
│   ├── basic_app.py
│   ├── logging_file_upload_and_download.py
│   ├── logging_form_and_file_upload.py
│   ├── uploads/
│   │   └── loan_approval_dataset.xlsx
│   └── templates/
│       ├── dashboard.html
│       ├── download_dashboard.html
│       ├── download_login.html
│       ├── index.html
│       ├── login.html
│       └── ...
├── 05_Spending_Score_System/
│   ├── app.py
│   ├── README.md
│   ├── logs/
│   │   └── app.log
│   ├── models/
│   │   ├── scaler.joblib
│   │   └── spending_score_model.joblib
│   ├── research/
│   │   ├── Mall Customer Segmentation Data.csv
│   │   └── research.ipynb
│   └── templates/
│       ├── login.html
│       └── predict.html
├── 06_Batch_and_Unit_Spending_Score_System/
│   ├── app.py
│   ├── logs/
│   │   └── app.log
│   ├── models/
│   │   ├── scaler.joblib
│   │   └── spending_score_model.joblib
│   ├── research/
│   │   ├── Mall Customer Segmentation Data.csv
│   │   ├── Test Data (Mall Customer Segmentation Data).csv
│   │   └── research.ipynb
│   ├── templates/
│   │   ├── batch_predict.html
│   │   ├── login.html
│   │   └── predict.html
│   └── uploads/
│       ├── Test_Data_Mall_Customer_Segmentation_Data.csv
│       └── predicted_Test_Data_Mall_Customer_Segmentation_Data.csv
├── 07_Complete_Spending_Score_System/
│   ├── app.py
│   ├── logs/
│   │   └── app.log
│   ├── models/
│   │   ├── scaler.joblib
│   │   └── spending_score_model.joblib
│   ├── research/
│   │   ├── Mall Customer Segmentation Data.csv
│   │   ├── Test Data (Mall Customer Segmentation Data).csv
│   │   └── research.ipynb
│   ├── static/
│   │   └── css/
│   │       └── styles.css
│   ├── templates/
│   │   ├── batch_predict.html
│   │   ├── login.html
│   │   └── predict.html
│   └── uploads/
│       ├── Test_Data_Mall_Customer_Segmentation_Data.csv
│       └── predicted_Test_Data_Mall_Customer_Segmentation_Data.csv
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
└── .gitignore
```

---

## What You Will Learn

- Flask fundamentals: routing, templates, forms, and file handling.
- How to build interactive, data-driven web applications.
- Step-by-step deployment of a trained ML model with Flask.
- Handling single and batch predictions (CSV upload/download).
- Simple login/logout flows for web apps.
- Logging user actions and structuring a real-world project.

---

## Directory Walkthrough

- **01_Flask_Basic/**: Start here! Learn Flask basics with simple scripts and templates.
- **02_Dynamic_URLs/**: Explore dynamic URL handling in Flask.
- **03_URL_Building_and_Redirection/**: Learn about URL building and redirection.
- **04_Forms_POST_Files/**: Practice handling forms, POST requests, and file uploads.
- **05_Spending_Score_System/**: 
  - A web app for single-customer spending score prediction.
  - User authentication (demo credentials).
  - Uses a trained regression model and scaler (in `models/`).
  - Logging of user actions.
- **06_Batch_and_Unit_Spending_Score_System/**: 
  - Adds batch prediction (CSV upload) to the previous system.
- **07_Complete_Spending_Score_System/**: 
  - Full-featured app with:
    - User login/logout.
    - Single and batch prediction (CSV upload and download).
    - Logging, file uploads, and downloads.
    - Clean UI with custom CSS.
    - Research notebook for model training and export.

---

## Final Project: Complete Spending Score System

The `07_Complete_Spending_Score_System` directory contains a polished, production-style Flask app:

- Login: Demo users (`john`, `samuel`, `james`) with passwords.
- Single Prediction: Enter gender, age, and income to get a predicted spending score.
- Batch Prediction: Upload a CSV with columns `Gender`, `Age`, `Annual Income (k$)` for multiple predictions. Download results as CSV.
- Logout: Securely end your session.

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd Data-Science-and-ML-Engineering-Deployment-with-Flask
   ```

2. Install dependencies:
   - Using pipenv:
     ```bash
     pipenv install
     pipenv shell
     ```
   - Or using pip:
     ```bash
     pip install flask pandas openpyxl scikit-learn joblib
     ```

3. Run the app:
   ```bash
   cd 07_Complete_Spending_Score_System
   python app.py
   ```
   - The app will be available at http://localhost:5000

4. Demo Credentials:
   - Username: `john` / `samuel` / `james`
   - Password: `password123` / `password456` / `password789`

---

## File and Folder Highlights

- `models/`: Contains `spending_score_model.joblib` and `scaler.joblib` (required for predictions).
- `templates/`: HTML templates for login, prediction, and batch prediction.
- `static/css/styles.css`: Custom styles for a clean UI.
- `uploads/`: Stores uploaded CSVs and downloadable results.
- `logs/app.log`: Logs user actions and predictions.
- `research/research.ipynb`: Jupyter notebook for model training.

---

## Example CSV for Batch Prediction

```csv
Gender,Age,Annual Income (k$)
Male,25,40
Female,30,60
```

---

## Model Training

See `07_Complete_Spending_Score_System/research/research.ipynb` for data preparation, model training, and export of the model and scaler.
