import os
from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
from models import db, User, JobApplication
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = 'your_secret_key_here_please_change_in_production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'all resumes')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize extensions
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    """Displays the home page of the application."""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

# Hardcoded Authentication Credentials
HARDCODED_USERNAME = 'admin'
HARDCODED_PASSWORD = 'password'

@app.route('/register', methods=['GET', 'POST'])
def register():
    flash('Registration is disabled for security. Please login with provided credentials.', 'info')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == HARDCODED_USERNAME and password == HARDCODED_PASSWORD:
            user = User.query.filter_by(username=username).first()
            if not user:
                # Create the default user in DB if it doesn't exist
                user = User(username=username, password_hash='hardcoded')
                db.session.add(user)
                db.session.commit()
            
            login_user(user, remember=True)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/upload_cv', methods=['POST'])
@login_required
def upload_cv():
    if 'cv' not in request.files:
        flash('No file part', 'danger')
        return redirect(request.url)
    file = request.files['cv']
    if file.filename == '':
        flash('No selected file', 'danger')
        return redirect(request.url)
    if file and file.filename.endswith('.pdf'):
        filename = secure_filename(f"user_{current_user.id}_{file.filename}")
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Update user's CV path relative or absolute
        current_user.cv_path = file_path
        db.session.commit()
        flash('CV uploaded successfully', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Only PDF files are allowed', 'danger')
        return redirect(url_for('dashboard'))

@app.route('/set_active_bot', methods=['POST'])
@login_required
def set_active_bot():
    # Only one user can be active at a time for the bot
    User.query.update({User.is_active_bot_user: False})
    current_user.is_active_bot_user = True
    db.session.commit()
    flash('You are now the active user for the automation bot!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/start_bot', methods=['POST'])
@login_required
def start_bot():
    if not current_user.is_active_bot_user:
        flash('You must be the Active User to start the bot.', 'danger')
        return redirect(url_for('dashboard'))
    try:
        # Launch runAiBot.py as a background process
        bot_script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'runAiBot.py')
        subprocess.Popen(['python', bot_script_path])
        flash('Bot started successfully! It is now running in the background.', 'success')
    except Exception as e:
        flash(f'Failed to start bot: {str(e)}', 'danger')
    return redirect(url_for('dashboard'))

@app.route('/applied-jobs', methods=['GET'])
@login_required
def get_applied_jobs():
    '''
    Retrieves a list of applied jobs from the database for the current logged-in user.
    '''
    try:
        jobs = []
        for app in current_user.applications:
            jobs.append({
                'Job_ID': app.job_id,
                'Title': app.title,
                'Company': app.company,
                'HR_Name': app.hr_name,
                'HR_Link': app.hr_link,
                'Job_Link': app.job_link,
                'External_Job_link': app.external_link,
                'Date_Applied': app.date_applied
            })
        return jsonify(jobs)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/applied-jobs/<job_id>', methods=['PUT'])
@login_required
def update_applied_date(job_id):
    try:
        from datetime import datetime
        application = JobApplication.query.filter_by(user_id=current_user.id, job_id=job_id).first()
        if application:
            application.date_applied = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            db.session.commit()
            return jsonify({"message": "Date Applied updated successfully"}), 200
        return jsonify({"error": f"Job ID {job_id} not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)