from flask import Flask, render_template

app = Flask(__name__)

# Filter 1: Greet with name
@app.template_filter('greet')
def format_name(value):
    """Filter to format name with a greeting"""
    return f"Hello, {value.title()}!"

# Filter 2: Create work email from name
@app.template_filter('work_email')
def create_email(value):
    """Filter to create a work email from name"""
    username = value.strip().lower().replace(' ', '.')
    return f"{username}@colabNG.com"

@app.route('/')
def index():
    students = ["alice", "mike", "sophia", "john"]
    return render_template('filter.html', students=students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
