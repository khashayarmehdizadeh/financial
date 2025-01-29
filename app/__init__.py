from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the app

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///financial_managmnet.db'
    db.init_app(app)



    from. routes import main
    app.register_blueprint(main)
    return app