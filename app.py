from flask import Flask, render_template

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Game page
@app.route('/game')
def game():
    return render_template('game.html')

# Static page
@app.route('/static-page')
def static_page():
    return render_template('static.html')

if __name__ == '__main__':
    app.run(debug=True)