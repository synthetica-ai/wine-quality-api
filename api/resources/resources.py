from flask_restful import Resource

from models.qualities import Qualities

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
