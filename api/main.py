from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_validation.decorators import validate_with_jsonschema

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
from sqlalchemy import and_

from models import Qualities
from validators import wines_schema, wine_schema

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
        return {'max_fixed_acidity': max_fixed_acidity[0]}, 201


# Return ids of wines with 6 <= PH <= 8 (I think such values do not exist)
class NeutralWines(Resource):
    def get(self):
        wines = db.session.query(Qualities).filter(and_(0 <= Qualities.ph, Qualities.ph <= 8)).all()
        ids = [q.id for q in wines]
        return {'wines': ids}, 201


# Returns (ids, alcohol) of top 10 alcoholic wines
class TopAlcoholWines(Resource):
    def get(self):
        wines = db.session.query(Qualities).order_by(Qualities.alcohol.desc()).limit(10)
        ids_alcohol = [{'id': q.id, 'alcohol': q.alcohol} for q in wines]
        return {'wines': ids_alcohol}, 201


# Returns (ids, density) of bottom 10 density wines
class BottomDensityWines(Resource):
    def get(self):
        wines = db.session.query(Qualities).order_by(Qualities.density).limit(10)
        ids_density = [{'id': q.id, 'density': q.density} for q in wines]
        return {'wines': ids_density}, 201


# Part 1
api.add_resource(MaxFixedAcidicity, '/api/getMaxFixedAcidicity')
api.add_resource(NeutralWines, '/api/getNeutralWines')
api.add_resource(TopAlcoholWines, '/api/getTopAlcoholWines')
api.add_resource(BottomDensityWines, '/api/getBottomDensityWines')


# Adds list of wines in database
class AddWines(Resource):
    @validate_with_jsonschema(wines_schema)
    def post(self):
        wines = request.get_json()['wines']
        for wine in wines:
            new_wine = Qualities(fixed_acidity=wine['fixed_acidity'],
                                 volatile_acidity=wine['volatile_acidity'],
                                 citric_acid=wine['citric_acid'],
                                 residual_sugar=wine['residual_sugar'],
                                 chlorides=wine['chlorides'],
                                 free_sulfur_dioxide=wine['free_sulfur_dioxide'],
                                 total_sulfur_dioxide=wine['total_sulfur_dioxide'],
                                 density=wine['density'],
                                 ph=wine['ph'],
                                 sulphates=wine['sulphates'],
                                 alcohol=wine['alcohol'])
            db.session.add(new_wine)

        db.session.commit()
        return {"msg": "Created Successfully"}, 201


# Edits an existing wine
class EditWine(Resource):
    @validate_with_jsonschema(wine_schema)
    def patch(self, wine_id):
        data = request.get_json()
        wine = db.session.query(Qualities).filter_by(id=wine_id).first()
        if not wine:
            return {"msg": "Wine not found"}, 404
        wine.fixed_acidity = data['fixed_acidity']
        wine.volatile_acidity = data['volatile_acidity']
        wine.citric_acid = data['citric_acid']
        wine.residual_sugar = data['residual_sugar']
        wine.chlorides = data['chlorides']
        wine.free_sulfur_dioxide = data['free_sulfur_dioxide']
        wine.total_sulfur_dioxide = data['total_sulfur_dioxide']
        wine.density = data['density']
        wine.ph = data['ph']
        wine.sulphates = data['sulphates']
        wine.alcohol = data['alcohol']

        db.session.flush()
        db.session.commit()

        return {"msg": "Updated Successfully"}, 201


# Deletes an existing wine
class DeleteWine(Resource):
    def delete(self, wine_id):
        wine = db.session.query(Qualities).filter_by(id=wine_id).first()
        if not wine:
            return {"msg": "Wine not found"}, 404
        db.session.delete(wine)
        db.session.commit()
        return {"msg": "Deleted Successfully"}, 201


api.add_resource(AddWines, '/api/addWine')
api.add_resource(EditWine, '/api/editWine/<wine_id>')
api.add_resource(DeleteWine, '/api/removeWine/<wine_id>')


if __name__ == '__main__':
    print('Flask Wine App is Running!')
    app.run(host='0.0.0.0', debug=True)
