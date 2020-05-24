from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Qualities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fixed_acidity = db.Column(db.REAL, unique=False, nullable=False)
    volatile_acidity = db.Column(db.REAL, unique=False, nullable=False)
    citric_acid = db.Column(db.REAL, unique=False, nullable=False)
    residual_sugar = db.Column(db.REAL, unique=False, nullable=False)
    chlorides = db.Column(db.REAL, unique=False, nullable=False)
    free_sulfur_dioxide = db.Column(db.REAL, unique=False, nullable=False)
    total_sulfur_dioxide = db.Column(db.REAL, unique=False, nullable=False)
    density = db.Column(db.REAL, unique=False, nullable=False)
    ph = db.Column(db.REAL, unique=False, nullable=False)
    sulphates = db.Column(db.REAL, unique=False, nullable=False)
    alcohol = db.Column(db.REAL, unique=False, nullable=False)

