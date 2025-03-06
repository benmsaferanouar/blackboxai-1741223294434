from app import create_app, db
from app.models.models import User, Property, CleaningTask

app = create_app()

def init_db():
    with app.app_context():
        db.create_all()
        print('Database tables created successfully!')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080, debug=True)
