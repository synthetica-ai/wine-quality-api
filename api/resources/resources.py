from flask_restful import Resource, reqparse

from db import db
from models.qualities import Qualities

def read_args():
    parser=reqparse.RequestParser()
    parser.add_argument('fixed_acidity',
        type=float,
        required=True,
        help="This field cannot be left blank!")
    parser.add_argument('volatile_acidity',
        type=float,
        default=0)
    parser.add_argument('citric_acid',
        type=float,
        default=0)
    parser.add_argument('residual_sugar',
        type=float,
        default=0)
    parser.add_argument('chlorides',
        type=float,
        default=0)
    parser.add_argument('free_sulfur_dioxide',
        type=float,
        default=0)
    parser.add_argument('total_sulfur_dioxide',
        type=float,
        default=0)
    parser.add_argument('density',
        type=float,
        default=0)
    parser.add_argument('ph',
        type=float,
        default=0)
    parser.add_argument('sulphates',
        type=float,
        default=0)
    parser.add_argument('alcohol',
        type=float,
        default=0)
    return parser.parse_args()

class FindWine(Resource):
    def get(self):
        data=read_args()
        wine=Qualities.find_by_key(fxd_acdt=data['fixed_acidity'],vlt_acdt=data['volatile_acidity'])
        if wine:
            return {'Wine':[x.__repr__() for x in wine]}
        return {'Message':'Wine not found'}

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
        data=read_args()
        wine=Qualities(**data)
        wine.add_wine()
        return {'Message':'Wine added'}

class EditWine(Resource):
    def post(self):
        data=read_args()
        wine=Qualities.find_by_key(fxd_acdt=data['fixed_acidity'],vlt_acdt=data['volatile_acidity'])
        if wine:
            Qualities.updt(fxd_acdt=data['fixed_acidity'],vlt_acdt=data['volatile_acidity'],data=data)
            return {'Message':'Wine updated'}

        wine=Qualities(**data)
        wine.add_wine()
        return {'Message':'Wine added'}

class RemoveWine(Resource):
    def post(self):
        data=read_args()
        wine=Qualities.find_by_key(fxd_acdt=data['fixed_acidity'],vlt_acdt=data['volatile_acidity'])
        if wine:
            Qualities.delete_wine(fxd_acdt=data['fixed_acidity'],vlt_acdt=data['volatile_acidity'])
            return {'Message':'Wine deleted'}
        return{'Message':'Wine doesn\'t exist'}, 404
