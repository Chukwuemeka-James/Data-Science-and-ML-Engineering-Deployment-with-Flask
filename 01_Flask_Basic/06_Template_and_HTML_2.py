from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    students = ["Mike", "Alice", "Sophia", "John"]
    modules = {
        "Python Programming": 100,
        "Exploratory Data Analysis": 70,
        "Machine Learning Basics": 30,
        "Deep Learning with PyTorch": 0
    }
    projects = ["Customer Churn Prediction", "Market Segmentation Model"]

    return render_template('index1.html', students_list=students, modules_list=modules, projects_list=projects)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5555, debug=True)
