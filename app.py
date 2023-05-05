from flask import Flask

app = Flask(__name__)

@app.route('/')
def index ():
    return "hello world"

@app.route('/jose')
def jose():
    return "hello Jose!"

if __name__ == '__main__':
    app.run (debug=True)