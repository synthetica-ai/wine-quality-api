from flask import Flask
from flask_restful import Api
from db import db
from resources.wines import getMaxFixedAcidicity, getBottomDensityWines, getNeutralWines, getTopAlcoholWines, removeWine, editWine, addWine    
 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:postgres@localhost:5430/wine'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

api.add_resource(getMaxFixedAcidicity, '/api/getMaxFixedAcidicity')
api.add_resource(getNeutralWines, '/api/getNeutralWines')
api.add_resource(getTopAlcoholWines, '/api/getTopAlcoholWines')
api.add_resource(getBottomDensityWines, '/api/getBottomDensityWines')
api.add_resource(addWine, '/api/addWine')
api.add_resource(editWine, '/api/editWine')
api.add_resource(removeWine, '/api/removeWine')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
    
    


