from flask_restful import Resource, reqparse
from flask import request

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
        parser=reqparse.RequestParser()
        parser.add_argument('fixed_acidity',
            type=float,
            required=True,
            help="This field cannot be left blank!")
        parser.add_argument('volatile_acidity',
            type=float,
            default=0)
        data=parser.parse_args()
        wine=Qualities.find_by_key(fxd_acdt=data['fixed_acidity'],vlt_acdt=data['volatile_acidity'])
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
        wine=schema.load(request.get_json())
        wine.add_wine()
        return {'Message':'Wine added'}, 201

class EditWine(Resource):
    def post(self,_id):
        wine=schema.load(request.get_json())
        w=Qualities.find_by_id(aa=_id)
        if w:
            wine.id=_id
            Qualities.update_wine(wine=schema.dump(wine))
            return {'Message':'Wine updated'}, 200
        else:
            wine.add_wine()
            return {'Message':'Wine added'}, 201

class RemoveWine(Resource):
    def post(self,_id):
        wine=Qualities.find_by_id(aa=_id)
        if wine:
            wine.delete_wine()
            return {'Message':'Wine deleted'},200
        return{'Message':'Wine doesn\'t exist'}, 404
