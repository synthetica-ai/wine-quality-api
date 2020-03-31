from flask import Flask
from flask_restful import Api

from resources.resources import MaxFixedAcidicity, NeutralWines, TopAlcoholWines, BottomDensityWines, AddWine, EditWine, RemoveWine, FindWine
from db import db

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost:5430/wine'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
api=Api(app)



api.add_resource(MaxFixedAcidicity, '/api/getMaxFixedAcidicity')
api.add_resource(NeutralWines, '/api/getNeutralWines')
api.add_resource(TopAlcoholWines, '/api/getTopAlcoholWines')
api.add_resource(BottomDensityWines, '/api/getBottomDensityWines')
api.add_resource(AddWine, '/api/addWine')
api.add_resource(EditWine, '/api/editWine')
api.add_resource(RemoveWine, '/api/removeWine')
api.add_resource(FindWine, '/api/findwine')



if __name__=="__main__":
    db.init_app(app)
    app.run(port=5000,debug=True)
