from flask_restful import Resource, reqparse

from models.qualities import Qualities


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
            return {'Wine': [str(x) for x in wine]}
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
        parser=reqparse.RequestParser()
        parser.add_argument('fixed_acidity',
            type=float,
            required=True,
            help="This field cannot be left blank!")
        parser.add_argument('volatile_acidity',
            type=float,
            required=True)
        parser.add_argument('citric_acid',
            type=float,
            required=True)
        parser.add_argument('residual_sugar',
            type=float,
            required=True)
        parser.add_argument('chlorides',
            type=float,
            required=True)
        parser.add_argument('free_sulfur_dioxide',
            type=float,
            required=True)
        parser.add_argument('total_sulfur_dioxide',
            type=float,
            required=True)
        parser.add_argument('density',
            type=float,
            required=True)
        parser.add_argument('ph',
            type=float,
            required=True)
        parser.add_argument('sulphates',
            type=float,
            required=True)
        parser.add_argument('alcohol',
            type=float,
            required=True)
        data=parser.parse_args()
        wine=Qualities(**data)
        wine.add_wine()
        return {'Message':'Wine added'}

class EditWine(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('id',
        type=int,
        required=True,
        help="This field cannot be left blank!")
        parser.add_argument('fixed_acidity',
            type=float,
            required=True,
            help="This field cannot be left blank!")
        parser.add_argument('volatile_acidity',
            type=float,
            required=True)
        parser.add_argument('citric_acid',
            type=float,
            required=True)
        parser.add_argument('residual_sugar',
            type=float,
            required=True)
        parser.add_argument('chlorides',
            type=float,
            required=True)
        parser.add_argument('free_sulfur_dioxide',
            type=float,
            required=True)
        parser.add_argument('total_sulfur_dioxide',
            type=float,
            required=True)
        parser.add_argument('density',
            type=float,
            required=True)
        parser.add_argument('ph',
            type=float,
            required=True)
        parser.add_argument('sulphates',
            type=float,
            required=True)
        parser.add_argument('alcohol',
            type=float,
            required=True)
        data=parser.parse_args()
        wine=Qualities.find_by_id(aa=data['id'])
        if wine:
            Qualities.updt(aa=data['id'],data=data)
            return {'Message':'Wine updated'}

        wine=Qualities(**data)
        wine.add_wine()
        return {'Message':'Wine added'}

class RemoveWine(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('id',
        type=int,
        required=True,
        help="This field cannot be left blank!")
        data=parser.parse_args()
        wine=Qualities.find_by_id(aa=data['id'])
        if wine:
            wine.delete_wine()
            return {'Message':'Wine deleted'}
        return{'Message':'Wine doesn\'t exist'}, 404
