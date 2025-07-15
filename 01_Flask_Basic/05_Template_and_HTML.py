from flask import Flask, render_template

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def index():
    myvalue = 'Data Science'
    DS_course_fee = 'Course fee is 45000'
    age_of_DS_Students = 'course age range [20,23,21,24,26]'
    return render_template("index.html", val1= myvalue, val2 = DS_course_fee, val3 = age_of_DS_Students)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5555, debug=True)
