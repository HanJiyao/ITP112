from flask import Flask, render_template, request
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, validators

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/timeline')
def timeline():
    return render_template('timeline.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/accountinfo')
def accountinfo():
    return render_template('accountinfo.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/plans')
def plans():
    return render_template('plans.html')


@app.route('/diet')
def diet():
    return render_template('healthy_diet.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route('/community')
def community():
    return render_template('community.html')


@app.route('/rewards')
def rewards():
    return render_template('rewards.html')


@app.route('/bread')
def bread():
    return render_template('bread.html')

@app.route('/porridge')
def porridge():
    return render_template('porridge.html')


@app.route('/oats')
def oats():
    return render_template('oats.html')


@app.route('/salad')
def salad():
    return render_template('salad.html')


@app.route('/juices')
def juices():
    return render_template('juices.html')


@app.route('/kway_teow_soup')
def kway_teow_soup():
    return render_template('kway_teow_soup.html')


@app.route('/fishsoup')
def fishsoup():
    return render_template('fishsoup.html')


@app.route('/herbalsoup')
def herbalsoup():
    return render_template('herbalsoup.html')


@app.route('/seafoodsoup')
def seafoodsoup():
    return render_template('seafoodsoup.html')

@app.route('/leaderboards')
def leaderboards():
    return render_template('leaderboards.html')

if __name__ == '__main__':
    app.run()