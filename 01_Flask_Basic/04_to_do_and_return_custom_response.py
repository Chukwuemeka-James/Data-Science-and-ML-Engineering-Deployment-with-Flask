from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

@app.route('/hello')
def hello():
    #return "Hello Data Science world!\n", 201
   #return "Hello Data Science world!\n"                 # Monitoring status: curl -I http://127.0.0.1:5555/hello: 200 by default
   response = make_response("Hello Data Scientists")
   response.status_code = 202
   #response.headers['content-type'] = 'application/octate-stream'
   response.headers['content-type'] = 'text/plain'
   return response


# Create dynamic urls by adding url processors
@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}, how is the Data industry?"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"

# Query parameter: ?
@app.route('/handle_url_params')                # http://your_localhost/handle_url_params?name=james
def handle_params():                            # http://192.168.200.21:5555/handle_url_params?name=james&greeting=Hello
    return str(request.args)

@app.route("/pro_handle_url_params")            # http://192.168.200.21:5555/pro_handle_url_params?name=mike&greeting=hello
def pro_handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get("name")
        return f'{greeting}, {name}'
    else:
        return 'Some parameters are missing'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
