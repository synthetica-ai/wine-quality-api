from db import db

class Qualities(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    fixed_acidity=db.Column(db.Float)
    volatile_acidity=db.Column(db.Float)
    citric_acid=db.Column(db.Float)
    residual_sugar=db.Column(db.Float)
    chlorides=db.Column(db.Float)
    free_sulfur_dioxide=db.Column(db.Float)
    total_sulfur_dioxide=db.Column(db.Float)
    density=db.Column(db.Float)
    ph=db.Column(db.Float)
    sulphates=db.Column(db.Float)
    alcohol=db.Column(db.Float)

    def __repr__(self):
        return f"""id={self.id},\
                fixed_acidity={self.fixed_acidity},\
                volatile_acidity={self.volatile_acidity},\
                citric_acid={self.citric_acid},\
                residual_sugar={self.residual_sugar},\
                chlorides={self.chlorides},\
                free_sulfur_dioxide={self.free_sulfur_dioxide},\
                total_sulfur_dioxide={self.total_sulfur_dioxide},\
                density={self.density},\
                ph={self.ph},\
                sulphates={self.sulphates},\
                alcohol={self.alcohol}""".replace('                ',' ')

    def add_wine(self):
        db.session.add(self)
        db.session.commit()

    def delete_wine(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_acidity(cls):
        return cls.query.order_by(cls.fixed_acidity.desc()).first()

    @classmethod
    def find_neutral(cls):
        return cls.query.filter(cls.ph>6,cls.ph<8).all()

    @classmethod
    def find_top_alcohol(cls):
        return cls.query.order_by(cls.alcohol.desc()).limit(10).all()

    @classmethod
    def find_bottom_dens(cls):
        return cls.query.order_by(cls.density).limit(10).all()

    @classmethod
    def find_by_id(cls, aa):
        return cls.query.filter(cls.id==aa).first()

    @classmethod
    def find_by_key(cls,fxd_acdt,vlt_acdt):
        if vlt_acdt is None:
            return cls.query.filter(cls.fixed_acidity==str(fxd_acdt)).all()
        return cls.query.filter(cls.fixed_acidity==str(fxd_acdt),cls.volatile_acidity==str(vlt_acdt)).all()

    @classmethod
    def update_wine(cls,wine):
        cls.query.filter(cls.id==wine['id']).update(wine)
        db.session.commit()
        return
