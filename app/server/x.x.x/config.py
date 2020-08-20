class Config(object):
    DEBUG = False
    TESTING = False
    

class PRDConfig(Config):
    DB_HOST = "10.5.0.2"

    SESSION_COOKIE_SECURE = True

class LOCALConfig(Config):
    DEBUG = True
    DB_HOST = "10.0.0.2"

    SESSION_COOKIE_SECURE = False

class UATConfig(Config):
    TESTING = True
    DB_HOST = "10.1.0.2"

    SESSION_COOKIE_SECURE = False
