from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    cv_path = db.Column(db.String(500), nullable=True)
    is_active_bot_user = db.Column(db.Boolean, default=False)
    
    applications = db.relationship('JobApplication', backref='user', lazy=True)

class JobApplication(db.Model):
    __tablename__ = 'job_applications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    job_id = db.Column(db.String(100), nullable=True)
    title = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    hr_name = db.Column(db.String(200), nullable=True)
    hr_link = db.Column(db.String(500), nullable=True)
    job_link = db.Column(db.String(500), nullable=True)
    external_link = db.Column(db.String(500), nullable=True)
    date_applied = db.Column(db.String(100), default=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

