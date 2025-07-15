from flask import Flask, render_template

app = Flask(__name__)

# Sample student data dictionary
students_data = {
    'alice': {
        'name': 'Alice',
        'interest': 'Machine Learning'
    },
    'mike': {
        'name': 'Mike',
        'interest': 'Data Visualization'
    },
    'sophia': {
        'name': 'Sophia',
        'interest': 'Deep Learning'
    },
    'john': {
        'name': 'John',
        'interest': 'Natural Language Processing'
    }
}

# Custom filter to create work email
@app.template_filter('work_email')
def create_email(value):
    username = value.strip().lower().replace(' ', '.')
    return f"{username}@ColanNG.com"

@app.route('/')
def index():
    students = students_data.keys()  # ['alice', 'mike', 'sophia', 'john']
    return render_template('dynamic_index.html', students=students)

# Route to handle /student (without name)
@app.route('/students')
def student_prompt():
    students = students_data.keys()
    return render_template('dynamic_student_prompt.html', students=students)

# Dynamic URL route
@app.route('/students/<student_name>')
def student_detail(student_name):
    student = students_data.get(student_name.lower())
    if student:
        return render_template('dynamic_student_detail.html', student=student)
    else:
        return f"<h2>Student '{student_name}' not found.</h2>", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
