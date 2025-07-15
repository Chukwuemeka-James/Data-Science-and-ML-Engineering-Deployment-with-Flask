from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined static username and password (for demo purposes)
STATIC_USERNAME = "James"
STATIC_PASSWORD = "Deployment"

@app.route('/')
def login_page():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the username and password match the predefined values
    if username == STATIC_USERNAME and password == STATIC_PASSWORD:
        return "Login Successful!"  # Success message
    else:
        return "Login Failed! Invalid username or password."  # Failure message

if __name__ == "__main__":
    app.run(debug=True)
