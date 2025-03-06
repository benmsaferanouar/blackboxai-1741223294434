from app import create_app, db
from app.models.models import User, Property, CleaningTask

app = create_app()

def init_db():
    with app.app_context():
        db.create_all()
        
        # Delete all existing users
        User.query.delete()
        
        # Create admin user
        admin = User(username='admin', email='admin@example.com', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)

        db.session.commit()
        print('Database initialized successfully!')
        print('Admin account created:')
        print('Username: admin')
        print('Password: admin123')

if __name__ == '__main__':
    init_db()
