# from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    aqi_threshold = db.Column(db.Integer, nullable=False)