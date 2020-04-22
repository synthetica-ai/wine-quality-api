from db import db

class WineModel(db.Model):
    __tablename__ = 'qualities'

    id = db.Column(db.Integer, primary_key= True)
    fcd = db.Column(db.Float(precision = 1))
    vcd = db.Column(db.Float(precision = 2))
    ccd = db.Column(db.Float(precision = 2))
    rsgr = db.Column(db.Float(precision = 1))
    chloro = db.Column(db.Float(precision = 3))
    fsulf = db.Column(db.Integer)
    tsulf = db.Column(db.Integer)
    dens = db.Column(db.Float(precision = 4))
    pH = db.Column(db.Float(precision = 2))    
    sulph = db.Column(db.Float(precision = 2))
    alcho = db.Column(db.Float(precision = 1))

    def __init__(self, id, fcd, vcd, ccd, rsgr, chloro, fsulf, tsulf, dens, pH, sulph, alcho):
        self.id = id
        self.fixed_acidity = fcd
        self.volatile_acidity = vcd   
        self.citric_acid = ccd   
        self.residual_sugar = rsgr   
        self.chlorides = chloro  
        self.free_sulfur_dioxide = fsulf  
        self.total_sulfur_dioxide = tsulf  
        self.density = dens 
        self.pH = pH   
        self.sulphates = sulph 
        self.alchohol = alcho

    def json(self):  
        return {'id': self.id, 'fixed_acidity' : self.fixed_acidity, 'volatile_acidity' : self.volatile_acidity, 'citric_acid' : self.citric_acid, 'residual_sugar' : self.residual_sugar, 'chlorides' : self.chlorides,  'free_sulfur_dioxide' : self.free_sulfur_dioxide, 'total_sulfur_dioxide' : self.total_sulfur_dioxide, 'density': self.density, 'pH' : self.pH, 'sulphates' : self.sulphates, 'alchohol' :self.alchohol}

    def give_dict(self, dict):
        if 'id' in dict: self.id = dict['id']
        if 'fixed_acidicity' in dict: self.fixed_acidity = dict['fixed_acidity']
        if 'volatile_acidity' in dict: self.volatile_acidity = dict['volatile_acidity']  
        if 'citric_acid' in dict: self.citric_acid = dict['citric_acid']  
        if 'residual_sugar' in dict: self.residual_sugar = dict['residual_sugar']
        if 'chlorides' in dict: self.chlorides = dict['chlorides']
        if 'free_sulfur_dioxide' in dict: self.free_sulfur_dioxide = dict['free_sulfur_dioxide']
        if 'total_sulfur_dioxide' in dict: self.total_sulfur_dioxide = dict['total_sulfur_dioxide']  
        if 'density' in dict: self.density = dict['density']
        if 'pH' in dict: self.pH = dict['pH']
        if 'sulphates' in dict: self.sulphates = dict['sulphates']
        if 'alchohol' in dict: self.alchohol = dict['alchohol']
        db.session.commit()

    
    @classmethod   
    def find_wine(cls, number):
        return cls.query.filter_by(id = number)


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()






