class Config(object):
    DEBUG = True
    TESTING = True
    DEVELOPMENT = True
    CSRF_ENABLED = True
    SECRET_KEY = 'a-really-random-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    VALIDATION_ERROR_ABORT_CODE = "There is a problem with your JSON request"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@db/wine'
