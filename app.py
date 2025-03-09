from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime, timedelta
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy.dialects import postgresql
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
app.config['SESSION_PERMANENT'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitedb'


#postgres://default:y5AmTrIcR4zW@ep-royal-lake-92857756.us-east-1.postgres.vercel-storage.com:5432/verceldb

db = SQLAlchemy(app)

login_manager = LoginManager(app)
migrate = Migrate(app, db)

data = {
    1: {"temperature": [22, 24, 21, 26, 23, 25, 27, 30, 47], "humidity": [60, 55, 70, 65, 80, 75, 85]},
    2: {"temperature": [28, 26, 29, 31, 30, 32, 33, 35, 38], "humidity": [75, 70, 80, 85, 90, 88, 82]},
    # Add more items here as needed
}

# Define the User class
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class PostForm(FlaskForm):
    food_name = StringField('Food Name', validators=[DataRequired()])
    batch_number = StringField('Batch Number', validators=[DataRequired()])
    maximum_temperature = StringField('Maximum Temperature (°C)', validators=[DataRequired()])
    maximum_humidity = StringField('Maximum Humidity (g/kg)', validators=[DataRequired()])
    submit = SubmitField('Add Item')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(200), nullable=False)
    batch_number = db.Column(db.String(100), nullable=False)
    maximum_temperature = db.Column(db.String(100), nullable=False)
    maximum_humidity = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))

class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    optimum_temperature = db.Column(db.String(50), nullable=False)
    optimum_humidity = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"FoodItem('{self.name}', '{self.optimum_temperature}', '{self.optimum_humidity}')"

class FoodItemForm(FlaskForm):
    name = StringField('Food Name', validators=[DataRequired()])
    optimum_temperature = StringField('Optimum Temperature', validators=[DataRequired()])
    optimum_humidity = StringField('Optimum Humidity', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html', current_user=current_user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already taken. Please choose another username.', 'danger')
            return redirect(url_for('register'))
        
        # Check if the email already exists
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('Email already registered. Please use a different email address.', 'danger')
            return redirect(url_for('register'))



        # Use the default hashing method
        hashed_password = generate_password_hash(password)

        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
    
    return render_template('login.html')

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Extract data from the form
        food_name = form.food_name.data
        batch_number = form.batch_number.data
        maximum_temperature = form.maximum_temperature.data
        maximum_humidity = form.maximum_humidity.data

        # Create a new post instance
        new_post = Post(
            food_name=food_name,
            batch_number=batch_number,
            maximum_temperature=maximum_temperature,
            maximum_humidity=maximum_humidity,
            user_id=current_user.id
        )

        # Add the new post to the database session
        db.session.add(new_post)

        # Commit the changes to the database
        db.session.commit()

        # Redirect to the explore page after posting
        return redirect(url_for('explore'))

    return render_template('post.html', form=form)

@app.route('/explore')
def explore():
    # Retrieve all Food Names from the database
    all_food_names = Post.query.all()
    all_batch_number = Post.query.all()
    all_maximum_temperature = Post.query.all()
    all_maximum_humidity = Post.query.all()

    # Pass the list of Food Names to the template
    return render_template('explore.html', posts=all_food_names, batch_number=all_batch_number, maximum_temperature=all_maximum_temperature, maximum_humidity=all_maximum_humidity)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', current_user=current_user)

@app.route('/management', methods=['GET', 'POST'])
@login_required
def management():
    form = PostForm()

    if request.method == 'POST' and form.validate_on_submit():
        # Extract data from the form
        food_name = form.food_name.data
        batch_number = form.batch_number.data
        maximum_temperature = form.maximum_temperature.data
        maximum_humidity = form.maximum_humidity.data

        # Create a new post instance
        new_post = Post(
            food_name=food_name,
            batch_number=batch_number,
            maximum_temperature=maximum_temperature,
            maximum_humidity=maximum_humidity,
            user_id=current_user.id
        )

        # Add the new post to the database session
        db.session.add(new_post)

        # Commit the changes to the database
        db.session.commit()

            # Retrieve all Food Names from the database
    all_food_names = Post.query.all()
    all_batch_number = Post.query.all()
    all_maximum_temperature = Post.query.all()
    all_maximum_humidity = Post.query.all()

    # Pass the list of Food Names to the template
    return render_template('management.html', posts=all_food_names, batch_number=all_batch_number, maximum_temperature=all_maximum_temperature, maximum_humidity=all_maximum_humidity, form=form, current_user=current_user)

@app.route('/api/item_data/<int:item_id>')
def get_item_data(item_id):
    if item_id in data:
        return jsonify(data[item_id])
    else:
        return jsonify({'error': 'Item not found'}), 404

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', current_user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/add_food', methods=['GET', 'POST'])
@login_required
def add_food():
    form = FoodItemForm()
    if form.validate_on_submit():
        new_food = FoodItem(
            name=form.name.data,
            optimum_temperature=form.optimum_temperature.data,
            optimum_humidity=form.optimum_humidity.data
        )
        db.session.add(new_food)
        db.session.commit()
        flash('Food item added successfully!', 'success')
        return redirect(url_for('managefood'))
    return render_template('add_food.html', form=form)

@app.route('/managefood')
@login_required
def managefood():
    food_items = FoodItem.query.all()
    return render_template('managefood.html', food_items=food_items)

@app.route('/edit_food/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_food(id):
    food_item = Post.query.get_or_404(id) 
    form = PostForm(obj=food_item)
    if form.validate_on_submit():
        food_item.food_name = form.food_name.data
        food_item.batch_number = form.batch_number.data
        food_item.maximum_temperature = form.maximum_temperature.data
        food_item.maximum_humidity = form.maximum_humidity.data
        db.session.commit()
        flash('Food item updated successfully!', 'success')
        return redirect(url_for('management'))
    return render_template('edit_food.html', form=form, post=food_item)

@app.route('/delete_food/<int:id>', methods=['POST'])
@login_required
def delete_food(id):
    food_item = Post.query.get_or_404(id) #change from FoodItem to Post
    db.session.delete(food_item)
    db.session.commit()
    flash('Food item deleted successfully!', 'success')
    return redirect(url_for('management'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)