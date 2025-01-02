from flask_sqlalchemy import SQLAlchemy
from app import app

app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Configuring SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()