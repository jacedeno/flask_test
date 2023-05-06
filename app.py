from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='My Calculator')

@app.route('/jose')
def jose():
    return render_template('jose.html', pageTitle='About Jose Cedeno')

if __name__ == '__main__':
    app.run (debug=True)