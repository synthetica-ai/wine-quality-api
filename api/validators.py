wine_schema = {
    "type": "object",
    "properties": {
        "fixed_acidity": {
            "type": "number"
        },
        "volatile_acidity": {
            "type": "number"
        },
        "citric_acid": {
            "type": "number"
        },
        "residual_sugar": {
            "type": "number"
        },
        "chlorides": {
            "type": "number"
        },
        "density": {
            "type": "number"
        },
        "ph": {
            "type": "number"
        },
        "sulphates": {
            "type": "number"
        },
        "alcohol": {
            "type": "number"
        },
    }
}


wines_schema = {
   'wines': {
       'type': 'array',
       'items': [
           wine_schema
       ]
   }
}
