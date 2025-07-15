from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index2.html')

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5555, debug=True)


#-------------Inheritance for two pages------------------------------------

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/students')
def students():
    return render_template('students.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
