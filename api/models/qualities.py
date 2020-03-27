from db import db

class Qualities(db.Model):
    fixed_acidity=db.Column(db.Float, primary_key=True)
    volatile_acidity=db.Column(db.Float, primary_key=True)
    citric_acid=db.Column(db.Float)
    residual_sugar=db.Column(db.Float)
    chlorides=db.Column(db.Float)
    free_sulfur_dioxide=db.Column(db.Float)
    total_sulfur_dioxide=db.Column(db.Float)
    density=db.Column(db.Float)
    ph=db.Column(db.Float)
    sulphates=db.Column(db.Float)
    alcohol=db.Column(db.Float)

    def __init__(self, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, ph, sulphates, alcohol):
        self.fixed_acidity=fixed_acidity
        self.volatile_acidity=volatile_acidity
        self.citric_acid=citric_acid
        self.residual_sugar=residual_sugar
        self.chlorides=chlorides
        self.free_sulfur_dioxide=free_sulfur_dioxide
        self.total_sulfur_dioxide=total_sulfur_dioxide
        self.density=density
        self.ph=ph
        self.sulphates=sulphates
        self.alcohol=alcohol

    def __repr__(self):
        return {'fixed_acidity':self.fixed_acidity, 'volatile_acidity':self.volatile_acidity, 'citric_acid':self.citric_acid, 'residual_sugar':self.residual_sugar, 'chlorides':self.chlorides, 'free_sulfur_dioxide':self.free_sulfur_dioxide, 'total_sulfur_dioxide':self.total_sulfur_dioxide, 'density':self.density, 'ph':self.ph, 'sulphates':self.sulphates, 'alcohol':self.alcohol}

    @classmethod
    def find_acidity(cls):
        return cls.query.order_by(cls.fixed_acidity.desc()).first()

    @classmethod
    def find_neutral(cls):
        return cls.query.filter(cls.ph<8).filter(cls.ph>6).all()

    @classmethod
    def find_top_alcohol(cls):
        return cls.query.order_by(cls.alcohol.desc()).limit(10).all()

    @classmethod
    def find_bottom_dens(cls):
        return cls.query.order_by(cls.density).limit(10).all()
