from flask_restful import Resource
from flask import request

from db import db
from models.qualities import Qualities
from schemas.qualities import QualitiesSchema

schema=QualitiesSchema()
schema_list=QualitiesSchema(many=True)

class FindById(Resource):
    def get(self,_id):
        wine=Qualities.find_by_id(aa=_id)
        return {'Wine':schema.dump(wine)}

class FindWine(Resource):
    def get(self):
        data=schema.load(request.get_json(), partial=True)
        wine=Qualities.find_by_key(fxd_acdt=data.fixed_acidity,vlt_acdt=data.volatile_acidity)
        if wine:
            return {'Number of wines found': len(wine), "Wines":schema_list.dump(wine)}
        return {'Message':'Wine not found'}, 404

class MaxFixedAcidicity(Resource):
    def get(self):
        data=Qualities.find_acidity()
        return {'Max fixed acidity':data.fixed_acidity}

class NeutralWines(Resource):
    def get(self):
        data=Qualities.find_neutral()
        return {'Neutral wines':[x.ph for x in data] or 'There is no such thing as neutral wines'}

class TopAlcoholWines(Resource):
    def get(self):
        data=Qualities.find_top_alcohol()
        return {'Top 10 alcohol wines':[x.alcohol for x in data]}

class BottomDensityWines(Resource):
    def get(self):
        data=Qualities.find_bottom_dens()
        return {'10 least density wines':[x.density for x in data]}

class AddWine(Resource):
    def post(self):
        wine=schema.load(request.get_json(), partial=True, session=db.session)
        wine.add_wine()
        return {'Message':'Wine added'}, 201

class EditWine(Resource):
    def post(self):
        wine=schema.load(request.get_json(), partial=True, session=db.session)
        w=Qualities.find_by_id(aa=wine.id)
        if w:
            Qualities.update_wine(wine=schema.dump(wine))
            return {'Message':'Wine updated'}, 200
        return {'Message':'Wine doesn\'t exist'}, 404

class RemoveWine(Resource):
    def post(self):
        wine=schema.load(request.get_json(), partial=True, session=db.session)
        wine=Qualities.find_by_id(aa=wine.id)
        if wine:
            wine.delete_wine()
            return {'Message':'Wine deleted'},200
        return{'Message':'Wine doesn\'t exist'}, 404
