from DateTime import DateTime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '2c61d979702a434493430f2e68c9277f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120), unique=True, nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
         return f"User('{self.username}', '{self.email}', '{self.image_file.jpg}')"


class Post(db.Model):
    id = db.Column(db.integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date-posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer. db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
         return f"Post('{self.title}', '{self.date_posted}')"


posts = [
    {
        'author': 'Gasar Iyali',
        'title': 'Blog Post 1',
        'content': ' First post content',
        'date_posted': 'March 31, 2021'
    },
    {
        'author': 'Quentin Pemberton',
        'title': 'Blog Post 2',
        'content': ' Second post content',
        'date_posted': 'March 31, 2021'
    },
    {
        'author': 'Sequana Madidi',
        'title': 'Blog Post 3',
        'content': ' Third post content',
        'date_posted': 'March 31, 2021'
    },
    {
        'author': 'Okwe Daniel',
        'title': 'Blog Post 4',
        'content': ' Fourth post content',
        'date_posted': 'April 2, 2021'
    },
    {
        'author': 'Mena Sarauniya',
        'title': 'Blog Post 5',
        'content': ' Fifth post content',
        'date_posted': 'April 3, 2021'
    },
]
 # Home Route
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', posts=posts, title="Home")

@app.route('/zack')
def zack():
    return render_template('zack.html', title='Zack info page')

@app.route('/about')
def about():
    return render_template('about.html', title='About page')

# <!--Registration Route-->
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password and try again', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
        app.run(debug=True)