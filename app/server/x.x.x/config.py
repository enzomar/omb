class Config(object):
    DEBUG = False
    TESTING = False
    

class PRDConfig(Config):
    DB_NAME = "prd-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"
    DB_HOST = "10.0.1.2"

    SESSION_COOKIE_SECURE = True

class LOCALConfig(Config):
    DEBUG = True

    DB_NAME = "local-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"
    DB_HOST = "10.0.0.2"

    SESSION_COOKIE_SECURE = False

class UATConfig(Config):
    TESTING = True

    DB_NAME = "uat-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"
    DB_HOST = "10.0.0.2"

    SESSION_COOKIE_SECURE = False
