from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Olá, mundo!"

@app.route('/greet')
def greet():
    name = request.args.get('name', 'User')
    return "Olá, {}!".format(name)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=5000)