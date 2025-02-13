from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate')
def generate():
    response = requests.get('https://random-word-api.herokuapp.com/word?number=1')
    word = response.json()[0]
    return render_template('home.html', word=word)

if __name__ == '__main__':
    app.run(debug=True)