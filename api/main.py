from flask import Flask
from flask_restful import Resource, Api

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
from sqlalchemy import and_

from models import Qualities

app = Flask(__name__)

app.config.from_object('config.Config')

db = SQLAlchemy(app)
db.create_all()
db.session.commit()

api = Api(app)


# Returns Max Fixed Acidity
class MaxFixedAcidicity(Resource):
    def get(self):
        max_fixed_acidity = db.session.query(func.max(Qualities.fixed_acidity)).one()
        return {'max_fixed_acidity': max_fixed_acidity[0]}


# Return ids of wines with 6 <= PH <= 8 (I think such values do not exist)
class NeutralWines(Resource):
    def get(self):
        wines = db.session.query(Qualities).filter(and_(6 <= Qualities.ph, Qualities.ph <= 8)).all()
        ids = [q.id for q in wines]
        return {'wines': ids}


# Returns (ids, alcohol) of top 10 alcoholic wines
class TopAlcoholWines(Resource):
    def get(self):
        wines = db.session.query(Qualities).order_by(Qualities.alcohol.desc()).limit(10)
        ids_alcohol = [{'id': q.id, 'alcohol': q.alcohol} for q in wines]
        return {'wines': ids_alcohol}


# Returns (ids, density) of bottom 10 density wines
class BottomDensityWines(Resource):
    def get(self):
        wines = db.session.query(Qualities).order_by(Qualities.density).limit(10)
        ids_density = [{'id': q.id, 'density': q.density} for q in wines]
        return {'wines': ids_density}


# Part 1
api.add_resource(MaxFixedAcidicity, '/api/getMaxFixedAcidicity')
api.add_resource(NeutralWines, '/api/getNeutralWines')
api.add_resource(TopAlcoholWines, '/api/getTopAlcoholWines')
api.add_resource(BottomDensityWines, '/api/getBottomDensityWines')


if __name__ == '__main__':
    print('Flask Wine App is Running!')
    app.run(host='0.0.0.0', debug=True)
