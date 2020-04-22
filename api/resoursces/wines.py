from flask_restful import Resource, reqparse
from models.wines import WineModel

class getMaxFixedAcidicity(Resource):

    def get(self):
        winelist = WineModel.query.order_by(WineModel.fixed_acidity).filter_by(WineModel.fixed_acidity == (WineModel.query(WineModel.fixed_acidity).order_by(WineModel.fixed_Acidity).desc().limit(1))).all()
        datalist = []
        for item in winelist:  
            temp = item.json()
            datalist.append(temp)
        if not datalist:
            return{'message' : 'No results'} 
        return datalist                               

class getNeutralWines(Resource):
    
    def get(self):
        winelist = WineModel.query.filter_by(WineModel.pH > 6, WineModel.pH < 8).all()
        datalist = []
        for item in winelist:  
            temp = item.json()
            datalist.append(temp)
        if not datalist:
            return{'message' : 'No results'}
        return datalist  

class getTopAlchohol(Resource):

    def get(self):
        winelist = WineModel.query.order_by(WineModel.alchohol.desc()).limit(10).all()
        datalist = []
        for item in winelist:  
            temp = item.json()
            datalist.append(temp)
        if not datalist:
            return{'message' : 'No results'}    
        return datalist  


class getBottomDensityWines(Resource):

    def get(self):
        winelist = WineModel.query.order_by(WineModel.density).limit(10).all()
        datalist = []
        for item in winelist:  
            temp = item.json()
            datalist.append(temp)
        if not datalist:
            return{'message' : 'No results'} 
        return datalist  

class removeWine(Resource):
    parser = reqparse.RequestPasrser()
    parser.add_argument('id', type=int, required=True)

    def post(self):
        id = removeWine.parser.parse_args()['id']
        wine = WineModel.find_by_number(id)
        if wine:
            wine.delete_from_db()
            return{'message': 'Wine deleted'}, 200
        return {'message' : 'Wine not found'}, 404      

class editWine(Resource):
    parser = reqparse.Requestparser()
    parser.add_argument('id', type=int, required=True)
    parser.add_argument('fixed_acidity', type=float)
    parser.add_argument('volatile_acidity', type=float)
    parser.add_argument('citric_acid', type=float)
    parser.add_argument('residual_sugar', type=float)
    parser.add_argument('chlorides', type=float)
    parser.add_argument('free_sulfur_dioxide', type=int)
    parser.add_argument('total_sulfur_dioxide', type=int)
    parser.add_argument('density', type=float)
    parser.add_argument('pH', type=float)
    parser.add_argument('sulphates', type=float)
    parser.add_argument('alchohol', type=float)

    def post(self):
        id = editWine.parser.parse_args()['id']
        wine = WineModel.find_wine(id)
        if wine:   
            data = editWine.parser.parse_args()
            wine.give_dict(data)
            return {'message' : 'Wine updated'}, 200
        return {'message' : 'Wine not found'}, 404

class addWine(Resource):
    parser = reqparse.Requestparser()
    parser.add_argument('fixed_acidity', type=float, required=True)
    parser.add_argument('volatile_acidity', type=float, required=True)
    parser.add_argument('citric_acid', type=float, required=True)
    parser.add_argument('residual_sugar', type=float, required=True)
    parser.add_argument('chlorides', type=float, required=True)
    parser.add_argument('free_sulfur_dioxide', type=int, required=True)
    parser.add_argument('total_sulfur_dioxide', type=int, required=True)
    parser.add_argument('density', type=float, required=True)
    parser.add_argument('pH', type=float, required=True)
    parser.add_argument('sulphates', type=float, required=True)
    parser.add_argument('alchohol', type=float, required=True)

    def post(self):
        data = addWine.parser.parse_args()
        wine = WineModel(id=None, *data)
        wine.save_to_db()
        return {'message' : 'Wine inserted to database'}, 201


        



                









