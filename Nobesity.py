from flask import Flask, render_template, request, flash, redirect, url_for, session
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, PasswordField, validators
from Diet import Diet
import firebase_admin
from firebase_admin import credentials, db
cred = credentials.Certificate('./cred/nobesity-it1705-firebase-adminsdk-xo793-bbfa4432da.json')
default_app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://nobesity-it1705.firebaseio.com/'})
root = db.reference()
app = Flask(__name__)
app.secret_key = 'secret'


class RequiredIf(object):
    def __init__(self, *args, **kwargs):
        self.conditions = kwargs

    def __call__(self, form, field):
        for name, data in self.conditions.items():
            if name not in form._fields:
                validators.Optional()(field)
            else:
                condition_field = form._fields.get(name)
                if condition_field.data == data:
                    validators.DataRequired().__call__(form, field)
                else:
                    validators.Optional().__call__(form, field)


@app.route('/')
def index():
    if session.get('logged_in') is True:
        return redirect(url_for('timeline'))
    return render_template('home.html')


class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


@app.route('/login')
def login():
    login_form = SignUpForm(request.form)
    session['logged_in'] = True
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = SignUpForm(request.form)
    if request.method == 'POST' and signup_form.validate():
        user = UserAccount(SignUpForm.username.data, SignUpForm.email.data, SignUpForm.password.data)
        return redirect(url_for('login'))
    return render_template('signup.html', form=signup_form)


class SignUpForm(Form):
    username = StringField('User Name', [
        validators.length(max=20),
        validators.DataRequired()])
    email = StringField('Email', [
        validators.email(),
        validators.DataRequired()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))


@app.route('/timeline')
def timeline():
    session['logged_in'] = True
    return render_template('timeline.html')


@app.route('/registerName')
def registername():
    return render_template('firstTimeRegisterName.html')


@app.route('/registerGender')
def registergender():
    return render_template('firstTimeRegisterGender.html')


@app.route('/registerInfo')
def registerinfo():
    return render_template('firstTimeRegisterInfo.html')



@app.route('/accountinfo')
def accountinfo():
    return render_template('accountinfoDisplay.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/plans')
def plans():
    return render_template('plans.html')


class nutrition_food(Form):
    food_name = StringField('Name',[validators.length(min=1,max=150),validators.DataRequired()])
    food_type = StringField('Type',[validators.length(min=1,max=150),validators.DataRequired()])
    calories = StringField('Calories value',[validators.length(min=1,max=3),validators.DataRequired()])
    fats = StringField('Fats value',[validators.length(min=1,max=3),validators.DataRequired()])
    carbohydrates = StringField('Carbohydrates value',[validators.length(min=1,max=3),validators.DataRequired()])
    proteins = StringField('Protein value',[validators.length(min=1,max=3),validators.DataRequired()])


@app.route('/diet', methods=['GET','POST'])
def new_diet():
    food_form = nutrition_food(request.form)
    if request.method == 'POST' and food_form.validate():
        name = food_form.food_name.data
        type = food_form.food_type.data
        calories = food_form.calories.data
        fats = food_form.fats.data
        carbohydrates = food_form.carbohydrates.data
        protein = food_form.proteins.data
        diet = Diet(name, type, calories, fats, carbohydrates, protein)
        diet.db = root.child('Food')
        diet.db.push({'Name': diet.get_name(), 'Type': diet.get_type(),
                      'Calories value': diet.get_calories(), 'Fats Value': diet.get_fats(),
                      'Carbohydrates value': diet.get_carbohydrates(),'Protein value': diet.get_protein()
          })
        flash('Food inserted successfully', 'sucess')
    return render_template('diet.html', form=food_form)


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/rewards')
def rewards():
    return render_template('rewards.html')


@app.route('/leaderboards')
def leaderboards():
    return render_template('leaderboards.html')

if __name__ == '__main__':
    app.run()
