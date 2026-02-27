import os
from models import app, db, User

if __name__ == "__main__":
    with app.app_context():
        user = User(username='test_student', password_hash='dummy_hash')
        db.session.add(user)
        db.session.commit()
        print('User test_student created with ID:', user.id)
